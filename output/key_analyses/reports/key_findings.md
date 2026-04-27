# Key Findings for Key Analysis Drafting

0. The processed benchmark matrix is task-first and uses `column_median` task filling, not direct benchmark imputation.

Benchmark scores are simple means over the filled task matrix. The imputation reliability check compares candidate task fillers on held-out observed cells; SVD has lower RMSE here but higher MAE, so the selected fill is conservative rather than low-rank.

| method | rank | holdout_cells | rmse | mae |
| --- | --- | --- | --- | --- |
| column_median | 0 | 5491 | 11.222 | 0.837 |
| iterative_svd | 2 | 5491 | 11.246 | 0.839 |
| row_mean_shrunk | 0 | 5491 | 11.222 | 0.888 |
| two_way_shrunk | 0 | 5491 | 11.966 | 1.158 |

1. Use 53 coverage-filtered benchmarks for benchmark-level claims; keep sparse benchmarks in appendix/provisional analysis.

The filtering table is now evidence-based on the task-first pipeline: benchmark scores come from filled-task aggregates, while the missingness columns describe how much original task evidence supported each aggregate before filling.

![Benchmark predictability ranking](../figures/benchmark_level/benchmark_uniqueness_vs_coverage.png)

| benchmark | include_in_key_analysis | observed_count | task_cell_missing_fraction |
| --- | --- | --- | --- |
| aider-polyglot | True | 16 | 0.000 |
| aime | True | 16 | 0.000 |
| algotune | True | 16 | 0.000 |
| arc-agi-2 | True | 16 | 0.000 |
| bfcl | True | 16 | 0.000 |
| bigcodebench | True | 16 | 0.000 |
| bixbench | True | 16 | 0.000 |
| codepde | True | 16 | 0.000 |

2. Model identity is the larger overall factor. Within-family analysis shows switching model produces larger score changes than switching agent across the majority of benchmarks.

![Within-family model vs agent effect size](../figures/benchmark_level/within_family_model_vs_agent_summary.png)

| family | model_effect_median | agent_effect_median | model_wins | total_benchmarks |
| --- | --- | --- | --- | --- |
| Anthropic | 0.229 | 0.051 | 41 | 47 |
| Google | 0.073 | 0.063 | 27 | 50 |
| OpenAI | 0.219 | 0.149 | 35 | 49 |

3. Separate model and agent dimensions. The useful agent evidence is paired lift over `terminus-2` for the same model, not an unqualified agent+model leaderboard.

The Terminus table should be read as a harnessing-effect estimate: the paired comparison holds model fixed where the same model appears under Terminus and another agent.

![Agent lift vs terminus by model](../figures/benchmark_level/terminus_delta_by_model_heatmap.png)

| agent | mean_delta_vs_terminus | win_rate_vs_terminus | compared_models |
| --- | --- | --- | --- |
| gemini-cli | -0.085 | 0.604 | 2 |
| codex | -0.103 | 0.717 | 3 |
| claude-code | -5342380.699 | 0.623 | 3 |

4. BenchPress-style predictability applies here: redundant benchmarks can be compressed; least-predictable benchmarks should be preserved for behavioral breadth.

The benchmark-predictability result is deliberately separate from clustering: regression asks whether other benchmarks reconstruct a target, while the heatmap shows score-profile similarity. Use both when deciding whether two benchmarks are redundant.

![Clustered benchmark similarity heatmap](../figures/benchmark_level/benchmark_similarity_clustered_heatmap.png)

| benchmark | cv_r2_from_other_included_benchmarks | cv_rmse |
| --- | --- | --- |
| featurebench-modal | -10.000 | 0.534 |
| crustbench | -10.000 | 0.480 |
| bfcl | -10.000 | 0.644 |
| usaco | -10.000 | 0.602 |
| aime | -10.000 | 0.431 |
| swe-lancer | -9.356 | 0.496 |
| strongreject | -8.983 | 1.711 |
| simpleqa | -8.445 | 0.347 |

5. Task predictability and task representativeness are distinct: hard-to-predict tasks are stress tests, while representative tasks are compact proxies for a benchmark.

