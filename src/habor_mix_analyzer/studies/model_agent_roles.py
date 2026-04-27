from __future__ import annotations

from ..core import *

from .intermediate_tables import bounded_tier, design_matrix


def adjusted_group_effects(long_df: pd.DataFrame, group_col: str, controls: list[str]) -> pd.DataFrame:
    df = long_df.dropna(subset=["normalized_score"]).copy()
    y = df["normalized_score"].astype(float)
    x = design_matrix(df, controls)
    if x.empty:
        df["adjusted_score"] = y
    else:
        model = LinearRegression()
        model.fit(x, y)
        df["adjusted_score"] = y - model.predict(x) + float(y.mean())
    return (
        df.groupby(group_col)
        .agg(
            adjusted_mean=("adjusted_score", "mean"),
            adjusted_std=("adjusted_score", "std"),
            unadjusted_benchmark_relative_mean=("normalized_score", "mean"),
            observations=("normalized_score", "size"),
        )
        .reset_index()
        .sort_values("adjusted_mean", ascending=False)
    )


def within_family_model_vs_agent(
    raw_benchmark: pd.DataFrame,
    included_benchmarks: list[str],
) -> pd.DataFrame:
    """For each (family, benchmark): compute model-effect range (fixing terminus-2)
    and mean agent-effect delta (fixing model), then compare."""
    benchmarks = [c for c in included_benchmarks if c in raw_benchmark.columns]
    df = raw_benchmark[KEY_COLUMNS + benchmarks].copy()
    df["family"] = df["model"].map(MODEL_TO_FAMILY)
    df = df.dropna(subset=["family"])

    rows = []
    for family, family_models in MODEL_FAMILIES.items():
        fam = df[df["family"] == family]
        if fam.empty:
            continue
        baseline_rows = fam[fam["agent"] == BASELINE_AGENT]
        own_agents = fam[fam["agent"] != BASELINE_AGENT]["agent"].unique()

        for bench in benchmarks:
            t2_scores = baseline_rows[["model", bench]].dropna()
            if len(t2_scores) < 2:
                continue
            model_range = float(t2_scores[bench].max() - t2_scores[bench].min())

            agent_deltas = []
            for m in family_models:
                m_rows = fam[fam["model"] == m][["agent", bench]].dropna()
                if len(m_rows) == 2:
                    agent_deltas.append(float(m_rows[bench].values[0] - m_rows[bench].values[1]))

            if not agent_deltas:
                continue
            mean_agent_delta = float(np.mean(np.abs(agent_deltas)))
            rows.append(
                {
                    "family": family,
                    "benchmark": bench,
                    "model_effect_range": model_range,
                    "agent_effect_mean_delta": mean_agent_delta,
                    "model_over_agent_ratio": model_range / mean_agent_delta if mean_agent_delta > 1e-9 else float("inf"),
                    "dominant": "model" if model_range > mean_agent_delta else "agent",
                    "n_models": len(t2_scores),
                    "n_agent_pairs": len(agent_deltas),
                }
            )

    return pd.DataFrame(rows).sort_values(["family", "model_over_agent_ratio"], ascending=[True, False])


def benchmark_headroom_by_domain(
    raw_benchmark: pd.DataFrame,
    included_benchmarks: list[str],
) -> pd.DataFrame:
    """For each benchmark, find the best system score and classify difficulty tier."""
    benchmarks = [c for c in included_benchmarks if c in raw_benchmark.columns]
    rows = []
    for bench in benchmarks:
        scores = raw_benchmark[["model", "agent", bench]].dropna(subset=[bench])
        if scores.empty:
            continue
        best_idx = scores[bench].idxmax()
        best_row = scores.loc[best_idx]
        domain = BENCHMARK_DOMAIN.get(bench, "Other")
        mean_val = float(scores[bench].mean())
        min_val = float(scores[bench].min())
        max_val = float(scores[bench].max())
        rows.append(
            {
                "benchmark": bench,
                "domain": domain,
                "difficulty_tier": bounded_tier(mean_val, min_val, max_val),
                "best_score": float(best_row[bench]),
                "best_model": best_row["model"],
                "best_agent": best_row["agent"],
                "headroom": 1.0 - float(best_row[bench]),
                "mean_score": mean_val,
                "median_score": float(scores[bench].median()),
                "score_range": max_val - min_val,
                "n_systems": len(scores),
            }
        )
    return pd.DataFrame(rows).sort_values(["domain", "best_score"], ascending=[True, True])


def within_family_summary(detail: pd.DataFrame) -> pd.DataFrame:
    """Aggregate within_family_model_vs_agent to one row per family."""
    if detail.empty:
        return pd.DataFrame()
    return (
        detail.groupby("family")
        .agg(
            model_effect_median=("model_effect_range", "median"),
            model_effect_mean=("model_effect_range", "mean"),
            agent_effect_median=("agent_effect_mean_delta", "median"),
            agent_effect_mean=("agent_effect_mean_delta", "mean"),
            model_wins=("dominant", lambda s: (s == "model").sum()),
            total_benchmarks=("benchmark", "size"),
        )
        .reset_index()
    )


