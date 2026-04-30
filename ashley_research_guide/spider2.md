# Spider 2.0 Benchmark Research

```json
{
  "name": "Spider 2.0",
  "category": "Agentic/Interactive",
  "used_llm_or_agent": "both",

  "links": {
    "website": "https://spider2-sql.github.io/",
    "leaderboard": "https://spider2-sql.github.io/",
    "paper": "https://arxiv.org/abs/2411.07763",
    "github": "https://github.com/xlang-ai/Spider2",
    "dataset": null
  },

  "meta": {
    "release_date": "2024-11",
    "num_tasks": 632
  },

  "evaluation": {
    "primary_metric": "Execution Accuracy (EX) for Spider 2.0-Lite/Snow; Success Rate (SR) for Spider 2.0/DBT",
    "harbor_aligned_metric": "Mean Resolved Rate (%) — Harbor adapter covers spider2-dbt split only (64 of 68 tasks). Parity: original 18.8% vs harbor 18.3% (±0.53) averaged over 3 trials with spider-agent+gpt-5-mini-2025-08-07."
  },

  "results_over_time": [
    {
      "date": "2024-11",
      "source_type": "paper",
      "source_url": "https://arxiv.org/abs/2411.07763",
      "results": [
        {
          "model": "o1-preview",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.2322, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.2377, "unit": null },
            { "metric": "SR (Spider 2.0)", "value": 0.2136, "unit": null }
          ]
        },
        {
          "model": "o3-mini",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.2340, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.1920, "unit": null }
          ]
        },
        {
          "model": "Claude-3.5-Sonnet",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.1554, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.1554, "unit": null },
            { "metric": "SR (Spider 2.0)", "value": 0.1487, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.1316, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.1298, "unit": null },
            { "metric": "SR (Spider 2.0)", "value": 0.1234, "unit": null }
          ]
        },
        {
          "model": "GPT-4",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0986, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-V3",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0878, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0878, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-V2.5",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0522, "unit": null }
          ]
        },
        {
          "model": "Qwen2.5-72B",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0617, "unit": null }
          ]
        },
        {
          "model": "Qwen2.5-Coder",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0530, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0548, "unit": null }
          ]
        },
        {
          "model": "Gemini-Pro-1.5",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0253, "unit": null }
          ]
        },
        {
          "model": "Llama-3.1-405B",
          "system_description": "Spider-Agent",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0221, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "AutoEval",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0570, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "Reflexion",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0728, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "CodeR",
          "scores": [
            { "metric": "SR (Spider 2.0)", "value": 0.0791, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "DAIL-SQL",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0568, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0220, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "CHESS",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0384, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0128, "unit": null }
          ]
        },
        {
          "model": "GPT-4o",
          "system_description": "DIN-SQL",
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0146, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0000, "unit": null }
          ]
        },
        {
          "model": "CodeS-15B",
          "system_description": null,
          "scores": [
            { "metric": "EX (Spider 2.0-Lite)", "value": 0.0073, "unit": null },
            { "metric": "EX (Spider 2.0-Snow)", "value": 0.0000, "unit": null }
          ]
        }
      ],
      "note": "Paper release baselines from Tables 4, 5, and 6. DeepSeek-V3 appears in Table 4 (Lite/Snow EX) while DeepSeek-V2.5 appears in Table 6 (Spider 2.0 full SR) — these are different models. Qwen2.5-Coder (Table 4) and Qwen2.5-72B (Table 6) are also distinct. CodeS-15B is a fine-tuned model, not a scaffold, so system_description is null."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://spider2-sql.github.io/",
      "results": [
        { "model": "Genloop's Sentinel Agent v2 Pro", "system_description": "Genloop's Sentinel Agent v2 Pro", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.9670, "unit": null }] },
        { "model": "Native mini", "system_description": "Native mini", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.9653, "unit": null }] },
        { "model": "Gemini-3-pro-preview", "system_description": "QUVI-3", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.9415, "unit": null }] },
        { "model": "TCDataAgent-SQL with Contextual Scaling Engine", "system_description": "TCDataAgent-SQL with Contextual Scaling Engine", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.9397, "unit": null }] },
        { "model": "Claude-Sonnet-4.5", "system_description": "Prism Swarm with Deepthink", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.9049, "unit": null }] },
        { "model": "Genloop's Sentinel Agent v2", "system_description": "Genloop's Sentinel Agent v2", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8848, "unit": null }] },
        { "model": "Claude-Opus-4.6", "system_description": "QUVI-3", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8628, "unit": null }] },
        { "model": "Ask Data with Relational Knowledge Graph", "system_description": "Ask Data with Relational Knowledge Graph", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8628, "unit": null }] },
        { "model": "ByteBrain-Agent", "system_description": "ByteBrain-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8410, "unit": null }] },
        { "model": "Genloop's Sentinel Agent v1.5", "system_description": "Genloop's Sentinel Agent v1.5", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8336, "unit": null }] },
        { "model": "AiCheng Agent", "system_description": "AiCheng Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8281, "unit": null }] },
        { "model": "Claude-Sonnet-4.5", "system_description": "Prism Swarm", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.8263, "unit": null }] },
        { "model": "Claude-Sonnet-4.5", "system_description": "LingXi Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7989, "unit": null }] },
        { "model": "Arctic-FLEX", "system_description": "Arctic-FLEX", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7514, "unit": null }] },
        { "model": "Sophon-Agent", "system_description": "Sophon-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7404, "unit": null }] },
        { "model": "APEX-SQL", "system_description": "APEX-SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7313, "unit": null }] },
        { "model": "Deepseek3.2", "system_description": "QiSi-SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7038, "unit": null }] },
        { "model": "PExA", "system_description": "PExA", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.7020, "unit": null }] },
        { "model": "Claude Sonnet 4.5 + Opus 4.5 Judge", "system_description": "Chicory AI Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6728, "unit": null }] },
        { "model": "GPT-5", "system_description": "SSDAT", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6563, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "DSR-SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6380, "unit": null }] },
        { "model": "o3", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6289, "unit": null }] },
        { "model": "Claude-4-Sonnet", "system_description": "WindAgent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6143, "unit": null }] },
        { "model": "PAI-DataSurfer Agent", "system_description": "PAI-DataSurfer Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.6033, "unit": null }] },
        { "model": "Kimi K2.5", "system_description": "DSR-SQL (w/o voting)", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.5594, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "AutoLink", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.5484, "unit": null }] },
        { "model": "GLM-5", "system_description": "PGV-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.5027, "unit": null }] },
        { "model": "Meituan-agent", "system_description": "Meituan-agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.4534, "unit": null }] },
        { "model": "Qwen3-Max", "system_description": "KDGCCloud-KCILab", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.4515, "unit": null }] },
        { "model": "GPT-5-mini", "system_description": "AgenticView", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.4095, "unit": null }] },
        { "model": "Claude-4-Sonnet", "system_description": "Chat2DB-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.3839, "unit": null }] },
        { "model": "DeepSeek-V3", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.3803, "unit": null }] },
        { "model": "Qwen3-Coder-Plus", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.3780, "unit": null }] },
        { "model": "o1-preview", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.3126, "unit": null }] },
        { "model": "Qwen3-Coder", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.3108, "unit": null }] },
        { "model": "Claude-4-Sonnet-20250514", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.2578, "unit": null }] },
        { "model": "Claude-3.7-Sonnet-20250219", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.2450, "unit": null }] },
        { "model": "Claude-3.7-Sonnet-20250219-Thinking", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.2431, "unit": null }] },
        { "model": "o1-preview", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.2358, "unit": null }] },
        { "model": "o1-2024-12-17", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.2321, "unit": null }] },
        { "model": "o3-mini-2025-01-31", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1920, "unit": null }] },
        { "model": "Claude-3.5-Sonnet-20241022 (AWS ProServe)", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1901, "unit": null }] },
        { "model": "Claude-3.5-Sonnet-20241022", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1554, "unit": null }] },
        { "model": "Gemini-2.0-Pro", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1389, "unit": null }] },
        { "model": "GPT-4o-2024-11-20", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1298, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.1055, "unit": null }] },
        { "model": "GPT-4o", "system_description": "CollideNL2SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0968, "unit": null }] },
        { "model": "QwQ-32B", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0896, "unit": null }] },
        { "model": "DeepSeek-V3", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0878, "unit": null }] },
        { "model": "Qwen2.5-Coder-32B-Instruct", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0548, "unit": null }] },
        { "model": "GPT-4o", "system_description": "Dail-SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0220, "unit": null }] },
        { "model": "GPT-4o", "system_description": "CHESS", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0128, "unit": null }] },
        { "model": "GPT-4o", "system_description": "DIN-SQL", "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0000, "unit": null }] },
        { "model": "SFT CodeS-15B", "system_description": null, "scores": [{ "metric": "EX (Spider 2.0-Snow)", "value": 0.0000, "unit": null }] }
      ],
      "note": "Spider 2.0-Snow leaderboard snapshot as of 2026-04-25 — 54 entries in rank order. For 'X + Y' entries, system_description = X (scaffold/agent) and model = Y. For single-name product entries (e.g., Native mini, ByteBrain-Agent), both fields = product name per template copy rules. Two distinct Spider-Agent + Claude-3.5-Sonnet-20241022 entries appear (ranks 42 and 43); the higher-scored one is annotated 'AWS ProServe' on the leaderboard."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://spider2-sql.github.io/",
      "results": [
        { "model": "SignalPilot Agent", "system_description": "SignalPilot Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.5156, "unit": null }] },
        { "model": "Databao Agent", "system_description": "Databao Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.4411, "unit": null }] },
        { "model": "GPT-5", "system_description": "Shadowfax-DBT-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.4118, "unit": null }] },
        { "model": "Qwen3-Max", "system_description": "CT-ChatBI", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.4040, "unit": null }] },
        { "model": "GPT-5", "system_description": "Spider-Agent-Extended", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.3971, "unit": null }] },
        { "model": "GPT-5", "system_description": "Symbiote Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.3529, "unit": null }] },
        { "model": "Claude Sonnet 4.5", "system_description": "Chicory AI Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.3529, "unit": null }] },
        { "model": "DAQUV_QUVI_Agent", "system_description": "DAQUV_QUVI_Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.1765, "unit": null }] },
        { "model": "Claude-3.7-Sonnet-20250219", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.1470, "unit": null }] },
        { "model": "o1-preview", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.1324, "unit": null }] },
        { "model": "GPT-4.1", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.1029, "unit": null }] },
        { "model": "GPT-4o", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.0735, "unit": null }] },
        { "model": "o3-mini", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.0441, "unit": null }] },
        { "model": "o3", "system_description": "Spider-Agent", "scores": [{ "metric": "SR (Spider 2.0-DBT)", "value": 0.0294, "unit": null }] }
      ],
      "note": "Spider 2.0-DBT leaderboard snapshot as of 2026-04-25 — 14 entries in rank order. SignalPilot Agent (#1) and CT-ChatBI + Qwen3-Max (#4) are new entries since the prior snapshot; CT-ChatBI previously appeared on the Lite leaderboard."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://spider2-sql.github.io/",
      "results": [
        { "model": "SOMA-SQL", "system_description": "SOMA-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.7202, "unit": null }] },
        { "model": "Databao Agent", "system_description": "Databao Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.6965, "unit": null }] },
        { "model": "Claude-Opus-4.5", "system_description": "QUVI-2.3", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.6581, "unit": null }] },
        { "model": "EXA-SQL", "system_description": "EXA-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.6416, "unit": null }] },
        { "model": "Claude-4.5-Opus", "system_description": "ProSPy: Profiling-driven SQL-Python Analysis Framework", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.6015, "unit": null }] },
        { "model": "o3", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.5521, "unit": null }] },
        { "model": "GPT-5", "system_description": "CoFD-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.5466, "unit": null }] },
        { "model": "Deepseek-R1", "system_description": "AutoLink", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.5228, "unit": null }] },
        { "model": "Gemini-3-Flash + DeepSeek-V3.2", "system_description": "GRASP + Reforce", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.5131, "unit": null }] },
        { "model": "DeepSeek-R1-0528 + DeepSeek-V3.2", "system_description": "DSR-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.4680, "unit": null }] },
        { "model": "Qwen3", "system_description": "AgenticData", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.4450, "unit": null }] },
        { "model": "Claude-Sonnet-4.5", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.4186, "unit": null }] },
        { "model": "Qwen3", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.3560, "unit": null }] },
        { "model": "o3", "system_description": "RSL-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.3309, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "LinkAlign", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.3309, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "RSL-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.3053, "unit": null }] },
        { "model": "o1-preview", "system_description": "ReFoRCE", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.3035, "unit": null }] },
        { "model": "Claude-3.7-Sonnet-20250219-Thinking", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2852, "unit": null }] },
        { "model": "Claude-4-Sonnet-20250514", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2779, "unit": null }] },
        { "model": "DeepSeek-V3", "system_description": "RSL-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2614, "unit": null }] },
        { "model": "Claude-3.7-Sonnet-20250219", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2541, "unit": null }] },
        { "model": "DeepSeek-V3", "system_description": "LinkAlign", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2486, "unit": null }] },
        { "model": "o3-mini-2025-01-31", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2340, "unit": null }] },
        { "model": "o1-preview", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.2303, "unit": null }] },
        { "model": "DeepSeek-R1", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.1371, "unit": null }] },
        { "model": "GPT-4o-2024-11-20", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.1316, "unit": null }] },
        { "model": "QwQ-32B", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.1133, "unit": null }] },
        { "model": "Duo", "system_description": "Duo", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0896, "unit": null }] },
        { "model": "Claude-3.5-Sonnet-20240620", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0832, "unit": null }] },
        { "model": "Qwen2.5-Coder-32B-Instruct", "system_description": "Spider-Agent", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0585, "unit": null }] },
        { "model": "GPT-4o", "system_description": "DailSQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0568, "unit": null }] },
        { "model": "GPT-4o", "system_description": "CHESS", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0384, "unit": null }] },
        { "model": "GPT-4o", "system_description": "DIN-SQL", "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0146, "unit": null }] },
        { "model": "SFT CodeS-15B", "system_description": null, "scores": [{ "metric": "EX (Spider 2.0-Lite)", "value": 0.0073, "unit": null }] }
      ],
      "note": "Spider 2.0-Lite leaderboard snapshot as of 2026-04-25 — 34 entries in rank order. Each entry carries only the Lite metric — Snow and DBT are tracked as separate entries above. CT-ChatBI no longer appears on the Lite leaderboard (now on DBT)."
    }
  ],

  "notes": "Spider 2.0 is a multi-setting benchmark with THREE distinct sub-benchmarks that should be tracked separately:\n\n1. **Spider 2.0-Lite** (547 tasks): Text-to-SQL across BigQuery (214), Snowflake (198), SQLite (135). Metric: Execution Accuracy (EX). Cost: some BigQuery/Snowflake costs.\n2. **Spider 2.0-Snow** (547 tasks): Text-to-SQL on Snowflake only. Metric: Execution Accuracy (EX). Cost: free.\n3. **Spider 2.0-DBT** (68 tasks): Code agent tasks using DuckDB with DBT projects. Metric: Success Rate (SR). Cost: free.\n4. **Spider 2.0 (full)** (632 tasks): The complete benchmark including all database systems and DBT tasks. Metric: Success Rate (SR). Reported in the paper but not on the current leaderboard.\n\nThe Harbor adapter only covers the spider2-dbt split (64 of 68 tasks, 4 excluded due to upstream data bugs). There are NO Harbor adapters for spider2-lite or spider2-snow.\n\nKey characteristics distinguishing Spider 2.0 from prior text-to-SQL benchmarks:\n- Real enterprise databases with avg 812 columns/DB (vs 27 in Spider 1.0, 54 in BIRD)\n- Multiple SQL dialects (BigQuery, Snowflake, SQLite, DuckDB, Postgres, ClickHouse)\n- 85.98% of tasks use specialized dialect functions (avg 7.1 per query)\n- Average SQL length: 148 tokens (vs 18.5 in Spider 1.0)\n- Includes project-level DBT tasks requiring codebase navigation\n- Tasks sourced from real tutorials and forums, rewritten to prevent data leakage\n- Annotated by 8 expert SQL annotators through a 6-step pipeline with multi-round quality control"
}
```

