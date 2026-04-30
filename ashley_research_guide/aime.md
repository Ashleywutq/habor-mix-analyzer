# AIME Benchmark Research

```json
{
  "name": "AIME",
  "category": "Math",
  "used_llm_or_agent": "llm",

  "links": {
    "website": "https://www.vals.ai/benchmarks/aime",
    "leaderboard": "https://www.vals.ai/benchmarks/aime",
    "paper": null,
    "github": "https://github.com/GAIR-NLP/AIME-Preview",
    "dataset": null
  },

  "meta": {
    "release_date": "2024-02",
    "num_tasks": 60
  },

  "evaluation": {
    "primary_metric": "accuracy",
    "harbor_aligned_metric": null
  },

  "results_over_time": [
    {
      "date": "2025-03",
      "source_type": "other",
      "source_url": "https://github.com/GAIR-NLP/AIME-Preview",
      "results": [
        {
          "model": "o3-mini-high",
          "effort": "high",
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.838, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.767, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.850, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.8085, "unit": null }
          ]
        },
        {
          "model": "o3-mini-medium",
          "effort": "medium",
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.758, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.667, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.7417, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.7044, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.798, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.650, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.750, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.7000, "unit": null }
          ]
        },
        {
          "model": "QwQ-32B",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.795, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.600, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.638, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.6194, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Llama-70B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.571, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.514, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.6114, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.5627, "unit": null }
          ]
        },
        {
          "model": "o1-mini",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.636, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.508, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.567, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.5375, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Qwen-32B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.583, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.461, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.531, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.4960, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Qwen-14B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.617, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.467, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.492, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.4795, "unit": null }
          ]
        },
        {
          "model": "limo",
          "effort": null,
          "system_description": "817 samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.563, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.445, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.447, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.4460, "unit": null }
          ]
        },
        {
          "model": "gemini-2.0-flash-thinking",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.615, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.433, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.458, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.4455, "unit": null }
          ]
        },
        {
          "model": "o3-mini-low",
          "effort": "low",
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.563, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.442, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.400, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.4210, "unit": null }
          ]
        },
        {
          "model": "o1-preview",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.446, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.375, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.383, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.3790, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Qwen-7B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.496, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.369, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.367, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.3680, "unit": null }
          ]
        },
        {
          "model": "QwQ-32B-Preview",
          "effort": null,
          "system_description": "API model, default config",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.467, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.372, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.281, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.3265, "unit": null }
          ]
        },
        {
          "model": "s1",
          "effort": null,
          "system_description": "1k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.329, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.289, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.283, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.2860, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Llama-8B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.371, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.247, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.230, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.2385, "unit": null }
          ]
        },
        {
          "model": "DeepSeek-R1-Distill-Qwen-1.5B",
          "effort": null,
          "system_description": "800k samples, local deployment",
          "scores": [
            { "metric": "accuracy (AIME 2024)", "value": 0.250, "unit": null },
            { "metric": "accuracy (AIME I 2025 AVG)", "value": 0.280, "unit": null },
            { "metric": "accuracy (AIME II 2025 AVG)", "value": 0.144, "unit": null },
            { "metric": "accuracy (AIME 2025)", "value": 0.2120, "unit": null }
          ]
        }
      ],
      "note": "AIME-Preview results from March 2025 (updated 0311). 8 samples per question, averaged across temperatures (0.0, 0.3, 0.6) for locally deployed models. API models use default configs. Scores shown as percentages in source; converted to decimals here. Source: Result-AIME-2025-0311.jpeg from GAIR-NLP/AIME-Preview repo."
    },
    {
      "date": "2026-04",
      "source_type": "leaderboard",
      "source_url": "https://www.vals.ai/benchmarks/aime",
      "results": [
        {
          "model": "google/gemini-3.1-pro-preview",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9812, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5.2-2025-12-11",
          "effort": "xhigh",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9688, "unit": null }
          ]
        },
        {
          "model": "meta/muse_spark",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9688, "unit": null }
          ]
        },
        {
          "model": "google/gemini-3-pro-preview",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9668, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5.4-2026-03-05",
          "effort": "xhigh",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9667, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4.20-0309-reasoning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9646, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-7",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9625, "unit": null }
          ]
        },
        {
          "model": "google/gemini-3-flash-preview",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9563, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-6-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9563, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5.4-mini-2026-03-17",
          "effort": "xhigh",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9563, "unit": null }
          ]
        },
        {
          "model": "kimi/kimi-k2.5-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9563, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-5-20251101-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9542, "unit": null }
          ]
        },
        {
          "model": "alibaba/qwen3.6-plus",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9458, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5-2025-08-07",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9337, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5.1-2025-11-13",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9333, "unit": null }
          ]
        },
        {
          "model": "zai/glm-4.7",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9333, "unit": null }
          ]
        },
        {
          "model": "zai/glm-4.6",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9271, "unit": null }
          ]
        },
        {
          "model": "fireworks/gpt-oss-120b",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.926, "unit": null }
          ]
        },
        {
          "model": "alibaba/qwen3.5-flash",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.925, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-sonnet-4-6",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9229, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4-1-fast-reasoning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9187, "unit": null }
          ]
        },
        {
          "model": "zai/glm-5.1-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9187, "unit": null }
          ]
        },
        {
          "model": "zai/glm-5-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9167, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5-mini-2025-08-07",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9146, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4-fast-reasoning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9125, "unit": null }
          ]
        },
        {
          "model": "minimax/MiniMax-M2.7",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9104, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4-0709",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.9056, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5.4-nano-2026-03-17",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8875, "unit": null }
          ]
        },
        {
          "model": "minimax/MiniMax-M2.5-Lightning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8875, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-sonnet-4-5-20250929-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8819, "unit": null }
          ]
        },
        {
          "model": "zai/glm-4.5",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8667, "unit": null }
          ]
        },
        {
          "model": "openai/o3-mini-2025-01-31",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8646, "unit": null }
          ]
        },
        {
          "model": "alibaba/qwen3.5-plus-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8604, "unit": null }
          ]
        },
        {
          "model": "fireworks/gpt-oss-20b",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8604, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.5-pro-exp-03-25",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8583, "unit": null }
          ]
        },
        {
          "model": "kimi/kimi-k2-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8542, "unit": null }
          ]
        },
        {
          "model": "openai/o3-2025-04-16",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8528, "unit": null }
          ]
        },
        {
          "model": "grok/grok-3-mini-fast-high-reasoning",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.85, "unit": null }
          ]
        },
        {
          "model": "fireworks/deepseek-v3p2-thinking",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8458, "unit": null }
          ]
        },
        {
          "model": "fireworks/qwen3-235b-a22b",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8396, "unit": null }
          ]
        },
        {
          "model": "openai/o4-mini-2025-04-16",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8367, "unit": null }
          ]
        },
        {
          "model": "mistralai/magistral-medium-2509",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8354, "unit": null }
          ]
        },
        {
          "model": "google/gemini-3.1-flash-lite-preview",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8333, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-haiku-4-5-20251001-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8271, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-5-nano-2025-08-07",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8118, "unit": null }
          ]
        },
        {
          "model": "alibaba/qwen3-max",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8104, "unit": null }
          ]
        },
        {
          "model": "mistralai/magistral-small-2509",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.8068, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-1-20250805-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7818, "unit": null }
          ]
        },
        {
          "model": "minimax/MiniMax-M2.1",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7792, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-5-20251101",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7688, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-sonnet-4-20250514-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7625, "unit": null }
          ]
        },
        {
          "model": "fireworks/deepseek-r1",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7396, "unit": null }
          ]
        },
        {
          "model": "openai/o1-2024-12-17",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7146, "unit": null }
          ]
        },
        {
          "model": "grok/grok-3-mini-fast-low-reasoning",
          "effort": "low",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.7063, "unit": null }
          ]
        },
        {
          "model": "fireworks/deepseek-v3p2",
          "effort": "none",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.6479, "unit": null }
          ]
        },
        {
          "model": "together/moonshotai/Kimi-K2-Instruct",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.6271, "unit": null }
          ]
        },
        {
          "model": "alibaba/qwen3-max-preview",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.6069, "unit": null }
          ]
        },
        {
          "model": "grok/grok-3",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.5875, "unit": null }
          ]
        },
        {
          "model": "together/langston/nim/nvidia/llama-3.3-nemotron-super-49b-v1-42e84561-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.5354, "unit": null }
          ]
        },
        {
          "model": "fireworks/deepseek-v3-0324",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.522, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.5-flash-preview-09-2025-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.5146, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.5-flash-preview-09-2025",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4979, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4.1-mini-2025-04-14",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4938, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-3-7-sonnet-20250219-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4458, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-1-20250805",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4424, "unit": null }
          ]
        },
        {
          "model": "mistralai/mistral-large-2512",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4292, "unit": null }
          ]
        },
        {
          "model": "mistralai/mistral-medium-2505",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4229, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.5-flash-lite-preview-09-2025-thinking",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4208, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-opus-4-20250514",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.4125, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4.1-2025-04-14",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.3958, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-sonnet-4-20250514",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.3854, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4-fast-non-reasoning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.3333, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.0-flash-001",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2979, "unit": null }
          ]
        },
        {
          "model": "fireworks/deepseek-v3",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.275, "unit": null }
          ]
        },
        {
          "model": "grok/grok-4-1-fast-non-reasoning",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2708, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4.1-nano-2025-04-14",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2646, "unit": null }
          ]
        },
        {
          "model": "google/gemini-2.5-flash-lite-preview-09-2025",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2625, "unit": null }
          ]
        },
        {
          "model": "fireworks/llama4-maverick-instruct-basic",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2521, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-3-7-sonnet-20250219",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.2229, "unit": null }
          ]
        },
        {
          "model": "together/meta-llama/Llama-4-Scout-17B-16E-Instruct",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1896, "unit": null }
          ]
        },
        {
          "model": "google/gemini-1.5-pro-002",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1875, "unit": null }
          ]
        },
        {
          "model": "google/gemini-1.5-flash-002",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1729, "unit": null }
          ]
        },
        {
          "model": "together/meta-llama/Llama-3.3-70B-Instruct-Turbo",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1604, "unit": null }
          ]
        },
        {
          "model": "grok/grok-2-1212",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1521, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4o-2024-08-06",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1396, "unit": null }
          ]
        },
        {
          "model": "cohere/command-a-03-2025",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1333, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4o-2024-11-20",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1187, "unit": null }
          ]
        },
        {
          "model": "openai/gpt-4o-mini-2024-07-18",
          "effort": "high",
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1146, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-3-5-sonnet-20241022",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.1, "unit": null }
          ]
        },
        {
          "model": "together/langston/nim/nvidia/llama-3.3-nemotron-super-49b-v1-42e84561",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0938, "unit": null }
          ]
        },
        {
          "model": "mistralai/mistral-large-2411",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0917, "unit": null }
          ]
        },
        {
          "model": "mistralai/mistral-small-2402",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0563, "unit": null }
          ]
        },
        {
          "model": "mistralai/mistral-small-2503",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0354, "unit": null }
          ]
        },
        {
          "model": "anthropic/claude-3-5-haiku-20241022",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0333, "unit": null }
          ]
        },
        {
          "model": "ai21labs/jamba-mini-1.6",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0042, "unit": null }
          ]
        },
        {
          "model": "ai21labs/jamba-large-1.6",
          "effort": null,
          "system_description": null,
          "scores": [
            { "metric": "accuracy (pass@1, 60 questions)", "value": 0.0042, "unit": null }
          ]
        }
      ],
      "note": "Vals AI AIME leaderboard (updated 2026-04-16). 96 models across 15+ providers. 60 questions (30 from 2024, 30 from 2025). Methodology: pass@1 averaged across 8 runs per model. Prompt: Please reason step by step, and put your final answer within \boxed{}. Image questions excluded. Key insights: 9/10 top models are reasoning models; single questions commonly require 30k+ reasoning tokens; hardest questions take 15+ min generation time. Data contamination concern: models perform better on 2024 vs 2025 questions."
    }
  ],

  "notes": "AIME (American Invitational Mathematics Examination) is a prestigious math competition used as an LLM benchmark. Unlike purpose-built benchmarks, AIME consists of real competition problems not designed for AI evaluation.\n\nKey characteristics:\n- 30 questions per year (15 per session, AIME I and AIME II)\n- Integer answers in range 0-999\n- Exact match scoring only (no partial credit)\n- Covers algebra, geometry, number theory, combinatorics, probability\n- Problems require multi-step mathematical reasoning\n- Human median top competitor: 26-40% (4-6 of 15 problems)\n\nThe Harbor adapter uses 60 tasks: AIME 2024 (30 questions) + AIME 2025-I (15) + AIME 2025-II (15), sourced from GAIR-NLP/AIME-Preview.\n\n**No adapter_metadata.json or parity_experiment.json exist** in the Harbor repo for this adapter (404 errors). The adapter appears to be simpler — just exact-match integer comparison in a Docker environment.\n\n**Benchmark saturation**: As of April 2026, AIME is heavily saturated. Top model (Gemini 3.1 Pro Preview) at 98.13%, with 12 models above 95%. Vals AI tracks 96 models across 15+ providers.\n\n**No single authoritative paper**: AIME is a math competition, not an ML benchmark paper. The GAIR-NLP/AIME-Preview repo provides an evaluation framework with citation but is not a traditional benchmark paper. Vals AI is the primary third-party leaderboard.\n\n**Tool-augmented results**: With code execution (Python), GPT-5 Pro achieves 100%. Tool use significantly boosts performance on computational problems.\n\n**Data contamination risk**: AIME problems are publicly available after competition, so models trained on post-competition data may have seen the problems. AIME 2025 problems released Feb 2025 mitigate this for models with earlier training cutoffs."
}
```

