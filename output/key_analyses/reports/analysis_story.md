# Key Analysis Cross-Benchmark Analysis

This report is intended to be read directly. Figures and compact table previews are embedded inline; CSV paths are listed for exact numbers and reproducibility.

## Directory Contract

- Key analysis tables: `output/key_analyses/tables/`
- Key analysis figures: `output/key_analyses/figures/`
- Layered table groups: `benchmark_level/`, `leaderboards/`, `task_level/`, `harbormix/`, and `provenance/`.
- Layered figure groups: `benchmark_level/`, `leaderboards/`, `task_level/`, and `harbormix/`.
- Leaderboard figures are further layered into `leaderboards/per_benchmark/` and `leaderboards/clustered/`; the report embeds only the clustered pages to keep reading compact.
- Intermediate study outputs: `output/intermediate_studies/`
- Intermediate imputed matrices and diagnostics: `data/processed/intermediate/`

The current preprocessing contract is task-first: task scores are filled first, then benchmark scores are aggregated from the filled task matrix. The original benchmark matrix is retained as metadata and as a sanity check, but benchmark scores are not imputed directly.

BenchPress mapping note: Dimitris's BenchPress repo treats benchmark prediction as an explicit analysis problem, compares benchmark-regression and SVD families under held-out validation, and uses a blend because regression can be more accurate while SVD gives broader coverage. Our schema is task-rich rather than model-benchmark-only, so we map that lesson by validating several task-fill families on held-out observed cells, using benchmark/task predictability tables for difficulty ranking, and keeping task aggregate alignment as a diagnostic rather than blindly trusting every aggregate.

Data provenance for the main studies:

| analysis | primary_matrix | processed_output |
| --- | --- | --- |
| coverage filtering | task-observed benchmark aggregate metadata | data/processed/intermediate/benchmark_from_task_aggregate_column_quality.csv |
| agent+model aggregate leaderboard | benchmark scores aggregated from filled task matrix | data/processed/intermediate/benchmark_from_task_aggregate_matrix.csv |
| per-benchmark mini-leaderboards | benchmark scores aggregated from filled task matrix | data/processed/intermediate/benchmark_from_task_aggregate_matrix.csv |
| model vs agent roles | benchmark-relative matrix aggregated from filled tasks | data/processed/intermediate/benchmark_from_task_aggregate_normalized_matrix.csv |
| benchmark predictability and similarity | benchmark-relative matrix aggregated from filled tasks | data/processed/intermediate/benchmark_from_task_aggregate_normalized_matrix.csv |
| terminus harness deltas | benchmark-relative matrix aggregated from filled tasks | data/processed/intermediate/benchmark_from_task_aggregate_normalized_matrix.csv |
| task similarity and representatives | filled task benchmark-relative matrix plus task quality metadata | data/processed/intermediate/task_imputed_normalized_matrix.csv |
| HaborMix candidate selection | processed task item statistics | data/processed/intermediate/task_item_stats.csv |

Preprocessing diagnostics:

Task imputation method: each score column is robustly centered and scaled after `log1p` for nonnegative unbounded columns. The pipeline compares column-median, row-mean shrinkage, two-way shrinkage, and low-rank iterative SVD candidates on held-out observed cells, then uses the lowest-MAE method. For this run the selected task imputer is `column_median` with rank 0. Observed task cells are restored exactly; filled task scores are inverse-transformed and clipped to the observed range of that task. Benchmark scores are then calculated as per-benchmark means across those task scores. Task-level imputation remains less stable than dense benchmark tables because the task matrix is much wider and sparser, so task conclusions are restricted to reliable bounded non-degenerate tasks.

| matrix | preprocessing_method | selected_imputation_method | missing_fraction_before_processing | selected_imputation_rank | task_imputation_method_used_for_benchmark_aggregation | task_imputation_rank_used_for_benchmark_aggregation | holdout_cells | holdout_rmse_scaled_score_space | holdout_mae_scaled_score_space |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| benchmark | task_imputation_then_benchmark_aggregate |  | 0.027 |  | column_median | 0.000 | 0 |  |  |
| task | column_median | column_median | 0.059 | 0.000 |  |  | 5491 | 11.222 | 0.837 |

Held-out task imputation comparison:

| method | rank | holdout_cells | rmse | mae |
| --- | --- | --- | --- | --- |
| column_median | 0 | 5491 | 11.222 | 0.837 |
| iterative_svd | 2 | 5491 | 11.246 | 0.839 |
| row_mean_shrunk | 0 | 5491 | 11.222 | 0.888 |
| two_way_shrunk | 0 | 5491 | 11.966 | 1.158 |

Interpretation: the task matrix is sparse and very wide, so this is a validation-backed fill, not ground truth. The aggregate benchmark table is more stable than individual filled cells because it averages over many task columns, but sparse benchmarks should still be read with their task-cell missingness fields.

