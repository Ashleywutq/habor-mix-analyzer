"""BenchPress-style benchmark predictability analysis.

Implements the methodology from Dimitris's BenchPress repo
(https://github.com/anadim/llm-benchmark-matrix):

1. LogitBenchReg: For each target benchmark, predict from the k=5 most
   correlated benchmarks using ridge regression in logit space.
2. SVD-Logit (rank=2): Soft-impute SVD in logit space for global coverage.
3. BenchPress blend: 0.6 × LogitBenchReg + 0.4 × SVD-Logit.
4. Per-benchmark predictability: Measured via per-model holdout MAE.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from ..core import KEY_COLUMNS, RANDOM_SEED


# ─── Logit helpers ────────────────────────────────────────────────────────────

def _is_pct_col(values: np.ndarray) -> bool:
    """Heuristic: column uses a [0, 1] proportion scale."""
    valid = values[~np.isnan(values)]
    if len(valid) == 0:
        return False
    return float(valid.min()) >= -0.01 and float(valid.max()) <= 1.01


def _to_logit(x: np.ndarray, eps: float = 0.005) -> np.ndarray:
    """Convert proportion [0, 1] -> logit space. Clips to [eps, 1-eps]."""
    p = np.clip(x, eps, 1 - eps)
    return np.log(p / (1 - p))


def _from_logit(z: np.ndarray) -> np.ndarray:
    """Convert logit -> proportion [0, 1]."""
    return 1.0 / (1.0 + np.exp(-z))


# ─── LogitBenchReg ────────────────────────────────────────────────────────────

def _logit_benchreg(matrix: np.ndarray, obs: np.ndarray, is_pct: np.ndarray,
                    top_k: int = 5, min_r2: float = 0.1) -> np.ndarray:
    """Predict each benchmark from top-k most correlated using regression in logit space.

    For each target benchmark j, finds the k benchmarks whose observed scores
    best predict j (measured by R² on shared observations), then fits a simple
    linear regression from each predictor to the target. Final prediction is an
    R²-weighted average of individual regressions.

    Returns a matrix with predictions for missing cells; observed cells unchanged.
    """
    n_models, n_bench = matrix.shape
    M_work = matrix.copy()
    for j in range(n_bench):
        if is_pct[j]:
            valid = obs[:, j]
            M_work[valid, j] = _to_logit(matrix[valid, j])

    M_pred = np.full_like(matrix, np.nan)
    M_pred[obs] = matrix[obs]

    for j in range(n_bench):
        targets_obs = np.where(obs[:, j])[0]
        if len(targets_obs) < 3:
            continue

        correlations = []
        for j2 in range(n_bench):
            if j2 == j:
                continue
            shared = obs[:, j] & obs[:, j2]
            n_shared = shared.sum()
            if n_shared < 3:
                correlations.append((j2, -1.0))
                continue
            x = M_work[shared, j2]
            y = M_work[shared, j]
            ss_tot = np.sum((y - y.mean()) ** 2)
            if ss_tot < 1e-10:
                correlations.append((j2, -1.0))
                continue
            var_x = np.sum((x - x.mean()) ** 2)
            if var_x < 1e-10:
                correlations.append((j2, -1.0))
                continue
            slope = np.sum((x - x.mean()) * (y - y.mean())) / var_x
            intercept = y.mean() - slope * x.mean()
            ss_res = np.sum((y - (slope * x + intercept)) ** 2)
            r2 = 1.0 - ss_res / ss_tot
            correlations.append((j2, r2))

        correlations.sort(key=lambda t: -t[1])
        best = [(j2, r2) for j2, r2 in correlations[:top_k] if r2 >= min_r2]
        if not best:
            continue

        for i in range(n_models):
            if obs[i, j]:
                continue
            preds, weights = [], []
            for j2, r2 in best:
                if np.isnan(M_work[i, j2]):
                    continue
                shared = obs[:, j] & obs[:, j2]
                if shared.sum() < 3:
                    continue
                x = M_work[shared, j2]
                y = M_work[shared, j]
                var_x = np.sum((x - x.mean()) ** 2)
                if var_x < 1e-10:
                    continue
                slope = np.sum((x - x.mean()) * (y - y.mean())) / var_x
                intercept = y.mean() - slope * x.mean()
                preds.append(slope * M_work[i, j2] + intercept)
                weights.append(r2)
            if preds:
                pred_val = np.average(preds, weights=weights)
                if is_pct[j]:
                    M_pred[i, j] = _from_logit(pred_val)
                else:
                    M_pred[i, j] = pred_val

    return M_pred


# ─── SVD-Logit ────────────────────────────────────────────────────────────────

def _svd_logit(matrix: np.ndarray, obs: np.ndarray, is_pct: np.ndarray,
               rank: int = 2, max_iter: int = 100, tol: float = 1e-4) -> np.ndarray:
    """Soft-Impute SVD in logit space for proportion benchmarks, z-score for others."""
    n_models, n_bench = matrix.shape
    M_work = matrix.copy()
    for j in range(n_bench):
        if is_pct[j]:
            valid = obs[:, j]
            M_work[valid, j] = _to_logit(matrix[valid, j])

    cm = np.nanmean(M_work, axis=0)
    cs = np.nanstd(M_work, axis=0)
    cs[cs < 1e-8] = 1.0
    M_norm = (M_work - cm) / cs
    M_norm[~obs] = np.nan

    M_imp = M_norm.copy()
    M_imp[np.isnan(M_imp)] = 0.0

    effective_rank = min(rank, n_models - 1, n_bench - 1)
    if effective_rank < 1:
        effective_rank = 1

    for _ in range(max_iter):
        M_old = M_imp.copy()
        try:
            U, s, Vt = np.linalg.svd(M_imp, full_matrices=False)
        except np.linalg.LinAlgError:
            break
        M_approx = U[:, :effective_rank] @ np.diag(s[:effective_rank]) @ Vt[:effective_rank, :]
        M_imp = np.where(obs, M_norm, M_approx)
        M_imp[np.isnan(M_imp)] = 0.0
        denom = np.sqrt(np.mean(M_old ** 2)) + 1e-12
        rel_diff = np.sqrt(np.mean((M_imp - M_old) ** 2)) / denom
        if rel_diff < tol:
            break

    M_pred_work = M_imp * cs + cm
    M_pred = np.full_like(matrix, np.nan)
    for j in range(n_bench):
        if is_pct[j]:
            M_pred[:, j] = _from_logit(M_pred_work[:, j])
        else:
            M_pred[:, j] = M_pred_work[:, j]
    M_pred[obs] = matrix[obs]
    return M_pred


# ─── BenchPress blend ─────────────────────────────────────────────────────────

def _benchpress_predict(matrix: np.ndarray, obs: np.ndarray, is_pct: np.ndarray,
                        alpha: float = 0.6) -> np.ndarray:
    """BenchPress = alpha × LogitBenchReg + (1-alpha) × SVD-Logit(rank=2)."""
    M_breg = _logit_benchreg(matrix, obs, is_pct)
    M_svd = _svd_logit(matrix, obs, is_pct, rank=2)
    col_mean = np.nanmean(matrix, axis=0)

    M_pred = matrix.copy()
    n_models, n_bench = matrix.shape
    for i in range(n_models):
        for j in range(n_bench):
            if obs[i, j]:
                continue
            b = M_breg[i, j]
            s = M_svd[i, j]
            b_ok = np.isfinite(b)
            s_ok = np.isfinite(s)
            if b_ok and s_ok:
                M_pred[i, j] = alpha * b + (1 - alpha) * s
            elif b_ok:
                M_pred[i, j] = b
            elif s_ok:
                M_pred[i, j] = s
            else:
                M_pred[i, j] = col_mean[j]
    return M_pred


# ─── Per-benchmark predictability via holdout ─────────────────────────────────

def predictability_for_cols(normalized: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """BenchPress-style per-benchmark predictability.

    For each model, hides 50% of its known scores, trains BenchPress on the rest,
    predicts the hidden cells, and measures per-benchmark error using both
    MedAPE (BenchPress's primary metric) and MedAE.

    Returns a DataFrame with columns:
      - benchmark
      - cv_r2_from_other_included_benchmarks (pseudo-R² for downstream compat)
      - cv_rmse (median absolute error in original score units)
      - benchpress_medae (median absolute error)
      - benchpress_medape (median absolute percentage error — BenchPress primary)
      - benchpress_coverage (fraction of holdout cells that got predictions)
    """
    matrix_df = normalized[cols].astype(float)
    matrix = matrix_df.to_numpy()
    n_models, n_bench = matrix.shape
    obs = ~np.isnan(matrix)
    is_pct = np.array([_is_pct_col(matrix[:, j]) for j in range(n_bench)])

    n_folds = 3
    rng = np.random.RandomState(RANDOM_SEED)

    per_bench_abs_errors: dict[str, list[float]] = {col: [] for col in cols}
    per_bench_pct_errors: dict[str, list[float]] = {col: [] for col in cols}
    per_bench_coverage: dict[str, int] = {col: 0 for col in cols}
    per_bench_total: dict[str, int] = {col: 0 for col in cols}

    for fold in range(n_folds):
        M_train = matrix.copy()
        holdout_mask = np.zeros_like(obs, dtype=bool)

        for i in range(n_models):
            obs_indices = np.where(obs[i])[0]
            if len(obs_indices) < 4:
                continue
            n_hide = max(1, len(obs_indices) // 2)
            hide_indices = rng.choice(obs_indices, size=n_hide, replace=False)
            M_train[i, hide_indices] = np.nan
            holdout_mask[i, hide_indices] = True

        train_obs = ~np.isnan(M_train)
        M_pred = _benchpress_predict(M_train, train_obs, is_pct)

        for j_idx, col in enumerate(cols):
            held_cells = np.where(holdout_mask[:, j_idx])[0]
            for i in held_cells:
                per_bench_total[col] += 1
                actual = matrix[i, j_idx]
                pred = M_pred[i, j_idx]
                if np.isfinite(pred):
                    per_bench_abs_errors[col].append(abs(pred - actual))
                    if abs(actual) > 1e-6:
                        per_bench_pct_errors[col].append(
                            abs(pred - actual) / abs(actual) * 100
                        )
                    per_bench_coverage[col] += 1

    rows = []
    baseline_errors = []
    for col in cols:
        j_idx = cols.index(col)
        col_vals = matrix[obs[:, j_idx], j_idx]
        if len(col_vals) > 1:
            col_mean = col_vals.mean()
            baseline_errors.append(np.median(np.abs(col_vals - col_mean)))
        else:
            baseline_errors.append(1.0)

    global_baseline = np.median(baseline_errors) if baseline_errors else 1.0

    for col_idx, col in enumerate(cols):
        abs_errors = per_bench_abs_errors[col]
        pct_errors = per_bench_pct_errors[col]
        total = per_bench_total[col]
        covered = per_bench_coverage[col]
        coverage = covered / total if total > 0 else 0.0

        medae = float(np.median(abs_errors)) if abs_errors else float("inf")
        mae = float(np.mean(abs_errors)) if abs_errors else float("inf")
        medape = float(np.median(pct_errors)) if pct_errors else float("inf")

        baseline = baseline_errors[col_idx] if baseline_errors[col_idx] > 1e-8 else global_baseline
        pseudo_r2 = 1.0 - (mae / baseline) ** 2 if baseline > 1e-8 and np.isfinite(mae) else -10.0
        pseudo_r2 = max(pseudo_r2, -10.0)

        rows.append({
            "benchmark": col,
            "cv_r2_from_other_included_benchmarks": pseudo_r2,
            "cv_rmse": medae,
            "benchpress_medae": medae,
            "benchpress_medape": medape,
            "benchpress_coverage": coverage,
        })

    return pd.DataFrame(rows).sort_values("benchpress_medape")


# ─── PCA (unchanged) ─────────────────────────────────────────────────────────

def pca_for_cols(
    normalized: pd.DataFrame, cols: list[str], n_components: int = 4
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    x = normalized[cols].astype(float).to_numpy()
    n_components = min(n_components, x.shape[0] - 1, x.shape[1])
    pca = PCA(n_components=n_components, random_state=RANDOM_SEED)
    scores = pca.fit_transform(x)
    loadings = pd.DataFrame(
        pca.components_.T,
        index=cols,
        columns=[f"PC{i + 1}" for i in range(n_components)],
    ).reset_index(names="benchmark")
    agent_model_scores = normalized[KEY_COLUMNS].copy()
    for i in range(n_components):
        agent_model_scores[f"PC{i + 1}"] = scores[:, i]
    explained = pd.DataFrame(
        {
            "component": [f"PC{i + 1}" for i in range(n_components)],
            "explained_variance_ratio": pca.explained_variance_ratio_,
        }
    )
    return loadings, agent_model_scores, explained