---

## Detailed Research Notes

### 1. What is AIME?

The American Invitational Mathematics Examination (AIME) is a math competition administered by the Mathematical Association of America (MAA). It serves as a qualifying exam for the USA Mathematical Olympiad (USAMO).

**Format:**
- 15 questions per session (AIME I and AIME II each year)
- All answers are integers from 000 to 999
- 3 hours for 15 questions
- No calculators allowed (for human competitors)
- Topics: algebra, geometry, number theory, combinatorics, probability, trigonometry

**As an LLM benchmark:**
- Used informally — not designed as an ML benchmark
- 60 problems in Harbor adapter: AIME 2024 (30) + AIME 2025 (30)
- Exact match only, no partial credit
- Tests multi-step mathematical reasoning
- Problems range from moderately difficult to extremely challenging

### 2. GAIR-NLP/AIME-Preview (https://github.com/GAIR-NLP/AIME-Preview)

**Authors:** Yixin Ye, Yang Xiao, Tiantian Mi, Pengfei Liu (Shanghai AI Laboratory / GAIR)

**Framework features:**
- Real-time evaluation for AIME 2025 (released February 14, 2025)
- Multiple temperature settings evaluated: 0.0, 0.3, 0.6
- 8 samples per question for API models
- Max tokens: 32,768
- Top-p: 0.95, Seed: 0 (for reproducibility)
- Standardized evaluation protocol

