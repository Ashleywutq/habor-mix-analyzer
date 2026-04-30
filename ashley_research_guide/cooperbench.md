# CooperBench Benchmark Research

```json
{
  "name": "CooperBench",
  "category": "Agentic/Interactive",
  "used_llm_or_agent": "agent",

  "links": {
    "website": "https://cooperbench.com/",
    "leaderboard": "https://cooperbench.com/leaderboard",
    "paper": "https://arxiv.org/abs/2601.13295",
    "github": "https://github.com/cooperbench/CooperBench",
    "dataset": "https://huggingface.co/datasets/CodeConflict/cooperbench-dataset"
  },

  "meta": {
    "release_date": "2025-01",
    "num_tasks": 652
  },

  "evaluation": {
    "primary_metric": "Cooperative Success Rate (Coop)",
    "harbor_aligned_metric": "pass_rate — Harbor adapter covers all 652 tasks. Parity on flash subset (50 pairs): original 32.7% ±2.3% vs harbor 30.7% ±2.3% (3 runs each) with openhands-sdk@1.10.0+gemini-3-flash-preview."
  },

  "results_over_time": [
    {
      "date": "2025-01",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2601.13295",
      "results": [
        {
          "model": "GPT-5",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.48, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.28, "unit": null },
            { "metric": "Coordination Gap", "value": -0.20, "unit": null }
          ]
        },
        {
          "model": "Claude Sonnet 4.5",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.47, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.26, "unit": null },
            { "metric": "Coordination Gap", "value": -0.21, "unit": null }
          ]
        },
        {
          "model": "MiniMax-M2",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.36, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.14, "unit": null },
            { "metric": "Coordination Gap", "value": -0.22, "unit": null }
          ]
        },
        {
          "model": "Qwen3-Coder-30B-A3B-Instruct",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.22, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.13, "unit": null },
            { "metric": "Coordination Gap", "value": -0.09, "unit": null }
          ]
        },
        {
          "model": "Qwen3-30B-A3B-Instruct-2507",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.06, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.05, "unit": null },
            { "metric": "Coordination Gap", "value": -0.01, "unit": null }
          ]
        }
      ],
      "note": "Paper release baselines from Figure 4. All use OpenHands v0.54 agent framework. Solo = one agent does both features. Coop = two agents each do one feature, communicating via SQL-based message passing. 100 action steps budget per agent. Error bars are 95% Wilson confidence intervals."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://cooperbench.com/leaderboard",
      "results": [
        {
          "model": "Gemini-3-Flash",
          "system_description": "OpenHands SDK",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.486, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.262, "unit": null },
            { "metric": "Coordination Gap", "value": -0.224, "unit": null }
          ]
        },
        {
          "model": "GPT-5",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.4831, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.2795, "unit": null },
            { "metric": "Coordination Gap", "value": -0.2036, "unit": null }
          ]
        },
        {
          "model": "Claude Sonnet 4.5",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.471, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.259, "unit": null },
            { "metric": "Coordination Gap", "value": -0.212, "unit": null }
          ]
        },
        {
          "model": "Gemini-3-Pro",
          "system_description": "Mini-SWE",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.368, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.204, "unit": null },
            { "metric": "Coordination Gap", "value": -0.164, "unit": null }
          ]
        },
        {
          "model": "MiniMax-M2",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.362, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.140, "unit": null },
            { "metric": "Coordination Gap", "value": -0.222, "unit": null }
          ]
        },
        {
          "model": "Gemini-3-Flash",
          "system_description": "Mini-SWE",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.252, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.123, "unit": null },
            { "metric": "Coordination Gap", "value": -0.129, "unit": null }
          ]
        },
        {
          "model": "Qwen3-Coder-30B",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.216, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.133, "unit": null },
            { "metric": "Coordination Gap", "value": -0.083, "unit": null }
          ]
        },
        {
          "model": "Qwen3-30B",
          "system_description": "OpenHands",
          "scores": [
            { "metric": "Solo Success Rate", "value": 0.063, "unit": null },
            { "metric": "Coop Success Rate", "value": 0.046, "unit": null },
            { "metric": "Coordination Gap", "value": -0.017, "unit": null }
          ]
        }
      ],
      "note": "Current leaderboard snapshot as of 2026-04-18. Leaderboard tracks Solo, Coop, and Gap metrics. Gemini-3-Flash (OpenHands SDK) tops the leaderboard by Coop rate. Multiple agent frameworks (OpenHands, OpenHands SDK, Mini-SWE) are represented."
    }
  ],

  "notes": "CooperBench evaluates multi-agent cooperation on shared codebases. Two agents work simultaneously on paired features from the same repository, communicating via message passing to avoid merge conflicts while delivering working code.\n\nKey characteristics:\n- 199 features across 30 tasks from 12 open-source repositories\n- 652 unique feature pairs (tasks) from C(n,2) combinations within each feature pool\n- 4 languages: Python, TypeScript, Go, Rust\n- 8 annotators with software engineering backgrounds\n- Expert-written features, unit tests, and ground-truth solutions\n- 77.3% of tasks have conflicting ground-truth solutions\n- Tasks not adversarial but require coordination under conflicts\n\nCore finding — 'The Curse of Coordination': agents consistently perform worse in Coop vs Solo settings (~50% coordination gap for leading models). Communication tool does not improve success rate but does reduce merge conflicts.\n\nThree capability gaps identified:\n1. Expectation failures (42%): agents neglect partner state information\n2. Commitment failures (32%): agents break promises or make unverifiable assertions\n3. Communication failures (26%): unanswered questions, vague/repetitive messages\n\nEmergent coordination patterns in successful cases: role division, resource division, negotiation.\n\nScaling experiment: 2 agents (68.6%) → 3 agents (46.5%) → 4 agents (30.0%) on 46-task subset.\n\nHarbor adapter covers all 652 tasks. Uses OpenHands SDK with isolated Docker volumes and Redis for message brokering."
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2601.13295)

**Authors:** Arpandeep Khatua*, Hao Zhu* (equal contribution), Peter Tran**, Arya Prabhudesai**, Frederic Sadrieh**, Johann K. Lieberwirth** (equal contribution), Xinkai Yu, Yicheng Fu, Michael J. Ryan, Jiaxin Pei, Diyi Yang

**Affiliations:** Stanford University, SAP Labs US

**Paper:** 33 pages. Submitted January 27, 2025.

#### 1.1 Task Definition

Each task assigns two agents different features to implement on the same repository state:
- **Coop setting**: Two agents, each handling one feature, communicating via message passing in real time
- **Solo baseline**: One agent handles both features sequentially
- Features are compatible (can be jointly implemented) but potentially conflicting (77.3% have overlapping code changes)

**Evaluation pipeline:**
1. Merge compatibility: patches from both agents are merged; if conflicts exist, a coding model attempts resolution
2. Implementation correctness: merged patch tested against both features' unit tests

**Action space:** Communication tool (natural language messages via SQL database) + computer-use tools (file/terminal operations). 100 action steps budget per agent.

#### 1.2 Dataset Construction (3 stages)

**Stage I — Repository & PR Selection:**
- 12 actively maintained open-source repos, each >1K GitHub stars
- Not in SWE-Bench or Multi-SWE-Bench (reduces contamination)
- PRs with clear description, code+tests, feature addition, <200 lines and 2 files

**Stage II — Feature Creation:**
- Anchor features from real PRs, slightly modified
- Adjacent features authored by human annotators (8 co-authors with SE backgrounds)
- LLM-assisted ideation, but all features hand-written
- Manual test writing without coding assistants
- Ground-truth solutions written and verified

**Stage III — Environment Setup:**
- Deterministic execution via containerized environments
- Setup scripts clone repo at exact base commit, install dependencies, run full test suite
- Feature pools: 2-12 features per pool, 34 pools total

**Repositories:** dspy, jinja, click, pillow, tiktoken, llama_index, typst, and others across Python, TypeScript, Go, Rust

**Dataset composition:** 199 features, 30 tasks, 12 repos, 652 unique feature pairs

#### 1.3 Models Evaluated

All use OpenHands v0.54 agent framework:
- GPT-5 (via official API)
- Claude Sonnet 4.5 (via GCP)
- MiniMax-M2 (via official API)
- Qwen3-Coder-30B-A3B-Instruct (via vLLM)
- Qwen3-30B-A3B-Instruct-2507 (via vLLM)

#### 1.4 Main Results (Figure 4)

| Model | Solo | Coop | Gap |
|-------|------|------|-----|
| GPT-5 | 48% | 28% | -20% |
| Claude Sonnet 4.5 | 47% | 26% | -21% |
| MiniMax-M2 | 36% | 14% | -22% |
| Qwen3-Coder | 22% | 13% | -9% |
| Qwen3-30B | 6% | 5% | -1% |

> "The curse of coordination": All models perform worse in Coop vs Solo. Gap is ~50% for leading models.

#### 1.5 Communication Analysis (Figure 5)

- Communication does NOT improve cooperation success rate (no statistically significant difference between "with comm" and "no comm")
- Communication DOES reduce merge conflicts significantly
- Agents spend up to 20% of action budget on communication
- Communication types: Plan (~1/3), Question (~1/3), Update (~1/3)

**What distinguishes effective communication:**
- Successful agents plan more and question less (Plan:Question ratio 2.04 vs 1.31)
- First-turn planning nearly halves conflict rate (29.4% vs 51.5%)
- Specificity matters: successful trajectories have 32.6 line number mentions vs 22.5

**Spatial vs semantic coordination:** Communication helps spatial coordination (who edits where) but not semantic coordination (what to implement). This explains why conflicts decrease but success doesn't improve.

**Communication defects:** Repetition (up to 37.1% of conversations), unresponsiveness (up to 21.3%), hallucination (up to 6.9%).

#### 1.6 Failure Analysis

**Failure symptoms (Table 1):** Categorized via GPT-5 as LLM-as-Judge, validated by human annotators.

**Failure root causes (Table 2, from 50 manually reviewed traces):**
1. **Expectation failures (42%):** Agents fail to integrate partner state information, duplicate work, overwrite changes
2. **Commitment failures (32%):** Agents break promises, make unverifiable claims about code state
3. **Communication failures (26%):** Unanswered questions, messages arrive too late, repetitive/vague updates

#### 1.7 Scaling Experiment

On 46-task subset, scaling number of agents:
- 2 agents: 68.6% success
- 3 agents: 46.5% success
- 4 agents: 30.0% success

> Monotonic decline confirms "curse of coordination" beyond 2-agent setting.

#### 1.8 Mid-Difficulty Crisis

The coordination gap is largest for middle-difficulty tasks. Very easy tasks allow agents to spare effort for coordination; very hard tasks are difficult regardless. Middle-difficulty tasks create the most tension between technical and coordination demands.

#### 1.9 Emergent Coordination Patterns (§6.4)

In successful runs, three spontaneous patterns emerge:
1. **Role Division:** Agents establish clear task boundaries with mutual confirmation
2. **Resource Division:** Agents partition shared resources (files, line ranges) with specific boundaries
3. **Negotiation:** Agents propose mutually exclusive alternatives before implementation

These are rare but suggest latent coordination capabilities that could be reinforced.

### 2. GitHub Repository (https://github.com/cooperbench/CooperBench)

- pip installable: `pip install cooperbench`
- CLI: `cooperbench run`, `cooperbench eval`, `cooperbench config`
- Backends: Modal (default), GCP, Docker
- Redis for inter-agent communication
- Python 3.12+ required
- Settings: `coop` (two agents) and `solo` (one agent)
- MIT License

### 3. Leaderboard (https://cooperbench.com/leaderboard)

8 entries as of 2026-04-18:

| Model | Framework | Solo | Coop | Gap |
|-------|-----------|------|------|-----|
| Gemini 3 Flash | OpenHands SDK | 48.6% | 26.2% | -22.4% |
| GPT-5 | OpenHands | 48.31% | 27.95% | -20.36% |
| Claude Sonnet 4.5 | OpenHands | 47.1% | 25.9% | -21.2% |
| Gemini 3 Pro | Mini-SWE | 36.8% | 20.4% | -16.4% |
| MiniMax M2 | OpenHands | 36.2% | 14.0% | -22.2% |
| Gemini 3 Flash | Mini-SWE | 25.2% | 12.3% | -12.9% |
| Qwen3-Coder-30B | OpenHands | 21.6% | 13.3% | -8.3% |
| Qwen3-30B | OpenHands | 6.3% | 4.6% | -1.7% |

### 4. Harbor Adapter (cooperbench)

**adapter_metadata.json:**
- Split: full, Size: 652 tasks
- Harness: agent (openhands-sdk, mini_swe_agent supported)
- Parity on flash subset (50 pairs): original 32.7% ±2.3% vs harbor 30.7% ±2.3%
- Parity matching agent: openhands-sdk@1.10.0+gemini-3-flash-preview
- Parity cost: ~$30 (3 runs × 50 tasks)
- Both agents run as openhands-sdk sidecars with isolated Docker volumes
- Redis brokers messages
- Verification merges both patches and runs both feature test suites
- Oracle: 30/30 base tasks pass

**parity_experiment.json:**
- Agent: openhands-sdk@1.10.0, Model: gemini-3-flash-preview
- Date: 2026-03-17
- 3 runs
- Original: 32.67% ±2.31% (runs: 0.34, 0.30, 0.34)
- Harbor: 30.67% ±2.31% (runs: 0.28, 0.32, 0.32)
- Metric: pass_rate

---

## Questions

1. **Primary metric**: CooperBench tracks both Solo and Coop success rates, plus the Gap. The primary evaluation metric should be the Coop success rate (the cooperative setting is the benchmark's core contribution), but Solo provides important context. Should both be tracked in the template?

2. **Multiple agent frameworks**: The leaderboard shows models tested with different frameworks (OpenHands, OpenHands SDK, Mini-SWE). Per the template `system_description` rules, these should be listed as the scaffold. But some entries have the same model with different frameworks — should they be treated as separate entries?

3. **Leaderboard vs paper numbers differ slightly**: The paper (Figure 4) shows GPT-5 Solo=0.48, Coop=0.28; the leaderboard shows Solo=48.31%, Coop=27.95%. These are close but not identical — likely due to the leaderboard using a slightly different evaluation or more runs. I used the leaderboard values for the leaderboard snapshot.

4. **Harbor adapter parity subset**: Parity was only run on the "flash" subset (50 of 652 tasks), not the full benchmark. This is a 7.7% sampling rate, which the adapter_metadata.json documents.

5. **Category classification**: I classified this as "Agentic/Interactive" since it evaluates multi-agent cooperation with real-time communication. It could also be "Repo-level Software Engineering" since the underlying tasks are coding tasks. Which fits better?
