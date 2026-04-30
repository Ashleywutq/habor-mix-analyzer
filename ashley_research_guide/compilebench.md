# CompileBench Benchmark Research

```json
{
  "name": "CompileBench",
  "category": "Agentic/Interactive",
  "used_llm_or_agent": "agent",

  "links": {
    "website": "https://www.compilebench.com/",
    "leaderboard": "https://www.compilebench.com/",
    "paper": null,
    "github": "https://github.com/QuesmaOrg/compilebench",
    "dataset": null
  },

  "meta": {
    "release_date": "2025-09",
    "num_tasks": 15
  },

  "evaluation": {
    "primary_metric": "accuracy (pass@1)",
    "harbor_aligned_metric": "Accuracy — CompileBench is already in Harbor format (built with Harbor Framework). Parity: terminus-2+claude-haiku-4-5 achieves 0.733 (73.3%) across 3 identical trials."
  },

  "results_over_time": [
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://www.compilebench.com/",
      "results": [
        {
          "model": "claude-opus-4.1-thinking-16k",
          "effort": "thinking-16k",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 1, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.8, "unit": null },
            { "metric": "cost", "value": 70.2, "unit": "USD" },
            { "metric": "time", "value": 11819.0, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-sonnet-4-thinking-16k",
          "effort": "thinking-16k",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.9333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.9111, "unit": null },
            { "metric": "cost", "value": 22.46, "unit": "USD" },
            { "metric": "time", "value": 10625.9, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-5-codex-high",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.9333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.9111, "unit": null },
            { "metric": "cost", "value": 10.19, "unit": "USD" },
            { "metric": "time", "value": 10953.7, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-5-high",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.9333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.8667, "unit": null },
            { "metric": "cost", "value": 8.38, "unit": "USD" },
            { "metric": "time", "value": 14302.0, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-sonnet-4.5",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.8667, "unit": null },
            { "metric": "cost", "value": 20.66, "unit": "USD" },
            { "metric": "time", "value": 7694.1, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-sonnet-4.5-thinking-16k",
          "effort": "thinking-16k",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.8444, "unit": null },
            { "metric": "cost", "value": 20.25, "unit": "USD" },
            { "metric": "time", "value": 9750.7, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-haiku-4.5-thinking-16k",
          "effort": "thinking-16k",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.7333, "unit": null },
            { "metric": "cost", "value": 9.04, "unit": "USD" },
            { "metric": "time", "value": 10653.5, "unit": "seconds" }
          ]
        },
        {
          "model": "grok-4",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.7111, "unit": null },
            { "metric": "cost", "value": 28.25, "unit": "USD" },
            { "metric": "time", "value": 17372.2, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-haiku-4.5",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.6889, "unit": null },
            { "metric": "cost", "value": 7.23, "unit": "USD" },
            { "metric": "time", "value": 7423.9, "unit": "seconds" }
          ]
        },
        {
          "model": "claude-sonnet-4",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.7778, "unit": null },
            { "metric": "cost", "value": 20.04, "unit": "USD" },
            { "metric": "time", "value": 8281.3, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-5-mini-high",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.7556, "unit": null },
            { "metric": "cost", "value": 2.73, "unit": "USD" },
            { "metric": "time", "value": 16558.9, "unit": "seconds" }
          ]
        },
        {
          "model": "deepseek-v3.1",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.6444, "unit": null },
            { "metric": "cost", "value": 21.28, "unit": "USD" },
            { "metric": "time", "value": 6570.2, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-5-minimal",
          "effort": "minimal",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5778, "unit": null },
            { "metric": "cost", "value": 2.47, "unit": "USD" },
            { "metric": "time", "value": 5080.3, "unit": "seconds" }
          ]
        },
        {
          "model": "kimi-k2-0905",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.8, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5778, "unit": null },
            { "metric": "cost", "value": 26.42, "unit": "USD" },
            { "metric": "time", "value": 6807.0, "unit": "seconds" }
          ]
        },
        {
          "model": "deepseek-v3.1-terminus",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.7333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.6444, "unit": null },
            { "metric": "cost", "value": 7.34, "unit": "USD" },
            { "metric": "time", "value": 10305.5, "unit": "seconds" }
          ]
        },
        {
          "model": "grok-code-fast-1",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.7333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.6444, "unit": null },
            { "metric": "cost", "value": 0.71, "unit": "USD" },
            { "metric": "time", "value": 9483.7, "unit": "seconds" }
          ]
        },
        {
          "model": "grok-4-fast",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.7333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5556, "unit": null },
            { "metric": "cost", "value": 2.08, "unit": "USD" },
            { "metric": "time", "value": 12739.1, "unit": "seconds" }
          ]
        },
        {
          "model": "glm-4.5",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.7333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.4889, "unit": null },
            { "metric": "cost", "value": 3.86, "unit": "USD" },
            { "metric": "time", "value": 4961.8, "unit": "seconds" }
          ]
        },
        {
          "model": "qwen3-max",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5333, "unit": null },
            { "metric": "cost", "value": 55.08, "unit": "USD" },
            { "metric": "time", "value": 6756.7, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-4.1-mini",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.4667, "unit": null },
            { "metric": "cost", "value": 3.78, "unit": "USD" },
            { "metric": "time", "value": 5657.2, "unit": "seconds" }
          ]
        },
        {
          "model": "gemini-2.5-pro",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5333, "unit": null },
            { "metric": "cost", "value": 11.3, "unit": "USD" },
            { "metric": "time", "value": 7880.5, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-4.1",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.5333, "unit": null },
            { "metric": "cost", "value": 11.71, "unit": "USD" },
            { "metric": "time", "value": 4038.9, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-oss-120b-high",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.4222, "unit": null },
            { "metric": "cost", "value": 2.3, "unit": "USD" },
            { "metric": "time", "value": 6636.8, "unit": "seconds" }
          ]
        },
        {
          "model": "gemini-2.5-flash",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.6, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.4, "unit": null },
            { "metric": "cost", "value": 2.27, "unit": "USD" },
            { "metric": "time", "value": 6144.8, "unit": "seconds" }
          ]
        },
        {
          "model": "gemini-2.5-flash-thinking",
          "effort": "thinking-16k",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.5333, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.4444, "unit": null },
            { "metric": "cost", "value": 6.41, "unit": "USD" },
            { "metric": "time", "value": 13765.7, "unit": "seconds" }
          ]
        },
        {
          "model": "gpt-5-mini-minimal",
          "effort": "minimal",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1)", "value": 0.4667, "unit": null },
            { "metric": "accuracy (pass@3)", "value": 0.2889, "unit": null },
            { "metric": "cost", "value": 0.33, "unit": "USD" },
            { "metric": "time", "value": 5371.9, "unit": "seconds" }
          ]
        }
      ],
      "note": "compilebench.com leaderboard snapshot as of 2026-04-22. 26 models tested on 15 compilation tasks. pass@1 = at least 1 of 3 attempts succeeds per task; pass@3 = fraction of all attempts that succeed. Cost and time are totals across all 15 tasks x 3 attempts. Claude Opus 4.1 (thinking-16k) is the only model to achieve 100% pass@1 but at highest cost ($70.20). GPT-5-mini (minimal) is the cheapest ($0.33) but only 46.7%."
    }
  ],"notes": "CompileBench tests whether LLMs can compile real-world open-source C/C++ projects from source. Created by Quesma, it focuses on practical build challenges that go beyond typical coding benchmarks.\n\n15 tasks across 4 open-source projects:\n- **curl** (HTTP client): SSL build, static linking, ARM64 cross-compilation, Windows cross-compilation\n- **jq** (JSON processor): standard build, static, musl static\n- **GNU Coreutils**: v9.7 standard, static, v5.0 legacy (2003)\n- **cowsay**: legacy build\n\nDifficulty range:\n- Easiest: curl-ssl (97% pass@1, median 1m48s)\n- Hardest: curl-ssl-arm64-static (1% pass@1, median 7m40s) — only Claude Opus 4.1 succeeded\n\nKey challenges:\n- Dependency resolution ('dependency hell')\n- Cross-compilation (ARM64, Windows)\n- Static linking with musl libc\n- Legacy toolchains (22-year-old code from 2003)\n- Alpine Linux builds\n\nBenchmark stats: 30,240 commands executed, 31,065 LLM requests, 66 hours total runtime, $376.77 total cost across all models.\n\nNo academic paper — this is an industry benchmark from Quesma. Made Hacker News front page (Sep 22, 2025).\n\nAlready in Harbor format (built with Harbor Framework). The adapter is essentially a pass-through.\n\nNotable: GPT-5-mini attempted to cheat by creating symlinks to system binaries instead of compiling from source. Verification checks caught this.\n\nLeaderboard at compilebench.com shows interactive results with Pareto frontiers for cost vs accuracy and speed vs accuracy."
}
```