**Full results table (from Result-AIME-2025-0311.jpeg):**

| Model | Samples | AIME 2024 | AIME I 2025 (AVG) | AIME II 2025 (AVG) | AIME 2025 |
|-------|---------|-----------|-------------------|---------------------|-----------|
| o3-mini-high | N/A | 83.8 | 76.7 | 85.0 | 80.85 |
| o3-mini-medium | N/A | 75.8 | 66.7 | 74.17 | 70.44 |
| DeepSeek-R1 | N/A | 79.8 | 65.0 | 75.0 | 70.00 |
| QwQ-32B | N/A | 79.5 | 60.0 | 63.8 | 61.94 |
| DeepSeek-R1-Distill-Llama-70B | 800k | 57.1 | 51.4 | 61.14 | 56.27 |
| o1-mini | N/A | 63.6 | 50.8 | 56.7 | 53.75 |
| DeepSeek-R1-Distill-Qwen-32B | 800k | 58.3 | 46.1 | 53.1 | 49.60 |
| DeepSeek-R1-Distill-Qwen-14B | 800k | 61.7 | 46.7 | 49.2 | 47.95 |
| limo | 817 | 56.3 | 44.5 | 44.7 | 44.60 |
| gemini-2.0-flash-thinking | N/A | 61.5 | 43.3 | 45.8 | 44.55 |
| o3-mini-low | N/A | 56.3 | 44.2 | 40.0 | 42.10 |
| o1-preview | N/A | 44.6 | 37.5 | 38.3 | 37.90 |
| DeepSeek-R1-Distill-Qwen-7B | 800k | 49.6 | 36.9 | 36.7 | 36.80 |
| QwQ-32B-Preview | N/A | 46.7 | 37.2 | 28.1 | 32.65 |
| s1 | 1k | 32.9 | 28.9 | 28.3 | 28.60 |
| DeepSeek-R1-Distill-Llama-8B | 800k | 37.1 | 24.7 | 23.0 | 23.85 |
| DeepSeek-R1-Distill-Qwen-1.5B | 800k | 25.0 | 28.0 | 14.4 | 21.20 |

