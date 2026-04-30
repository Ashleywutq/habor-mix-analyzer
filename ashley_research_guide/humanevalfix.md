# HumanEvalFix Benchmark Research

```json
{
  "name": "HumanEvalFix",
  "category": "Competitive/Function-level Programming",
  "used_llm_or_agent": "both",

  "links": {
    "website": null,
    "leaderboard": null,
    "paper": "https://arxiv.org/abs/2308.07124",
    "github": "https://github.com/bigcode-project/octopack",
    "dataset": "https://huggingface.co/datasets/bigcode/humanevalpack"
  },

  "meta": {
    "release_date": "2023-08",
    "num_tasks": 164
  },

  "evaluation": {
    "primary_metric": "pass@1",
    "harbor_aligned_metric": "Accuracy — Harbor adapter covers Python subset (164 tasks). Parity: openhands+gpt-4o-mini original 55.27%±3.49 vs harbor 56.1%±1.31; openhands+gpt-5-mini original 98.1%±0.8 vs harbor 97.9%±0.5 (3 trials each)."
  },

  "results_over_time": [
    {
      "date": "2023-08",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2308.07124",
      "results": [
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "non-permissive",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.470, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.482, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.500, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.506, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.476, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.433, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.478, "unit": null }
          ]
        },
        {
          "model": "WizardCoder (16B)",
          "effort": null,
          "system_description": "non-permissive, trained on OpenAI outputs",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.318, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.295, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.307, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.304, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.187, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.130, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.257, "unit": null }
          ]
        },
        {
          "model": "OctoCoder (16B)",
          "effort": null,
          "system_description": "permissive, CommitPackFT+OASST",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.304, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.284, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.306, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.302, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.261, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.165, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.270, "unit": null }
          ]
        },
        {
          "model": "OctoGeeX (6B)",
          "effort": null,
          "system_description": "permissive, CommitPackFT+OASST",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.281, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.277, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.304, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.276, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.229, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.096, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.244, "unit": null }
          ]
        },
        {
          "model": "InstructCodeT5+ (16B)",
          "effort": null,
          "system_description": "non-permissive, trained on OpenAI outputs",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.027, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.012, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.043, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.021, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.002, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.005, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.018, "unit": null }
          ]
        },
        {
          "model": "BLOOMZ (176B)",
          "effort": null,
          "system_description": "permissive",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.166, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.155, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.152, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.164, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.067, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.057, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.125, "unit": null }
          ]
        },
        {
          "model": "StarCoder (16B)",
          "effort": null,
          "system_description": "permissive, base model (no instruction tuning)",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.087, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.157, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.133, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.201, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.156, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.067, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.134, "unit": null }
          ]
        },
        {
          "model": "CodeGeeX2 (6B)",
          "effort": null,
          "system_description": "permissive (commercial license via form)",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.159, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.147, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.180, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.136, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.043, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.061, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.121, "unit": null }
          ]
        },
        {
          "model": "StarChat-β (16B)",
          "effort": null,
          "system_description": "permissive",
          "scores": [
            { "metric": "pass@1 (Python)", "value": 0.181, "unit": null },
            { "metric": "pass@1 (JavaScript)", "value": 0.181, "unit": null },
            { "metric": "pass@1 (Java)", "value": 0.241, "unit": null },
            { "metric": "pass@1 (Go)", "value": 0.181, "unit": null },
            { "metric": "pass@1 (C++)", "value": 0.082, "unit": null },
            { "metric": "pass@1 (Rust)", "value": 0.036, "unit": null },
            { "metric": "pass@1 (Avg 6 langs)", "value": 0.112, "unit": null }
          ]
        }
      ],
      "note": "Paper release baselines from Table 2 (HumanEvalFix, tests variant). Zero-shot pass@1 (%). All 9 models with per-language breakdown across Python, JavaScript, Java, Go, C++, Rust. GPT-4 evaluated with 1 sample; all others with T=0.2, top_p=0.95, 20 samples. Models marked non-permissive are trained on OpenAI outputs. Rust is consistently the hardest language. Go performance varies widely. Published at NeurIPS 2023."
    }
  ],

  "notes": "HumanEvalFix is one of three tasks in HumanEvalPack, introduced in the OctoPack paper (NeurIPS 2023). The task: given a buggy function and unit tests, fix the bug.\n\nKey characteristics:\n- 164 buggy functions per language (derived from original HumanEval solutions)\n- 6 languages: Python, JavaScript, Java, Go, C++, Rust (984 total tasks across all languages)\n- Bugs manually inserted into correct HumanEval solutions\n- Each bug causes at least one unit test to fail\n- Code remains executable but produces incorrect results\n- Two evaluation variants: 'tests' (given unit tests) and 'docs' (given docstring)\n\nHumanEvalPack also includes:\n- HumanEvalSynthesize: generate code from docstrings (NL→C)\n- HumanEvalExplain: explain code then regenerate from explanation (NL+C→NL→C)\n\nThe Harbor adapter covers only the Python subset (164 tasks) and converts the benchmark from direct LLM code generation to agent-based code repair using OpenHands.\n\nPaper findings on HumanEvalFix:\n- 'Most challenging task for most models' — models commonly regenerate buggy function unchanged or introduce new bugs\n- 'Bugs that require removing excess code are the most challenging'\n- CommitPackFT training data (~20% bug fixes) is critical for HumanEvalFix performance\n- GPT-4 at 47.8% (avg across 6 languages) was best at paper release\n\nHarbor parity shows gpt-5-mini achieves 98.1% — the benchmark is largely saturated for frontier models on Python.\n\nNo external leaderboard specific to HumanEvalFix. EvalPlus leaderboard tracks HumanEval (synthesis) but not HumanEvalFix.\n\nPublished at NeurIPS 2023 (ICLR 2024 per OpenReview). Authors from BigCode project (HuggingFace, various institutions)."
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2308.07124, NeurIPS 2023)

**Authors:** Niklas Muennighoff, Qian Liu, Armel Zebaze, Qinkai Zheng, Binyuan Hui, Terry Yue Zhuo, Swayam Singh, Xiangru Tang, Leandro von Werra, Shayne Longpre

**Affiliations:** BigCode project (HuggingFace and various institutions)

**Paper:** 60 pages (9 main + extensive appendix), 40 figures, 19 tables. Submitted August 14, 2023.

#### 1.1 HumanEvalFix Task Definition

Given a buggy function and unit tests (or docstring), fix the bug.

**Format:** NL+C→C (natural language description + buggy code → corrected code)

**Construction:**
- Start with 164 correct HumanEval solutions
- Manually insert bugs into each solution
- Bugs designed to be similar across 6 languages for cross-language comparison
- Each bug causes at least one unit test to fail
- Code remains syntactically valid and executable, just produces wrong results
- Total: 984 buggy functions across 6 languages (164 × 6)

**Two evaluation variants:**
- `humanevalfixtests`: Given unit tests as context (primary)
- `humanevalfixdocs`: Given docstring as context (alternative)

**Evaluation:** pass@1 metric, T=0.2, top_p=0.95, 20 samples per problem

#### 1.2 HumanEvalPack (full benchmark)

Three tasks across 6 languages:

| Task | Input | Output | Description |
|------|-------|--------|-------------|
| HumanEvalFix | NL + buggy code | Fixed code | Bug repair |
| HumanEvalExplain | NL + correct code | Explanation → code | Explain then regenerate |
| HumanEvalSynthesize | NL (docstring) | Code | Code generation (original HumanEval) |

Languages: Python, JavaScript, Java, Go, C++, Rust

#### 1.3 Paper Results — Full Table 2 (HumanEvalFix, tests variant, zero-shot pass@1 %)

**Non-permissive models:**

| Model | Params | Python | JS | Java | Go | C++ | Rust | Avg |
|-------|--------|--------|-----|------|-----|------|------|-----|
| GPT-4 | unknown | 47.0 | 48.2 | 50.0 | 50.6 | 47.6 | 43.3 | **47.8** |
| WizardCoder† | 16B | 31.8 | 29.5 | 30.7 | 30.4 | 18.7 | 13.0 | 25.7 |
| InstructCodeT5+† | 16B | 2.7 | 1.2 | 4.3 | 2.1 | 0.2 | 0.5 | 1.8 |

**Permissive models:**

| Model | Params | Python | JS | Java | Go | C++ | Rust | Avg |
|-------|--------|--------|-----|------|-----|------|------|-----|
| OctoCoder | 16B | 30.4 | 28.4 | 30.6 | 30.2 | 26.1 | 16.5 | **27.0** |
| OctoGeeX | 6B | 28.1 | 27.7 | 30.4 | 27.6 | 22.9 | 9.6 | 24.4 |
| StarChat-β | 16B | 18.1 | 18.1 | 24.1 | 18.1 | 8.2 | 3.6 | 11.2 |
| BLOOMZ | 176B | 16.6 | 15.5 | 15.2 | 16.4 | 6.7 | 5.7 | 12.5 |
| StarCoder | 16B | 8.7 | 15.7 | 13.3 | 20.1 | 15.6 | 6.7 | 13.4 |
| CodeGeeX2* | 6B | 15.9 | 14.7 | 18.0 | 13.6 | 4.3 | 6.1 | 12.1 |

†: Trained on OpenAI outputs. *: Commercial license via form.

**Per-language patterns:**
- Rust is consistently the hardest language (GPT-4: 43.3%, OctoCoder: 16.5%, most models <10%)
- Go shows high variance: StarCoder (20.1%) beats its Python score (8.7%) on Go
- Java tends to be slightly easier than Python for most models
- GPT-4 is remarkably consistent across languages (43.3–50.6% range)

#### 1.4 Bug Types

The paper notes that bugs were carefully designed:
- Each bug makes the function produce incorrect output for at least one test case
- Bugs span different types: logic errors, off-by-one, wrong operator, missing condition, excess code
- Cross-language consistency maintained where possible

### 2. GitHub Repository (https://github.com/bigcode-project/octopack)

- Contains CommitPack/CommitPackFT creation scripts
- HumanEvalPack evaluation harness
- OctoCoder and OctoGeeX fine-tuning scripts
- Evaluation parameters: T=0.2, 20 samples, batch_size=5, max_length=2048, bf16 precision
- Language versions: Python 3.9.13, C++ 11.4.0, Java 18, Go 1.18.4, Rust 1.71.1
- License: MIT (code), model licenses follow base models

### 3. Harbor Adapter (humanevalfix)

**adapter_metadata.json:**
- Split: python, Size: 164 tasks
- Harness: agent (openhands supported)
- Converts from direct LLM code generation to agent-based code repair
- Parity agents: openhands@v0.60.0 with gpt-4o-mini and gpt-5-mini

**parity_experiment.json (2 experiments):**

| Agent | Model | Trials | Original | Harbor |
|-------|-------|--------|----------|--------|
| openhands@v0.60.0 | gpt-4o-mini | 3 | 55.27% ±3.49 | 56.1% ±1.31 |
| openhands@v0.60.0 | gpt-5-mini | 3 | 98.1% ±0.8 | 97.9% ±0.5 |

Settings: OPENHANDS_MAX_ITERATIONS=10, OPENHANDS_ENABLE_PROMPT_EXTENSIONS=false, n-concurrent-trials=4

**Note:** gpt-5-mini achieves ~98% — the Python subset is largely saturated for frontier models.

### 4. Leaderboard

No external leaderboard specific to HumanEvalFix exists. The EvalPlus leaderboard tracks HumanEval/HumanEval+ (code synthesis) but not the Fix variant.

---

## Questions

1. **Benchmark saturation**: gpt-5-mini achieves 98.1% on HumanEvalFix Python. The benchmark appears largely solved for frontier models on the Python subset. Should this be flagged prominently?

2. **Python-only in Harbor**: The adapter covers only Python (164 tasks), but HumanEvalFix has 984 tasks across 6 languages. Should `num_tasks` be 164 (Harbor/Python) or 984 (all languages)?

3. **Agent-based vs direct**: The paper evaluates models via direct code generation (pass@1 with sampling). The Harbor adapter converts this to agent-based repair via OpenHands. This changes the evaluation modality — the results aren't directly comparable. Should this be noted?

4. **No dedicated leaderboard**: HumanEvalFix doesn't have its own leaderboard. Results are scattered across individual papers and the OctoPack paper. The Harbor parity experiments are the most recent standardized results available.

5. **Category classification**: I classified this as "Competitive/Function-level Programming" since tasks are individual function-level bug fixes. Could also be "Code Performance" or "Repo-level Software Engineering" but the tasks are isolated functions, not repositories.

6. **Paper venue**: The arXiv page says NeurIPS 2023, but OpenReview shows ICLR 2024 (openreview.net/forum?id=mw1PWNSWZP). The citation in the Harbor adapter says NeurIPS 2023. Which is correct?
