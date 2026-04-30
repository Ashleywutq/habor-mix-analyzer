# SWE-Lancer Benchmark Research

```json
{
  "name": "SWE-Lancer",
  "category": "Repo-level Software Engineering",
  "used_llm_or_agent": "agent",

  "links": {
    "website": "https://openai.com/index/swe-lancer/",
    "leaderboard": null,
    "paper": "https://arxiv.org/abs/2502.12115",
    "github": "https://github.com/openai/SWELancer-Benchmark",
    "dataset": null
  },

  "meta": {
    "release_date": "2025-02",
    "num_tasks": 1488
  },

  "evaluation": {
    "primary_metric": "pass@1",
    "harbor_aligned_metric": "Pass Rate (%) — Harbor adapter covers Diamond split (463 tasks). Parity: original 48.38% ±1.40% vs harbor 47.56% ±0.86% (claude-code@1.0.53+claude-sonnet-4, 5 vs 3 trials)."
  },

  "results_over_time": [
    {
      "date": "2025-02",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2502.12115",
      "results": [
        {
          "model": "Claude-3.5-Sonnet",
          "system_description": null,
          "scores": [
            { "metric": "pass@1 (Diamond overall)", "value": 0.361, "unit": null },
            { "metric": "pass@1 (IC SWE Diamond)", "value": 0.262, "unit": null },
            { "metric": "pass@1 (SWE Manager Diamond)", "value": 0.449, "unit": null },
            { "metric": "Earn Rate (Diamond)", "value": 0.415, "unit": null },
            { "metric": "Dollars Earned (Diamond)", "value": 208000, "unit": "USD" },
            { "metric": "pass@1 (Full overall)", "value": 0.337, "unit": null },
            { "metric": "Dollars Earned (Full)", "value": 403000, "unit": "USD" }
          ]
        },
        {
          "model": "o1",
          "system_description": null,
          "scores": [
            { "metric": "pass@1 (Diamond overall)", "value": 0.297, "unit": null },
            { "metric": "pass@1 (IC SWE Diamond, High)", "value": 0.165, "unit": null },
            { "metric": "pass@1 (SWE Manager Diamond)", "value": 0.415, "unit": null },
            { "metric": "Earn Rate (Diamond)", "value": 0.331, "unit": null },
            { "metric": "Dollars Earned (Diamond)", "value": 166000, "unit": "USD" },
            { "metric": "pass@1 (Full overall)", "value": 0.329, "unit": null },
            { "metric": "Dollars Earned (Full)", "value": 380000, "unit": "USD" }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": null,
          "scores": [
            { "metric": "pass@1 (Diamond overall)", "value": 0.233, "unit": null },
            { "metric": "pass@1 (IC SWE Diamond)", "value": 0.080, "unit": null },
            { "metric": "pass@1 (SWE Manager Diamond)", "value": 0.370, "unit": null },
            { "metric": "Earn Rate (Diamond)", "value": 0.277, "unit": null },
            { "metric": "Dollars Earned (Diamond)", "value": 139000, "unit": "USD" },
            { "metric": "pass@1 (Full overall)", "value": 0.233, "unit": null },
            { "metric": "Dollars Earned (Full)", "value": 304000, "unit": "USD" }
          ]
        }
      ],
      "note": "Paper release baselines from Table 1. Diamond set: 237 IC SWE tasks ($236,300) + 265 SWE Manager tasks ($264,500) = 502 tasks ($500,800). Full set: 764 IC SWE ($414,775) + 724 Manager ($585,225) = 1,488 tasks ($1M). IC SWE use user tool (Playwright) by default. o1 uses 'High' reasoning effort. All pass@1, single attempt. All models use basic scaffold (browse files, edit, execute terminal commands) in Docker with no internet."
    }
  ],

  "notes": "SWE-Lancer is an OpenAI benchmark of real freelance software engineering tasks from Upwork/Expensify, valued at $1 million USD total.\n\nTwo task types:\n1. **IC SWE** (Individual Contributor): Code generation tasks from $50 bug fixes to $32,000 feature implementations. Graded with end-to-end Playwright tests triple-verified by experienced engineers.\n2. **SWE Manager**: Choose between technical implementation proposals. Assessed against original engineering managers' decisions. 99% agreement between independent engineers and original choices.\n\nSplits:\n- **SWE-Lancer Diamond** (public eval): 502 tasks worth $500,800 (237 IC SWE + 265 Manager)\n- **SWE-Lancer Full** (private): 1,488 tasks worth $1,000,000 (764 IC SWE + 724 Manager)\n\nHarbor adapter covers Diamond split with 463 tasks (198 IC SWE + 265 Manager — slightly different from paper's 237 IC SWE, possibly due to filtering).\n\nUnique features:\n- Real economic value: tasks have actual Upwork payouts\n- User tool: Playwright browser simulation for IC SWE tasks, giving agents visual feedback\n- Price analysis: models can reduce freelancer costs by 8-33% when used as first pass\n- Single repo (Expensify), $300M public company, 12M users\n- Tasks from 2023-2024 public GitHub issues\n\nKey findings:\n- Best: Claude 3.5 Sonnet earns $208K on Diamond, $403K on Full ($1M total)\n- o1 with higher reasoning effort improves from 9.3% to 16.5% on IC SWE Diamond\n- Pass@k increases significantly: o1 nearly triples with 6 attempts\n- User tool removal has minimal impact on pass@1 but stronger models lose more\n- Published at ICML 2025\n\nGitHub repo archived July 2025, merged into https://github.com/openai/preparedness"
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2502.12115, ICML 2025)

**Authors:** Samuel Miserendino*, Michele Wang* (equal contribution), Tejal Patwardhan, Johannes Heidecke

**Affiliation:** OpenAI

**Paper:** 39 pages (9 main + 30 appendix). Submitted February 17, 2025; last revised May 29, 2025.

#### 1.1 Benchmark Construction Pipeline

1. **Repository selection:** Expensify — $300M public company (NASDAQ: EXFY), 12M users, open-source repo with Upwork freelance tasks
2. **Task selection:** 100 professional software engineers reviewed tasks for clarity, specificity, executability. High-value IC SWE tasks (>$5,000) validated by 10 experienced engineers. Triple review for IC SWE, double for Manager.
3. **Task generation:** From each validated GitHub issue, generate IC SWE task (title + description + codebase snapshot at posting time). If ≥2 proposals exist, also generate SWE Manager task.
4. **End-to-end test development:** Comprehensive Playwright tests simulating real user flows (login, financial transactions, etc.). Triple-verified by professional engineers.
5. **User tool:** Playwright browser simulation — agent invokes it to view work. Gets text trajectory + screenshots. No success/failure feedback.

#### 1.2 Task Composition

**SWE-Lancer Diamond (public eval):**
- 237 IC SWE tasks worth $236,300
- 265 SWE Manager tasks worth $264,500
- Total: 502 tasks worth $500,800

**SWE-Lancer Full (private):**
- 764 IC SWE tasks worth $414,775
- 724 SWE Manager tasks worth $585,225
- Total: 1,488 tasks worth $1,000,000

IC SWE task prices range from $50 bug fixes to $32,000 feature implementations.

#### 1.3 Main Results (Table 1)

**IC SWE Diamond (with user tool):**

| Model | Reasoning | pass@1 | Earned | Earn Rate |
|-------|-----------|--------|--------|-----------|
| Claude 3.5 Sonnet | N/A | 26.2% | $58K/$236K | 24.5% |
| o1 | High | 16.5% | $29K/$236K | 12.1% |
| o1 | Medium | 15.6% | $24K/$236K | 9.9% |
| o1 | Low | 9.3% | $16K/$236K | 6.8% |
| GPT-4o | N/A | 8.0% | $14K/$236K | 6.0% |

**SWE Manager Diamond:**

| Model | pass@1 | Earned | Earn Rate |
|-------|--------|--------|-----------|
| Claude 3.5 Sonnet | 44.9% | $150K/$265K | 56.8% |
| o1 | 41.5% | $137K/$265K | 51.8% |
| GPT-4o | 37.0% | $125K/$265K | 47.1% |

**Diamond Overall:**

| Model | pass@1 | Earned | Earn Rate |
|-------|--------|--------|-----------|
| Claude 3.5 Sonnet | 36.1% | $208K/$501K | 41.5% |
| o1 (High) | 29.7% | $166K/$501K | 33.1% |
| GPT-4o | 23.3% | $139K/$501K | 27.7% |

**Full Set:**

| Model | pass@1 | Earned |
|-------|--------|--------|
| Claude 3.5 Sonnet | 33.7% | $403K/$1M |
| o1 (High) | 32.9% | $380K/$1M |
| GPT-4o | 23.3% | $304K/$1M |

#### 1.4 Task Type Breakdown (Table 2)

| Task Type | GPT-4o | o1 | Sonnet 3.5 | n (IC) | n (Mgr) |
|-----------|--------|-----|------------|--------|---------|
| App Logic (Client-Side) | 8.0% | 15.9% | 23.9% | 176 | 201 |
| UI/UX | 2.4% | 17.1% | 31.7% | 41 | 49 |
| Server-Side Logic | 23.5% | 23.5% | 41.2% | 17 | 13 |
| System-Wide Quality | 0.0% | 0.0% | 0.0% | 3 | 2 |

#### 1.5 Pass@k Analysis

Giving models more attempts significantly increases pass rate:
- o1 nearly triples from pass@1 to pass@7 on Diamond IC SWE
- GPT-4o with pass@6 equals o1 pass@1 (16.5%)

#### 1.6 Test-Time Compute

o1 on IC SWE Diamond with user tool:
- Low reasoning: 9.3% pass@1, $16K earned
- Medium reasoning: 15.6% pass@1, $24K earned
- High reasoning: 16.5% pass@1, $29K earned

Higher reasoning effort especially helps on harder, more expensive problems.

#### 1.7 User Tool Ablation

Removing user tool minimally reduces pass@1 (Figure 9). Stronger models benefit more from the tool and experience greater performance drop without it.

#### 1.8 Price Analysis

On Diamond IC SWE (237 tasks, $236,300):
- GPT-4o + freelancer fallback: 8.84% cheaper than all-freelancer
- o1 + freelancer fallback: 13.26% cheaper
- Pass@5 savings: GPT-4o 18.6%, o1 33.5%
- Model contribution ratio: GPT-4o returns $0.10 per $1, o1 returns $0.16 per $1

### 2. GitHub Repository

Original: https://github.com/openai/SWELancer-Benchmark (archived July 2025)
Current: merged into https://github.com/openai/preparedness

### 3. Harbor Adapter (swe-lancer-diamond)

**adapter_metadata.json:**
- Split: diamond, Size: 463 tasks (198 IC SWE + 265 Manager)
- Note: paper says Diamond has 502 tasks (237 IC + 265 Manager), adapter has 463 (198 IC + 265 Manager) — 39 fewer IC SWE tasks
- Harness: agent (swelancer_agent)
- Parity matching agent: claude-code@1.0.53+claude-sonnet-4-20250514

**parity_experiment.json:**
- Agent: claude-code@1.0.53, Model: claude-sonnet-4-20250514
- Date: 2026-01-08
- 5 Harbor trials vs 3 original trials
- Original: 48.38% ±1.40% (trials: 46.44, 49.68, 49.03)
- Harbor: 47.56% ±0.86% (trials: 47.95, 48.60, 46.65, 48.16, 46.44)
- Metric: Pass Rate (%)

**Technical notes:**
- x86_64 Docker images (requires emulation on macOS)
- Total Docker images >200GB
- Playwright user tool can take >10 minutes, requiring 20-minute command timeouts

### 4. Leaderboard

No external leaderboard. Results only in the paper.

---

## Questions

1. **Task count discrepancy**: Paper says Diamond has 502 tasks (237 IC + 265 Manager). Harbor adapter has 463 (198 IC + 265 Manager). The adapter is missing 39 IC SWE tasks. Should this be flagged?

2. **Earn rate vs pass@1**: SWE-Lancer tracks both pass@1 and earn rate (dollar-weighted). Harder tasks are worth more, so a model could have lower pass@1 but higher earn rate if it solves expensive tasks. Which should be the primary metric?

3. **Harbor parity uses claude-sonnet-4** (a newer model not in the paper), achieving ~48% pass rate — much higher than the paper's best of 36.1% (Claude 3.5 Sonnet). This reflects model improvement since paper publication.

4. **Single repository limitation**: All tasks come from Expensify's codebase. This is both a strength (real commercial software) and limitation (not generalizable). Should this be noted prominently?

5. **Private full set**: SWE-Lancer Full (1,488 tasks, $1M) is not publicly available. Only Diamond (502/463 tasks) is public. Should `num_tasks` be 1488 (paper total) or 463 (Harbor adapter / public eval)?