The representative-task score now uses leave-one-out aggregate correlation times task variance, so tasks that are merely typical but non-discriminative are less likely to dominate the selected base set.

![Hard-to-predict reliable tasks](../figures/task_level/task_hard_to_predict_ranked.png)

![Best representative task per benchmark](../figures/task_level/task_best_representatives.png)

| benchmark | task_id | task_unpredictability_score | difficulty_tier |
| --- | --- | --- | --- |
| qcircuitbench | simon_oracle-n4 | 0.680 | frontier |
| mmmlu | mmmlu-bn-bd-00015 | 0.676 | hard |
| strongreject | strongreject_hate_harassment_and_discrimination_0000_pap_logical_appeal | 0.616 | easy |
| kumo | mythicalcreatureenv-t4-a6-v1-s0 | 0.604 | medium |
| crustbench | crustbench-fs-c | 0.601 | hard |
| bixbench | bix-29-q2 | 0.594 | hard |
| simpleqa | simpleqa-1339 | 0.592 | hard |
| strongreject | strongreject_hate_harassment_and_discrimination_0016_pap_logical_appeal | 0.589 | easy |

| benchmark | task_id | useful_representativeness_score | difficulty_tier |
| --- | --- | --- | --- |
| mmmlu | mmmlu-bn-bd-00012 | 0.470 | medium |
| mmmlu | mmmlu-en-us-00032 | 0.470 | medium |
| mmmlu | mmmlu-ko-kr-00106 | 0.470 | medium |
| mmmlu | mmmlu-ja-jp-00099 | 0.464 | medium |
| mmmlu | mmmlu-yo-ng-00142 | 0.464 | medium |
| research-code-bench | len_split_input_and_compute_norm | 0.459 | medium |
| research-code-bench | tabdiff_initialize_the_learnable_feature-wise_parameter_k_for_categorical_features | 0.459 | medium |
| research-code-bench | minp_scale_min_p_threshold | 0.459 | medium |

6. The current HaborMix final set contains 160 diversified tasks.

The HaborMix scorer is no longer centered on moderate difficulty. It first takes useful representative base tasks, then fills to a compact target size with difficult, frontier-with-variance, unique/unpredictable, and high-composite tasks.

![HaborMix selection diagnostics](../figures/harbormix/harbormix_selection_diagnostics.png)

| benchmark | difficulty_tier | selected_tasks | mean_selection_score |
| --- | --- | --- | --- |
| arc-agi-2 | medium | 3 | 0.752 |
| featurebench-modal | medium | 3 | 0.750 |
| seal0 | medium | 3 | 0.747 |
| strongreject | medium | 3 | 0.719 |
| gso | medium | 3 | 0.714 |
| qcircuitbench | medium | 3 | 0.707 |
| aider-polyglot | medium | 3 | 0.707 |
| labbench | medium | 3 | 0.693 |
| swesmith | medium | 3 | 0.692 |
| skillsbench | medium | 3 | 0.687 |

7. Task-to-benchmark alignment should be used as a sanity check before interpreting benchmark-level scores from task-level tables.

This table is diagnostic rather than a gate. Weak alignment means the reliable bounded subset may not proxy the full task-derived aggregate well; it does not automatically remove the benchmark from the benchmark-level analysis.

![Task aggregate vs benchmark score alignment](../figures/task_level/task_to_benchmark_alignment.png)

| benchmark | n_reliable_bounded_tasks | spearman_agent_model_correlation | alignment_quality |
| --- | --- | --- | --- |
| featurebench-modal | 185 | 1.000 | strong |
| arc-agi-2 | 100 | 0.999 | strong |
| skillsbench | 75 | 0.997 | strong |
| labbench | 181 | 0.991 | strong |
| aider-polyglot | 225 | 0.991 | strong |
| widesearch | 100 | 0.988 | strong |
| aime | 60 | 0.988 | strong |
| simpleqa | 200 | 0.988 | strong |

Primary reference file: `output/key_analyses/reports/analysis_story.md`.