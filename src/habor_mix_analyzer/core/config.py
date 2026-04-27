from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed" / "intermediate"

OUTPUT_DIR = ROOT / "output"
INTERMEDIATE_STUDY_DIR = OUTPUT_DIR / "intermediate_studies"
BENCHMARK_INTERMEDIATE_STUDY_DIR = INTERMEDIATE_STUDY_DIR / "benchmark_level"
TASK_INTERMEDIATE_STUDY_DIR = INTERMEDIATE_STUDY_DIR / "task_level"

KEY_ANALYSIS_DIR = OUTPUT_DIR / "key_analyses"
KEY_TABLE_DIR = KEY_ANALYSIS_DIR / "tables"
KEY_FIGURE_DIR = KEY_ANALYSIS_DIR / "figures"
KEY_REPORT_DIR = KEY_ANALYSIS_DIR / "reports"

KEY_COLUMNS = ["model", "agent"]
RANDOM_SEED = 42

RELATIVE_SCORE_LABEL = "Benchmark-relative score (0 = benchmark median; +1 = one robust scale above median)"
DELTA_SCORE_LABEL = "Benchmark-relative score change\nvs terminus-2"

BASELINE_AGENT = "terminus-2"

MANUALLY_EXCLUDED_BENCHMARKS: set[str] = {
    "crmarena",
}

MODEL_FAMILIES: dict[str, list[str]] = {
    "OpenAI": ["gpt-5.4", "gpt-5-mini", "gpt-5-nano"],
    "Anthropic": ["claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5-20251001"],
    "Google": ["gemini-3.1-pro-preview", "gemini-3-flash-preview"],
    "DeepSeek": ["deepseek-reasoner", "deepseek-chat"],
    "Moonshot": ["kimi-k2.5"],
    "MiniMax": ["MiniMax-M2.5"],
    "Zhipu": ["glm-5"],
    "Xiaomi": ["mimo-v2-pro"],
    "Alibaba": ["qwen3-max"],
}

MODEL_TO_FAMILY: dict[str, str] = {
    model: family for family, models in MODEL_FAMILIES.items() for model in models
}

BENCHMARK_DOMAIN: dict[str, str] = {
    # Software Engineering
    "aider-polyglot": "Software Engineering",
    "algotune": "Software Engineering",
    "bigcodebench": "Software Engineering",
    "compilebench": "Software Engineering",
    "crustbench": "Software Engineering",
    "devopsgym": "Software Engineering",
    "featbench": "Software Engineering",
    "featurebench-modal": "Software Engineering",
    "gso": "Software Engineering",
    "humanevalfix": "Software Engineering",
    "livecodebench": "Software Engineering",
    "multi-swe-bench": "Software Engineering",
    "quixbugs": "Software Engineering",
    "swe-lancer": "Software Engineering",
    "swebench-multilingual": "Software Engineering",
    "swebench-verified": "Software Engineering",
    "swebenchpro": "Software Engineering",
    "swegym": "Software Engineering",
    "swesmith": "Software Engineering",
    "swtbench": "Software Engineering",
    "usaco": "Software Engineering",
    # Mathematics & Reasoning
    "aime": "Mathematics & Reasoning",
    "arc-agi-2": "Mathematics & Reasoning",
    "ineqmath": "Mathematics & Reasoning",
    "kumo": "Mathematics & Reasoning",
    "omnimath": "Mathematics & Reasoning",
    "reasoning-gym": "Mathematics & Reasoning",
    # Knowledge & Long Context
    "gpqa-diamond": "Knowledge & Long Context",
    "hle": "Knowledge & Long Context",
    "mmmlu": "Knowledge & Long Context",
    "simpleqa": "Knowledge & Long Context",
    # Scientific Research
    "bixbench": "Scientific Research",
    "codepde": "Scientific Research",
    "labbench": "Scientific Research",
    "mlgym": "Scientific Research",
    "qcircuitbench": "Scientific Research",
    "replicationbench": "Scientific Research",
    "research-code-bench": "Scientific Research",
    "scicode": "Scientific Research",
    "sldbench": "Scientific Research",
    # Agents, Tools & Systems
    "bfcl": "Agents, Tools & Systems",
    "deepsynth": "Agents, Tools & Systems",
    "gaia": "Agents, Tools & Systems",
    "gaia2": "Agents, Tools & Systems",
    "seal0": "Agents, Tools & Systems",
    "skillsbench": "Agents, Tools & Systems",
    "terminal-bench": "Agents, Tools & Systems",
    "widesearch": "Agents, Tools & Systems",
    # Data & Analytics
    "dacode": "Data & Analytics",
    "spider2": "Data & Analytics",
    # Professional Domains
    "crmarena": "Professional Domains",
    "financeagent_terminal": "Professional Domains",
    "lawbench": "Professional Domains",
    "medagentbench": "Professional Domains",
    "pixiu": "Professional Domains",
    "spreadsheetbench": "Professional Domains",
    # Safety & Security
    "strongreject": "Safety & Security",
    # Multimodal
    "mmau": "Multimodal",
}