---

## Detailed Research Notes

### 1. Official Website (https://spider2-sql.github.io/)

Spider 2.0 is presented as an evaluation framework for real-world enterprise text-to-SQL workflows. The website hosts three separate leaderboards for the three sub-benchmarks (Lite, Snow, DBT). It was accepted as an **ICLR 2025 Oral** presentation.

> "Spider 2.0 introduces an evaluation framework comprising 632 real-world text-to-SQL workflow problems derived from enterprise-level database use cases."

> "Databases in Spider 2.0 are sourced from real data applications, often containing over 1,000 columns and stored in local or cloud database systems such as BigQuery and Snowflake."

### 2. Paper (arXiv:2411.07763, ICLR 2025 Oral)

**Authors:** Fangyu Lei*, Jixuan Chen* (equal contribution), Yuxiao Ye, Ruisheng Cao, Dongchan Shin, Hongjin Su, Zhaoqing Suo, Hongcheng Gao, Wenjing Hu, Pengcheng Yin, Victor Zhong, Caiming Xiong, Ruoxi Sun, Qian Liu, Sida I. Wang, Tao Yu

**Affiliations:** University of Hong Kong (primary), Salesforce Research, Sea AI Lab, Google DeepMind, Google Cloud AI Research, University of Waterloo

**Paper:** 45 pages total (10 main + 4 references + 31 appendix pages)