Reliability conclusion: SVD is not automatically the right fill here. In this run, low-rank SVD improves RMSE because it reduces a few large scaled errors, but it loses on MAE, which is the better primary criterion for this mixed-scale sparse matrix because many robust-normalized task columns have outlier-sensitive tails. The selected column-median fill is therefore intentionally conservative: it preserves each task's observed center and avoids hallucinating row-level structure where the held-out cells do not support it.

## Research Question Coverage Checklist

| Question | Status | Main artifacts |
| --- | --- | --- |
| Agent vs model role overall and per benchmark | covered | `tables/benchmark_level/benchmark_within_family_model_vs_agent.csv`, `tables/benchmark_level/benchmark_within_family_summary.csv`, `figures/benchmark_level/within_family_model_vs_agent_summary.png` |
| BenchPress-style benchmark predictability and hard-to-predict benchmarks/tasks | covered | `tables/benchmark_level/benchmark_uniqueness_filtered.csv`, `tables/task_level/task_predictability_ranked.csv`, benchmark/task predictability figures |
| Benchmark/task similarity and clustering | covered | `tables/benchmark_level/benchmark_similarity_clusters.csv`, `tables/task_level/task_cross_benchmark_similarity.csv`, clustered heatmaps |
| Representative tasks per benchmark | covered | `tables/task_level/task_representative_tasks.csv`, `figures/task_level/task_best_representatives.png` |
| Mini-leaderboards grouped by similar benchmarks | covered | `tables/leaderboards/benchmark_mini_leaderboards.csv`, `figures/leaderboards/clustered/mini_leaderboards_cluster_*.png` |
| Agent harness improvements over Terminus | covered | `tables/benchmark_level/benchmark_agent_lift_vs_terminus.csv`, `tables/benchmark_level/terminus_delta_by_model.csv`, Terminus heatmaps |
| Quantitative HaborMix task selection | covered | `tables/harbormix/harbormix_selected_tasks.csv`, `tables/harbormix/harbormix_selection_by_benchmark.csv`, `figures/harbormix/harbormix_selection_diagnostics.png` |

## Study 1: Coverage Filtering

**Method:** Benchmark-level claims use benchmark aggregates derived from the filled task matrix, but coverage filtering still uses evidence metadata: at least 15 agent+model rows need some observed task evidence for that benchmark, and the missingness fields describe coverage before task filling. This filter keeps the key analysis story from leaning too heavily on filled task values.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/benchmark_level/benchmark_filtering.csv`

**Result overview and analysis:**
- Included 49 of 57 benchmarks.
- Excluded sparse benchmarks: crmarena, devopsgym, featurebench-modal, mlgym, dacode, aa-lcr, swebench-multilingual, cybergym.
- Benchmark scores are task aggregates, not direct benchmark-imputation outputs; pre-aggregation benchmark missing fraction was 0.027.

| benchmark | include_in_key_analysis | observed_count | missing_fraction | task_cell_missing_fraction |
| --- | --- | --- | --- | --- |
| aider-polyglot | True | 16 | 0.000 | 0.000 |
| aime | True | 16 | 0.000 | 0.000 |
| algotune | True | 16 | 0.000 | 0.000 |
| arc-agi-2 | True | 16 | 0.000 | 0.000 |
| bfcl | True | 16 | 0.000 | 0.000 |
| bigcodebench | True | 16 | 0.000 | 0.000 |
| bixbench | True | 16 | 0.000 | 0.000 |
| codepde | True | 16 | 0.000 | 0.000 |
| compilebench | True | 16 | 0.000 | 0.000 |
| crustbench | True | 16 | 0.000 | 0.123 |
| deepsynth | True | 16 | 0.000 | 0.000 |
| financeagent_terminal | True | 16 | 0.000 | 0.000 |

**Insight and findings:** Sparse columns should stay in appendix/provisional analysis until more experiments land. The main key analysis story should use the coverage-filtered benchmark set.

## Study 2: Model vs Agent Roles

**Method:** Within-family analysis compares model effect (score range across models in the same family, fixing agent to terminus-2) against agent effect (score delta from switching agent, fixing model). This is computed per (family, benchmark) pair and aggregated per family.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/benchmark_level/benchmark_within_family_model_vs_agent.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_within_family_summary.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_model_adjusted_effects.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_agent_adjusted_effects.csv`

![Within-family model vs agent effect size](../figures/benchmark_level/within_family_model_vs_agent_summary.png)

![Within-family model vs agent effect by benchmark](../figures/benchmark_level/within_family_model_vs_agent_detail.png)

![Model effects adjusted for agent and benchmark](../figures/benchmark_level/benchmark_model_adjusted_effects.png)

![Agent effects adjusted for model and benchmark](../figures/benchmark_level/benchmark_agent_adjusted_effects.png)

