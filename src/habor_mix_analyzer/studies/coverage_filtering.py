from __future__ import annotations

from ..core import *
from ..core.config import MANUALLY_EXCLUDED_BENCHMARKS


def benchmark_filter_table(stats: pd.DataFrame, min_observed: int = 15, max_missing: float = 0.45) -> pd.DataFrame:
    table = stats.rename(columns={"column": "benchmark"}).copy()
    table["include_in_key_analysis"] = (
        (table["observed_count"] >= min_observed)
        & (table["missing_fraction"] <= max_missing)
        & (~table["benchmark"].isin(MANUALLY_EXCLUDED_BENCHMARKS))
    )

    def reason(row: pd.Series) -> str:
        if row["include_in_key_analysis"]:
            return "included"
        if row["benchmark"] in MANUALLY_EXCLUDED_BENCHMARKS:
            return "excluded: manually removed"
        if row["observed_count"] < min_observed:
            return f"excluded: fewer than {min_observed} observed agent+model rows"
        return f"excluded: missing fraction above {max_missing:.0%}"

    table["filter_reason"] = table.apply(reason, axis=1)
    ordered = [
        "benchmark",
        "include_in_key_analysis",
        "filter_reason",
        "observed_count",
        "missing_count",
        "missing_fraction",
        "task_count",
        "task_cell_missing_fraction",
        "mean_observed_task_cells_per_agent_model",
        "mean",
        "std",
        "median",
        "min",
        "max",
        "transform",
        "negative_count",
        "gt_one_count",
    ]
    ordered = [col for col in ordered if col in table.columns]
    return table[ordered].sort_values(["include_in_key_analysis", "observed_count"], ascending=[False, False])