**Temperature sensitivity analysis (from Result-Temperature-0311.jpeg, AIME I 2025 only, locally deployed models):**

| Model | Temp 0.0 | Temp 0.3 | Temp 0.6 | Average |
|-------|----------|----------|----------|---------|
| QwQ-32B | 53.3 | 65.0 | 61.7 | 60.0 |
| DeepSeek-R1-Distill-Llama-70B | 60.0 | 45.8 | 48.3 | 51.4 |
| DeepSeek-R1-Distill-Qwen-14B | 53.3 | 40.0 | 46.7 | 46.7 |
| DeepSeek-R1-Distill-Qwen-32B | 46.7 | 42.5 | 49.2 | 46.1 |
| limo | 46.7 | 45.0 | 41.7 | 44.5 |
| QwQ-32B-Preview | 33.3 | 40.8 | 37.5 | 37.2 |
| DeepSeek-R1-Distill-Qwen-7B | 33.3 | 37.5 | 40.0 | 36.9 |
| s1 | 33.3 | 25.0 | 28.3 | 28.9 |
| DeepSeek-R1-Distill-Qwen-1.5B | 33.3 | 23.3 | 27.5 | 28.0 |
| DeepSeek-R1-Distill-Llama-8B | 20.0 | 28.3 | 25.8 | 24.7 |