**Result overview and analysis:**
| family | model_effect_median | agent_effect_median | model_wins | total_benchmarks |
| --- | --- | --- | --- | --- |
| Anthropic | 0.233 | 0.059 | 44 | 48 |
| Google | 0.057 | 0.070 | 27 | 49 |
| OpenAI | 0.227 | 0.149 | 39 | 49 |

**Insight and findings:** Across all families with multiple models, switching model produces larger score changes than switching agent on the majority of benchmarks. The effect is strongest for Anthropic (model effect ~4x agent effect) and consistent for OpenAI (model wins 70% of benchmarks).

## Study 3: Agent+Model Leaderboards

**Method:** I keep `agent+model` rankings as descriptive mini-leaderboards. Per-benchmark mini-leaderboards use benchmark scores aggregated from filled tasks on each benchmark's original metric scale. Each mini-leaderboard shows all available agent+model rows, grouped by model with colored bars for agents, so the same plot makes model differences and agent harness differences visible. The aggregate top-agent plot uses mean within-benchmark score percentile, because averaging scores across benchmarks with different scales would be misleading.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/leaderboards/benchmark_agent_model_scores.csv`
- `output/key_analyses/tables/leaderboards/benchmark_scores_long.csv`
- `output/key_analyses/tables/leaderboards/benchmark_mini_leaderboards.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_similarity_clusters.csv`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_*.png`
- `output/key_analyses/figures/leaderboards/per_benchmark/mini_leaderboard_*.png`

![Top agent+model pairs on included benchmarks](../figures/leaderboards/benchmark_agent_model_top_scores.png)

![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_1_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_1_page_1.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_1.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_2.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_2.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_3.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_3.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_4.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_4.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_5.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_5.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_6.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_6.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_7.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_7.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_8.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_8.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_9.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_9.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_2_page_10.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_10.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_3_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_1.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_4_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_1.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_5_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_5_page_1.png)
![Mini-leaderboards leaderboards/clustered/mini_leaderboards_cluster_6_page_1.png](../figures/leaderboards/clustered/mini_leaderboards_cluster_6_page_1.png)

**Result overview and analysis:**
| rank | agent_model | mean_score_percentile_across_benchmarks | original_benchmark_table_coverage |
| --- | --- | --- | --- |
| 1 | codex + gpt-5.4 | 0.854 | 1.000 |
| 2 | gemini-cli + gemini-3.1-pro-preview | 0.814 | 1.000 |
| 3 | terminus-2 + gemini-3.1-pro-preview | 0.768 | 1.000 |
| 4 | claude-code + claude-opus-4-6 | 0.742 | 1.000 |
| 5 | terminus-2 + claude-opus-4-6 | 0.716 | 0.959 |
| 6 | claude-code + claude-sonnet-4-6 | 0.649 | 1.000 |
| 7 | terminus-2 + gemini-3-flash-preview | 0.580 | 1.000 |
| 8 | terminus-2 + claude-sonnet-4-6 | 0.575 | 0.980 |
| 9 | gemini-cli + gemini-3-flash-preview | 0.568 | 0.980 |
| 10 | codex + gpt-5-mini | 0.486 | 1.000 |

**Insight and findings:** Benchmark scores should be read benchmark by benchmark. The percentile aggregate is a compact descriptive ranking only; it is not a causal agent claim because model and agent are entangled in the row identity.

## Study 4: How Correlated Are Benchmarks?

### 4.1 Effective Dimensionality

**Method:** PCA on the full normalized benchmark score matrix (49 included benchmarks). The participation ratio (PR = (Σλ)² / Σλ²) measures how many components carry meaningful variance — a PR of k means the suite behaves like k independent benchmarks.

![Effective dimensionality: scree and cumulative variance](../figures/benchmark_level/benchmark_effective_dimensionality.png)

**Result:** 49 benchmarks collapse to ~1 effective independent dimensions (participation ratio). The first component alone explains 90.1% of variance; 1 components reach 90%, 3 reach 95%.

### 4.2 Domain-Aware Correlation Structure

**Method:** Every benchmark pair is labeled within-domain or cross-domain (using the domain taxonomy in `config.py`). We compare the Spearman correlation distributions to quantify how much domain grouping explains the correlation structure.

![Within- vs cross-domain correlation distributions](../figures/benchmark_level/benchmark_domain_correlation_comparison.png)

![Domain-grouped benchmark correlation heatmap](../figures/benchmark_level/benchmark_correlation_by_domain.png)

**Result:**
| group | n_pairs | mean_spearman | median_spearman | frac_above_0.7 |
| --- | --- | --- | --- | --- |
| cross-domain | 984 | 0.549 | 0.636 | 0.390 |
| within-domain | 192 | 0.639 | 0.694 | 0.479 |
| within: Agents, Tools & Systems | 28 | 0.685 | 0.754 | 0.571 |
| within: Knowledge & Long Context | 6 | 0.648 | 0.623 | 0.333 |
| within: Mathematics & Reasoning | 15 | 0.575 | 0.592 | 0.333 |
| within: Professional Domains | 10 | 0.741 | 0.716 | 0.500 |
| within: Scientific Research | 28 | 0.399 | 0.508 | 0.143 |
| within: Software Engineering | 105 | 0.690 | 0.728 | 0.571 |

### 4.3 Benchmark Predictability

**Method:** BenchPress-style predictability (adapted from Dimitris's BenchPress repo). For each model, 50% of its known scores are hidden; the remaining scores are used to predict the hidden cells via BenchPress = 0.6 × LogitBenchReg (top-5 correlated benchmarks, ridge regression in logit space) + 0.4 × SVD-Logit (rank-2 soft-impute in logit space). Per-benchmark median absolute error on held-out cells measures predictability: higher error means the benchmark carries more unique signal.

![Benchmark predictability ranking (BenchPress holdout error)](../figures/benchmark_level/benchmark_uniqueness_vs_coverage.png)

Hardest-to-predict benchmarks (highest holdout error):
| benchmark | cv_r2_from_other_included_benchmarks | cv_rmse |
| --- | --- | --- |
| gaia | -10.000 | 0.374 |
| codepde | -9.301 | 1.165 |
| ineqmath | -6.817 | 0.793 |
| bigcodebench | -5.005 | 1.011 |
| crustbench | -2.927 | 0.355 |
| mmau | -2.223 | 0.798 |
| aime | -1.986 | 0.461 |
| mmmlu | -1.854 | 0.545 |
| quixbugs | -1.623 | 1.174 |
| humanevalfix | -1.610 | 5.460 |

Most similar benchmark pairs:
| left | right | spearman |
| --- | --- | --- |
| aider-polyglot | swe-lancer | 0.974 |
| arc-agi-2 | kumo | 0.970 |
| deepsynth | terminal-bench | 0.965 |
| gaia2 | spreadsheetbench | 0.964 |
| gaia2 | spider2 | 0.952 |
| pixiu | qcircuitbench | 0.950 |
| aider-polyglot | arc-agi-2 | 0.950 |
| arc-agi-2 | swe-lancer | 0.950 |
| spider2 | spreadsheetbench | 0.947 |
| aider-polyglot | terminal-bench | 0.947 |

### 4.4 Greedy Benchmark Selection

**Method:** Starting from the most independent benchmark (lowest mean |correlation| to all others), greedily add the benchmark whose max |correlation| to the already-selected set is smallest. This orders benchmarks from most to least independently informative.

![Greedy benchmark selection order](../figures/benchmark_level/benchmark_greedy_selection.png)

### 4.5 Data-Driven Clustering

![Clustered benchmark similarity heatmap](../figures/benchmark_level/benchmark_similarity_clustered_heatmap.png)

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/benchmark_level/benchmark_uniqueness_filtered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_redundancy_pairs_filtered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_correlation_clustered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_domain_correlation_summary.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_effective_dimensionality.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_greedy_selection.csv`