BENCHMARK_DISPLAY_NAME: dict[str, str] = {
    # Software Engineering
    "aider-polyglot": "Aider Polyglot",
    "algotune": "AlgoTune",
    "bigcodebench": "BigCodeBench",
    "compilebench": "CompileBench",
    "crustbench": "CRUST-Bench",
    "devopsgym": "DevOpsGym",
    "featbench": "FeatBench",
    "featurebench-modal": "FeatureBench",
    "gso": "GSO",
    "humanevalfix": "HumanEvalFix",
    "livecodebench": "LiveCodeBench",
    "multi-swe-bench": "Multi-SWE-bench",
    "quixbugs": "QuixBugs",
    "swe-lancer": "SWE-Lancer",
    "swebench-multilingual": "SWE-bench Multilingual",
    "swebench-verified": "SWE-bench Verified",
    "swebenchpro": "SWE-bench Pro",
    "swegym": "SWEGym",
    "swesmith": "SWE-smith",
    "swtbench": "SWT-Bench",
    "usaco": "USACO",
    # Mathematics & Reasoning
    "aime": "AIME",
    "arc-agi-2": "ARC-AGI-2",
    "ineqmath": "IneqMath",
    "kumo": "KUMO",
    "omnimath": "Omni-Math",
    "reasoning-gym": "Reasoning Gym",
    # Knowledge & Long Context
    "gpqa-diamond": "GPQA Diamond",
    "hle": "Humanity's Last Exam",
    "mmmlu": "MMMLU",
    "simpleqa": "SimpleQA",
    # Scientific Research
    "bixbench": "BIX-Bench",
    "codepde": "CodePDE",
    "labbench": "LAB-Bench",
    "mlgym": "MLGym-Bench",
    "qcircuitbench": "QCircuitBench",
    "replicationbench": "ReplicationBench",
    "research-code-bench": "ResearchCodeBench",
    "scicode": "SciCode",
    "sldbench": "SLDBench",
    # Agents, Tools & Systems
    "bfcl": "BFCL",
    "deepsynth": "DeepSynth",
    "gaia": "GAIA",
    "gaia2": "GAIA2",
    "seal0": "Seal-0",
    "skillsbench": "SkillsBench",
    "terminal-bench": "Terminal-Bench 2.0",
    "widesearch": "WideSearch",
    # Data & Analytics
    "dacode": "DA-Code",
    "spider2": "Spider 2",
    # Professional Domains
    "crmarena": "CRMArena",
    "financeagent_terminal": "FinanceAgent",
    "lawbench": "LawBench",
    "medagentbench": "MedAgentBench",
    "pixiu": "PIXIU",
    "spreadsheetbench": "SpreadsheetBench",
    # Safety & Security
    "strongreject": "StrongReject",
    # Multimodal
    "mmau": "MMAU",
}


def benchmark_display_name(key: str) -> str:
    return BENCHMARK_DISPLAY_NAME.get(key, key)


@dataclass(frozen=True)
class ImputationResult:
    normalized: pd.DataFrame
    raw: pd.DataFrame
    stats: pd.DataFrame
    cv: pd.DataFrame
    best_rank: int
    missing_fraction: float
