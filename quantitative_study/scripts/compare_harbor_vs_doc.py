#!/usr/bin/env python3
"""
Compare Harbor benchmark scores (CSV matrix) to documented original scores
in benchmark_info_jobs/*.json (results_over_time).

Metric alignment strategy:
  1. Read data/metadata/benchmark_metric_alignment.csv as the source of truth.
  2. Use only rows where include_in_comparison=true.
  3. Select scores by exact doc_metric / doc_score_field.
  4. Apply the reviewed transform, then compute delta = score_harbor - score_doc.

Usage (from habor-mix-analyzer/):
  uv run python quantitative_study/scripts/compare_harbor_vs_doc.py \
    --harbor-csv benchmark_level_matrix.csv
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd

# ---------------------------------------------------------------------------
# Column -> JSON stem mapping overrides
# ---------------------------------------------------------------------------
MATRIX_COLUMN_TO_STEM: dict[str, str | None] = {
    "bixbench": "bix_bench",
    "crustbench": "crust_bench",
    "dacode": "da_code",
    "featurebench-modal": "featurebench",
    "financeagent_terminal": "financeagent",
    "labbench": "lab_bench",
    "mlgym": "mlgym_bench",
    "omnimath": "omni_math",
    "research-code-bench": "researchcodebench",
    "spider2": "spider_2",
    "swebench-verified": "swe_bench_verified",
    "swebench-multilingual": "swe_bench_multilingual",
    "swebenchpro": "swe_bench_pro",
    "swtbench": "swt_bench",
    "terminal-bench": "terminalbench_2_0",
    "qwen-coder": None,
    "swegym": None,
    "swesmith": "swe_smith",
}

# ---------------------------------------------------------------------------
# Model alias table: harbor_model -> list of normalized doc model patterns
# The first entry is the "canonical" name; others are known leaderboard variants.
# Matching is case-insensitive and strips parenthetical suffixes by default.
# ---------------------------------------------------------------------------
MODEL_ALIASES: dict[str, list[str]] = {
    "gpt-5.4": [
        "gpt-5.4",
        "gpt 5.4",
    ],
    "gpt-5-mini": [
        "gpt-5-mini",
        "gpt 5 mini",
        "gpt-5-mini-2025-08-07",
    ],
    "gpt-5-nano": [
        "gpt-5-nano",
        "gpt 5 nano",
        "gpt-5-nano-2025-08-07",
    ],
    "claude-haiku-4-5-20251001": [
        "claude-haiku-4-5",
        "claude haiku 4.5",
    ],
    "claude-sonnet-4-6": [
        "claude-sonnet-4-6",
        "claude sonnet 4.6",
    ],
    "claude-opus-4-6": [
        "claude-opus-4-6",
        "claude opus 4.6",
    ],
    "gemini-3.1-pro-preview": [
        "gemini-3.1-pro-preview",
        "gemini 3.1 pro preview",
        "gemini-3.1-pro",
        "gemini 3.1 pro",
    ],
    "gemini-3-flash-preview": [
        "gemini-3-flash-preview",
        "gemini 3 flash preview",
        "gemini-3-flash",
        "gemini 3 flash",
    ],
    "deepseek-reasoner": [
        "deepseek-reasoner",
        "deepseek-r1",
        "deepseek r1",
    ],
    "deepseek-chat": [
        "deepseek-chat",
        "deepseek-v3",
        "deepseek v3",
        "deepseek-v3.1",
        "deepseek v3.1",
    ],
    "kimi-k2.5": [
        "kimi-k2.5",
        "kimi k2.5",
    ],
    "minimax-m2.5": [
        "minimax-m2.5",
        "minimax m2.5",
    ],
    "glm-5": [
        "glm-5",
        "glm 5",
    ],
    "mimo-v2-pro": [
        "mimo-v2-pro",
        "mimo v2 pro",
    ],
    "qwen3-max": [
        "qwen3-max",
        "qwen 3 max",
        "qwen3 max",
        "qwen-3-max",
    ],
}

# Harbor agent -> list of normalized doc system_description patterns
AGENT_ALIASES: dict[str, list[str]] = {
    "terminus-2": ["terminus-2", "terminus 2", "terminus"],
    "codex": ["codex"],
    "claude-code": ["claude-code", "claude code"],
    "gemini-cli": ["gemini-cli", "gemini cli"],
    "qwen-coder": ["qwen-coder", "qwen coder"],
}


# ---------------------------------------------------------------------------
# Score transforms: map raw doc scores to [0, 1] to match Harbor's scale.
# Harbor matrix already has these transforms applied; doc scores are raw.
# ---------------------------------------------------------------------------
SCORE_TRANSFORM_ALGOTUNE = {"algotune"}
SCORE_TRANSFORM_NEGONE_TO_ONE = {"sldbench", "ineqmath"}


def transform_doc_score(score: float, stem: str) -> float:
    """Apply benchmark-specific transform so doc score is on [0, 1]."""
    if stem in SCORE_TRANSFORM_ALGOTUNE:
        # Speedup factor (can be >> 1).  y = ln(max(1, x)) / (ln(max(1, x)) + 1)
        lnx = math.log(max(1.0, score))
        return lnx / (lnx + 1.0) if (lnx + 1.0) != 0 else 0.0
    if stem in SCORE_TRANSFORM_NEGONE_TO_ONE:
        # Raw reward in [-1, 1].  y = (x + 1) / 2
        return (score + 1.0) / 2.0
    return score


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def norm(s: str) -> str:
    """Normalize a model/agent string for matching."""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[_]", "-", s)
    return s


def strip_parenthetical(s: str) -> str:
    """Remove trailing parenthetical like ' (Non-Thinking)' or ' (high)'."""
    return re.sub(r"\s*\(.*?\)\s*$", "", s).strip()


def strip_date_suffix(s: str) -> str:
    """Remove date suffixes like '-2026-03-05' or '-2025-08-07'."""
    return re.sub(r"-\d{4}-\d{2}-\d{2}$", "", s).strip()


def make_model_index(aliases: dict[str, list[str]]) -> dict[str, str]:
    """Build normalized-pattern -> harbor_model lookup."""
    idx: dict[str, str] = {}
    for harbor_model, patterns in aliases.items():
        for p in patterns:
            idx[norm(p)] = norm(harbor_model)
    return idx


def make_agent_index(aliases: dict[str, list[str]]) -> dict[str, str]:
    idx: dict[str, str] = {}
    for harbor_agent, patterns in aliases.items():
        for p in patterns:
            idx[norm(p)] = norm(harbor_agent)
    return idx


def parse_doc_date(s: str) -> tuple[int, int, int]:
    s = (s or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return tuple(map(int, s.split("-")))  # type: ignore[return-value]
    if re.fullmatch(r"\d{4}-\d{2}", s):
        y, m = map(int, s.split("-"))
        return (y, m, 1)
    return (0, 0, 0)


def resolve_stem(column: str, stems: set[str]) -> str | None:
    col = column.strip()
    if col in ("model", "agent"):
        return None
    if col in MATRIX_COLUMN_TO_STEM:
        mapped = MATRIX_COLUMN_TO_STEM[col]
        if mapped is None:
            return None
        return mapped if mapped in stems else None
    cand = col.replace("-", "_")
    return cand if cand in stems else None


@dataclass
class DocRow:
    model_raw: str
    system_raw: str | None
    metric_name: str
    score: float
    model_norm: str = ""
    system_norm: str = ""

    def __post_init__(self):
        self.model_norm = norm(self.model_raw)
        self.system_norm = norm(self.system_raw) if self.system_raw else ""


@dataclass
class DocSlice:
    stem: str
    benchmark_name: str
    primary_metric: str
    aligned_metric: str | None
    slice_date: str
    source_url: str
    rows: list[DocRow] = field(default_factory=list)


def pick_newest_slice(rot: list[dict]) -> dict | None:
    if not rot:
        return None
    best_key, best_idx = (0, 0, 0), 0
    for i, block in enumerate(rot):
        k = parse_doc_date(str(block.get("date", "")))
        if k > best_key:
            best_key, best_idx = k, i
    return rot[best_idx]


def extract_metric_value(
    scores: list[dict], primary: str, aligned: str | None
) -> tuple[float | None, str]:
    if not scores:
        return None, ""
    want = []
    if aligned and aligned.strip():
        want.append(aligned.strip().lower())
    if primary and primary.strip():
        want.append(primary.strip().lower())

    # Pass 1: exact match on metric name
    for w in want:
        for s in scores:
            m = (s.get("metric") or "").strip()
            if m.lower() == w and isinstance(s.get("value"), (int, float)):
                return float(s["value"]), m

    # Pass 2: substring match — e.g. primary="accuracy" matches "accuracy (overall)"
    for w in want:
        for s in scores:
            m = (s.get("metric") or "").strip()
            if w in m.lower() and isinstance(s.get("value"), (int, float)):
                return float(s["value"]), m

    # Pass 3: first numeric score (skip cost/latency-like metrics)
    skip_metrics = {"cost", "latency", "latency mean", "latency_mean"}
    for s in scores:
        m = (s.get("metric") or "").strip().lower()
        if m in skip_metrics:
            continue
        if isinstance(s.get("value"), (int, float)):
            return float(s["value"]), str(s.get("metric", ""))

    # Final fallback
    for s in scores:
        if isinstance(s.get("value"), (int, float)):
            return float(s["value"]), str(s.get("metric", ""))
    return None, ""


def load_doc_slice(path: Path) -> DocSlice:
    data = json.loads(path.read_text())
    stem = path.stem
    ev = data.get("evaluation") or {}
    primary = str(ev.get("primary_metric") or "").strip()
    aligned = ev.get("harbor_aligned_metric")
    if aligned:
        aligned_clean = re.split(r"[.;]", str(aligned))[0].strip()
        if not aligned_clean:
            aligned = None
        else:
            aligned = aligned_clean

    rot = data.get("results_over_time") or []
    block = pick_newest_slice(rot)
    if block is None:
        return DocSlice(
            stem=stem,
            benchmark_name=str(data.get("name") or stem),
            primary_metric=primary,
            aligned_metric=aligned,
            slice_date="",
            source_url="",
        )

    rows: list[DocRow] = []
    for r in block.get("results") or []:
        model = str(r.get("model") or "").strip()
        if not model:
            continue
        system = r.get("system_description")
        if system is not None:
            system = str(system).strip() or None
        val, mname = extract_metric_value(r.get("scores") or [], primary, aligned)
        if val is None:
            continue
        val = transform_doc_score(val, stem)
        rows.append(DocRow(model_raw=model, system_raw=system, metric_name=mname, score=val))

    return DocSlice(
        stem=stem,
        benchmark_name=str(data.get("name") or stem),
        primary_metric=primary,
        aligned_metric=aligned,
        slice_date=str(block.get("date", "")),
        source_url=str(block.get("source_url", "")),
        rows=rows,
    )


def try_match_model(harbor_model_norm: str, doc_model_norm: str, model_idx: dict[str, str]) -> bool:
    """Check if a doc model name maps to the same harbor model."""
    if harbor_model_norm == doc_model_norm:
        return True
    # Try stripping parenthetical / date suffixes from doc name
    candidates = [
        doc_model_norm,
        strip_parenthetical(doc_model_norm),
        strip_date_suffix(doc_model_norm),
        strip_date_suffix(strip_parenthetical(doc_model_norm)),
    ]
    for c in candidates:
        cn = norm(c)
        mapped = model_idx.get(cn)
        if mapped == harbor_model_norm:
            return True
    return False


def try_match_agent(harbor_agent_norm: str, doc_system_norm: str, agent_idx: dict[str, str]) -> bool:
    if not doc_system_norm:
        return False
    if harbor_agent_norm == doc_system_norm:
        return True
    mapped = agent_idx.get(doc_system_norm)
    return mapped == harbor_agent_norm


def find_doc_match(
    harbor_model: str,
    harbor_agent: str,
    doc: DocSlice,
    model_idx: dict[str, str],
    agent_idx: dict[str, str],
) -> tuple[float | None, str, str, str, str]:
    """
    Returns (score_doc_transformed, doc_model_raw, doc_system_raw, metric_used, match_status).
    Doc scores are already transformed to [0,1] at load time.
    Priority: exact (model+agent) > model_only (agent unmatched/null in doc).
    """
    if not doc.rows:
        return None, "", "", "", "no_doc_data"

    hm = norm(harbor_model)
    ha = norm(harbor_agent)

    model_matches: list[DocRow] = []
    for row in doc.rows:
        if try_match_model(hm, row.model_norm, model_idx):
            model_matches.append(row)

    if not model_matches:
        return None, "", "", "", "no_model_match"

    # Try exact model + agent match
    for row in model_matches:
        if row.system_raw and try_match_agent(ha, row.system_norm, agent_idx):
            return row.score, row.model_raw, row.system_raw or "", row.metric_name, "matched_model_and_agent"

    # Fall back: model matched, agent either null in doc or mismatch
    # Prefer rows where system_description is null (pure LLM baseline)
    null_system = [r for r in model_matches if not r.system_raw]
    if null_system:
        row = null_system[0]
        return row.score, row.model_raw, "", row.metric_name, "matched_model_only_doc_no_agent"

    # All doc rows have a system_description but none matched harbor agent
    row = model_matches[0]
    return row.score, row.model_raw, row.system_raw or "", row.metric_name, "matched_model_agent_mismatch"


def main() -> None:
    root = repo_root()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    from quantitative_study.pipeline.analysis import (
        build_comparison_long,
        build_comparison_summary,
    )
    from quantitative_study.pipeline.loading import (
        load_all_docs,
        load_harbor_matrix,
        load_metric_alignment,
    )

    p = argparse.ArgumentParser(description="Harbor vs original benchmark score comparison.")
    p.add_argument("--harbor-csv", type=Path, default=None)
    p.add_argument("--benchmark-info-dir", type=Path, default=root / "benchmark_info_jobs")
    p.add_argument("--out", type=Path, default=root / "output" / "quantitative" / "harbor_vs_doc_long.csv")
    p.add_argument("--summary-out", type=Path, default=root / "output" / "quantitative" / "harbor_vs_doc_summary.csv")
    args = p.parse_args()

    df = load_harbor_matrix(args.harbor_csv)
    alignments = load_metric_alignment()
    docs = load_all_docs(args.benchmark_info_dir, alignments)

    out_df = build_comparison_long(df, docs, alignments)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(args.out, index=False)

    # ---- Summary statistics ----
    counts = out_df["match_status"].value_counts()
    matched = out_df[out_df["match_status"].str.startswith("matched")]
    has_delta = matched.dropna(subset=["delta"])

    print(f"Wrote {args.out}  ({len(out_df)} rows total)")
    print(f"\nmatch_status breakdown:")
    for status, n in counts.items():
        print(f"  {status:40s} {n:5d}")

    print(f"\nRows with delta (both scores present): {len(has_delta)}")

    if not has_delta.empty:
        summary = build_comparison_summary(out_df)
        summary.to_csv(args.summary_out, index=False)
        print(f"\nWrote summary: {args.summary_out}  ({len(summary)} rows)")
        print(f"\n{'='*100}")
        print("TOP DELTAS (Harbor - Original):")
        print(f"{'='*100}")
        cols = ["benchmark", "model", "harbor_agent", "score_harbor", "score_doc", "delta", "match_status"]
        print(summary[cols].to_string(index=False))
    else:
        print("\nNo deltas to summarize.")


if __name__ == "__main__":
    main()