**Insight and findings:** The 49 benchmarks carry ~1 effective independent dimension of variation (participation ratio), with PC1 alone explaining 90% of variance — a dominant 'general capability' factor ranks systems similarly across most benchmarks. Within-domain benchmarks are more correlated than cross-domain pairs, but domain alone does not explain all overlap: some cross-domain pairs correlate highly because they tap shared model capabilities. High correlation does NOT mean one benchmark can substitute for another — each benchmark still tests domain-specific skills and has independent value for diagnosing system strengths and weaknesses within its domain. Correlation tells us about the amount of independent ranking information, not about interchangeability. The least reconstructable benchmarks are gaia, codepde, ineqmath, bigcodebench, crustbench. The most predictable are aider-polyglot, deepsynth, terminal-bench, algotune, swe-lancer.

## Study 5: Task Similarity, Predictability, and Representatives

**Method:** Task-level analysis uses reliable, bounded, non-degenerate tasks only. Task similarity also uses same-dimensional vectors: every task is represented by its filled, standardized score profile across the same agent+model rows. A task is hard to predict when its maximum absolute profile correlation to peer tasks in the same benchmark is low. Representativeness is no longer pure correlation with the benchmark aggregate: I compute a leave-one-out aggregate correlation and multiply it by observed cross-agent/model variance, so redundant but low-discrimination tasks no longer dominate. Within- and cross-benchmark task similarity use median absolute task-profile correlations, with at most the most discriminative 40 tasks sampled per benchmark for cross-benchmark pair summaries. Difficulty tiers use mean task score thresholds: frontier <5%, hard 5-30%, medium 30-70%, easy 70-95%, saturated >95%.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/task_level/task_predictability_ranked.csv`
- `output/key_analyses/tables/task_level/task_representative_tasks.csv`
- `output/key_analyses/tables/task_level/task_within_benchmark_similarity.csv`
- `output/key_analyses/tables/task_level/task_cross_benchmark_similarity.csv`

![Hard-to-predict reliable tasks](../figures/task_level/task_hard_to_predict_ranked.png)

![Best representative task per benchmark](../figures/task_level/task_best_representatives.png)

![Task similarity across benchmark pairs](../figures/task_level/task_similarity_benchmark_pair_heatmap.png)

**Result overview and analysis:**
Hardest-to-predict reliable tasks:
| benchmark | task_id | task_unpredictability_score | difficulty_tier | task_score |
| --- | --- | --- | --- | --- |
| qcircuitbench | simon_oracle-n4 | 0.680 | frontier | 0.028 |
| mmmlu | mmmlu-bn-bd-00015 | 0.676 | hard | 0.075 |
| strongreject | strongreject_hate_harassment_and_discrimination_0000_pap_logical_appeal | 0.616 | easy | 0.887 |
| kumo | mythicalcreatureenv-t4-a6-v1-s0 | 0.604 | medium | 0.487 |
| crustbench | crustbench-fs-c | 0.601 | hard | 0.180 |
| bixbench | bix-29-q2 | 0.594 | hard | 0.087 |
| simpleqa | simpleqa-1339 | 0.592 | hard | 0.250 |
| strongreject | strongreject_hate_harassment_and_discrimination_0016_pap_logical_appeal | 0.589 | easy | 0.903 |
| strongreject | strongreject_violence_0019_pap_logical_appeal | 0.577 | easy | 0.938 |
| algotune | algotune-polynomial-real | 0.572 | hard | 0.052 |
| deepsynth | 14 | 0.571 | medium | 0.396 |
| financeagent_terminal | financeagent-7 | 0.567 | hard | 0.125 |

Most representative tasks:
| benchmark | task_id | useful_representativeness_score | representativeness_score | difficulty_tier | task_score |
| --- | --- | --- | --- | --- | --- |
| mmmlu | mmmlu-bn-bd-00012 | 0.470 | 0.941 | medium | 0.500 |
| mmmlu | mmmlu-en-us-00032 | 0.470 | 0.941 | medium | 0.500 |
| mmmlu | mmmlu-ko-kr-00106 | 0.470 | 0.941 | medium | 0.500 |
| mmmlu | mmmlu-ja-jp-00099 | 0.464 | 0.949 | medium | 0.487 |
| mmmlu | mmmlu-yo-ng-00142 | 0.464 | 0.949 | medium | 0.487 |
| research-code-bench | len_split_input_and_compute_norm | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | tabdiff_initialize_the_learnable_feature-wise_parameter_k_for_categorical_features | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | minp_scale_min_p_threshold | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | eomt_scale_block_forward | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | eomt_store_parameters | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | fractalgen_cfg_schedule | 0.459 | 0.918 | medium | 0.500 |
| research-code-bench | fractalgen_chunk_mask_to_pred | 0.459 | 0.918 | medium | 0.500 |

Benchmarks with strongest within-benchmark task similarity:
| benchmark | n_reliable_tasks | median_abs_task_similarity_within_benchmark |
| --- | --- | --- |
| humanevalfix | 139 | 0.947 |
| ineqmath | 96 | 0.850 |
| mmmlu | 132 | 0.822 |
| research-code-bench | 191 | 0.740 |
| lawbench | 155 | 0.704 |
| financeagent_terminal | 48 | 0.702 |
| kumo | 196 | 0.683 |
| compilebench | 15 | 0.668 |
| mlgym | 2 | 0.651 |
| sldbench | 8 | 0.646 |

**Insight and findings:** Task predictability and useful representativeness are different objectives. Representative tasks are the base set for predicting benchmark aggregates; hard-to-predict and difficult tasks are additional stress tests for broad coverage.

Paper-facing read: the hardest-to-predict task examples begin with qcircuitbench/simon_oracle-n4, mmmlu/mmmlu-bn-bd-00015, strongreject/strongreject_hate_harassment_and_discrimination_0000_pap_logical_appeal. The most useful representative task examples begin with mmmlu/mmmlu-bn-bd-00012, mmmlu/mmmlu-en-us-00032, mmmlu/mmmlu-ko-kr-00106. That split is the main reason HaborMix should not be selected from one scalar alone: a task can be representative without being unique, and a unique task can be too idiosyncratic to stand in for its benchmark.

## Study 6: Terminus Harnessing Effects

**Method:** Terminus is treated as the fair baseline across models. For every model with both `terminus-2` and another agent row, I compute paired benchmark-relative score deltas while holding the model fixed.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/benchmark_level/benchmark_agent_lift_vs_terminus.csv`
- `output/key_analyses/tables/benchmark_level/terminus_delta_by_model.csv`
- `output/intermediate_studies/benchmark_level/benchmark_agent_lift_by_benchmark.csv`

