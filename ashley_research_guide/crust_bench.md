# CRUST-Bench Benchmark Research

```json
{
  "name": "CRUST-Bench",
  "category": "Repo-level Software Engineering",
  "used_llm_or_agent": "both",

  "links": {
    "website": null,
    "leaderboard": null,
    "paper": "https://arxiv.org/abs/2504.15254",
    "github": "https://github.com/anirudhkhatry/CRUST-bench",
    "dataset": null
  },

  "meta": {
    "release_date": "2025-04",
    "num_tasks": 100
  },

  "evaluation": {
    "primary_metric": "Test Pass Rate (pass@1)",
    "harbor_aligned_metric": "Resolved Rate — Harbor adapter covers all 100 tasks. Parity: original 58.3% ±1.2% vs harbor 58.3% ±2.1% averaged over 3 trials with codex@0.77.0+gpt-5-nano."
  },

  "results_over_time": [
    {
      "date": "2025-04",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2504.15254",
      "results": [
        {
          "model": "o3",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.19, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.35, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.31, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.68, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.48, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.63, "unit": null }
          ]
        },
        {
          "model": "Claude Opus 4",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.22, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.43, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.29, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.78, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.40, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.65, "unit": null }
          ]
        },
        {
          "model": "o1",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.15, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.32, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.28, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.69, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.37, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.54, "unit": null }
          ]
        },
        {
          "model": "Claude-3.7-Sonnet",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.13, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.26, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.23, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.54, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.32, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.49, "unit": null }
          ]
        },
        {
          "model": "Claude-3.5-Sonnet",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.11, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.26, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.21, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.49, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.24, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.38, "unit": null }
          ]
        },
        {
          "model": "o1-mini",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.09, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.19, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.16, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.47, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.21, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.27, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.07, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.18, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.18, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.52, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.22, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.42, "unit": null }
          ]
        },
        {
          "model": "Gemini-1.5-Pro",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.03, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.11, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.11, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.35, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.14, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.30, "unit": null }
          ]
        },
        {
          "model": "Virtuoso (Distilled DeepSeek-V3)",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.02, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.02, "unit": null },
            { "metric": "Test (Compiler repair r=3)", "value": 0.06, "unit": null },
            { "metric": "Build (Compiler repair r=3)", "value": 0.21, "unit": null },
            { "metric": "Test (Test repair r=3)", "value": 0.06, "unit": null },
            { "metric": "Build (Test repair r=3)", "value": 0.10, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-Coder-32B",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.00, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.01, "unit": null }
          ]
        },
        {
          "model": "QwQ-32B-Preview",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.00, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.01, "unit": null }
          ]
        },
        {
          "model": "Qwen-2.5-Coder-32B",
          "system_description": null,
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.00, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.00, "unit": null }
          ]
        },
        {
          "model": "Claude-3.7-Sonnet",
          "system_description": "Pipelined SWE-agent",
          "scores": [
            { "metric": "Test (pass@1)", "value": 0.32, "unit": null },
            { "metric": "Build (pass@1)", "value": 0.41, "unit": null }
          ]
        }
      ],
      "note": "Paper release baselines from Table 4. All pass@1 results use greedy decoding (T=0). Build = compilation success, Test = test passage. Values are counts out of 100 (= rates). Compiler repair and Test repair use r=3 rounds. LLaMA-3-8B omitted from paper as it produced no correct solutions. Pipelined SWE-agent uses $2 cost budget."
    }
  ],

  "notes": "CRUST-Bench evaluates C-to-safe-Rust transpilation at the repository level. Key characteristics:\n\n- 100 C repositories from GitHub (created 2005-2025), avg 958 LoC, covering PL infra, algorithms, data structures, system utilities, networking, crypto\n- Each paired with manually-written safe Rust interfaces (299 interface files, 3,085 functions total) and test cases (avg 76.4 tests, 67% coverage)\n- Three validation criteria: (1) interface conformance, (2) successful compilation (type check + borrow checker), (3) all tests pass\n- Annotated by 4 experts, avg 1.5 hours per benchmark, reviewed by first author\n- No external leaderboard — results only in paper\n- Published at COLM 2025\n\nThe Harbor adapter covers all 100 tasks with 1:1 mapping. Parity experiment uses codex@0.77.0+gpt-5-nano achieving 58.3% resolved rate (averaged over 3 trials).\n\nNote: The paper reports raw counts (e.g., o3 passes 19 tests out of 100 = 19%), not percentages. All values in the JSON are converted to [0,1] rates."
}
```

---

## Detailed Research Notes

### 1. Paper (arXiv:2504.15254, COLM 2025)

**Authors:** Anirudh Khatry, Robert Zhang*, Jia Pan*, Ziteng Wang* (*equal contribution), Qiaochu Chen, Greg Durrett, Isil Dillig

**Affiliations:** University of Texas at Austin (primary), New York University

**Paper:** 23 pages total. Submitted April 21, 2025; current version (v3) October 1, 2025. To be published at COLM 2025.

#### 1.1 Task Definition