#### 2.1 Task Definition

The benchmark defines two settings:

**Code Agent Task (Spider 2.0 / Spider 2.0-DBT):**
- Given: Question Q, database interface I, codebase C (project context, config, documentation)
- Task: Iteratively modify code (SQL/Python) based on execution observations until final result obtained
- Metric: Success Rate (SR)

**Text-to-SQL Task (Spider 2.0-Lite / Spider 2.0-Snow):**
- Given: Database schema D, natural language question Q, auxiliary documentation E
- Output: SQL query S = f(Q, D, E | θ)
- Metric: Execution Accuracy (EX) — compares execution results with "focused evaluation" that checks essential columns and ignores non-essential ones to reduce false negatives

> "EX = Σ(1[v_i ∈ v̂ ∀v_i ∈ v]) / N"

#### 2.2 Annotation Pipeline (6 steps, 8 expert annotators)

1. **Database and SQL Collection:** Sources from BigQuery, Snowflake Marketplace, public data platforms. Criteria: >200 columns or nested schema structure. Collected 1,021 complex SQL queries from tutorials/forums and 157 DBT projects (Fivetran). Retained 547 high-quality SQLs + 78 DBT projects.

2. **SQL Rewrite to Prevent Data Leakage:** Two levels of rewriting:
   - Surface-level (84.2% of tasks): answer format changes, condition parameter changes, advanced calculation additions
   - Semantic-level (42% of tasks): advanced requirements, merging related SQLs, SQL codebase file changes