**Key findings:**
- "No single temperature setting was universally optimal across all models."
- Larger models showed greater stability across temperatures.
- QwQ-32B performed best at temp 0.3 (65.0%), worst at temp 0.0 (53.3%) — a 12 point spread.
- DeepSeek-R1-Distill-Llama-70B performed best at temp 0.0 (60.0%), worst at temp 0.3 (45.8%) — opposite pattern.
- Smallest model (Qwen-1.5B) was most erratic: temp 0.0 tied with larger models at 33.3% but dropped to 23.3% at temp 0.3.

### 3. Vals AI Leaderboard Results (as of April 2026)

Source: https://www.vals.ai/benchmarks/aime (updated 2026-04-16)

**Methodology**: Pass@1 averaged across 8 runs per model. 60 questions (30 from 2024, 30 from 2025). Prompt: "Please reason step by step, and put your final answer within \boxed{}". Image questions excluded.

96 models tracked across 15+ providers. Top 30 shown below (full data in JSON above):

| # | Model | Provider | Accuracy | Effort |
|---|-------|----------|----------|--------|
| 1 | google/gemini-3.1-pro-preview | Google | 98.13% | high |
| 2 | openai/gpt-5.2-2025-12-11 | OpenAI | 96.88% | xhigh |
| 3 | meta/muse_spark | Meta | 96.88% | — |
| 4 | google/gemini-3-pro-preview | Google | 96.68% | high |
| 5 | openai/gpt-5.4-2026-03-05 | OpenAI | 96.67% | xhigh |
| 6 | grok/grok-4.20-0309-reasoning | xAI | 96.46% | — |
| 7 | anthropic/claude-opus-4-7 | Anthropic | 96.25% | — |
| 8 | google/gemini-3-flash-preview | Google | 95.63% | high |
| 9 | anthropic/claude-opus-4-6-thinking | Anthropic | 95.63% | — |
| 10 | openai/gpt-5.4-mini-2026-03-17 | OpenAI | 95.63% | xhigh |
| 11 | kimi/kimi-k2.5-thinking | Moonshot AI | 95.63% | — |
| 12 | anthropic/claude-opus-4-5-20251101-thinking | Anthropic | 95.42% | — |
| 13 | alibaba/qwen3.6-plus | Alibaba | 94.58% | — |
| 14 | openai/gpt-5-2025-08-07 | OpenAI | 93.37% | high |
| 15 | openai/gpt-5.1-2025-11-13 | OpenAI | 93.33% | high |
| 16 | zai/glm-4.7 | Zhipu AI | 93.33% | — |
| 17 | zai/glm-4.6 | Zhipu AI | 92.71% | — |
| 18 | fireworks/gpt-oss-120b | Fireworks AI | 92.60% | — |
| 19 | alibaba/qwen3.5-flash | Alibaba | 92.50% | — |
| 20 | anthropic/claude-sonnet-4-6 | Anthropic | 92.29% | — |
| 21 | grok/grok-4-1-fast-reasoning | xAI | 91.88% | — |
| 22 | zai/glm-5.1-thinking | Zhipu AI | 91.88% | — |
| 23 | zai/glm-5-thinking | Zhipu AI | 91.67% | — |
| 24 | openai/gpt-5-mini-2025-08-07 | OpenAI | 91.46% | high |
| 25 | grok/grok-4-fast-reasoning | xAI | 91.25% | — |
| 26 | minimax/MiniMax-M2.7 | MiniMax | 91.04% | — |
| 27 | grok/grok-4-0709 | xAI | 90.56% | — |
| 28 | openai/gpt-5.4-nano-2026-03-17 | OpenAI | 88.75% | high |
| 29 | minimax/MiniMax-M2.5-Lightning | MiniMax | 88.75% | — |
| 30 | anthropic/claude-sonnet-4-5-20250929-thinking | Anthropic | 88.19% | — |