Each benchmark instance consists of:
- **C repository** S = {S₁, ..., Sₙ}: collection of C source files
- **Target Rust repository** R = {R₁, ..., Rₙ}: parallel file structure
- **Interface** I = ((s₁, ..., sₙ), (f₁, ..., fₘ)): n abstract datatypes + m functions with type constraints and function signatures
- **Tests** T = (t₁, ..., tₖ): functional correctness validation

Transpilation is successful if:
1. R conforms to interface I (types, ownership semantics)
2. R compiles (type check + borrow checker)
3. All tests pass: tᵢ(R) = pass for all i

#### 1.2 Benchmark Construction

**Sourcing:** Open-source GitHub repos created 2005-2025, compiling with GCC 11.4.0 and Clang 14.0.0.

**Categories** (Figure 2): PL infra (15), Algorithmic (20), Data structures (21), System utilities (23), Networking (3), Crypto & security (11), Other (7)

**Preprocessing pipeline:**
- Filter: entirely C, ≥1 dynamic memory allocation keyword, build scripts, test files
- Automated de-duplication
- Manual review for code quality and test completeness
- Architecture-portable only (x86/x64)
- No GUI-based projects

**C Code Properties** (Table 2):

| Property | Avg | Max |
|----------|-----|-----|
| Test cases | 76.4 | 952 |
| Test files | 3.0 | 19 |
| Test coverage | 67% | 100% |
| Lines of code | 958 | 25,436 |
| Pointer dereferences | 264 | 12,664 |
| Functions | 34.6 | 418 |

**Annotation process:** 4 annotators (paper authors), 3 steps:
1. Convert C custom types (structs, enums) to Rust equivalents with safety/ownership enforcement
2. Specify function signatures with ownership annotations, bodies replaced with `unimplemented!()`
3. Construct Rust test files by adapting existing C tests

Average annotation time: 1.5 hours per benchmark. First author reviewed all. Pilot study: 20 benchmarks implemented and verified.

**Rust Interface Statistics** (Table 3):

| Metric | Total | Avg | Max |
|--------|-------|-----|-----|
| Interface files | 299 | 3.0 | 21 |
| Interface functions | 3,085 | 30.9 | 415 |
| Function arguments | 5,716 | 57.2 | 1,484 |

Ownership features: 56% functions use reference args, 44% custom type args, 50% return custom types, 30% mutable references.

#### 1.3 Experiments

**Models tested:**

Closed-source: o3, o1, o1-mini, GPT-4o (OpenAI); Claude Opus 4, Claude-3.7-Sonnet, Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google)

Open-weight: Virtuoso (Arcee.ai distilled DeepSeek-V3), QwQ-32B-Preview, Qwen-Coder-32B-Instruct, DeepSeek-Coder-33B-Instruct, LLaMA-3-8B (on 4x NVIDIA A40 via vLLM)

Settings: T=0 greedy decoding, avg 5,165 tokens generated per task.

**Self-repair strategies (3 rounds each):**
- Compiler repair: only compiler error messages in prompt
- Test repair: compiler errors + failing test case information

**Pipelined SWE-agent:** LLM generates initial Rust → SWE-agent iteratively repairs via Docker environment with Rust toolchain.

#### 1.4 Results (Table 4 — exact counts out of 100)

| Model | Build (pass@1) | Test (pass@1) | Build (Compiler r=3) | Test (Compiler r=3) | Build (Test r=3) | Test (Test r=3) |
|-------|---------------|---------------|---------------------|--------------------|-----------------|-----------------| 
| o3 | 35 | 19 | 68 | 31 | 63 | **48** |
| Claude Opus 4 | 43 | **22** | **78** | 29 | 65 | 40 |
| o1 | 32 | 15 | 69 | 28 | 54 | 37 |
| Claude 3.7 | 26 | 13 | 54 | 23 | 49 | 32 |
| Claude 3.5 | 26 | 11 | 49 | 21 | 38 | 24 |
| o1-mini | 19 | 9 | 47 | 16 | 27 | 21 |
| GPT-4o | 18 | 7 | 52 | 18 | 42 | 22 |
| Gemini 1.5 Pro | 11 | 3 | 35 | 11 | 30 | 14 |
| Virtuoso | 2 | 2 | 21 | 6 | 10 | 6 |
| DeepSeek-Coder-32B | 1 | 0 | 2 | 0 | 2 | 0 |
| QwQ-32B-Preview | 1 | 0 | 1 | 0 | 1 | 0 |
| Qwen-2.5-Coder-32B | 0 | 0 | 0 | 0 | 0 | 0 |
| Pipelined SWE-agent (Claude 3.7) | 41 | 32 | — | — | — | — |

Key findings:
- Best single-shot: Claude Opus 4 at 22/100 test pass, o3 at 19/100
- Best with repair: o3 + Test repair at 48/100
- Claude Opus 4 has highest single-shot build rate (43/100) and highest compiler repair build rate (78/100)
- Test repair improves test pass by 0-9% over compiler repair but decreases build stability by 5-20%
- Pipelined SWE-agent matches Claude 3.7 + Test repair (both 32/100)
- Open-weight models largely fail (0-2 tasks solved in pass@1)