---

## Detailed Research Notes

### 1. What is CompileBench?

CompileBench is an industry benchmark (no academic paper) created by Quesma that tests LLMs on real-world software compilation tasks. Published September 17, 2025. Made Hacker News front page September 22, 2025.

**Author:** Piotr Grabowski (Quesma)

#### 1.1 Task Design

15 tasks across 4 open-source projects, ranging from Easy to Hard:

**curl (HTTP client):**
- curl-ssl: Standard build with SSL/TLS 1.3, brotli, zlib, zstd (97% pass@1, easiest)
- curl-ssl-static: Static linking variant
- curl-ssl-musl: musl libc build
- curl-ssl-arm64: ARM64 cross-compilation
- curl-ssl-arm64-static: ARM64 + static + all dependencies (1% pass@1, hardest)
- curl-ssl-windows: Windows cross-compilation

**jq (JSON processor):**
- jq: Standard autotools build
- jq-static: Static linking
- jq-static-musl: musl toolchain

**GNU Coreutils:**
- coreutils-9.7: Standard build
- coreutils-9.7-static: Static linking
- coreutils-5.0-legacy: 2003-era code, outdated autotools/compilers

**cowsay:**
- cowsay: Small legacy build with unusual packaging

#### 1.2 Evaluation

Each task provides:
- Unmodified source code
- Interactive Linux terminal (Docker via Harbor Framework)
- Clear build objective

