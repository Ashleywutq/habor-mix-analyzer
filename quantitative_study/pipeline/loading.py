"""
Data loading: Harbor CSV matrix and benchmark_info_jobs/*.json files.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd

from .config import (
    BENCHMARK_INFO_DIR,
    HARBOR_CSV_CANDIDATES,
    METRIC_ALIGNMENT_PATH,
)


def norm(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[_]", "-", s)
    return s


# ---------------------------------------------------------------------------
# Harbor matrix
# ---------------------------------------------------------------------------

def load_harbor_matrix(path: Path | None = None) -> pd.DataFrame:
    if path is None:
        for c in HARBOR_CSV_CANDIDATES:
            if c.is_file():
                path = c
                break
    if path is None or not path.is_file():
        raise FileNotFoundError(f"Harbor CSV not found; tried {HARBOR_CSV_CANDIDATES}")
    return pd.read_csv(path)


def harbor_to_long(df: pd.DataFrame) -> pd.DataFrame:
    return df.melt(
        id_vars=["model", "agent"],
        var_name="matrix_column",
        value_name="score_harbor",
    )


# ---------------------------------------------------------------------------
# Doc JSON structures
# ---------------------------------------------------------------------------

@dataclass
class MetricAlignment:
    matrix_column: str
    info_stem: str
    benchmark_name: str
    harbor_metric: str
    doc_score_field: str
    doc_metric: str
    alignment_status: str
    transform: str
    include_in_comparison: bool
    evidence_level: str
    reviewer: str
    review_date: str
    notes: str


@dataclass
class DocRow:
    model_raw: str
    effort_raw: str | None
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
    alignment: MetricAlignment | None
    slice_date: str
    source_url: str
    rows: list[DocRow] = field(default_factory=list)


def load_metric_alignment(path: Path | None = None) -> dict[str, MetricAlignment]:
    path = path or METRIC_ALIGNMENT_PATH
    if not path.is_file():
        raise FileNotFoundError(f"Benchmark metric alignment CSV not found: {path}")

    df = pd.read_csv(path, dtype=str).fillna("")
    required = {
        "matrix_column", "info_stem", "benchmark_name", "harbor_metric",
        "doc_score_field", "doc_metric", "alignment_status", "transform",
        "include_in_comparison", "evidence_level", "reviewer", "review_date",
        "notes",
    }
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(f"Alignment CSV is missing columns: {missing}")

    alignments: dict[str, MetricAlignment] = {}
    for _, row in df.iterrows():
        matrix_column = str(row["matrix_column"]).strip()
        if not matrix_column:
            continue
        if matrix_column in alignments:
            raise ValueError(f"Duplicate alignment row for {matrix_column}")
        include = str(row["include_in_comparison"]).strip().lower() == "true"
        alignments[matrix_column] = MetricAlignment(
            matrix_column=matrix_column,
            info_stem=str(row["info_stem"]).strip(),
            benchmark_name=str(row["benchmark_name"]).strip(),
            harbor_metric=str(row["harbor_metric"]).strip(),
            doc_score_field=str(row["doc_score_field"]).strip(),
            doc_metric=str(row["doc_metric"]).strip(),
            alignment_status=str(row["alignment_status"]).strip(),
            transform=str(row["transform"]).strip() or "identity",
            include_in_comparison=include,
            evidence_level=str(row["evidence_level"]).strip(),
            reviewer=str(row["reviewer"]).strip(),
            review_date=str(row["review_date"]).strip(),
            notes=str(row["notes"]).strip(),
        )
    return alignments


def _apply_alignment_transform(value: float, transform: str) -> float:
    transform = (transform or "identity").strip()
    if transform == "identity":
        return value
    if not transform.startswith("lambda x:"):
        raise ValueError(f"Transform must be identity or a lambda expression: {transform}")

    safe_names = {"math": math, "max": max, "min": min, "abs": abs, "float": float}
    fn = eval(  # noqa: S307 - alignment CSV is repo-local reviewed metadata.
        transform,
        {"__builtins__": {}, **safe_names},
        {},
    )
    if not callable(fn):
        raise ValueError(f"Transform did not evaluate to a callable: {transform}")
    return float(fn(value))


# ---------------------------------------------------------------------------
# JSON parsing helpers
# ---------------------------------------------------------------------------

def _parse_doc_date(s: str) -> tuple[int, int, int]:
    s = (s or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return tuple(map(int, s.split("-")))  # type: ignore[return-value]
    if re.fullmatch(r"\d{4}-\d{2}", s):
        y, m = map(int, s.split("-"))
        return (y, m, 1)
    return (0, 0, 0)


def _pick_newest_slice(rot: list[dict]) -> dict | None:
    if not rot:
        return None
    best_key, best_idx = (0, 0, 0), 0
    for i, block in enumerate(rot):
        k = _parse_doc_date(str(block.get("date", "")))
        if k > best_key:
            best_key, best_idx = k, i
    return rot[best_idx]


def _row_has_alignment_metric(row: dict, alignment: MetricAlignment) -> bool:
    if alignment.doc_score_field == "score":
        return alignment.doc_metric == "legacy_score" and isinstance(row.get("score"), (int, float))
    if alignment.doc_score_field != "scores[].value" or not alignment.doc_metric:
        return False
    return any(
        str(score.get("metric") or "").strip() == alignment.doc_metric
        and isinstance(score.get("value"), (int, float))
        for score in row.get("scores") or []
    )


def _pick_newest_slice_with_metric(
    rot: list[dict],
    alignment: MetricAlignment | None,
) -> dict | None:
    if not alignment or not alignment.include_in_comparison:
        return _pick_newest_slice(rot)

    candidates = [
        block for block in rot
        if any(_row_has_alignment_metric(row, alignment) for row in block.get("results") or [])
    ]
    return _pick_newest_slice(candidates) if candidates else _pick_newest_slice(rot)


def _extract_metric_value(row: dict, alignment: MetricAlignment) -> tuple[float | None, str]:
    if alignment.doc_score_field == "score":
        value = row.get("score")
        if isinstance(value, (int, float)) and alignment.doc_metric == "legacy_score":
            return float(value), "legacy_score"
        return None, ""

    if alignment.doc_score_field != "scores[].value" or not alignment.doc_metric:
        return None, ""

    for score in row.get("scores") or []:
        metric = str(score.get("metric") or "").strip()
        value = score.get("value")
        if metric == alignment.doc_metric and isinstance(value, (int, float)):
            return float(value), metric
    return None, ""


def load_doc_slice(path: Path, alignment: MetricAlignment | None = None) -> DocSlice:
    data = json.loads(path.read_text())
    stem = path.stem
    ev = data.get("evaluation") or {}
    primary = str(ev.get("primary_metric") or "").strip()

    rot = data.get("results_over_time") or []
    block = _pick_newest_slice_with_metric(rot, alignment)
    if block is None:
        return DocSlice(stem=stem, benchmark_name=str(data.get("name") or stem),
                        primary_metric=primary, alignment=alignment,
                        slice_date="", source_url="")

    rows: list[DocRow] = []
    if alignment and alignment.include_in_comparison:
        for r in block.get("results") or []:
            model = str(r.get("model") or "").strip()
            if not model:
                continue
            system = r.get("system_description")
            if system is not None:
                system = str(system).strip() or None
            effort = r.get("effort")
            if effort is not None:
                effort = str(effort).strip() or None
            val, mname = _extract_metric_value(r, alignment)
            if val is None:
                continue
            val = _apply_alignment_transform(val, alignment.transform)
            rows.append(DocRow(
                model_raw=model, effort_raw=effort, system_raw=system,
                metric_name=mname, score=val,
            ))

    return DocSlice(
        stem=stem, benchmark_name=str(data.get("name") or stem),
        primary_metric=primary, alignment=alignment,
        slice_date=str(block.get("date", "")),
        source_url=str(block.get("source_url", "")),
        rows=rows,
    )


def load_all_docs(
    info_dir: Path | None = None,
    alignments: dict[str, MetricAlignment] | None = None,
) -> dict[str, DocSlice]:
    info_dir = info_dir or BENCHMARK_INFO_DIR
    alignment_by_stem = {
        alignment.info_stem: alignment
        for alignment in (alignments or {}).values()
        if alignment.info_stem
    }
    docs: dict[str, DocSlice] = {}
    for p in sorted(info_dir.glob("*.json")):
        docs[p.stem] = load_doc_slice(p, alignment_by_stem.get(p.stem))
    return docs