#### 1.5 Error Analysis (Table 5)

Error categories (% of projects with error):
- **Mismatch**: Type mismatches in function calls or return types
- **Borrowing**: Ownership, borrowing, mutability, lifetime violations — reduce 75% after compiler repair
- **Missing**: Non-existent or out-of-scope variables
- **Unimpl**: Unimplemented functions (token budget truncation) — widespread, especially for models with shorter output limits
- **Trait**: Missing trait implementations — reduce 90% with repair
- **Args**: Incorrect argument counts
- **Unsafe**: Use of unsafe keyword (rare, due to prompt design)

> "Type-related errors (mismatch and borrow categories) are quite common... These errors suggest that models often struggle to reason precisely about lifetimes, mutability, and type compatibility."

#### 1.6 SWE-Agent Cost Budget Analysis (Table 6)

| Cost Budget | Test Pass |
|-------------|-----------|
| $1.00 | 14 |
| $2.00 | 32 |
| $4.00 | 21 |

> Performance plateaus at $2; $2-to-$4 increase yields no additional gains. Most fixed errors resolve in relatively few steps. ~80% of resolved test failures are addressed within first 50 steps.

#### 1.7 Self-Repair Strategy (Appendix B)

Pilot study (10 tasks) compared:
- Sample-and-repair: 3 candidates at T=0.8, each repaired once
- Greedy self-repair: 1 candidate, up to 5 repairs at T=0

Greedy outperformed sample-and-repair. Reasons: (a) compilers don't surface all errors simultaneously, requiring multiple iterations; (b) fixing errors can introduce new errors needing subsequent repair. 3 rounds found sufficient — improvements plateau beyond that.

#### 1.8 Related Benchmarks (Table 1)

| Benchmark | Tasks | Scope | Has Interfaces | Has Tests | Multi-file |
|-----------|-------|-------|---------------|-----------|-----------|
| CROWN | 20 | Full programs | No | Yes | Yes |
| TransCoder-Rust | 520 | Functions | No | Yes | No |
| FLOURINE | 112 | Narrow tasks | No | Yes | No |
| C2SaferRust | 7 | Large programs (9.3K LoC avg) | No | Yes | Yes |
| SYZYGY | 1 | Single project (2.5K LoC) | Yes | Yes | Yes |
| **CRUST-Bench** | **100** | **Full repos (958 LoC avg)** | **Yes** | **Yes** | **Yes** |

### 2. GitHub Repository (https://github.com/anirudhkhatry/CRUST-bench)

- Dataset: 100 C repos in `datasets/CBench/`, Rust interfaces in `datasets/RBench/`
- Pipeline: `src/run.py` for transpilation, `repair_tests.py` for test-guided repair
- Sanity check: `src/check_benchmarks/check_build.py` produces compilable projects with `unimplemented!()` bodies
- Custom model support via `endpoints/` folder
- License: GNU GPL

### 3. Harbor Adapter (crustbench)

**adapter_metadata.json:**
- Split: full, Size: 100 tasks
- Harness: agent
- 1:1 mapping from source benchmark
- Parity matching agent: codex@0.77.0+gpt-5-nano

**parity_experiment.json:**
- Agent: codex@0.77.0, Model: gpt-5-nano
- Date: 2026-01-07
- 3 trials
- Original: 58.3% ±1.2% (trials: 0.59, 0.59, 0.57)
- Harbor: 58.3% ±2.1% (trials: 0.59, 0.56, 0.60)
- Metric: Resolved Rate

Features: Docker environment with Rust 1.83-slim, vendored C sources, test-driven evaluation via `cargo test`.

### 4. Leaderboard

No external leaderboard exists. Results are only in the paper.

---

## Questions

1. **No leaderboard**: CRUST-Bench has no external leaderboard. The only results are from the paper (Table 4). Should we note this as a gap, or is it expected for newer benchmarks?

2. **Harbor parity vs paper results**: The Harbor parity experiment (codex@0.77.0+gpt-5-nano) achieves 58.3% resolved rate, which is much higher than any paper result (best is o3 + Test repair at 48%). This makes sense because the parity uses a newer model (gpt-5-nano) not in the paper, but it's worth noting the gap.

3. **Metric interpretation**: The paper reports raw counts (e.g., "19 tasks") rather than percentages. Since there are exactly 100 tasks, the counts equal percentages directly. I've converted to [0,1] rates in the JSON. The Harbor adapter uses "Resolved Rate" which appears equivalent to the paper's test pass rate.

4. **Build vs Test metrics**: CRUST-Bench tracks both build success (compilation) and test pass rates. The primary metric for the benchmark is test passage (since build is a prerequisite), but build rates provide useful signal about compilation challenges. Should both be included as separate scores per model in the JSON, or only the test rate?

5. **Multiple evaluation settings**: The paper reports 3 settings per model (pass@1, compiler repair, test repair) plus an agent setting. These are different compute regimes, not different benchmarks. The template may not be designed for this level of granularity per model.