Verification checks:
- Binary actually created
- Correct version reported matching source
- Functional capability (e.g., successful HTTP requests for curl)

Metrics tracked: accuracy (pass@1 and pass@3), cost (USD), speed (inference + execution), commands executed.

#### 1.3 Key Results

**Pareto frontier (cost vs accuracy):**

| Accuracy | Model | Cost | Cost Ratio |
|----------|-------|------|-----------|
| 100% | Claude Opus 4.1 (thinking-16k) | $21.72 | 799x |
| 93% | GPT-5 (high reasoning) | $1.99 | 73x |
| 87% | Claude Haiku 4.5 | $1.08 | 40x |
| 80% | GPT-5-mini (high) | $0.27 | 10x |
| 47% | Grok Code Fast 1 | $0.10 | 3.5x |
| baseline | GPT-5-mini (minimal) | $0.03 | 1x |

**Pareto frontier (speed vs accuracy):**

| Accuracy | Model | Time | Speed Ratio |
|----------|-------|------|-----------|
| 100% | Claude Opus 4.1 (thinking-16k) | 58m48s | 7.2x |
| 93% | Claude Sonnet 4 (thinking-16k) | 45m40s | 5.6x |
| 87% | Claude Haiku 4.5 | 26m37s | 3.3x |
| 67% | Qwen3-Max | 11m18s | 1.4x |
| baseline | GPT-4.1 | 8m10s | 1x |

#### 1.4 Key Findings

- **Anthropic dominates accuracy**: Claude Sonnet/Opus top 2 positions
- **OpenAI dominates cost-efficiency**: GPT-5-mini on Pareto frontier
- **Google underperforms**: Gemini 2.5 Pro near bottom, with models producing incorrect outputs or expressing lack of confidence
- **Thinking-enabled models** substantially improve reliability but require much more time/cost
- **Cross-compilation is extremely hard**: ARM64 static build at 1% pass@1
- **Cheating detected**: GPT-5-mini tried to symlink system binaries instead of compiling

#### 1.5 Benchmark Scale

- 26 models tested (expanded from initial 19)
- 30,240 commands executed
- 31,065 LLM requests
- 66 hours total runtime (39h20m inference + 26h40m execution)
- $376.77 total cost

### 2. GitHub Repository (https://github.com/QuesmaOrg/compilebench)

- Uses Harbor Framework for Docker, LLM interactions, test execution
- ~70 line bash script invokes `harbor run` for each model/task combination
- Report generator: TypeScript/Astro static site
- MIT License
- Structure: datasets/ (Harbor task definitions), run/ (scripts), report/ (site generator)

### 3. Harbor Adapter (compilebench)

**adapter_metadata.json:**
- Split: full, Size: 15 tasks
- Harness: agent
- **Already in Harbor format** — the benchmark was built with Harbor Framework, so the adapter is a pass-through
- Parity matching agent: terminus-2+claude-haiku-4-5-20251001

**parity_experiment.json:**
- Agent: terminus-2, Model: claude-haiku-4-5-20251001
- Date: 2025-12-10
- 3 trials, all identical: 0.733 (73.3%)
- Metric: Accuracy
- Note: "Because compilebench is already in Harbor format, the parity test would always pass."

### 4. Leaderboard (https://www.compilebench.com/, as of April 2026)

26 models tested on 15 tasks, each with 3 attempts. Data extracted from inline JSON on the page.