**Key observations:**
- Benchmark is heavily saturated — top 12 models all above 95%
- 9/10 top models are reasoning models
- Meta's muse_spark ties for 2nd at 96.88% with lowest cost ($0.005/test)
- Non-reasoning models (grok-4-fast-non-reasoning at 33.3%, claude-3-5-sonnet at 10%) show massive gap vs reasoning variants
- Bottom tier (<5%): Claude 3.5 Haiku, Mistral Small, Jamba models

### 4. Harbor Adapter (aime)

**Structure:** 60 tasks from AIME 2024 (30) + AIME 2025-I (15) + AIME 2025-II (15)

**Files:** adapter.py, run_adapter.py, aime.yaml, templates/ directory

**Evaluation:** Integer exact match (0-999). Docker-based isolated environment.

**No adapter_metadata.json or parity_experiment.json** — these files returned 404, suggesting the adapter may be newer or simpler (no parity validation yet).

---

## Questions

1. **No paper**: AIME is a math competition, not a published benchmark with a paper. Should the `paper` field link to the GAIR-NLP/AIME-Preview citation, or remain null? There's no single authoritative paper describing AIME as an LLM benchmark.

2. **No Harbor parity data**: The adapter has no adapter_metadata.json or parity_experiment.json. This is a gap compared to other benchmarks. Should this be flagged?

3. **Benchmark saturation**: Top models now score 100% on AIME 2025. This raises questions about the benchmark's continued utility for differentiating frontier models. Should this be noted in the JSON?

4. **Methodology inconsistency**: Different leaderboards report AIME scores differently — some use pass@1, some use consensus/majority voting (maj@k), some use best-of-k. The values in the JSON may not be directly comparable across sources. The template doesn't have a field for specifying the evaluation methodology per result.

5. **Year-specific splits**: AIME 2024 and AIME 2025 are different question sets. Some leaderboards report them separately, others combine. The Harbor adapter uses both (60 total). Should results be reported per-year or combined?

6. **Tool augmentation**: Some reported scores use code execution (Python), which dramatically boosts performance. The template's `system_description` could capture this (e.g., "with Python code execution"), but many sources don't clearly distinguish tool-augmented vs closed-book results.
