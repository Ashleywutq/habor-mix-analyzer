# SWT-Bench Benchmark Research

```json
{
  "name": "SWT-Bench",
  "category": "Repo-level Software Engineering",
  "used_llm_or_agent": "both",

  "links": {
    "website": "https://swtbench.com",
    "leaderboard": "https://swtbench.com",
    "paper": "https://arxiv.org/abs/2406.12952",
    "github": "https://github.com/logic-star-ai/swt-bench",
    "dataset": null
  },

  "meta": {
    "release_date": "2024-06",
    "num_tasks": 1983
  },

  "evaluation": {
    "primary_metric": "Success Rate (S)",
    "harbor_aligned_metric": "Resolved Rate (%) — Harbor adapter covers the Verified split (433 tasks). Parity across 3 agents (claude-code, terminus-2, openhands) all with claude-haiku-4-5: 20.55%, 22.63%, 20.32% respectively, matching original exactly."
  },

  "results_over_time": [
    {
      "date": "2024-06",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2406.12952",
      "results": [
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "SWE-Agent+",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.185, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.855, "unit": null },
            { "metric": "F→× rate", "value": 0.464, "unit": null },
            { "metric": "F→P rate", "value": 0.192, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.276, "unit": null },
            { "metric": "Change Coverage (ΔC_S)", "value": 0.694, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.159, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.873, "unit": null },
            { "metric": "F→P rate", "value": 0.167, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.265, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "LIBRO",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.141, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.920, "unit": null },
            { "metric": "F→P rate", "value": 0.152, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.238, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "Aider",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.127, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.667, "unit": null },
            { "metric": "F→P rate", "value": 0.170, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.278, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "ZeroShotPlus",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.094, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.895, "unit": null },
            { "metric": "F→P rate", "value": 0.101, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.215, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "AutoCodeRover",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.091, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.471, "unit": null },
            { "metric": "F→P rate", "value": 0.091, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.179, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "ZeroShot",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.036, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.486, "unit": null },
            { "metric": "F→P rate", "value": 0.058, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.076, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "effort": null,
          "system_description": "Pass@5 (oracle)",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.203, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.931, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.313, "unit": null }
          ]
        },
        {
          "model": "Mistral Large 2",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.163, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.761, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.230, "unit": null }
          ]
        },
        {
          "model": "Claude-3.5-Sonnet",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.123, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.678, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.303, "unit": null }
          ]
        },
        {
          "model": "GPT-4o-mini",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.098, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.710, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.209, "unit": null }
          ]
        },
        {
          "model": "Claude-3.0-Haiku",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.025, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.203, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.030, "unit": null }
          ]
        },
        {
          "model": "Mixtral-8x22B",
          "effort": null,
          "system_description": "SWE-Agent",
          "scores": [
            { "metric": "Success Rate (S)", "value": 0.007, "unit": null },
            { "metric": "Well-formed (W)", "value": 0.033, "unit": null },
            { "metric": "Change Coverage (ΔC_all)", "value": 0.009, "unit": null }
          ]
        }
      ],
      "note": "Paper release baselines evaluated on SWT-Bench Lite (276 instances). Table 2 compares methods (all using GPT-4 unless noted). Table 4 compares LLMs within SWE-Agent. SWE-Agent+ instructs the agent to execute generated tests before submitting. Pass@5 uses oracle selection (not practical). All methods use T=0 except LIBRO and Pass@5 (T=0.7)."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://swtbench.com",
      "results": [
        { "model": "Devstral 2", "effort": null, "system_description": "DevstralTestGen", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.891, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.576, "unit": null }] },
        { "model": "Bytedance (SE Lab)", "effort": null, "system_description": "AEGIS", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.478, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.260, "unit": null }] },
        { "model": "Claude 3.7 Sonnet", "effort": null, "system_description": "e-Otter++", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.525, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.564, "unit": null }] },
        { "model": "v20250405-dev", "effort": null, "system_description": "Amazon Q Developer Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.399, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.527, "unit": null }] },
        { "model": "GPT-4o", "effort": null, "system_description": "AssertFlip", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.380, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.442, "unit": null }] },
        { "model": "Cl. Sonnet 3.5, CI setup", "effort": null, "system_description": "OpenHands", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.283, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.524, "unit": null }] },
        { "model": "Cl. Sonnet 3.5, vanilla", "effort": null, "system_description": "OpenHands", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.228, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.436, "unit": null }] },
        { "model": "GPT-4", "effort": null, "system_description": "SWE-Agent+", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.185, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.276, "unit": null }] },
        { "model": "Mistral Large 2", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.163, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.230, "unit": null }] },
        { "model": "GPT-4", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.159, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.265, "unit": null }] },
        { "model": "GPT-4", "effort": null, "system_description": "LIBRO", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.141, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.238, "unit": null }] },
        { "model": "GPT-4", "effort": null, "system_description": "Aider", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.127, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.278, "unit": null }] },
        { "model": "Cl. 3.5 Sonnet", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.123, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.303, "unit": null }] },
        { "model": "GPT-4o mini", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.098, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.209, "unit": null }] },
        { "model": "GPT-4 + BM25", "effort": null, "system_description": "Zero-Shot Plus", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.094, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.215, "unit": null }] },
        { "model": "GPT-4", "effort": null, "system_description": "AutoCodeRover", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.091, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.179, "unit": null }] },
        { "model": "GPT-4 + BM25", "effort": null, "system_description": "Zero-Shot Base", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.036, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.076, "unit": null }] },
        { "model": "Claude 3 Haiku", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.025, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.030, "unit": null }] },
        { "model": "Mixtral 8x22B", "effort": null, "system_description": "SWE-Agent", "scores": [{ "metric": "Success Rate (S) — Lite Script", "value": 0.007, "unit": null }, { "metric": "Change Coverage (ΔC) — Lite Script", "value": 0.009, "unit": null }] }
      ],
      "note": "SWT-Bench Lite — Script Mode (Reproduction Scripts) leaderboard snapshot as of 2026-04-25 — 19 entries in exact page order (the page does not strictly sort by S; e.g. AEGIS 47.8 listed above e-Otter++ 52.5)."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://swtbench.com",
      "results": [
        { "model": "Claude 4 Sonnet", "effort": null, "system_description": "TEX-T", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.870, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.698, "unit": null }] },
        { "model": "L*Agent v1", "effort": null, "system_description": "LogicStar AI", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.840, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.677, "unit": null }] },
        { "model": "GPT-5", "effort": null, "system_description": "OpenHands", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.798, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.663, "unit": null }] },
        { "model": "GPT-5-mini", "effort": null, "system_description": "OpenHands", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.624, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.606, "unit": null }] },
        { "model": "Claude 3.7 Sonnet", "effort": null, "system_description": "e-Otter++", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.621, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.623, "unit": null }] },
        { "model": "v20250405-dev", "effort": null, "system_description": "Amazon Q Developer Agent", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.510, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.574, "unit": null }] },
        { "model": "GPT-4o", "effort": null, "system_description": "AssertFlip", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.455, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.474, "unit": null }] },
        { "model": "GPT-4o", "effort": null, "system_description": "Otter++", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.374, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.428, "unit": null }] },
        { "model": "GPT-4o", "effort": null, "system_description": "Otter", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.316, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.376, "unit": null }] },
        { "model": "Cl. Sonnet 3.5", "effort": null, "system_description": "OpenHands", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.277, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.529, "unit": null }] },
        { "model": "GPT-4o", "effort": null, "system_description": "LIBRO", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.178, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.380, "unit": null }] },
        { "model": "GPT-4o + BM25", "effort": null, "system_description": "Zero-Shot Plus", "scores": [{ "metric": "Success Rate (S) — Verified Unit Test", "value": 0.143, "unit": null }, { "metric": "Change Coverage (ΔC) — Verified Unit Test", "value": 0.340, "unit": null }] }
      ],
      "note": "SWT-Bench Verified — Unit Test Mode leaderboard snapshot as of 2026-04-25 — 12 entries in exact page order (descending by S). This is the Verified split (433 tasks), the same split the Harbor adapter targets."
    }
  ],

  "notes": "SWT-Bench is a test generation benchmark derived from SWE-Bench. The task: given a GitHub issue description and buggy codebase, generate tests that fail on the original code but pass after the developer's patch.\n\nThree dataset splits:\n- SWT-Bench Full: 1,983 instances (2,294 after filtering)\n- SWT-Bench Lite: 276 instances (subset used for paper experiments)\n- SWT-Bench Verified: 433 instances\n\nKey metrics:\n- **Success Rate (S)**: % instances where generated tests contain ≥1 fail-to-pass test and no tests incorrectly fail after patch\n- **Change Coverage (ΔC)**: portion of executable lines modified by golden patch that generated tests exercise\n- **Well-formedness (W)**: portion of instances with applicable patches\n- **F→P rate**: tests that fail before patch and pass after (issue reproduction)\n- **F→× rate**: tests that fail before patch (potentially reproducing)\n- **P→P rate**: valid but irrelevant tests\n\nKey findings from the paper:\n- Code repair agents (SWE-Agent) outperform test-generation-specific methods (LIBRO)\n- Novel fault-tolerant diff format boosts well-formedness from 48.6% to 89.5%\n- Generated tests double SWE-Agent precision from 23.9% to 47.8% when used as fix filter\n- Test generation and code repair show negligible correlation at instance level (p>70%)\n- The four best methods combined solve 87 instances vs 51 for best single method\n\nThe Harbor adapter covers the Verified split (433 tasks) with parity across 3 agents. Published at NeurIPS 2024.\n\nLeaderboard exists at swtbench.com — submissions accepted via email."
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2406.12952, NeurIPS 2024)

**Authors:** Niels Mündler, Mark Niklas Müller, Jingxuan He, Martin Vechev

**Affiliations:** ETH Zurich, LogicStar.ai

**Paper:** 24 pages (10 main + 14 appendix). Submitted June 18, 2024; last revised February 7, 2025. Published at NeurIPS 2024.

#### 1.1 Task Definition

Given a GitHub issue description and corresponding buggy codebase R, generate tests T such that:
- Tests **fail** on original codebase R (reproducing the bug)
- Tests **pass** on patched codebase R ∘ X* (validating the fix)

Derived from SWE-Bench: same repositories, same issues, but the task is test generation instead of code repair.

#### 1.2 Metrics

**Success Rate (S)**: % of instances where generated tests contain ≥1 fail-to-pass (F→P) test and no tests incorrectly fail after patch application.

**Change Coverage (ΔC)**: Portion of executable lines modified by golden patch that are exercised by generated tests. Measured on both removed and added lines. Non-executable lines (docs, config) excluded. Instances where no modified lines are executable are excluded (~1% of cases).

**Well-formedness (W)**: Portion of instances where generated patch can be applied without errors.

**Test outcome categories:**
- F→P: Fail before patch, pass after (reproducing test — the goal)
- F→×: Fail before patch, any result after (potentially reproducing)
- P→P: Pass both before and after (valid but irrelevant)
- P→F: Pass before, fail after (incorrect test — penalized)

#### 1.3 Novel Diff Format

The paper introduces a fault-tolerant code diff format optimized for LLM generation. Allows entire functions/classes to be inserted or replaced with fuzzy matching for locations, instead of requiring exact line numbers.

Impact: well-formedness jumps from 48.6% (unified diff) to 89.5% (custom format), yielding ~3x improvement in success rate.

#### 1.4 Methods Evaluated

**Direct LLM methods:**
- ZeroShot: unified diff format
- ZeroShotPlus: custom fault-tolerant diff format
- Pass@5: best of 5 via oracle selection
- LIBRO: state-of-the-art test generation (adapted from Java)

**Code agents:**
- SWE-Agent: shell-based code agent
- SWE-Agent+: SWE-Agent instructed to execute tests before submission
- Aider: repository indexing + code editing
- AutoCodeRover: two-stage (context collection → code generation)

#### 1.5 Main Results (Table 2 — SWT-Bench Lite, all using GPT-4)

| Method | W (%) | S (%) | F→× (%) | F→P (%) | P→P (%) |
|--------|-------|-------|---------|---------|---------|
| Golden | 100.0 | 100.0 | 100.0 | 100.0 | 11.2 |
| Pass@5 (oracle) | 93.1 | 20.3 | 62.7 | 22.1 | 7.2 |
| SWE-Agent+ | 85.5 | **18.5** | 46.4 | 19.2 | 10.1 |
| SWE-Agent | 87.3 | 15.9 | 48.2 | 16.7 | 9.8 |
| LIBRO | 92.0 | 14.1 | 60.1 | 15.2 | 7.2 |
| Aider | 66.7 | 12.7 | 57.6 | 17.0 | 8.7 |
| AutoCodeRover | 47.1 | 9.1 | 43.8 | 9.1 | 7.6 |
| ZeroShotPlus | 89.5 | 9.4 | 55.4 | 10.1 | 7.2 |
| ZeroShot | 48.6 | 3.6 | 38.8 | 5.8 | 3.6 |

#### 1.6 Change Coverage (Table 3)

| Method | ΔC_all (%) | ΔC_S (%) | ΔC_¬S (%) |
|--------|-----------|---------|----------|
| Golden | 72.0 | 72.0 | — |
| Pass@5 | 31.3 | 65.6 | 22.5 |
| SWE-Agent+ | 27.6 | 69.4 | 18.0 |
| SWE-Agent | 26.5 | 64.7 | 19.1 |
| Aider | 27.8 | 59.5 | 23.1 |
| LIBRO | 23.8 | 64.2 | 17.0 |
| ZeroShotPlus | 21.5 | 76.7 | 15.7 |
| AutoCodeRover | 17.9 | 61.3 | 13.6 |
| ZeroShot | 7.6 | 34.9 | 6.6 |

#### 1.7 Model Comparison (Table 4 — SWE-Agent across LLMs)

| Model | W (%) | S (%) | F→× (%) | ΔC_all (%) |
|-------|-------|-------|---------|-----------|
| Mistral Large 2 | 76.1 | 16.3 | 51.4 | 23.0 |
| GPT-4 | 87.3 | 15.9 | 48.2 | 26.5 |
| Claude 3.5 Sonnet | 67.8 | 12.3 | 59.1 | 30.3 |
| GPT-4o mini | 71.0 | 9.8 | 36.2 | 20.9 |
| Claude 3.0 Haiku | 20.3 | 2.5 | 6.9 | 3.0 |
| Mixtral 8x22B | 3.3 | 0.7 | 1.8 | 0.9 |

#### 1.8 Context Ablation (Table 5)

Providing the correct test file to change nearly doubles S from 8.1% to 15.1%. Providing the golden code patch increases S only to 10.5%. An incorrect patch also yields 10.5%, suggesting file context matters more than patch specifics.

#### 1.9 Filtering Code Fixes

Using SWE-Agent to generate both bug fixes and tests, then filtering fixes to only those where all generated tests pass:
- **Precision doubles**: 23.9% → 47.8%
- **Recall**: ~20% (limited)
- Demonstrates test generation as a practical filter for code repair quality

#### 1.10 Correlation Analysis (Table 6)

| Method | SWT solved | SWE solved | Overlap | p-value |
|--------|-----------|-----------|---------|---------|
| ZeroShotPlus | 26 | 16 | 1 | 80.4% |
| SWE-Agent | 44 | 50 | 7 | 72.8% |

> No statistical evidence of correlation between test generation and code repair success (p > 70%), suggesting they are distinct tasks.

#### 1.11 Method Complementarity

The four best methods (LIBRO, AutoCodeRover, Aider, SWE-Agent+) combined solve 87 instances, vs 51 for SWE-Agent+ alone.

#### 1.12 Data Contamination Analysis (Table 7)

ZeroShotPlus on PRs before vs after GPT-4 knowledge cutoff (April 2023): S of 6.0% vs 4.8%. Small difference, not statistically significant (p ≈ 37%).

### 2. GitHub Repository (https://github.com/logic-star-ai/swt-bench)

- Evaluation harness via Docker (x86_64, 120GB storage, 16GB RAM, 8 cores recommended)
- Three splits: Full, Lite, Verified (on HuggingFace)
- Two modes: Unit Test (default), Reproduction Script
- Leaderboard submission: submit@swtbench.com
- Built on SWE-Bench evaluation harness (Princeton NLP)
- License: MIT
- Gold validation results: Lite 10.86% P→P, Verified 15.01% P→P, Full 17.65% P→P

### 3. Harbor Adapter (swtbench)

**adapter_metadata.json:**
- Split: verified, Size: 433 tasks
- Parity matching agents: claude-code, terminus-2, openhands (all + claude-haiku-4-5-20251001)
- Adapted benchmark size: 433, parity sampling rate: 1.0

**parity_experiment.json (3 separate experiments):**

| Agent | Model | Resolved Rate |
|-------|-------|--------------|
| claude-code | claude-haiku-4-5 | 20.55% |
| terminus-2 | claude-haiku-4-5 | 22.63% |
| openhands | claude-haiku-4-5 | 20.32% |

All match original exactly (±0). Date: 2025-11-03. No trial repetitions recorded.

The adapter transforms repair tasks into test generation objectives. Uses Docker caching for baseline results (gold/base tests on gold/base code) and only runs 2 experiments during evaluation (model test × both code versions).

### 4. Leaderboard (https://swtbench.com, as of 2026-04-25)

The site hosts **two separate ranking tables** on different splits/modes. Listed below in the exact order shown on the page (the Script Mode page does not strictly sort by S — AEGIS at 47.8 appears above e-Otter++ at 52.5). Submissions accepted via email (submit@swtbench.com) with independent verification.

#### 4.1 SWT-Bench Lite — Script Mode (Reproduction Scripts) — 19 entries

| # | System | Model | S (%) | ΔC (%) | Date |
|---|--------|-------|-------|--------|------|
| 1 | DevstralTestGen | Devstral 2 | 89.1 | 57.6 | 2026-03-13 |
| 2 | AEGIS | Bytedance (SE Lab) | 47.8 | 26.0 | 2025-02-17 |
| 3 | e-Otter++ | Claude 3.7 Sonnet | 52.5 | 56.4 | 2025-08-11 |
| 4 | Amazon Q Developer Agent | v20250405-dev | 39.9 | 52.7 | 2025-04-10 |
| 5 | AssertFlip | GPT-4o | 38.0 | 44.2 | 2025-07-28 |
| 6 | OpenHands | Cl. Sonnet 3.5, CI setup | 28.3 | 52.4 | 2025-02-18 |
| 7 | OpenHands | Cl. Sonnet 3.5, vanilla | 22.8 | 43.6 | 2025-02-18 |
| 8 | SWE-Agent+ | GPT-4 | 18.5 | 27.6 | 2024-05-22 |
| 9 | SWE-Agent | Mistral Large 2 | 16.3 | 23.0 | 2024-05-22 |
| 10 | SWE-Agent | GPT-4 | 15.9 | 26.5 | 2024-05-22 |
| 11 | LIBRO | GPT-4 | 14.1 | 23.8 | 2024-05-22 |
| 12 | Aider | GPT-4 | 12.7 | 27.8 | 2024-05-22 |
| 13 | SWE-Agent | Cl. 3.5 Sonnet | 12.3 | 30.3 | 2024-05-22 |
| 14 | SWE-Agent | GPT-4o mini | 9.8 | 20.9 | 2024-05-22 |
| 15 | Zero-Shot Plus | GPT-4 + BM25 | 9.4 | 21.5 | 2024-05-22 |
| 16 | AutoCodeRover | GPT-4 | 9.1 | 17.9 | 2024-05-22 |
| 17 | Zero-Shot Base | GPT-4 + BM25 | 3.6 | 7.6 | 2024-05-22 |
| 18 | SWE-Agent | Claude 3 Haiku | 2.5 | 3.0 | 2024-05-22 |
| 19 | SWE-Agent | Mixtral 8x22B | 0.7 | 0.9 | 2024-05-22 |

#### 4.2 SWT-Bench Verified — Unit Test Mode — 12 entries

This is the **Verified** split (433 tasks) — the same split the Harbor adapter uses.

| # | System | Model | S (%) | ΔC (%) | Date |
|---|--------|-------|-------|--------|------|
| 1 | TEX-T | Claude 4 Sonnet | 87.0 | 69.8 | 2025-12-17 |
| 2 | LogicStar AI | L*Agent v1 | 84.0 | 67.7 | 2025-09-13 |
| 3 | OpenHands | GPT-5 | 79.8 | 66.3 | 2025-08-22 |
| 4 | OpenHands | GPT-5-mini | 62.4 | 60.6 | 2025-08-22 |
| 5 | e-Otter++ | Claude 3.7 Sonnet | 62.1 | 62.3 | 2025-08-11 |
| 6 | Amazon Q Developer Agent | v20250405-dev | 51.0 | 57.4 | 2025-04-10 |
| 7 | AssertFlip | GPT-4o | 45.5 | 47.4 | 2025-07-28 |
| 8 | Otter++ | GPT-4o | 37.4 | 42.8 | 2025-03-10 |
| 9 | Otter | GPT-4o | 31.6 | 37.6 | 2025-03-10 |
| 10 | OpenHands | Cl. Sonnet 3.5 | 27.7 | 52.9 | 2025-02-28 |
| 11 | LIBRO | GPT-4o | 17.8 | 38.0 | 2025-02-28 |
| 12 | Zero-Shot Plus | GPT-4o + BM25 | 14.3 | 34.0 | 2025-02-28 |

**Key observations:**
- Massive progress since paper: Script mode jumped from 18.5% (SWE-Agent+ GPT-4, 2024) to 89.1% (DevstralTestGen, 2026)
- Verified Unit Test mode reaches even higher: TEX-T at 87.0%, LogicStar at 84.0%
- Agent scaffolding matters enormously — same model (Claude 3.5 Sonnet) ranges from 12.3% (SWE-Agent) to 28.3% (OpenHands CI setup)
- Coverage (ΔC) doesn't always correlate with success rate — SWE-Agent Claude 3.5 Sonnet has highest ΔC among paper baselines (30.3%) but only 12.3% S
- The two leaderboards evaluate different splits (Lite=276 vs Verified=433) AND different output modes (Script vs Unit Test) — scores are NOT directly comparable across tables

---

## Questions

1. **Dataset split confusion**: The paper primarily evaluates on SWT-Bench Lite (276 instances), but the Harbor adapter uses Verified (433 instances). The full dataset is 1,983 instances. Should `num_tasks` in the JSON be 1,983 (full), 433 (verified, matching Harbor), or 276 (lite, matching paper experiments)?

2. **Benchmark naming**: The Harbor adapter directory is `swtbench`, the paper calls it "SWT-Bench", and it's sometimes hyphenated as "SWT-Bench". The template filename convention would be `swt_bench.json` or `swtbench.json`?

3. **Multiple metrics**: SWT-Bench has a richer metric space than most benchmarks — Success Rate, Change Coverage, Well-formedness, F→P rate, etc. The `primary_metric` should probably be Success Rate (S), but which secondary metrics are worth tracking?

4. **The paper results are from June 2024** using GPT-4 (gpt-4-1106-preview). The leaderboard at swtbench.com likely has newer results. I couldn't scrape the leaderboard — should this be noted?

5. **Harbor adapter uses different agents/models** than the paper (claude-code, terminus-2, openhands with claude-haiku-4-5 vs the paper's SWE-Agent with GPT-4). The Harbor resolved rates (~20-22%) are comparable to paper's SWE-Agent+ (18.5%) but evaluated on a different split (Verified vs Lite).
