#!/usr/bin/env python3
"""
Summarize overlap between benchmark_info_jobs model/agent metadata and Harbor.

The script answers two related questions:
  * How many benchmark JSON files are marked as evaluating LLMs or agents?
  * Among their recorded bare-LLM models / agent system descriptions, how many
    overlap with the models and agents present in Harbor's benchmark matrix?

Outputs are written to output/quantitative/ by default.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


ROOT = repo_root()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from quantitative_study.pipeline.config import (  # noqa: E402
    AGENT_ALIASES,
    HARBOR_CSV_CANDIDATES,
    MATRIX_COLUMN_TO_STEM,
    MODEL_ALIASES,
    OUTPUT_DIR,
)


VALID_USED_VALUES = {"llm", "agent", "both"}
LIST_SEP = "; "

# Practical aliases seen in benchmark_info_jobs system_description values.
# These extend the central config without changing score-comparison behavior.
AGENT_ALIAS_EXTENSIONS: dict[str, list[str]] = {
    "codex": [
        "codex cli",
        "openai codex cli",
        "simple codex",
    ],
    "claude-code": [
        "claude agent sdk",
    ],
}


def norm(value: Any) -> str:
    text = html.unescape(str(value)).strip().lower()
    text = re.sub(r"[_]", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text


def strip_parenthetical(value: str) -> str:
    return re.sub(r"\s*\(.*?\)\s*$", "", value).strip()


def strip_date_suffix(value: str) -> str:
    return re.sub(r"-\d{4}-\d{2}-\d{2}$", "", value).strip()


def sorted_join(values: set[str] | list[str]) -> str:
    return LIST_SEP.join(sorted(values, key=lambda x: x.lower()))


def clean_optional_string(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_used(value: Any) -> str:
    used = norm(value)
    return used if used in VALID_USED_VALUES else ""


def first_existing(paths: list[Path]) -> Path:
    for path in paths:
        if path.is_file():
            return path
    tried = ", ".join(str(path) for path in paths)
    raise FileNotFoundError(f"Could not find Harbor CSV; tried: {tried}")


def read_harbor_matrix(path: Path) -> tuple[set[str], set[str], list[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        models: set[str] = set()
        agents: set[str] = set()
        for row in reader:
            model = clean_optional_string(row.get("model"))
            agent = clean_optional_string(row.get("agent"))
            if model:
                models.add(norm(model))
            if agent:
                agents.add(norm(agent))
    return models, agents, columns


def build_matrix_stem_mapping(columns: list[str], json_stems: set[str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for column in columns:
        if column in {"model", "agent"}:
            continue
        candidates: list[str] = []
        configured = MATRIX_COLUMN_TO_STEM.get(column)
        if configured:
            candidates.append(configured)
        # For metadata overlap, direct stem matches are useful even when a
        # metric-comparison mapping explicitly skips a benchmark.
        candidates.append(column.replace("-", "_"))
        for stem in candidates:
            if stem in json_stems:
                mapping.setdefault(stem, column)
    return mapping


def build_alias_index(
    aliases: dict[str, list[str]],
    extensions: dict[str, list[str]] | None = None,
) -> dict[str, str]:
    index: dict[str, str] = {}
    extensions = extensions or {}
    for canonical, patterns in aliases.items():
        for pattern in [canonical, *patterns, *extensions.get(canonical, [])]:
            index[norm(pattern)] = norm(canonical)
    return index


def model_candidates(raw_model: str) -> list[str]:
    normalized = norm(raw_model)
    candidates = [
        normalized,
        strip_parenthetical(normalized),
        strip_date_suffix(normalized),
        strip_date_suffix(strip_parenthetical(normalized)),
    ]
    return list(dict.fromkeys(norm(candidate) for candidate in candidates if candidate))


def agent_candidates(raw_system: str) -> list[str]:
    normalized = norm(raw_system)
    candidates = [
        normalized,
        strip_parenthetical(normalized),
        norm(re.split(r"[;,]", normalized)[0]),
    ]
    return list(dict.fromkeys(candidate for candidate in candidates if candidate))


def match_model(raw_model: str, harbor_models: set[str], model_index: dict[str, str]) -> str:
    for candidate in model_candidates(raw_model):
        if candidate in harbor_models:
            return candidate
        mapped = model_index.get(candidate, "")
        if mapped in harbor_models:
            return mapped
    return ""


def match_agent(raw_system: str, harbor_agents: set[str], agent_index: dict[str, str]) -> str:
    for candidate in agent_candidates(raw_system):
        if candidate in harbor_agents:
            return candidate
        mapped = agent_index.get(candidate, "")
        if mapped in harbor_agents:
            return mapped

    normalized = norm(raw_system)
    phrase_rules = [
        ("claude-code", r"(^|[^a-z0-9])claude[- ]code(@|$|[^a-z0-9])"),
        ("gemini-cli", r"(^|[^a-z0-9])gemini[- ]cli($|[^a-z0-9])"),
        ("terminus-2", r"(^|[^a-z0-9])terminus[- ]2(@|$|[^a-z0-9])"),
    ]
    for canonical, pattern in phrase_rules:
        if canonical in harbor_agents and re.search(pattern, normalized):
            return canonical

    codex_pattern = r"(^|[^a-z0-9])codex(@| cli|-[0-9]| [0-9]|$|[^a-z0-9])"
    if "codex" in harbor_agents and (
        "openai codex cli" in normalized or re.search(codex_pattern, normalized)
    ):
        return "codex"

    return ""


def iter_result_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for block in data.get("results_over_time") or []:
        for row in block.get("results") or []:
            if isinstance(row, dict):
                rows.append(row)
    return rows


def collect_benchmark_row(
    path: Path,
    matrix_column: str,
    harbor_models: set[str],
    harbor_agents: set[str],
    model_index: dict[str, str],
    agent_index: dict[str, str],
) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    used_raw = clean_optional_string(data.get("used_llm_or_agent"))
    used = normalize_used(used_raw)
    result_blocks = data.get("results_over_time") or []
    result_rows = iter_result_rows(data)

    llm_names: set[str] = set()
    agent_names: set[str] = set()
    llm_matches: dict[str, set[str]] = defaultdict(set)
    agent_matches: dict[str, set[str]] = defaultdict(set)
    bare_llm_rows = 0
    agent_rows = 0

    for result in result_rows:
        model = clean_optional_string(result.get("model"))
        system = clean_optional_string(result.get("system_description"))

        if model and not system:
            bare_llm_rows += 1
            llm_names.add(model)
            matched_model = match_model(model, harbor_models, model_index)
            if matched_model:
                llm_matches[model].add(matched_model)

        if system:
            agent_rows += 1
            agent_names.add(system)
            matched_agent = match_agent(system, harbor_agents, agent_index)
            if matched_agent:
                agent_matches[system].add(matched_agent)

    llm_overlap_harbor = {
        matched for matches in llm_matches.values() for matched in matches
    }
    agent_overlap_harbor = {
        matched for matches in agent_matches.values() for matched in matches
    }

    return {
        "stem": path.stem,
        "name": clean_optional_string(data.get("name")) or path.stem,
        "used_llm_or_agent": used_raw,
        "used_llm_or_agent_normalized": used,
        "has_harbor_matrix_column": bool(matrix_column),
        "harbor_matrix_column": matrix_column,
        "has_llm_flag": used in {"llm", "both"},
        "has_agent_flag": used in {"agent", "both"},
        "n_result_time_blocks": len(result_blocks),
        "n_result_rows": len(result_rows),
        "n_bare_llm_result_rows": bare_llm_rows,
        "n_agent_result_rows": agent_rows,
        "n_unique_bare_llm_names": len(llm_names),
        "n_unique_bare_llm_names_overlapping_harbor": len(llm_matches),
        "n_unique_system_descriptions": len(agent_names),
        "n_unique_system_descriptions_overlapping_harbor": len(agent_matches),
        "overlapping_harbor_models": sorted_join(llm_overlap_harbor),
        "overlapping_bare_llm_names": sorted_join(set(llm_matches)),
        "overlapping_harbor_agents": sorted_join(agent_overlap_harbor),
        "overlapping_system_descriptions": sorted_join(set(agent_matches)),
        "_llm_names": llm_names,
        "_agent_names": agent_names,
        "_llm_matches": llm_matches,
        "_agent_matches": agent_matches,
    }


def summarize(scope: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    used_counts = Counter(row["used_llm_or_agent_normalized"] or "invalid_or_blank" for row in rows)

    llm_names: set[str] = set()
    llm_overlap_names: set[str] = set()
    llm_overlap_harbor: set[str] = set()
    agent_names: set[str] = set()
    agent_overlap_names: set[str] = set()
    agent_overlap_harbor: set[str] = set()

    for row in rows:
        if row["has_llm_flag"]:
            llm_names.update(row["_llm_names"])
            llm_overlap_names.update(row["_llm_matches"])
            for matches in row["_llm_matches"].values():
                llm_overlap_harbor.update(matches)
        if row["has_agent_flag"]:
            agent_names.update(row["_agent_names"])
            agent_overlap_names.update(row["_agent_matches"])
            for matches in row["_agent_matches"].values():
                agent_overlap_harbor.update(matches)

    return {
        "scope": scope,
        "total_benchmarks": len(rows),
        "field_llm": used_counts["llm"],
        "field_agent": used_counts["agent"],
        "field_both": used_counts["both"],
        "field_invalid_or_blank": used_counts["invalid_or_blank"],
        "benchmarks_used_llm": sum(row["has_llm_flag"] for row in rows),
        "benchmarks_used_llm_with_model_overlap": sum(
            row["has_llm_flag"] and bool(row["_llm_matches"]) for row in rows
        ),
        "unique_bare_llm_names": len(llm_names),
        "unique_bare_llm_names_overlapping_harbor": len(llm_overlap_names),
        "unique_harbor_models_overlapped": len(llm_overlap_harbor),
        "harbor_models_overlapped": sorted_join(llm_overlap_harbor),
        "benchmarks_used_agent": sum(row["has_agent_flag"] for row in rows),
        "benchmarks_used_agent_with_agent_overlap": sum(
            row["has_agent_flag"] and bool(row["_agent_matches"]) for row in rows
        ),
        "unique_system_descriptions": len(agent_names),
        "unique_system_descriptions_overlapping_harbor": len(agent_overlap_names),
        "unique_harbor_agents_overlapped": len(agent_overlap_harbor),
        "harbor_agents_overlapped": sorted_join(agent_overlap_harbor),
    }


def build_benchmark_perspective_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    valid_rows = [
        row for row in rows
        if row["used_llm_or_agent_normalized"] in VALID_USED_VALUES
    ]
    valid_stems = {row["stem"] for row in valid_rows}

    llm_total = {row["stem"] for row in valid_rows if row["has_llm_flag"]}
    agent_total = {row["stem"] for row in valid_rows if row["has_agent_flag"]}

    llm_overlap = {
        row["stem"] for row in valid_rows
        if row["has_llm_flag"] and bool(row["_llm_matches"])
    }
    agent_overlap = {
        row["stem"] for row in valid_rows
        if row["has_agent_flag"] and bool(row["_agent_matches"])
    }

    llm_non_harbor = {
        row["stem"] for row in valid_rows
        if row["has_llm_flag"] and len(row["_llm_names"]) > len(row["_llm_matches"])
    }
    agent_non_harbor = {
        row["stem"] for row in valid_rows
        if row["has_agent_flag"] and len(row["_agent_names"]) > len(row["_agent_matches"])
    }

    return [
        {
            "benchmark_group": "measured_llm",
            "has_harbor_overlap": len(llm_overlap),
            "has_non_harbor": len(llm_non_harbor),
            "total_benchmarks": len(llm_total),
        },
        {
            "benchmark_group": "measured_agent",
            "has_harbor_overlap": len(agent_overlap),
            "has_non_harbor": len(agent_non_harbor),
            "total_benchmarks": len(agent_total),
        },
        {
            "benchmark_group": "total_unique_benchmarks",
            "has_harbor_overlap": len(llm_overlap | agent_overlap),
            "has_non_harbor": len(llm_non_harbor | agent_non_harbor),
            "total_benchmarks": len(valid_stems),
        },
    ]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def build_name_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}

    def entry(kind: str, source_name: str) -> dict[str, Any]:
        key = (kind, source_name)
        if key not in index:
            index[key] = {
                "kind": kind,
                "source_name": source_name,
                "matched_harbor_name": set(),
                "benchmarks": set(),
                "harbor_mapped_benchmarks": set(),
            }
        return index[key]

    for row in rows:
        stem = row["stem"]
        mapped = row["has_harbor_matrix_column"]
        for name in row["_llm_names"]:
            record = entry("bare_llm_model", name)
            record["benchmarks"].add(stem)
            if mapped:
                record["harbor_mapped_benchmarks"].add(stem)
            record["matched_harbor_name"].update(row["_llm_matches"].get(name, set()))
        for name in row["_agent_names"]:
            record = entry("agent_system_description", name)
            record["benchmarks"].add(stem)
            if mapped:
                record["harbor_mapped_benchmarks"].add(stem)
            record["matched_harbor_name"].update(row["_agent_matches"].get(name, set()))

    output_rows: list[dict[str, Any]] = []
    for record in index.values():
        matched = record["matched_harbor_name"]
        benchmarks = record["benchmarks"]
        mapped_benchmarks = record["harbor_mapped_benchmarks"]
        output_rows.append({
            "kind": record["kind"],
            "source_name": record["source_name"],
            "has_overlap": bool(matched),
            "matched_harbor_name": sorted_join(matched),
            "n_benchmarks": len(benchmarks),
            "benchmarks": sorted_join(benchmarks),
            "n_harbor_mapped_benchmarks": len(mapped_benchmarks),
            "harbor_mapped_benchmarks": sorted_join(mapped_benchmarks),
        })

    return sorted(output_rows, key=lambda row: (row["kind"], row["source_name"].lower()))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize LLM/agent overlap between benchmark_info_jobs and Harbor."
    )
    parser.add_argument("--harbor-csv", type=Path, default=None)
    parser.add_argument("--benchmark-info-dir", type=Path, default=ROOT / "benchmark_info_jobs")
    parser.add_argument("--out-dir", type=Path, default=OUTPUT_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    harbor_csv = args.harbor_csv or first_existing(HARBOR_CSV_CANDIDATES)
    info_dir = args.benchmark_info_dir
    json_paths = sorted(info_dir.glob("*.json"))
    if not json_paths:
        raise FileNotFoundError(f"No benchmark JSON files found in {info_dir}")

    json_stems = {path.stem for path in json_paths}
    harbor_models, harbor_agents, matrix_columns = read_harbor_matrix(harbor_csv)
    stem_to_matrix = build_matrix_stem_mapping(matrix_columns, json_stems)
    model_index = build_alias_index(MODEL_ALIASES)
    agent_index = build_alias_index(AGENT_ALIASES, AGENT_ALIAS_EXTENSIONS)

    benchmark_rows = [
        collect_benchmark_row(
            path=path,
            matrix_column=stem_to_matrix.get(path.stem, ""),
            harbor_models=harbor_models,
            harbor_agents=harbor_agents,
            model_index=model_index,
            agent_index=agent_index,
        )
        for path in json_paths
    ]

    summary_rows = [
        summarize("all_json", benchmark_rows),
        summarize(
            "mapped_to_harbor_matrix",
            [row for row in benchmark_rows if row["has_harbor_matrix_column"]],
        ),
    ]

    out_dir = args.out_dir
    summary_path = out_dir / "benchmark_llm_agent_overlap_summary.csv"
    benchmark_path = out_dir / "benchmark_llm_agent_overlap_by_benchmark.csv"
    names_path = out_dir / "benchmark_llm_agent_overlap_names.csv"
    perspective_path = out_dir / "benchmark_llm_agent_overlap_3x3.csv"

    summary_fields = [
        "scope",
        "total_benchmarks",
        "field_llm",
        "field_agent",
        "field_both",
        "field_invalid_or_blank",
        "benchmarks_used_llm",
        "benchmarks_used_llm_with_model_overlap",
        "unique_bare_llm_names",
        "unique_bare_llm_names_overlapping_harbor",
        "unique_harbor_models_overlapped",
        "harbor_models_overlapped",
        "benchmarks_used_agent",
        "benchmarks_used_agent_with_agent_overlap",
        "unique_system_descriptions",
        "unique_system_descriptions_overlapping_harbor",
        "unique_harbor_agents_overlapped",
        "harbor_agents_overlapped",
    ]
    benchmark_fields = [
        "stem",
        "name",
        "used_llm_or_agent",
        "used_llm_or_agent_normalized",
        "has_harbor_matrix_column",
        "harbor_matrix_column",
        "has_llm_flag",
        "has_agent_flag",
        "n_result_time_blocks",
        "n_result_rows",
        "n_bare_llm_result_rows",
        "n_agent_result_rows",
        "n_unique_bare_llm_names",
        "n_unique_bare_llm_names_overlapping_harbor",
        "n_unique_system_descriptions",
        "n_unique_system_descriptions_overlapping_harbor",
        "overlapping_harbor_models",
        "overlapping_bare_llm_names",
        "overlapping_harbor_agents",
        "overlapping_system_descriptions",
    ]
    name_fields = [
        "kind",
        "source_name",
        "has_overlap",
        "matched_harbor_name",
        "n_benchmarks",
        "benchmarks",
        "n_harbor_mapped_benchmarks",
        "harbor_mapped_benchmarks",
    ]
    perspective_fields = [
        "benchmark_group",
        "has_harbor_overlap",
        "has_non_harbor",
        "total_benchmarks",
    ]

    write_csv(summary_path, summary_rows, summary_fields)
    write_csv(benchmark_path, benchmark_rows, benchmark_fields)
    write_csv(names_path, build_name_rows(benchmark_rows), name_fields)
    write_csv(
        perspective_path,
        build_benchmark_perspective_rows(benchmark_rows),
        perspective_fields,
    )

    print(f"Wrote {summary_path}")
    print(f"Wrote {benchmark_path}")
    print(f"Wrote {names_path}")
    print(f"Wrote {perspective_path}")
    print()
    for row in summary_rows:
        print(
            f"{row['scope']}: "
            f"LLM benchmarks {row['benchmarks_used_llm']} "
            f"({row['benchmarks_used_llm_with_model_overlap']} with Harbor model overlap); "
            f"agent benchmarks {row['benchmarks_used_agent']} "
            f"({row['benchmarks_used_agent_with_agent_overlap']} with Harbor agent overlap)."
        )


if __name__ == "__main__":
    main()
