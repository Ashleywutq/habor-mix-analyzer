from __future__ import annotations

from ..core import *


def pairwise_correlations(matrix: pd.DataFrame, cols: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    corr = matrix[cols].corr(method="spearman")
    rows = []
    for i, left in enumerate(cols):
        for right in cols[i + 1 :]:
            rows.append({"left": left, "right": right, "spearman": float(corr.loc[left, right])})
    pairs = pd.DataFrame(rows)
    pairs["abs_spearman"] = pairs["spearman"].abs()
    return corr.reset_index(names="benchmark"), pairs.sort_values("abs_spearman", ascending=False)


def benchmark_similarity_clusters(corr: pd.DataFrame, n_clusters: int = 6) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    matrix = corr.set_index("benchmark")
    matrix = matrix.loc[matrix.columns, matrix.columns].fillna(0)
    distance_array = (1 - matrix.abs()).to_numpy(copy=True)
    np.fill_diagonal(distance_array, 0)
    condensed = squareform(distance_array, checks=False)
    z = linkage(condensed, method="average")
    order = matrix.index[leaves_list(z)].tolist()
    labels = fcluster(z, t=n_clusters, criterion="maxclust")
    clusters = pd.DataFrame({"benchmark": matrix.index, "similarity_cluster": labels})
    clusters = clusters.sort_values(["similarity_cluster", "benchmark"]).reset_index(drop=True)
    ordered_corr = matrix.loc[order, order].reset_index(names="benchmark")
    return clusters, ordered_corr, order


def domain_correlation_decomposition(
    corr: pd.DataFrame,
    pairs: pd.DataFrame,
) -> pd.DataFrame:
    """Label each benchmark pair as within-domain or cross-domain, return enriched pairs."""
    enriched = pairs.copy()
    enriched["left_domain"] = enriched["left"].map(BENCHMARK_DOMAIN).fillna("Other")
    enriched["right_domain"] = enriched["right"].map(BENCHMARK_DOMAIN).fillna("Other")
    enriched["same_domain"] = enriched["left_domain"] == enriched["right_domain"]
    enriched["domain_pair"] = enriched.apply(
        lambda r: r["left_domain"] if r["same_domain"] else f"{min(r['left_domain'], r['right_domain'])} × {max(r['left_domain'], r['right_domain'])}",
        axis=1,
    )
    return enriched


def domain_correlation_summary(enriched_pairs: pd.DataFrame) -> pd.DataFrame:
    """Aggregate within- vs cross-domain correlation statistics."""
    rows = []
    for same_domain, group in enriched_pairs.groupby("same_domain"):
        rows.append({
            "group": "within-domain" if same_domain else "cross-domain",
            "n_pairs": len(group),
            "mean_spearman": float(group["spearman"].mean()),
            "median_spearman": float(group["spearman"].median()),
            "std_spearman": float(group["spearman"].std()),
            "mean_abs_spearman": float(group["abs_spearman"].mean()),
            "median_abs_spearman": float(group["abs_spearman"].median()),
            "frac_above_0.7": float((group["abs_spearman"] > 0.7).mean()),
        })
    for domain, group in enriched_pairs[enriched_pairs["same_domain"]].groupby("left_domain"):
        if len(group) < 2:
            continue
        rows.append({
            "group": f"within: {domain}",
            "n_pairs": len(group),
            "mean_spearman": float(group["spearman"].mean()),
            "median_spearman": float(group["spearman"].median()),
            "std_spearman": float(group["spearman"].std()),
            "mean_abs_spearman": float(group["abs_spearman"].mean()),
            "median_abs_spearman": float(group["abs_spearman"].median()),
            "frac_above_0.7": float((group["abs_spearman"] > 0.7).mean()),
        })
    return pd.DataFrame(rows)


def effective_dimensionality(explained_variance_ratios: np.ndarray, n_benchmarks: int = 0) -> dict[str, float]:
    """Compute effective dimensionality metrics from PCA explained variance ratios."""
    ratios = explained_variance_ratios[explained_variance_ratios > 0]
    cumulative = np.cumsum(ratios)
    participation_ratio = float(np.sum(ratios) ** 2 / np.sum(ratios ** 2))
    n_for_90 = int(np.searchsorted(cumulative, 0.90) + 1)
    n_for_95 = int(np.searchsorted(cumulative, 0.95) + 1)
    entropy = float(-np.sum(ratios * np.log(ratios)))
    effective_from_entropy = float(np.exp(entropy))
    return {
        "participation_ratio": participation_ratio,
        "effective_dim_entropy": effective_from_entropy,
        "n_components_90pct": n_for_90,
        "n_components_95pct": n_for_95,
        "top1_variance": float(ratios[0]),
        "top3_variance": float(cumulative[min(2, len(cumulative) - 1)]),
        "top5_variance": float(cumulative[min(4, len(cumulative) - 1)]),
        "n_benchmarks": n_benchmarks,
        "total_components": len(ratios),
    }


def full_pca_explained_variance(normalized: pd.DataFrame, cols: list[str]) -> np.ndarray:
    """Run PCA with all components and return explained variance ratios."""
    x = normalized[cols].astype(float).to_numpy()
    n_components = min(x.shape[0] - 1, x.shape[1])
    pca = PCA(n_components=n_components, random_state=RANDOM_SEED)
    pca.fit(x)
    return pca.explained_variance_ratio_


def greedy_benchmark_selection(corr_matrix: pd.DataFrame) -> pd.DataFrame:
    """Greedily select benchmarks to maximize coverage of independent information.

    At each step, add the benchmark whose maximum absolute correlation with
    already-selected benchmarks is smallest (i.e. the most independent one).
    Track cumulative PCA variance explained by the selected subset.
    """
    matrix = corr_matrix.set_index("benchmark") if "benchmark" in corr_matrix.columns else corr_matrix
    benchmarks = list(matrix.index)
    abs_corr = matrix.abs().to_numpy(copy=True)
    np.fill_diagonal(abs_corr, 0)

    mean_abs = abs_corr.mean(axis=1)
    first = int(np.argmin(mean_abs))
    selected_idx = [first]
    remaining = set(range(len(benchmarks))) - {first}

    rows = [{
        "step": 1,
        "benchmark": benchmarks[first],
        "domain": BENCHMARK_DOMAIN.get(benchmarks[first], "Other"),
        "max_abs_corr_to_selected": 0.0,
        "mean_abs_corr_to_selected": 0.0,
    }]

    while remaining:
        best_candidate = None
        best_max_corr = 2.0
        for candidate in remaining:
            max_corr = max(abs_corr[candidate, s] for s in selected_idx)
            if max_corr < best_max_corr:
                best_max_corr = max_corr
                best_candidate = candidate
        selected_idx.append(best_candidate)
        remaining.remove(best_candidate)
        mean_corr = float(np.mean([abs_corr[best_candidate, s] for s in selected_idx[:-1]]))
        rows.append({
            "step": len(selected_idx),
            "benchmark": benchmarks[best_candidate],
            "domain": BENCHMARK_DOMAIN.get(benchmarks[best_candidate], "Other"),
            "max_abs_corr_to_selected": float(best_max_corr),
            "mean_abs_corr_to_selected": mean_corr,
        })

    return pd.DataFrame(rows)