![Agent lift vs terminus by benchmark](../figures/benchmark_level/benchmark_agent_lift_heatmap.png)

![Agent lift vs terminus by model](../figures/benchmark_level/terminus_delta_by_model_heatmap.png)

**Result overview and analysis:**
| agent | mean_delta_vs_terminus | win_rate_vs_terminus | compared_models |
| --- | --- | --- | --- |
| claude-code | 0.300 | 0.639 | 3 |
| gemini-cli | -0.107 | 0.602 | 2 |
| codex | -0.131 | 0.707 | 3 |

| model | agent | mean_delta_vs_terminus | win_rate_vs_terminus |
| --- | --- | --- | --- |
| gpt-5.4 | codex | 0.825 | 0.939 |
| claude-haiku-4-5-20251001 | claude-code | 0.764 | 0.816 |
| gpt-5-mini | codex | 0.506 | 0.816 |
| claude-sonnet-4-6 | claude-code | 0.113 | 0.673 |
| gemini-3.1-pro-preview | gemini-cli | 0.085 | 0.633 |
| claude-opus-4-6 | claude-code | 0.022 | 0.429 |
| gemini-3-flash-preview | gemini-cli | -0.298 | 0.571 |
| gpt-5-nano | codex | -1.723 | 0.367 |

**Insight and findings:** Paired deltas are the best current evidence for whether an agent harness improves over Terminus. The deltas vary by model and benchmark, so claims should avoid saying one harness universally dominates.