3. **Codebase and Context Setup:** External reference documents for SQL dialects, original project codebases preserved, database interfaces established.

4. **Natural Language Task Instructions:** Two versions (agentic vs text-to-SQL). Agentic prioritizes naturalness; text-to-SQL prioritizes unambiguity. LLM-assisted paraphrasing for clarity.

5. **Execution-Based Focused Evaluation:** Results obtained programmatically. Focus-based approach evaluates essential components, ignores non-essential columns.

6. **Quality Control:** Each example reviewed by ≥3 annotators. First round: 45% contained errors. Second round: only 5%. Final: all fully annotated. Red team assessment performed.

#### 2.3 Dataset Statistics

| Feature | Spider 2.0 |
|---------|-----------|
| Total tasks | 632 (100%) |
| Easy (#tokens < 80) | 160 (25.32%) |
| Medium (80 ≤ #tokens < 160) | 279 (44.15%) |
| Hard (#tokens ≥ 160) | 193 (30.54%) |
| **Database Distribution** | |
| BigQuery | 214 (33.86%) |
| Snowflake | 198 (31.33%) |
| SQLite | 135 (21.36%) |
| DuckDB | 68 (10.76%) |
| PostgreSQL | 10 (1.58%) |
| ClickHouse | 7 (1.11%) |
| **Task Features** | |
| With DBT Project | 78 (12.34%) |
| With Documentation | 82 (12.97%) |
| With Functions | 474 (75.00%) |
| With Partition Tables | 54 (8.54%) |
| With Multiple Schemas | 140 (22.15%) |
| With Nested Schemas | 117 (18.51%) |
| **Answer Types** | |
| String/Number | 162 (25.63%) |
| Table | 392 (62.03%) |
| Database | 78 (12.34%) |

Comparison to prior benchmarks:

| Dataset | Examples | DBs | Cols/DB | Tokens/SQL | Funcs/SQL |
|---------|----------|-----|---------|-----------|-----------|
| Spider 1.0 | 2,147 | 40 | 27.1 | 18.5 | 0.0 |
| BIRD | 1,789 | 15 | 54.2 | 30.9 | 0.4 |
| **Spider 2.0** | **632** | **213** | **743.5** | **148.3** | **7.1** |
| **Spider 2.0-Lite** | **547** | **158** | **803.6** | **144.5** | **6.5** |
| **Spider 2.0-Snow** | **547** | **152** | **812.1** | **161.8** | **6.8** |

#### 2.4 Experiments

**Models tested:**
- Open-source: DeepSeek-Coder-V2.5, Qwen2.5-72B-Instruct, Llama-3.1-405B
- Closed-source: Gemini-Pro-1.5, Claude-3.5-Sonnet, GPT-4o, GPT-4, o1-preview, o3-mini

**Agent frameworks tested:** Reflexion, CodeR, AutoEval, Spider-Agent (developed for this work, ReAct-inspired)

**Text-to-SQL methods:** DIN-SQL, DAIL-SQL, CHESS (all + GPT-4o), SFT CodeS-15B

**Paper results (Spider-Agent):**

| Model | Lite | Snow | Full |
|-------|------|------|------|
| o1-preview | 23.22% | 23.77% | 21.36% |
| Claude-3.5-Sonnet | 15.54% | 15.54% | 14.87% |
| GPT-4o | 13.16% | 12.98% | 12.34% |
| GPT-4 | — | — | 9.86% |

**Text-to-SQL methods (paper):**

| Method | Spider 1.0 | BIRD | Spider 2.0-Snow | Spider 2.0-Lite |
|--------|-----------|------|-----------------|-----------------|
| DAIL-SQL + GPT-4o | 86.6% | 57.4% | 2.20% | 5.68% |
| CHESS + GPT-4o | 87.2% | 66.7% | 1.28% | 3.84% |

#### 2.5 Error Analysis (300 sampled examples)

| Error Type | % | Description |
|-----------|---|-------------|
| Erroneous Data Analysis | 35.5% | Dialect function usage (10.3%), advanced data calculation (7.5%), intricate query planning (17.7%) |
| Wrong Schema Linking | 27.6% | Column linking errors (16.6%), table linking errors (10.1%) — driven by avg 755+ columns per DB |
| JOIN Errors | 8.3% | Lack of explicit foreign keys in BigQuery; requires inference from column names |
| Other | 28.6% | — |

**Task-type specific challenges:**

| Task Subset | % of Total | Success Rate |
|-------------|-----------|--------------|
| With nested columns | 18.51% | 10.34% |
| Without nested columns | 68.04% | 27.38% |
| With external docs | 12.97% | 11.54% |
| Without external docs | 73.58% | 26.64% |
| With DBT project | 12.34% | 12.82% |
| Without DBT project | 87.65% | 23.22% |

**Oracle function analysis:** Providing gold function documentation showed only marginal improvement. DAIL-SQL+o1-preview actually performed worse with oracle functions (9.51%) than without (12.60%).

> "Models can select appropriate functions but struggle utilizing them correctly to reflect user intentions."

**Few-shot analysis:** 0-shot: 5.68%, 1-shot: 6.40%, 3-shot: 6.76% — marginal improvement.

> "Gap between simplistic pre-training data and complex examples" and "extensive schema prompts hinder assimilation."

#### 2.6 Evaluation Methodology

**Execution Accuracy (EX)** for Spider 2.0-Lite/Snow (formal definition from paper Appendix A):

```
EX = (Σ_{n=1}^{N} 1(v_n, v̂_n)) / N

where 1(v, v̂) = 1 if v_i ∈ v̂ ∀v_i ∈ v, else 0
```

v_i = i-th column of gold result, v̂_n = predicted SQL execution result. Uses "focused evaluation" — checks whether all gold columns appear in predicted output, ignoring extra non-essential columns. This reduces false negatives without increasing false positives.

**Success Rate (SR)** for Spider 2.0 full: proportion of tasks successfully completed, determined by human-written evaluation scripts that accept output as strings, tables, or database files.

Five evaluation script types (Table 12 in paper):
1. **String without numbers**: Check if answer substrings appear in predicted string. Params: pred, gold (list), conj (and/or), exclude list
2. **String with numbers**: Number matching with precision tolerance. Params: pred, gold, percentage flag, precision (default 4 decimal places), conj
3. **Table-based**: CSV/table evaluation. Params: result path, gold path(s), condition_cols (column indices to check), ignore_order
4. **Database-based**: DuckDB file evaluation. Params: result path, gold path, condition_tabs, condition_cols, ignore_orders
5. **SQL-based**: Execution-based comparison of predicted vs gold SQL results (for Spider 2.0-Lite)

#### 2.7 Spider-Agent Framework (Appendix C.1)

Spider-Agent is a ReAct-inspired code agent framework developed specifically for this benchmark. Key details:

**Action space** (Table 19):
- `BASH`: Execute shell commands
- `CreateFile`: Create new files
- `EditFile`: Overwrite file content
- `ExecuteSQL` / `BQ_EXEC_SQL`: Execute SQL on BigQuery/Snowflake, option to save or print
- `GetTables` / `GET_TABLES`: Retrieve all table names and DDL from a dataset
- `GetTabInfo` / `GET_TABLE_INFO`: Retrieve column info for a specific table
- `SampleRows` / `SAMPLE_ROWS`: Sample rows from a table
- `FAIL`: Agent determines task is infeasible
- `Terminate`: Agent determines task is complete

**Hyperparameters**: temperature=1.0, top-p=0.9, max steps=30. Truncates from beginning if exceeding context window. Auto-terminates if same output 3 times in a row or any action takes >120 seconds.

**Action analysis**: For correctly completed tasks, the agent needed avg 9.0 steps (min 6, max 17).

#### 2.8 SQL Dialect Documentation (Appendix B.7)

The benchmark crawled and pre-processed function documentation from official websites of each database system:

| Database | Documentation Pages | Categories | Functions |
|----------|-------------------|------------|-----------|
| BigQuery | 34 | 34 | 390 |
| Snowflake | 719 | 30 | 719 |
| PostgreSQL | 30 | 30 | 30 |
| ClickHouse | 226 | 6 | 226 |
| SQLite | 6 | 6 | 147 |
| DuckDB | 24 | 24 | 513 |
| **Total** | **1,039** | **130** | **2,025** |

#### 2.9 Per-Database Performance (Appendix C.4, Table 20)

Performance breakdown by database type on Spider 2.0 (o1-preview + Spider-Agent):

| Database | % of Examples | SR |
|----------|-------------|-----|
| BigQuery | 33.86% | 24.07% |
| SQLite | 21.36% | 20.74% |
| DuckDB | 10.76% | 17.69% |
| ClickHouse | 1.11% | 57.14% |
| PostgreSQL | 1.58% | 12.82% |
| Snowflake | 31.33% | 7.14% |

> Snowflake is significantly harder than BigQuery. Cross-dialect experiment: same 180 questions hosted on both BigQuery and Snowflake yielded 12.78% vs 6.6% respectively, highlighting dialect syntax impact.

#### 2.10 API Cost Per Instance (Appendix C.5, Table 21)

| Method | Avg Cost |
|--------|----------|
| Spider-Agent + o1-preview | $0.75 |
| Spider-Agent + GPT-4-Turbo | $0.58 |
| Spider-Agent + GPT-4o | $0.32 |
| DAIL-SQL + o1-preview | $0.32 |
| CHESS + GPT-4o | $0.43 |
| DIN-SQL + GPT-4o | $0.14 |
| DAIL-SQL + GPT-4o | $0.09 |
| SFT CodeS-15B | $0.00 |

#### 2.11 Extended Dataset Statistics (Appendix B.8)

**Data volume**: Average database in Spider 2.0 has 5,273.42M rows, with many reaching TB-level sizes. Compare: WikiSQL 17 rows, Spider 1.0 2K rows, KaggleDBQA 280K rows, BIRD 549K rows.

**SQL complexity comparison** (Figure 17):
- Tables/DB: Spider 2.0 has 52.63 (vs 1.0 for WikiSQL, 5.1 for Spider 1.0, 29.0 for BIRD)
- Keywords/SQL: Spider 2.0 has 55.90 (vs 3.04 for WikiSQL, 7.49 for Spider 1.0, 19.71 for BIRD)
- JOINs/SQL: Spider 2.0 has 4.80 (vs 0.0 for WikiSQL, 0.5 for Spider 1.0, 1.0 for BIRD)

**Number of JOINs vs performance**: No clear correlation between JOIN count and model performance. The paper speculates this is because all examples are complex enough that difficulty is independent of table count.

#### 2.12 Instruction Differences (Appendix B.6)

Spider 2.0 (agentic) prioritizes naturalness while Spider 2.0-Lite prioritizes unambiguity. Examples:

- Spider 2.0: "The company management has requested a detailed report on the year-to-date performance of the Magnificent 7 stocks."
- Spider 2.0-Lite: "Please show the price change rate of the Magnificent 7 stocks from the beginning of this year to today."

The Lite version adds explicit column specifications and exact conditions to remove ambiguity.

### 3. GitHub Repository (https://github.com/xlang-ai/Spider2)

The repo provides:
- Question/instruction files: `spider2-lite.jsonl`, `spider2-snow.jsonl`
- Partial gold SQL answers (for prompt design, not fine-tuning)
- Spider-Agent implementations: Docker-free tool-call format (updated June 2025), Docker-based versions
- Submission guidance for leaderboard
- BigQuery/Snowflake account setup instructions

### 4. Leaderboard (https://spider2-sql.github.io/)

Three separate leaderboards as of 2026-04-25 — each a distinct sub-benchmark with its own metric and task set. Listed below in the exact order shown on the official leaderboard page. Snow and Lite are NOT mixed; Snow uses EX on Snowflake-only tasks, Lite uses EX across BigQuery/Snowflake/SQLite, DBT uses SR on DuckDB+DBT code-agent tasks.

**Spider 2.0-Snow** (54 entries): Top is Genloop's Sentinel Agent v2 Pro at 96.70%. Massive improvement from paper's 23.77% best. Leaderboard dominated by commercial agent products.

**Spider 2.0-DBT** (14 entries): Top is SignalPilot Agent at 51.56%. Up from paper's 21.36%. Still the smallest leaderboard.

**Spider 2.0-Lite** (34 entries): Top is SOMA-SQL at 72.02%. Up from paper's 5.68% (text-to-SQL) and 23.22% (agent).

#### 4.1 Full Spider 2.0-Snow Leaderboard (54 entries, EX %)

| Rank | Method | Score |
|------|--------|-------|
| 1 | Genloop's Sentinel Agent v2 Pro | 96.70 |
| 2 | Native mini | 96.53 |
| 3 | QUVI-3 + Gemini-3-pro-preview | 94.15 |
| 4 | TCDataAgent-SQL with Contextual Scaling Engine | 93.97 |
| 5 | Prism Swarm with Deepthink + Claude-Sonnet-4.5 | 90.49 |
| 6 | Genloop's Sentinel Agent v2 | 88.48 |
| 7 | QUVI-3 + Claude-Opus-4.6 | 86.28 |
| 8 | Ask Data with Relational Knowledge Graph | 86.28 |
| 9 | ByteBrain-Agent | 84.10 |
| 10 | Genloop's Sentinel Agent v1.5 | 83.36 |
| 11 | AiCheng Agent | 82.81 |
| 12 | Prism Swarm + Claude-Sonnet-4.5 | 82.63 |
| 13 | LingXi Agent + Claude-Sonnet-4.5 | 79.89 |
| 14 | Arctic-FLEX | 75.14 |
| 15 | Sophon-Agent | 74.04 |
| 16 | APEX-SQL | 73.13 |
| 17 | QiSi-SQL + Deepseek3.2 | 70.38 |
| 18 | PExA | 70.20 |
| 19 | Chicory AI Agent + Claude Sonnet 4.5 + Opus 4.5 Judge | 67.28 |
| 20 | SSDAT + GPT-5 | 65.63 |
| 21 | DSR-SQL + DeepSeek-R1 | 63.80 |
| 22 | ReFoRCE + o3 | 62.89 |
| 23 | WindAgent + Claude-4-Sonnet | 61.43 |
| 24 | PAI-DataSurfer Agent | 60.33 |
| 25 | DSR-SQL (w/o voting) + Kimi K2.5 | 55.94 |
| 26 | AutoLink + DeepSeek-R1 | 54.84 |
| 27 | PGV-Agent + GLM-5 | 50.27 |
| 28 | Meituan-agent | 45.34 |
| 29 | KDGCCloud-KCILab + Qwen3-Max | 45.15 |
| 30 | AgenticView + GPT-5-mini | 40.95 |
| 31 | Chat2DB-Agent + Claude-4-Sonnet | 38.39 |
| 32 | ReFoRCE + DeepSeek-V3 | 38.03 |
| 33 | Spider-Agent + Qwen3-Coder-Plus | 37.80 |
| 34 | ReFoRCE + o1-preview | 31.26 |
| 35 | Spider-Agent + Qwen3-Coder | 31.08 |
| 36 | Spider-Agent + Claude-4-Sonnet-20250514 | 25.78 |
| 37 | Spider-Agent + Claude-3.7-Sonnet-20250219 | 24.50 |
| 38 | Spider-Agent + Claude-3.7-Sonnet-20250219-Thinking | 24.31 |
| 39 | Spider-Agent + o1-preview | 23.58 |
| 40 | Spider-Agent + o1-2024-12-17 | 23.21 |
| 41 | Spider-Agent + o3-mini-2025-01-31 | 19.20 |
| 42 | Spider-Agent + Claude-3.5-Sonnet-20241022 (AWS ProServe) | 19.01 |
| 43 | Spider-Agent + Claude-3.5-Sonnet-20241022 | 15.54 |
| 44 | Spider-Agent + Gemini-2.0-Pro | 13.89 |
| 45 | Spider-Agent + GPT-4o-2024-11-20 | 12.98 |
| 46 | Spider-Agent + DeepSeek-R1 | 10.55 |
| 47 | CollideNL2SQL + GPT-4o | 9.68 |
| 48 | Spider-Agent + QwQ-32B | 8.96 |
| 49 | Spider-Agent + DeepSeek-V3 | 8.78 |
| 50 | Spider-Agent + Qwen2.5-Coder-32B-Instruct | 5.48 |
| 51 | Dail-SQL + GPT-4o | 2.20 |
| 52 | CHESS + GPT-4o | 1.28 |
| 53 | DIN-SQL + GPT-4o | 0.00 |
| 54 | SFT CodeS-15B | 0.00 |

#### 4.2 Full Spider 2.0-DBT Leaderboard (14 entries, SR %)

| Rank | Method | Score |
|------|--------|-------|
| 1 | SignalPilot Agent | 51.56 |
| 2 | Databao Agent | 44.11 |
| 3 | Shadowfax-DBT-Agent + GPT-5 | 41.18 |
| 4 | CT-ChatBI + Qwen3-Max | 40.40 |
| 5 | Spider-Agent-Extended + GPT-5 | 39.71 |
| 6 | Symbiote Agent + GPT-5 | 35.29 |
| 7 | Chicory AI Agent + Claude Sonnet 4.5 | 35.29 |
| 8 | DAQUV_QUVI_Agent | 17.65 |
| 9 | Spider-Agent + Claude-3.7-Sonnet-20250219 | 14.70 |
| 10 | Spider-Agent + o1-preview | 13.24 |
| 11 | Spider-Agent + GPT-4.1 | 10.29 |
| 12 | Spider-Agent + GPT-4o | 7.35 |
| 13 | Spider-Agent + o3-mini | 4.41 |
| 14 | Spider-Agent + o3 | 2.94 |

#### 4.3 Full Spider 2.0-Lite Leaderboard (34 entries, EX %)

| Rank | Method | Score |
|------|--------|-------|
| 1 | SOMA-SQL | 72.02 |
| 2 | Databao Agent | 69.65 |
| 3 | QUVI-2.3 + Claude-Opus-4.5 | 65.81 |
| 4 | EXA-SQL | 64.16 |
| 5 | ProSPy: Profiling-driven SQL-Python Analysis Framework + Claude-4.5-Opus | 60.15 |
| 6 | ReFoRCE + o3 | 55.21 |
| 7 | CoFD-SQL + GPT-5 | 54.66 |
| 8 | AutoLink + Deepseek-R1 | 52.28 |
| 9 | GRASP + Reforce + Gemini-3-Flash + DeepSeek-V3.2 | 51.31 |
| 10 | DSR-SQL + DeepSeek-R1-0528 + DeepSeek-V3.2 | 46.80 |
| 11 | AgenticData + Qwen3 | 44.50 |
| 12 | Spider-Agent + Claude-Sonnet-4.5 | 41.86 |
| 13 | ReFoRCE + Qwen3 | 35.60 |
| 14 | RSL-SQL + o3 | 33.09 |
| 15 | LinkAlign + DeepSeek-R1 | 33.09 |
| 16 | RSL-SQL + DeepSeek-R1 | 30.53 |
| 17 | ReFoRCE + o1-preview | 30.35 |
| 18 | Spider-Agent + Claude-3.7-Sonnet-20250219-Thinking | 28.52 |
| 19 | Spider-Agent + Claude-4-Sonnet-20250514 | 27.79 |
| 20 | RSL-SQL + DeepSeek-V3 | 26.14 |
| 21 | Spider-Agent + Claude-3.7-Sonnet-20250219 | 25.41 |
| 22 | LinkAlign + DeepSeek-V3 | 24.86 |
| 23 | Spider-Agent + o3-mini-2025-01-31 | 23.40 |
| 24 | Spider-Agent + o1-preview | 23.03 |
| 25 | Spider-Agent + DeepSeek-R1 | 13.71 |
| 26 | Spider-Agent + GPT-4o-2024-11-20 | 13.16 |
| 27 | Spider-Agent + QwQ-32B | 11.33 |
| 28 | Duo | 8.96 |
| 29 | Spider-Agent + Claude-3.5-Sonnet-20240620 | 8.32 |
| 30 | Spider-Agent + Qwen2.5-Coder-32B-Instruct | 5.85 |
| 31 | DailSQL + GPT-4o | 5.68 |
| 32 | CHESS + GPT-4o | 3.84 |
| 33 | DIN-SQL + GPT-4o | 1.46 |
| 34 | SFT CodeS-15B | 0.73 |

### 5. Harbor Adapter (spider2-dbt)

**Only the DBT split is adapted.** No adapters exist for spider2-lite or spider2-snow.

**adapter_metadata.json:**
- Split: dbt, Size: 68 (original) → 64 (adapted, 4 tasks excluded due to upstream data bugs)
- Excluded tasks: chinook001, biketheft001, google_ads001, gitcoin001
- Harness: agent, supported agent: spider-agent
- Parity matching agent: spider-agent+gpt-5-mini-2025-08-07
- Parity sampling rate: 1.0

**parity_experiment.json:**
- Agent: spider-agent, Model: gpt-5-mini-2025-08-07
- Date: 2026-01-05
- 3 trials
- Original result: 18.8% ±0.0 (all three trials: 18.8%)
- Harbor result: 18.3% ±0.53 (trials: 18.8%, 17.2%, 18.8%)
- Metric: Mean Resolved Rate (%)

### 6. Dataset

The HuggingFace dataset page (https://huggingface.co/datasets/xlang-ai/spider2) returned a 401 error, suggesting it may be gated or require authentication.

---

## Questions

1. **Missing adapters for spider2-lite and spider2-snow**: The Harbor adapter only covers spider2-dbt (64/68 tasks). Spider2-lite (547 tasks) and spider2-snow (547 tasks) have no Harbor adapters. Is this planned? These are the larger and more commonly benchmarked splits.

2. **Dataset access**: The HuggingFace dataset page returned 401 — is the dataset gated? The GitHub repo provides JSONL files but references a separate dataset URL.

3. **Metric alignment**: Spider 2.0 uses different metrics for different splits (EX for Lite/Snow, SR for DBT/full). The Harbor adapter uses "Mean Resolved Rate (%)" for the DBT split, which appears equivalent to SR. Should the template JSON use a single primary_metric, or should we list the split-specific metrics?

4. **Sub-leaderboard granularity**: The leaderboard has three entirely separate tables (Snow, Lite, DBT). Should this be treated as one benchmark entry or three? The template seems designed for a single benchmark with one primary metric, but Spider 2.0 has three distinct sub-benchmarks with different task types (text-to-SQL vs code agent), different evaluation metrics (EX vs SR), and different database backends.

5. **"Spider 2.0 (full)" vs sub-benchmarks**: The paper reports results on the full 632-task "Spider 2.0" set, but the current leaderboard only tracks the three sub-benchmarks separately. The full set is not on the leaderboard. Should we include the paper's full-set results even though they aren't tracked on the leaderboard anymore?

6. **The Harbor parity experiment uses gpt-5-mini-2025-08-07** as the matching agent, but the original leaderboard doesn't show this exact configuration. The parity original score (18.8%) doesn't directly match any leaderboard entry. This may be because the parity was run on the adapted 64-task subset rather than the full 68 tasks.
