# DevOpsGym Benchmark Research

```json
{
  "name": "DevOps-Gym",
  "category": "Agentic/Interactive",
  "used_llm_or_agent": "agent",

  "links": {
    "website": "https://www.devops-gym.com/",
    "leaderboard": "https://www.devops-gym.com/",
    "paper": "https://arxiv.org/abs/2601.20882",
    "github": "https://github.com/ucsb-mlsec/DevOps-Gym",
    "dataset": null
  },

  "meta": {
    "release_date": "2026-01",
    "num_tasks": 733
  },

  "evaluation": {
    "primary_metric": "Resolved Rate (%) per category",
    "harbor_aligned_metric": "Resolved Rate — Harbor adapter covers all 733 tasks. Parity on 50-task subset: codex+gpt-5-nano original 4.0%±0.89 vs harbor 3.6%±1.17; codex+gpt-5-mini original 22.67%±1.76 vs harbor 22.0%±0.0; openhands+claude-haiku-4-5 original 20.0%±1.15 vs harbor 19.33%±1.76."
  },

  "results_over_time": [
    {
      "date": "2026-01",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2601.20882",
      "results": [
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "Claude Code",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.5185, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.2056, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.2387, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.1387, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.4259, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.1470, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.2387, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.1161, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "mini-SWE-Agent",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2962, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0291, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.0516, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0098, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "Aider",
          "scores": [
            { "metric": "Issue Resolving (%)", "value": 0.1710, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0516, "unit": null }
          ]
        },
        {
          "model": "o4-mini",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2407, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0294, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1645, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0839, "unit": null }
          ]
        },
        {
          "model": "Gemini-2.5-Pro",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2778, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0000, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1742, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0645, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-v3.1",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.1852, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0000, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1355, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0484, "unit": null }
          ]
        },
        {
          "model": "Qwen3-Coder-30B",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.0741, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0000, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.0516, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0161, "unit": null }
          ]
        }
      ],
      "note": "Paper baselines from Table 1. End-to-end pipeline tasks achieve 0% across all agent-model combinations (no agent completes all 4 stages). Build & Config has 54 tasks (repair + implementation). Monitoring has 34 tasks. Issue Resolving and Test Generation each have 310 tasks (same issues). End-to-end has 18 tasks. Some models score 0% on Monitoring. Gemini-2.5-Pro, DeepSeek-v3.1, and Qwen3-Coder-30B all get 0% on Monitoring."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://www.devops-gym.com/",
      "results": [
        {
          "model": "GPT-5.3-Codex",
          "effort": null,
          "system_description": "SageAgent",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.8182, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.3529, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.3214, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.3799, "unit": null },
            { "metric": "Avg (%)", "value": 0.4681, "unit": null },
            { "metric": "End-to-End (%)", "value": 0.1765, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "Claude Code",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.5185, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.2056, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.2387, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.1387, "unit": null },
            { "metric": "Avg (%)", "value": 0.2754, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.4259, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0589, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.2387, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.1161, "unit": null },
            { "metric": "Avg (%)", "value": 0.2099, "unit": null },
            { "metric": "End-to-End (%)", "value": 0.00, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "mini-SWE-Agent",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2962, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0291, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.0516, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0098, "unit": null },
            { "metric": "Avg (%)", "value": 0.0967, "unit": null }
          ]
        },
        {
          "model": "Claude-4-Sonnet",
          "effort": null,
          "system_description": "Aider",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.0555, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0000, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.0967, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0225, "unit": null },
            { "metric": "Avg (%)", "value": 0.0437, "unit": null }
          ]
        },
        {
          "model": "o4-mini",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2407, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0882, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1032, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0870, "unit": null },
            { "metric": "Avg (%)", "value": 0.1298, "unit": null },
            { "metric": "End-to-End (%)", "value": 0.00, "unit": null }
          ]
        },
        {
          "model": "Qwen3-Coder-30B",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.2037, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0589, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1322, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0613, "unit": null },
            { "metric": "Avg (%)", "value": 0.1140, "unit": null }
          ]
        },
        {
          "model": "Gemini-2.5-Pro",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.1666, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.1176, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1096, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0290, "unit": null },
            { "metric": "Avg (%)", "value": 0.1057, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-V3.1",
          "effort": null,
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Build & Config (%)", "value": 0.1111, "unit": null },
            { "metric": "Monitoring (%)", "value": 0.0000, "unit": null },
            { "metric": "Issue Resolving (%)", "value": 0.1420, "unit": null },
            { "metric": "Test Generation (%)", "value": 0.0322, "unit": null },
            { "metric": "Avg (%)", "value": 0.0713, "unit": null }
          ]
        }
      ],
      "note": "devops-gym.com leaderboard snapshot as of 2026-04-22. 9 entries sorted by average across 4 categories. Key update vs paper: SageAgent + GPT-5.3-Codex is the first to break 0% on End-to-End tasks (17.65%). Some scores differ from paper Table 1 — the leaderboard appears to be the live, updated version. Notably, Aider + Claude-4-Sonnet now shows Build & Config (5.55%) and Monitoring (0%), which were not reported in the paper. Qwen3-Coder-30B scores improved vs paper (e.g. Build & Config 20.37% vs paper's 7.41%)."
    }
  ],

  "notes": "DevOps-Gym is the first end-to-end benchmark covering core DevOps workflows. 733 tasks from 30+ Java and Go projects across 5 categories:\n\n1. **Build & Configuration** (66 tasks): Repair (dependency conflicts, misconfiguration, compilation errors, toolchain mismatches, dependency unavailability) and Implementation (migrations, upgrades, plugin integration)\n2. **Monitoring** (34 tasks): Resource anomalies (memory leaks, disk leaks, handle exhaustion, CPU spikes) and performance degradation (I/O bottlenecks, inefficient SQL). Agents use CLI tools without source code access.\n3. **Issue Resolving** (310 tasks): SWE-Bench style fail-to-pass test transitions on Java/Go repos\n4. **Test Generation** (310 tasks): SWT-Bench style test creation on same issues as Issue Resolving\n5. **End-to-End** (18 tasks): Sequential 4-stage pipelines (Build → Monitor → Fix → Test). 0% success rate across all models.\n\nNote: adapter_metadata.json lists 733 total (66 build + 34 monitor + 308 codegen + 308 testgen + 17 e2e), slightly different from paper counts (54 + 34 + 310 + 310 + 18 = 726). The adapter may include additional tasks or count differently.\n\nKey findings:\n- Best overall: Claude Code + Claude-4-Sonnet (51.85% build, 20.56% monitoring, 23.87% issue resolving, 13.87% test gen)\n- Monitoring is extremely hard: 0% for Gemini-2.5-Pro, DeepSeek-v3.1, and Qwen3-Coder-30B\n- Language bias: Claude-3.5-Sonnet drops from 70.4% on SWE-Bench-Verified (Python) to 23.87% on DevOps-Gym (Java/Go)\n- End-to-end: 0% across all agents — no agent can chain all 4 DevOps stages\n- Framework matters: Claude Code >> OpenHands >> mini-SWE-Agent with same model\n- Published at ICLR 2026\n\nHarbor adapter covers all 733 tasks with parity on 50-task subset (~6.8% sampling). Oracle achieves 100% across all 5 categories.\n\nLeaderboard at devops-gym.com shows 9 entries as of April 2026. SageAgent + GPT-5.3-Codex leads with 46.81% average and is the first agent to achieve non-zero End-to-End (17.65%)."
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2601.20882, ICLR 2026)

**Authors:** Yuheng Tang, Kaijie Zhu, Bonan Ruan, Chuqi Zhang, Michael Yang, Hongwei Li, Suyue Guo, Tianneng Shi, Zekun Li, Christopher Kruegel, Giovanni Vigna, Dawn Song, William Yang Wang, Lun Wang, Yangruibo Ding, Zhenkai Liang, Wenbo Guo

**Affiliations:** UC Santa Barbara, National University of Singapore, UC Berkeley, Google, UCLA

**Submitted:** January 27, 2026. Published at ICLR 2026.

#### 1.1 Benchmark Design Principles

1. **Realism**: Tasks from actual GitHub issues or expert-crafted synthetic failures
2. **Agentic evaluation**: Sequential decision-making with tool selection and multi-step planning
3. **Complete DevOps cycle**: Four stages forming minimum viable pipeline

Languages: Java and Go (deliberately non-Python to test generalization)
Repositories: 30+ well-maintained projects with standardized build systems

#### 1.2 Task Categories

**Build & Configuration (54 tasks in paper, 66 in adapter):**
- Repair tasks (5 error types): dependency version conflicts, build misconfiguration, compilation errors, toolchain mismatches, dependency unavailability
- Implementation tasks: build system migration (Maven→Gradle), version upgrades, plugin integration
- Input: repo with failing build + terminal access
- Output: patch or config files
- Evaluation: build succeeds + artifacts pass test cases

**Monitoring (34 tasks):**
- Resource anomalies: memory leaks, disk leaks, handle exhaustion, CPU spikes
- Performance degradation: I/O bottlenecks, inefficient SQL
- Includes healthy system cases (no anomaly)
- Input: containerized environment + CLI tools (top, free, ps, netstat). NO source code access.
- Output: structured diagnostic report with anomaly type + quantitative evidence
- Evaluation: binary accuracy (correct anomaly identification)
- Expert-injected bugs manifesting within 5-15 minutes, validated by 3 senior DevOps engineers

**Issue Resolving (310 tasks):**
- SWE-Bench style: translate bug descriptions into code patches
- Fail-to-pass test transitions
- Java and Go repos (adapted from Multi-SWE-bench pipeline)

**Test Generation (310 tasks):**
- SWT-Bench style: create regression tests from bug descriptions
- Same issues as Issue Resolving
- Tests must fail on buggy code, pass on patched code

**End-to-End (18 tasks):**
- Sequential 4-stage pipeline: Build fix → Deploy & Monitor → Code fix → Regression test
- Failure at any stage terminates pipeline
- **0% success rate** across all agent-model combinations

#### 1.3 Data Contamination Prevention

Prefix-completion analysis on 20 code snippets per repo:
- 5 metrics: normalized Levenshtein distance, consecutive token count, first mismatch position, longest common substring, sentence BLEU
- Repos with ≥20% high-risk snippets excluded
- Git metadata removed to prevent solution leakage

#### 1.4 Main Results (Table 1)

| Agent | Model | Build & Config | Monitoring | Issue Resolving | Test Gen |
|-------|-------|---------------|-----------|----------------|----------|
| Claude Code | Claude-4-Sonnet | **51.85%** | **20.56%** | **23.87%** | **13.87%** |
| OpenHands | Claude-4-Sonnet | 42.59% | 14.70% | 23.87% | 11.61% |
| OpenHands | o4-mini | 24.07% | 2.94% | 16.45% | 8.39% |
| OpenHands | Gemini-2.5-Pro | 27.78% | 0.00% | 17.42% | 6.45% |
| mini-SWE-Agent | Claude-4-Sonnet | 29.62% | 2.91% | 5.16% | 0.98% |
| OpenHands | DeepSeek-v3.1 | 18.52% | 0.00% | 13.55% | 4.84% |
| Aider | Claude-4-Sonnet | — | — | 17.10% | 5.16% |
| OpenHands | Qwen3-Coder-30B | 7.41% | 0.00% | 5.16% | 1.61% |

#### 1.5 Error Analysis

**Build Configuration errors:**
- Toolchain/environment limitations: 33%
- Multi-step reasoning failures: 23%
- Domain knowledge gaps: 37% (17% inherently difficult)

**Monitoring errors:**
- Inadequate methodology (one-time vs continuous): 37%
- Premature conclusion: 26%
- Insufficient temporal granularity: 11%
- Interpretation failure (correct metrics, wrong analysis): 26%

**Three fundamental monitoring challenges:**
1. Continuous state processing exhausts context limits
2. Agents lose focus during monitoring
3. Poor baseline discrimination generates false positives

#### 1.6 Language Bias

> "Claude-3.5-Sonnet achieved 70.4% on SWE-Bench-Verified, yet drops dramatically to 23.87% on Java/Go tasks"

#### 1.7 Stability Analysis (Table 2)

On 50-task sample, 5 independent runs:
- Claude Code + Claude-4-Sonnet: 16-22% per run, mean 18.8% (SD 2.40), Pass@5: 26%
- OpenHands + o4-mini: 14-20% per run, mean 16.8% (SD 2.04), Pass@5: 20%

### 2. GitHub Repository (https://github.com/ucsb-mlsec/DevOps-Gym)

Available at the repository link with full code and task definitions.

### 3. Leaderboard (https://www.devops-gym.com/, as of April 2026)

Data loaded from `assets/results/leaderboard.json`. 9 entries, sorted by average across 4 categories:

| # | Agent | Model | Build & Config | Monitoring | Issue Resolving | Test Gen | Avg | E2E |
|---|-------|-------|---------------|-----------|----------------|----------|-----|-----|
| 1 | SageAgent | GPT-5.3-Codex | **81.82%** | **35.29%** | **32.14%** | **37.99%** | **46.81%** | **17.65%** |
| 2 | Claude Code | Claude-4-Sonnet | 51.85% | 20.56% | 23.87% | 13.87% | 27.54% | — |
| 3 | OpenHands | Claude-4-Sonnet | 42.59% | 5.89% | 23.87% | 11.61% | 20.99% | 0% |
| 4 | OpenHands | o4-mini | 24.07% | 8.82% | 10.32% | 8.70% | 12.98% | 0% |
| 5 | OpenHands | Qwen3-Coder-30B | 20.37% | 5.89% | 13.22% | 6.13% | 11.40% | — |
| 6 | OpenHands | Gemini-2.5-Pro | 16.66% | 11.76% | 10.96% | 2.90% | 10.57% | — |
| 7 | mini-SWE-Agent | Claude-4-Sonnet | 29.62% | 2.91% | 5.16% | 0.98% | 9.67% | — |
| 8 | OpenHands | DeepSeek-V3.1 | 11.11% | 0.00% | 14.20% | 3.22% | 7.13% | — |
| 9 | Aider | Claude-4-Sonnet | 5.55% | 0.00% | 9.67% | 2.25% | 4.37% | — |

**Key changes vs paper:**
- **SageAgent + GPT-5.3-Codex** is new and dominates all categories — first to break 0% on End-to-End (17.65%)
- Several scores differ from paper Table 1 (the leaderboard is the live, updated source)
- Qwen3-Coder-30B improved significantly (Build & Config: 7.41% → 20.37%, Issue Resolving: 5.16% → 13.22%)
- Aider now reports Build & Config (5.55%) and Monitoring (0%), which were missing in the paper

### 4. Harbor Adapter (devopsgym)

**adapter_metadata.json:**
- Split: full, Size: 733 tasks
- Harness: agent (codex@0.81.0-alpha.8 supported)
- 5 categories: Build & Config (66), Monitoring (34), Issue Resolving/CodeGen (308), Test Gen (308), End-to-End (17)
- Two evaluation modes: code generation (nonstrict) and test generation (strict)
- Oracle: 100% across all categories
- Parity cost: $250

**parity_experiment.json (3 experiments on 50-task subset):**

| Agent | Model | Runs | Original | Harbor |
|-------|-------|------|----------|--------|
| codex@0.81.0 | gpt-5-nano | 5 | 4.0% ±0.89 | 3.6% ±1.17 |
| codex@0.81.0 | gpt-5-mini | 3 | 22.67% ±1.76 | 22.0% ±0.0 |
| openhands@1.5.0 | claude-haiku-4-5 | 3 | 20.0% ±1.15 | 19.33% ±1.76 |

---

## Questions

1. **Task count discrepancy**: The paper reports 54+34+310+310+18=726 tasks, but the adapter_metadata.json says 733 (66+34+308+308+17=733). Different counts for Build & Config (54 vs 66), Issue Resolving (310 vs 308), Test Gen (310 vs 308), and End-to-End (18 vs 17). Which is authoritative?

2. **Primary metric**: The benchmark reports separate metrics per category. There's no single aggregate score in the paper. The leaderboard shows an "Avg (%)" column. Should the primary_metric be the average, or should each category be tracked separately?

3. **End-to-End tasks**: All models score 0% on end-to-end. Should these still be included in the results? They demonstrate a fundamental limitation but don't differentiate between models.

4. **Leaderboard vs paper discrepancies**: Several scores on the leaderboard differ from the paper (e.g. Qwen3-Coder-30B Build & Config 20.37% vs paper's 7.41%, OpenHands Claude-4-Sonnet Monitoring 5.89% vs paper's 14.70%). The leaderboard may use updated evaluation or different splits. Which should be treated as authoritative?

5. **Category classification**: Classified as "Agentic/Interactive" due to the multi-stage DevOps pipeline and monitoring tasks requiring real-time system interaction. Could also be "Repo-level Software Engineering" for the issue resolving and test generation components.