## Study 7: HaborMix Selection

**Method:** Candidate tasks must be reliable and bounded. The final HaborMix selection targets a compact 100-200 task set, currently 160 tasks. It first includes a small base set of useful representative tasks per benchmark, then fills the remaining slots with a diversity-aware ranking over difficult, frontier-with-variance, unique/unpredictable, and high-composite tasks. The composite score combines useful representativeness, difficulty, unique/unpredictable signal, and cross-agent/model discrimination; it no longer excludes frontier or saturated items by construction. The broader scored pool is retained under intermediate studies for auditability.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/harbormix/harbormix_selected_tasks.csv`
- `output/key_analyses/tables/harbormix/harbormix_selection_by_benchmark.csv`
- `output/intermediate_studies/task_level/harbormix_scored_task_pool.csv`
- `output/intermediate_studies/task_level/task_frontier_or_saturated_watchlist.csv`

![HaborMix selection diagnostics](../figures/harbormix/harbormix_selection_diagnostics.png)

![Reliable bounded task difficulty composition](../figures/task_level/task_reliable_difficulty_composition.png)

![Reliable bounded task difficulty composition by percentage](../figures/task_level/task_reliable_difficulty_composition_percent.png)

**Result overview and analysis:**
| benchmark | difficulty_tier | selected_tasks | mean_selection_score | mean_representative_signal | mean_unique_unpredictable_signal | mean_difficulty_signal |
| --- | --- | --- | --- | --- | --- | --- |
| arc-agi-2 | medium | 3 | 0.752 | 0.963 | 0.485 | 0.621 |
| featurebench-modal | medium | 3 | 0.750 | 0.963 | 0.513 | 0.571 |
| seal0 | medium | 3 | 0.747 | 0.950 | 0.575 | 0.515 |
| strongreject | medium | 3 | 0.719 | 0.973 | 0.551 | 0.372 |
| gso | medium | 3 | 0.714 | 0.956 | 0.424 | 0.513 |
| qcircuitbench | medium | 3 | 0.707 | 0.933 | 0.487 | 0.478 |
| aider-polyglot | medium | 3 | 0.707 | 0.991 | 0.416 | 0.446 |
| labbench | medium | 3 | 0.693 | 0.943 | 0.244 | 0.621 |
| swesmith | medium | 3 | 0.692 | 0.962 | 0.359 | 0.500 |
| skillsbench | medium | 3 | 0.687 | 0.974 | 0.331 | 0.475 |
| hle | medium | 3 | 0.681 | 0.881 | 0.375 | 0.525 |
| omnimath | medium | 3 | 0.679 | 0.890 | 0.443 | 0.446 |
| gaia | medium | 3 | 0.677 | 0.960 | 0.390 | 0.410 |
| widesearch | medium | 3 | 0.675 | 0.940 | 0.447 | 0.373 |

- Selected 160 final HaborMix tasks from the broader scored candidate pool.

**Insight and findings:** HaborMix selection is quantitative and auditable: representative tasks anchor the minimal benchmark-prediction base, while difficult and unique/unpredictable tasks add breadth.

Paper-facing read: the final 160-task set is intentionally not just a hard-task list. Its difficulty composition is medium: 108, easy: 38, hard: 13, frontier: 1. The base representative set keeps each included benchmark anchored to its aggregate behavior, while the diversity-aware fill adds difficult, frontier, and uniquely informative items.

## Study 8: Task Aggregate vs Benchmark-Level Score Alignment

**Method:** For each benchmark, I average benchmark-relative task scores and correlate that aggregate with the benchmark-level benchmark-relative score across agent+model rows. This is intentionally diagnostic rather than a hard gate: the new benchmark score is already the task aggregate, so this table mainly identifies benchmarks where reliable bounded tasks alone do or do not track the full task-derived benchmark aggregate.

**Code files:**
- `src/habor_mix_analyzer/core/`
- `src/habor_mix_analyzer/preprocessing/svd_imputation.py`
- `src/habor_mix_analyzer/studies/coverage_filtering.py`
- `src/habor_mix_analyzer/studies/intermediate_tables.py`
- `src/habor_mix_analyzer/studies/model_agent_roles.py`
- `src/habor_mix_analyzer/studies/benchmark_predictability.py`
- `src/habor_mix_analyzer/studies/benchmark_similarity.py`
- `src/habor_mix_analyzer/studies/leaderboards.py`
- `src/habor_mix_analyzer/studies/terminus_comparison.py`
- `src/habor_mix_analyzer/studies/task_alignment.py`
- `src/habor_mix_analyzer/studies/task_selection.py`
- `src/habor_mix_analyzer/studies/task_similarity.py`
- `src/habor_mix_analyzer/studies/provenance.py`
- `src/habor_mix_analyzer/visualization/`
- `src/habor_mix_analyzer/reporting/key_analysis_report.py`
- `src/habor_mix_analyzer/cli.py`

**Result paths:**
- `output/key_analyses/tables/task_level/task_to_benchmark_alignment.csv`

![Task aggregate vs benchmark score alignment](../figures/task_level/task_to_benchmark_alignment.png)

**Result overview and analysis:**
| benchmark | n_reliable_bounded_tasks | spearman_agent_model_correlation | alignment_quality |
| --- | --- | --- | --- |
| arc-agi-2 | 100 | 0.999 | strong |
| skillsbench | 75 | 0.997 | strong |
| labbench | 181 | 0.991 | strong |
| aider-polyglot | 225 | 0.991 | strong |
| widesearch | 100 | 0.988 | strong |
| aime | 60 | 0.988 | strong |
| simpleqa | 200 | 0.988 | strong |
| livecodebench | 100 | 0.988 | strong |
| replicationbench | 90 | 0.988 | strong |
| gaia | 165 | 0.988 | strong |
| scicode | 80 | 0.985 | strong |
| terminal-bench | 89 | 0.982 | strong |

**Insight and findings:** Strong alignment means the reliable bounded subset is a good proxy for the task-derived benchmark score. Weak alignment is not used to remove benchmarks automatically; it flags cases for manual benchmark/task inspection.

## Cross-Study Story

The emerging story is that benchmark diversity matters more than a single aggregate leaderboard. Coverage filtering removes sparse columns from the main benchmark-level claims, and the imputation diagnostic makes the same point from the preprocessing side: the data are dense only after filling, and the selected fill is conservative because held-out validation did not justify stronger SVD structure by MAE.

Within the retained benchmarks, model identity is usually more impactful than agent identity. Within-family analysis shows that switching model produces larger score changes than switching agent on the majority of benchmarks across all major model families. The report keeps descriptive `agent+model` leaderboards for browsing, but uses paired Terminus deltas when making harness claims.

The BenchPress-style predictability layer identifies a preservation/compression axis. Benchmarks such as gaia, codepde, ineqmath, bigcodebench, crustbench are hard to reconstruct and therefore carry distinctive signal. Benchmarks such as aider-polyglot, deepsynth, terminal-bench, algotune, swe-lancer are easier to reconstruct and can be grouped more aggressively. The clustered heatmaps and clustered mini-leaderboards give the visual version of the same argument.

The task layer answers a different selection problem. Representative tasks are useful as small proxies for benchmark aggregates; unpredictable and difficult tasks are useful as stress tests. HaborMix combines those roles by taking representative base tasks first, then filling with difficult, unique, and discriminative tasks until the final compact set reaches the target size range. That is the clearest story for why HaborMix is not merely a random subset, not merely a hard subset, and not merely a redundant set of benchmark prototypes.

## Artifact Index

All key analysis tables:
- `output/key_analyses/tables/benchmark_level/benchmark_agent_adjusted_effects.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_agent_lift_vs_terminus.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_correlation_clustered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_domain_correlation_summary.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_domain_enriched_pairs.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_effective_dimensionality.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_filtering.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_greedy_selection.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_headroom_by_domain.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_model_adjusted_effects.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_redundancy_pairs_filtered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_similarity_clusters.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_uniqueness_filtered.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_within_family_model_vs_agent.csv`
- `output/key_analyses/tables/benchmark_level/benchmark_within_family_summary.csv`
- `output/key_analyses/tables/benchmark_level/terminus_delta_by_model.csv`
- `output/key_analyses/tables/harbormix/harbormix_selected_tasks.csv`
- `output/key_analyses/tables/harbormix/harbormix_selection_by_benchmark.csv`
- `output/key_analyses/tables/leaderboards/benchmark_agent_model_scores.csv`
- `output/key_analyses/tables/leaderboards/benchmark_mini_leaderboards.csv`
- `output/key_analyses/tables/leaderboards/benchmark_scores_long.csv`
- `output/key_analyses/tables/provenance/analysis_data_provenance.csv`
- `output/key_analyses/tables/provenance/imputation_diagnostics_summary.csv`
- `output/key_analyses/tables/task_level/task_benchmark_reliable_summary.csv`
- `output/key_analyses/tables/task_level/task_cross_benchmark_similarity.csv`
- `output/key_analyses/tables/task_level/task_predictability_ranked.csv`
- `output/key_analyses/tables/task_level/task_representative_tasks.csv`
- `output/key_analyses/tables/task_level/task_to_benchmark_alignment.csv`
- `output/key_analyses/tables/task_level/task_within_benchmark_similarity.csv`

All key analysis figures:
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_aider-polyglot.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_aime.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_algotune.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_arc-agi-2.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_bfcl.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_bigcodebench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_bixbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_codepde.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_compilebench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_crmarena.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_crustbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_dacode.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_deepsynth.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_featurebench-modal.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_financeagent_terminal.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_gaia.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_gaia2.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_gpqa-diamond.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_gso.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_hle.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_humanevalfix.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_ineqmath.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_kumo.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_labbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_lawbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_livecodebench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_medagentbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_mmau.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_mmmlu.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_omnimath.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_pixiu.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_qcircuitbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_quixbugs.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_reasoning-gym.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_replicationbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_research-code-bench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_scicode.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_seal0.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_simpleqa.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_skillsbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_sldbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_spider2.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_spreadsheetbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_strongreject.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swe-lancer.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swebench-multilingual.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swebench-verified.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swebenchpro.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swesmith.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_swtbench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_terminal-bench.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_usaco.png`
- `output/key_analyses/figures/appendix/task_correlation_per_benchmark/task_corr_widesearch.png`
- `output/key_analyses/figures/benchmark_level/benchmark_agent_lift_heatmap.png`
- `output/key_analyses/figures/benchmark_level/benchmark_correlation_by_domain.png`
- `output/key_analyses/figures/benchmark_level/benchmark_domain_correlation_comparison.png`
- `output/key_analyses/figures/benchmark_level/benchmark_effective_dimensionality.png`
- `output/key_analyses/figures/benchmark_level/benchmark_greedy_selection.png`
- `output/key_analyses/figures/benchmark_level/benchmark_headroom_by_domain.png`
- `output/key_analyses/figures/benchmark_level/benchmark_headroom_by_score.png`
- `output/key_analyses/figures/benchmark_level/benchmark_headroom_tier_summary.png`
- `output/key_analyses/figures/benchmark_level/benchmark_model_adjusted_effects.png`
- `output/key_analyses/figures/benchmark_level/benchmark_similarity_clustered_heatmap.png`
- `output/key_analyses/figures/benchmark_level/benchmark_uniqueness_vs_coverage.png`
- `output/key_analyses/figures/benchmark_level/terminus_delta_by_model_heatmap.png`
- `output/key_analyses/figures/benchmark_level/within_family_model_vs_agent_detail.png`
- `output/key_analyses/figures/benchmark_level/within_family_model_vs_agent_summary.png`
- `output/key_analyses/figures/harbormix/harbormix_selection_diagnostics.png`
- `output/key_analyses/figures/leaderboards/benchmark_agent_model_top_scores.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_1_page_1.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_1.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_10.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_2.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_3.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_4.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_5.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_6.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_7.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_8.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_2_page_9.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_1.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_10.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_11.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_2.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_3.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_4.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_5.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_6.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_7.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_8.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_3_page_9.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_1.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_10.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_11.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_2.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_3.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_4.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_5.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_6.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_7.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_8.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_4_page_9.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_5_page_1.png`
- `output/key_analyses/figures/leaderboards/clustered/mini_leaderboards_cluster_6_page_1.png`
- `output/key_analyses/figures/task_level/task_best_representatives.png`
- `output/key_analyses/figures/task_level/task_hard_to_predict_ranked.png`
- `output/key_analyses/figures/task_level/task_reliable_difficulty_composition.png`
- `output/key_analyses/figures/task_level/task_reliable_difficulty_composition_percent.png`
- `output/key_analyses/figures/task_level/task_similarity_benchmark_pair_heatmap.png`
- `output/key_analyses/figures/task_level/task_to_benchmark_alignment.png`
- `output/key_analyses/figures/leaderboards/per_benchmark/` (54 per-benchmark mini-leaderboard files, listed by directory rather than expanded here)

## Not Completed Yet

- Trial reliability, pass@k, efficiency curves, token/tool cost analysis, and trajectory failure taxonomy still require per-trial run records.
- Full IRT/DIF still requires repeated binary/calibrated task outcomes or enough dense task observations to fit stable item-response models.
- Provider scaling analysis still requires external model metadata such as provider family, parameter scale, release date, and inference budget.