| # | Model | Reasoning | pass@1 | pass@3 | Cost (USD) | Time (s) |
|---|-------|-----------|--------|--------|------------|----------|
| 1 | claude-opus-4.1-thinking-16k | yes | 100.0% | 80.0% | $70.20 | 11819 |
| 2 | claude-sonnet-4-thinking-16k | yes | 93.3% | 91.1% | $22.46 | 10626 |
| 3 | gpt-5-codex-high | yes | 93.3% | 91.1% | $10.19 | 10954 |
| 4 | gpt-5-high | yes | 93.3% | 86.7% | $8.38 | 14302 |
| 5 | claude-sonnet-4.5 | no | 86.7% | 86.7% | $20.66 | 7694 |
| 6 | claude-sonnet-4.5-thinking-16k | yes | 86.7% | 84.4% | $20.25 | 9751 |
| 7 | claude-haiku-4.5-thinking-16k | yes | 86.7% | 73.3% | $9.04 | 10654 |
| 8 | grok-4 | yes | 86.7% | 71.1% | $28.25 | 17372 |
| 9 | claude-haiku-4.5 | no | 86.7% | 68.9% | $7.23 | 7424 |
| 10 | claude-sonnet-4 | no | 80.0% | 77.8% | $20.04 | 8281 |
| 11 | gpt-5-mini-high | yes | 80.0% | 75.6% | $2.73 | 16559 |
| 12 | deepseek-v3.1 | no | 80.0% | 64.4% | $21.28 | 6570 |
| 13 | gpt-5-minimal | yes | 80.0% | 57.8% | $2.47 | 5080 |
| 14 | kimi-k2-0905 | no | 80.0% | 57.8% | $26.42 | 6807 |
| 15 | deepseek-v3.1-terminus | no | 73.3% | 64.4% | $7.34 | 10306 |
| 16 | grok-code-fast-1 | yes | 73.3% | 64.4% | $0.71 | 9484 |
| 17 | grok-4-fast | yes | 73.3% | 55.6% | $2.08 | 12739 |
| 18 | glm-4.5 | yes | 73.3% | 48.9% | $3.86 | 4962 |
| 19 | qwen3-max | no | 66.7% | 53.3% | $55.08 | 6757 |
| 20 | gpt-4.1-mini | no | 66.7% | 46.7% | $3.78 | 5657 |
| 21 | gemini-2.5-pro | yes | 60.0% | 53.3% | $11.30 | 7881 |
| 22 | gpt-4.1 | no | 60.0% | 53.3% | $11.71 | 4039 |
| 23 | gpt-oss-120b-high | yes | 60.0% | 42.2% | $2.30 | 6637 |
| 24 | gemini-2.5-flash | no | 60.0% | 40.0% | $2.27 | 6145 |
| 25 | gemini-2.5-flash-thinking | yes | 53.3% | 44.4% | $6.41 | 13766 |
| 26 | gpt-5-mini-minimal | yes | 46.7% | 28.9% | $0.33 | 5372 |

**Key observations:**
- Anthropic dominates top accuracy: only Claude Opus 4.1 achieves 100%
- Cost-efficiency Pareto: gpt-5-mini-minimal ($0.33/47%) → grok-code-fast-1 ($0.71/73%) → gpt-5-mini-high ($2.73/80%) → gpt-5-high ($8.38/93%) → claude-opus-4.1 ($70.20/100%)
- Gemini models cluster at 53-60% — weakest provider overall
- qwen3-max is expensive ($55.08) for only 66.7%
- pass@3 varies significantly at same pass@1 level — e.g. at 86.7% pass@1, claude-sonnet-4.5 has 86.7% pass@3 vs grok-4 at 71.1%

---

## Questions

1. **No paper**: CompileBench is an industry benchmark from Quesma with no academic paper. Should `paper` remain null, or should the blog post URL be used?

2. **Small benchmark**: Only 15 tasks. This is much smaller than other benchmarks in the list. Is this a concern for the template, or is it fine since each task is a complex multi-step compilation challenge?

3. **Already in Harbor format**: Unlike other adapters that translate from an external benchmark, CompileBench was built with Harbor Framework natively. The adapter is effectively a no-op. Should this be noted?

4. **Leaderboard data vs blog data**: The blog post reports different cost/time numbers than the leaderboard (e.g. Claude Opus 4.1 cost is $21.72 in blog vs $70.20 on leaderboard). The leaderboard appears to show totals across all 3 attempts × 15 tasks, while the blog may have shown per-attempt or different run configurations. The leaderboard is the authoritative source.

5. **Model naming**: The blog uses product names with reasoning effort levels (e.g., "GPT-5 (high reasoning)", "Claude Opus 4.1 (thinking-16k)"). Per the template system_description rules, these should probably be split (model = "GPT-5", system_description = null, with reasoning effort noted). But reasoning effort is a parameter, not a scaffold.

6. **Category**: I classified this as "Agentic/Interactive" since agents interact with a terminal to compile code. Could also be "Code Performance" since it tests build/compilation capabilities. Which fits better?
