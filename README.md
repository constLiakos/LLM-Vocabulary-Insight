# LLM Vocabulary Insight Report

[ℹ️ Project Info](README.dev.md)

## 🎯 Overview

This report presents a comprehensive analysis of Greek language tokenization capabilities across **29** Large Language Models (LLMs). The analysis evaluates how effectively different transformer-based models handle Greek text through their tokenizer vocabularies, providing insights into Greek language support, character coverage, and tokenization efficiency.

## Overall Statistics

| Metric | Value |
|--------|-------|
| **Total Models Analyzed** | 29 |
| **Combined Vocabulary Size** | 3,357,454 tokens |
| **Average Vocabulary Size** | 115,774 tokens |
| **Total Greek Tokens** | 64,491 (1.92%) |
| **Total Latin Tokens** | 2,344,092 (69.82%) |

## Model Performance Rankings

### 🇬🇷 Greek Language Support

#### By Absolute Token Count
🥇 **Most Tokens**: ilsp/Meltemi-7B-Instruct-v1.5 - 28,162 tokens (45.89%)  
📉 **Fewest Tokens**: ibm-granite/granite-4.0-tiny-preview - 42 tokens (0.09%)

#### By Percentage Coverage
🥇 **Highest %**: ilsp/Meltemi-7B-Instruct-v1.5 - 45.89% (28,162 tokens)  
📉 **Lowest %**: microsoft/phi-4 - 0.04% (44 tokens)

### 🇮🇹 Latin Language Support

#### By Absolute Token Count
🥇 **Most Tokens**: unsloth/gemma-2-2b-it - 184,588 tokens (72.10%)  
📉 **Fewest Tokens**: unsloth/Phi-3.5-mini-instruct - 25,624 tokens (80.08%)

#### By Percentage Coverage
🥇 **Highest %**: unsloth/SmolLM2-1.7B-Instruct - 95.94% (47,156 tokens)  
📉 **Lowest %**: ilsp/Meltemi-7B-Instruct-v1.5 - 42.28% (25,948 tokens)

## Greek Performance Rankings

### By Token Count (Absolute Numbers)

| Rank | Model | Greek Tokens | Total Vocabulary | Percentage |
|------|-------|--------------|------------------|------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 28,162 | 61,366 | 45.89% |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 22,212 | 149,248 | 14.88% |
| 3 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2,816 | 128,000 | 2.20% |
| 4 | **unsloth/gemma-3-4b-it** | 1,409 | 262,144 | 0.54% |
| 5 | **unsloth/Llama-3.2-3B-Instruct** | 1,378 | 128,000 | 1.08% |
| 6 | **unsloth/llama-3-8b** | 1,378 | 128,000 | 1.08% |
| 7 | **unsloth/Llama-3.3-70B-Instruct** | 1,378 | 128,000 | 1.08% |
| 8 | **microsoft/bitnet-b1.58-2B-4T** | 1,378 | 128,000 | 1.08% |
| 9 | **unsloth/gemma-2-2b-it** | 1,229 | 256,000 | 0.48% |
| 10 | **unsloth/DeepSeek-R1** | 629 | 128,000 | 0.49% |
| 11 | **unsloth/DeepSeek-Prover-V2-671B** | 629 | 128,000 | 0.49% |
| 12 | **tngtech/DeepSeek-R1T-Chimera** | 629 | 128,000 | 0.49% |
| 13 | **Qwen/Qwen2.5-1.5B-Instruct** | 127 | 151,643 | 0.08% |
| 14 | **Qwen/Qwen3-0.6B** | 127 | 151,643 | 0.08% |
| 15 | **Qwen/Qwen3-32B** | 127 | 151,643 | 0.08% |
| 16 | **Qwen/Qwen2.5-Omni-3B** | 127 | 151,643 | 0.08% |
| 17 | **XiaomiMiMo/MiMo-7B-RL** | 127 | 151,643 | 0.08% |
| 18 | **deepseek-ai/DeepSeek-V2.5-1210** | 86 | 100,000 | 0.09% |
| 19 | **unsloth/Phi-3.5-mini-instruct** | 63 | 32,000 | 0.20% |
| 20 | **unsloth/SmolLM2-1.7B-Instruct** | 60 | 49,152 | 0.12% |
| 21 | **unsloth/mistral-7b-v0.3** | 58 | 32,768 | 0.18% |
| 22 | **unsloth/Mistral-Small-Instruct-2409** | 58 | 32,768 | 0.18% |
| 23 | **Xenova/gpt-4** | 44 | 100,263 | 0.04% |
| 24 | **Xenova/text-embedding-ada-002** | 44 | 100,261 | 0.04% |
| 25 | **Xenova/gpt-3.5-turbo-16k** | 44 | 100,261 | 0.04% |
| 26 | **microsoft/phi-4** | 44 | 100,352 | 0.04% |
| 27 | **microsoft/Phi-4-reasoning-plus** | 44 | 100,352 | 0.04% |
| 28 | **ibm-granite/granite-4.0-tiny-preview** | 42 | 49,152 | 0.09% |
| 29 | **ibm-granite/granite-3.3-8b-instruct** | 42 | 49,152 | 0.09% |


### By Percentage (Relative Performance)

| Rank | Model | Percentage | Greek Tokens | Total Vocabulary |
|------|-------|------------|--------------|------------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 45.89% | 28,162 | 61,366 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 14.88% | 22,212 | 149,248 |
| 3 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2.20% | 2,816 | 128,000 |
| 4 | **unsloth/Llama-3.2-3B-Instruct** | 1.08% | 1,378 | 128,000 |
| 5 | **unsloth/llama-3-8b** | 1.08% | 1,378 | 128,000 |
| 6 | **unsloth/Llama-3.3-70B-Instruct** | 1.08% | 1,378 | 128,000 |
| 7 | **microsoft/bitnet-b1.58-2B-4T** | 1.08% | 1,378 | 128,000 |
| 8 | **unsloth/gemma-3-4b-it** | 0.54% | 1,409 | 262,144 |
| 9 | **unsloth/DeepSeek-R1** | 0.49% | 629 | 128,000 |
| 10 | **unsloth/DeepSeek-Prover-V2-671B** | 0.49% | 629 | 128,000 |
| 11 | **tngtech/DeepSeek-R1T-Chimera** | 0.49% | 629 | 128,000 |
| 12 | **unsloth/gemma-2-2b-it** | 0.48% | 1,229 | 256,000 |
| 13 | **unsloth/Phi-3.5-mini-instruct** | 0.20% | 63 | 32,000 |
| 14 | **unsloth/mistral-7b-v0.3** | 0.18% | 58 | 32,768 |
| 15 | **unsloth/Mistral-Small-Instruct-2409** | 0.18% | 58 | 32,768 |
| 16 | **unsloth/SmolLM2-1.7B-Instruct** | 0.12% | 60 | 49,152 |
| 17 | **deepseek-ai/DeepSeek-V2.5-1210** | 0.09% | 86 | 100,000 |
| 18 | **ibm-granite/granite-4.0-tiny-preview** | 0.09% | 42 | 49,152 |
| 19 | **ibm-granite/granite-3.3-8b-instruct** | 0.09% | 42 | 49,152 |
| 20 | **Qwen/Qwen2.5-1.5B-Instruct** | 0.08% | 127 | 151,643 |
| 21 | **Qwen/Qwen3-0.6B** | 0.08% | 127 | 151,643 |
| 22 | **Qwen/Qwen3-32B** | 0.08% | 127 | 151,643 |
| 23 | **Qwen/Qwen2.5-Omni-3B** | 0.08% | 127 | 151,643 |
| 24 | **XiaomiMiMo/MiMo-7B-RL** | 0.08% | 127 | 151,643 |
| 25 | **Xenova/text-embedding-ada-002** | 0.04% | 44 | 100,261 |
| 26 | **Xenova/gpt-3.5-turbo-16k** | 0.04% | 44 | 100,261 |
| 27 | **Xenova/gpt-4** | 0.04% | 44 | 100,263 |
| 28 | **microsoft/phi-4** | 0.04% | 44 | 100,352 |
| 29 | **microsoft/Phi-4-reasoning-plus** | 0.04% | 44 | 100,352 |


## Latin Performance Rankings

### By Token Count (Absolute Numbers)

| Rank | Model | Latin Tokens | Total Vocabulary | Percentage |
|------|-------|--------------|------------------|------------|
| 1 | **unsloth/gemma-2-2b-it** | 184,588 | 256,000 | 72.10% |
| 2 | **unsloth/gemma-3-4b-it** | 151,739 | 262,144 | 57.88% |
| 3 | **ilsp/Llama-Krikri-8B-Instruct** | 96,699 | 149,248 | 64.79% |
| 4 | **unsloth/Llama-3.2-3B-Instruct** | 96,687 | 128,000 | 75.54% |
| 5 | **unsloth/llama-3-8b** | 96,687 | 128,000 | 75.54% |
| 6 | **unsloth/Llama-3.3-70B-Instruct** | 96,687 | 128,000 | 75.54% |
| 7 | **microsoft/bitnet-b1.58-2B-4T** | 96,687 | 128,000 | 75.54% |
| 8 | **Qwen/Qwen2.5-1.5B-Instruct** | 93,859 | 151,643 | 61.89% |
| 9 | **Qwen/Qwen3-0.6B** | 93,859 | 151,643 | 61.89% |
| 10 | **Qwen/Qwen3-32B** | 93,859 | 151,643 | 61.89% |
| 11 | **Qwen/Qwen2.5-Omni-3B** | 93,859 | 151,643 | 61.89% |
| 12 | **XiaomiMiMo/MiMo-7B-RL** | 93,859 | 151,643 | 61.89% |
| 13 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 91,179 | 128,000 | 71.23% |
| 14 | **Xenova/gpt-4** | 89,643 | 100,263 | 89.41% |
| 15 | **Xenova/text-embedding-ada-002** | 89,643 | 100,261 | 89.41% |
| 16 | **Xenova/gpt-3.5-turbo-16k** | 89,643 | 100,261 | 89.41% |
| 17 | **microsoft/phi-4** | 89,643 | 100,352 | 89.33% |
| 18 | **microsoft/Phi-4-reasoning-plus** | 89,643 | 100,352 | 89.33% |
| 19 | **unsloth/DeepSeek-R1** | 71,454 | 128,000 | 55.82% |
| 20 | **unsloth/DeepSeek-Prover-V2-671B** | 71,454 | 128,000 | 55.82% |
| 21 | **tngtech/DeepSeek-R1T-Chimera** | 71,454 | 128,000 | 55.82% |
| 22 | **deepseek-ai/DeepSeek-V2.5-1210** | 70,489 | 100,000 | 70.49% |
| 23 | **unsloth/SmolLM2-1.7B-Instruct** | 47,156 | 49,152 | 95.94% |
| 24 | **ibm-granite/granite-4.0-tiny-preview** | 40,302 | 49,152 | 81.99% |
| 25 | **ibm-granite/granite-3.3-8b-instruct** | 40,302 | 49,152 | 81.99% |
| 26 | **ilsp/Meltemi-7B-Instruct-v1.5** | 25,948 | 61,366 | 42.28% |
| 27 | **unsloth/mistral-7b-v0.3** | 25,723 | 32,768 | 78.50% |
| 28 | **unsloth/Mistral-Small-Instruct-2409** | 25,723 | 32,768 | 78.50% |
| 29 | **unsloth/Phi-3.5-mini-instruct** | 25,624 | 32,000 | 80.08% |


### By Percentage (Relative Performance)

| Rank | Model | Percentage | Latin Tokens | Total Vocabulary |
|------|-------|------------|--------------|------------------|
| 1 | **unsloth/SmolLM2-1.7B-Instruct** | 95.94% | 47,156 | 49,152 |
| 2 | **Xenova/text-embedding-ada-002** | 89.41% | 89,643 | 100,261 |
| 3 | **Xenova/gpt-3.5-turbo-16k** | 89.41% | 89,643 | 100,261 |
| 4 | **Xenova/gpt-4** | 89.41% | 89,643 | 100,263 |
| 5 | **microsoft/phi-4** | 89.33% | 89,643 | 100,352 |
| 6 | **microsoft/Phi-4-reasoning-plus** | 89.33% | 89,643 | 100,352 |
| 7 | **ibm-granite/granite-4.0-tiny-preview** | 81.99% | 40,302 | 49,152 |
| 8 | **ibm-granite/granite-3.3-8b-instruct** | 81.99% | 40,302 | 49,152 |
| 9 | **unsloth/Phi-3.5-mini-instruct** | 80.08% | 25,624 | 32,000 |
| 10 | **unsloth/mistral-7b-v0.3** | 78.50% | 25,723 | 32,768 |
| 11 | **unsloth/Mistral-Small-Instruct-2409** | 78.50% | 25,723 | 32,768 |
| 12 | **unsloth/Llama-3.2-3B-Instruct** | 75.54% | 96,687 | 128,000 |
| 13 | **unsloth/llama-3-8b** | 75.54% | 96,687 | 128,000 |
| 14 | **unsloth/Llama-3.3-70B-Instruct** | 75.54% | 96,687 | 128,000 |
| 15 | **microsoft/bitnet-b1.58-2B-4T** | 75.54% | 96,687 | 128,000 |
| 16 | **unsloth/gemma-2-2b-it** | 72.10% | 184,588 | 256,000 |
| 17 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 71.23% | 91,179 | 128,000 |
| 18 | **deepseek-ai/DeepSeek-V2.5-1210** | 70.49% | 70,489 | 100,000 |
| 19 | **ilsp/Llama-Krikri-8B-Instruct** | 64.79% | 96,699 | 149,248 |
| 20 | **Qwen/Qwen2.5-1.5B-Instruct** | 61.89% | 93,859 | 151,643 |
| 21 | **Qwen/Qwen3-0.6B** | 61.89% | 93,859 | 151,643 |
| 22 | **Qwen/Qwen3-32B** | 61.89% | 93,859 | 151,643 |
| 23 | **Qwen/Qwen2.5-Omni-3B** | 61.89% | 93,859 | 151,643 |
| 24 | **XiaomiMiMo/MiMo-7B-RL** | 61.89% | 93,859 | 151,643 |
| 25 | **unsloth/gemma-3-4b-it** | 57.88% | 151,739 | 262,144 |
| 26 | **unsloth/DeepSeek-R1** | 55.82% | 71,454 | 128,000 |
| 27 | **unsloth/DeepSeek-Prover-V2-671B** | 55.82% | 71,454 | 128,000 |
| 28 | **tngtech/DeepSeek-R1T-Chimera** | 55.82% | 71,454 | 128,000 |
| 29 | **ilsp/Meltemi-7B-Instruct-v1.5** | 42.28% | 25,948 | 61,366 |


## Comparative Analysis

### Vocabulary Size Distribution

| Model | Total Vocabulary | Visual Scale | Relative Size |
|-------|------------------|--------------|---------------|
| **unsloth/gemma-3-4b-it** | 262,144 |  | 226.4% of avg |
| **unsloth/gemma-2-2b-it** | 256,000 |  | 221.1% of avg |
| **Qwen/Qwen2.5-1.5B-Instruct** | 151,643 |  | 131.0% of avg |
| **Qwen/Qwen3-0.6B** | 151,643 |  | 131.0% of avg |
| **Qwen/Qwen3-32B** | 151,643 |  | 131.0% of avg |
| **Qwen/Qwen2.5-Omni-3B** | 151,643 |  | 131.0% of avg |
| **XiaomiMiMo/MiMo-7B-RL** | 151,643 |  | 131.0% of avg |
| **ilsp/Llama-Krikri-8B-Instruct** | 149,248 |  | 128.9% of avg |
| **unsloth/Llama-3.2-3B-Instruct** | 128,000 |  | 110.6% of avg |
| **unsloth/llama-3-8b** | 128,000 |  | 110.6% of avg |
| **unsloth/Llama-3.3-70B-Instruct** | 128,000 |  | 110.6% of avg |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 128,000 |  | 110.6% of avg |
| **unsloth/DeepSeek-R1** | 128,000 |  | 110.6% of avg |
| **unsloth/DeepSeek-Prover-V2-671B** | 128,000 |  | 110.6% of avg |
| **tngtech/DeepSeek-R1T-Chimera** | 128,000 |  | 110.6% of avg |
| **microsoft/bitnet-b1.58-2B-4T** | 128,000 |  | 110.6% of avg |
| **microsoft/phi-4** | 100,352 |  | 86.7% of avg |
| **microsoft/Phi-4-reasoning-plus** | 100,352 |  | 86.7% of avg |
| **Xenova/gpt-4** | 100,263 |  | 86.6% of avg |
| **Xenova/text-embedding-ada-002** | 100,261 |  | 86.6% of avg |
| **Xenova/gpt-3.5-turbo-16k** | 100,261 |  | 86.6% of avg |
| **deepseek-ai/DeepSeek-V2.5-1210** | 100,000 |  | 86.4% of avg |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 61,366 |  | 53.0% of avg |
| **unsloth/SmolLM2-1.7B-Instruct** | 49,152 |  | 42.5% of avg |
| **ibm-granite/granite-4.0-tiny-preview** | 49,152 |  | 42.5% of avg |
| **ibm-granite/granite-3.3-8b-instruct** | 49,152 |  | 42.5% of avg |
| **unsloth/mistral-7b-v0.3** | 32,768 |  | 28.3% of avg |
| **unsloth/Mistral-Small-Instruct-2409** | 32,768 |  | 28.3% of avg |
| **unsloth/Phi-3.5-mini-instruct** | 32,000 |  | 27.6% of avg |


### Greek Support Comparison

| Rank | Model | Greek Percentage | Greek Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 45.89% | 28,162 | 🟩🟩🟩🟩🟩 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 14.88% | 22,212 | 🟩🟩🟩🟩🟩 |
| 3 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2.20% | 2,816 | 🟩🟩🟩🟩🟩 |
| 4 | **unsloth/gemma-3-4b-it** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 5 | **unsloth/Llama-3.2-3B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 6 | **unsloth/llama-3-8b** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 7 | **unsloth/Llama-3.3-70B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 8 | **microsoft/bitnet-b1.58-2B-4T** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 9 | **unsloth/gemma-2-2b-it** | 0.48% | 1,229 | 🟩🟩⬜⬜⬜ |
| 10 | **unsloth/DeepSeek-R1** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 11 | **unsloth/DeepSeek-Prover-V2-671B** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 12 | **tngtech/DeepSeek-R1T-Chimera** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 13 | **Qwen/Qwen2.5-1.5B-Instruct** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 14 | **Qwen/Qwen3-0.6B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 15 | **Qwen/Qwen3-32B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 16 | **Qwen/Qwen2.5-Omni-3B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 17 | **XiaomiMiMo/MiMo-7B-RL** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 18 | **deepseek-ai/DeepSeek-V2.5-1210** | 0.09% | 86 | ⬜⬜⬜⬜⬜ |
| 19 | **unsloth/Phi-3.5-mini-instruct** | 0.20% | 63 | ⬜⬜⬜⬜⬜ |
| 20 | **unsloth/SmolLM2-1.7B-Instruct** | 0.12% | 60 | ⬜⬜⬜⬜⬜ |
| 21 | **unsloth/mistral-7b-v0.3** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 22 | **unsloth/Mistral-Small-Instruct-2409** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 23 | **Xenova/gpt-4** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 24 | **Xenova/text-embedding-ada-002** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 25 | **Xenova/gpt-3.5-turbo-16k** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 26 | **microsoft/phi-4** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 27 | **microsoft/Phi-4-reasoning-plus** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 28 | **ibm-granite/granite-4.0-tiny-preview** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |
| 29 | **ibm-granite/granite-3.3-8b-instruct** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |


### Latin Support Comparison

| Rank | Model | Latin Percentage | Latin Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **unsloth/gemma-2-2b-it** | 72.10% | 184,588 | 🟦🟦🟦🟦🟦 |
| 2 | **unsloth/gemma-3-4b-it** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 3 | **ilsp/Llama-Krikri-8B-Instruct** | 64.79% | 96,699 | 🟦🟦🟦🟦🟦 |
| 4 | **unsloth/Llama-3.2-3B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 5 | **unsloth/llama-3-8b** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 6 | **unsloth/Llama-3.3-70B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 7 | **microsoft/bitnet-b1.58-2B-4T** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 8 | **Qwen/Qwen2.5-1.5B-Instruct** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 9 | **Qwen/Qwen3-0.6B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 10 | **Qwen/Qwen3-32B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 11 | **Qwen/Qwen2.5-Omni-3B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 12 | **XiaomiMiMo/MiMo-7B-RL** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 13 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 71.23% | 91,179 | 🟦🟦🟦🟦🟦 |
| 14 | **Xenova/gpt-4** | 89.41% | 89,643 | 🟦🟦🟦🟦🟦 |
| 15 | **Xenova/text-embedding-ada-002** | 89.41% | 89,643 | 🟦🟦🟦🟦🟦 |
| 16 | **Xenova/gpt-3.5-turbo-16k** | 89.41% | 89,643 | 🟦🟦🟦🟦🟦 |
| 17 | **microsoft/phi-4** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 18 | **microsoft/Phi-4-reasoning-plus** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 19 | **unsloth/DeepSeek-R1** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 20 | **unsloth/DeepSeek-Prover-V2-671B** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 21 | **tngtech/DeepSeek-R1T-Chimera** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 22 | **deepseek-ai/DeepSeek-V2.5-1210** | 70.49% | 70,489 | 🟦🟦🟦🟦🟦 |
| 23 | **unsloth/SmolLM2-1.7B-Instruct** | 95.94% | 47,156 | 🟦🟦🟦🟦🟦 |
| 24 | **ibm-granite/granite-4.0-tiny-preview** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 25 | **ibm-granite/granite-3.3-8b-instruct** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 26 | **ilsp/Meltemi-7B-Instruct-v1.5** | 42.28% | 25,948 | 🟦🟦🟦🟦🟦 |
| 27 | **unsloth/mistral-7b-v0.3** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |
| 28 | **unsloth/Mistral-Small-Instruct-2409** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |
| 29 | **unsloth/Phi-3.5-mini-instruct** | 80.08% | 25,624 | 🟦🟦🟦🟦🟦 |


### Cross-Language Performance Matrix

| Model | Total Vocab | Greek % | Greek Tokens | Latin % | Latin Tokens | Greek/Latin Ratio |
|-------|-------------|---------|--------------|---------|--------------|-------------------|
| **unsloth/Llama-3.2-3B-Instruct** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/llama-3-8b** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/Llama-3.3-70B-Instruct** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 128,000 | 2.20% | 2,816 | 71.23% | 91,179 | 0.03 |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 61,366 | 45.89% | 28,162 | 42.28% | 25,948 | 1.09 |
| **ilsp/Llama-Krikri-8B-Instruct** | 149,248 | 14.88% | 22,212 | 64.79% | 96,699 | 0.23 |
| **unsloth/mistral-7b-v0.3** | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |
| **unsloth/Mistral-Small-Instruct-2409** | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |
| **unsloth/SmolLM2-1.7B-Instruct** | 49,152 | 0.12% | 60 | 95.94% | 47,156 | 0.00 |
| **Xenova/gpt-4** | 100,263 | 0.04% | 44 | 89.41% | 89,643 | 0.00 |
| **Xenova/text-embedding-ada-002** | 100,261 | 0.04% | 44 | 89.41% | 89,643 | 0.00 |
| **Xenova/gpt-3.5-turbo-16k** | 100,261 | 0.04% | 44 | 89.41% | 89,643 | 0.00 |
| **Qwen/Qwen2.5-1.5B-Instruct** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen3-0.6B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen3-32B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen2.5-Omni-3B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **unsloth/gemma-2-2b-it** | 256,000 | 0.48% | 1,229 | 72.10% | 184,588 | 0.01 |
| **unsloth/gemma-3-4b-it** | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **deepseek-ai/DeepSeek-V2.5-1210** | 100,000 | 0.09% | 86 | 70.49% | 70,489 | 0.00 |
| **unsloth/DeepSeek-R1** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **unsloth/DeepSeek-Prover-V2-671B** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **tngtech/DeepSeek-R1T-Chimera** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **XiaomiMiMo/MiMo-7B-RL** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **unsloth/Phi-3.5-mini-instruct** | 32,000 | 0.20% | 63 | 80.08% | 25,624 | 0.00 |
| **microsoft/phi-4** | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **microsoft/Phi-4-reasoning-plus** | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **microsoft/bitnet-b1.58-2B-4T** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **ibm-granite/granite-4.0-tiny-preview** | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **ibm-granite/granite-3.3-8b-instruct** | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |


### Performance Categories

| High Greek Support (>1%) | Medium Greek Support (0.1-1%) | Low Greek Support (<0.1%) |
|---------------------------|--------------------------------|---------------------------|
| unsloth/Llama-3.2-3B-Instruct (1.08%) | unsloth/mistral-7b-v0.3 (0.18%) | Xenova/gpt-4 (0.04%) |
| unsloth/llama-3-8b (1.08%) | unsloth/Mistral-Small-Instruct-2409 (0.18%) | Xenova/text-embedding-ada-002 (0.04%) |
| unsloth/Llama-3.3-70B-Instruct (1.08%) | unsloth/SmolLM2-1.7B-Instruct (0.12%) | Xenova/gpt-3.5-turbo-16k (0.04%) |
| kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit (2.20%) | unsloth/gemma-2-2b-it (0.48%) | Qwen/Qwen2.5-1.5B-Instruct (0.08%) |
| ilsp/Meltemi-7B-Instruct-v1.5 (45.89%) | unsloth/gemma-3-4b-it (0.54%) | Qwen/Qwen3-0.6B (0.08%) |
| ilsp/Llama-Krikri-8B-Instruct (14.88%) | unsloth/DeepSeek-R1 (0.49%) | Qwen/Qwen3-32B (0.08%) |
| microsoft/bitnet-b1.58-2B-4T (1.08%) | unsloth/DeepSeek-Prover-V2-671B (0.49%) | Qwen/Qwen2.5-Omni-3B (0.08%) |
|  | tngtech/DeepSeek-R1T-Chimera (0.49%) | deepseek-ai/DeepSeek-V2.5-1210 (0.09%) |
|  | unsloth/Phi-3.5-mini-instruct (0.20%) | XiaomiMiMo/MiMo-7B-RL (0.08%) |
|  |  | microsoft/phi-4 (0.04%) |
|  |  | microsoft/Phi-4-reasoning-plus (0.04%) |
|  |  | ibm-granite/granite-4.0-tiny-preview (0.09%) |
|  |  | ibm-granite/granite-3.3-8b-instruct (0.09%) |


## Individual Model Analysis


### unsloth/Llama-3.2-3B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 1,378 | 1.08% |
| **Latin Tokens** | 96,687 | 75.54% |

#### Language Distribution
```
Greek:                                 1.08%
Latin:  ██████████████████████         75.54%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/llama-3-8b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 1,378 | 1.08% |
| **Latin Tokens** | 96,687 | 75.54% |

#### Language Distribution
```
Greek:                                 1.08%
Latin:  ██████████████████████         75.54%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Llama-3.3-70B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 1,378 | 1.08% |
| **Latin Tokens** | 96,687 | 75.54% |

#### Language Distribution
```
Greek:                                 1.08%
Latin:  ██████████████████████         75.54%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 2,816 | 2.20% |
| **Latin Tokens** | 91,179 | 71.23% |

#### Language Distribution
```
Greek:                                 2.20%
Latin:  █████████████████████          71.23%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: ` τ`, `ου`, ` π`, ` κ`, ` σ`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### ilsp/Meltemi-7B-Instruct-v1.5

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 61,366 | 100% |
| **Greek Tokens** | 28,162 | 45.89% |
| **Latin Tokens** | 25,948 | 42.28% |

#### Language Distribution
```
Greek:  █████████████                  45.89%
Latin:  ████████████                   42.28%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `ν`, `τ`, `ι`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### ilsp/Llama-Krikri-8B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 149,248 | 100% |
| **Greek Tokens** | 22,212 | 14.88% |
| **Latin Tokens** | 96,699 | 64.79% |

#### Language Distribution
```
Greek:  ████                           14.88%
Latin:  ███████████████████            64.79%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/mistral-7b-v0.3

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 32,768 | 100% |
| **Greek Tokens** | 58 | 0.18% |
| **Latin Tokens** | 25,723 | 78.50% |

#### Language Distribution
```
Greek:                                 0.18%
Latin:  ███████████████████████        78.50%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `ν`, `τ`, `ι`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Mistral-Small-Instruct-2409

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 32,768 | 100% |
| **Greek Tokens** | 58 | 0.18% |
| **Latin Tokens** | 25,723 | 78.50% |

#### Language Distribution
```
Greek:                                 0.18%
Latin:  ███████████████████████        78.50%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `ν`, `τ`, `ι`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/SmolLM2-1.7B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 49,152 | 100% |
| **Greek Tokens** | 60 | 0.12% |
| **Latin Tokens** | 47,156 | 95.94% |

#### Language Distribution
```
Greek:                                 0.12%
Latin:  ████████████████████████████   95.94%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `ν`, `ι`, `ρ`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Xenova/gpt-4

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,263 | 100% |
| **Greek Tokens** | 44 | 0.04% |
| **Latin Tokens** | 89,643 | 89.41% |

#### Language Distribution
```
Greek:                                 0.04%
Latin:  ██████████████████████████     89.41%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Xenova/text-embedding-ada-002

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,261 | 100% |
| **Greek Tokens** | 44 | 0.04% |
| **Latin Tokens** | 89,643 | 89.41% |

#### Language Distribution
```
Greek:                                 0.04%
Latin:  ██████████████████████████     89.41%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Xenova/gpt-3.5-turbo-16k

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,261 | 100% |
| **Greek Tokens** | 44 | 0.04% |
| **Latin Tokens** | 89,643 | 89.41% |

#### Language Distribution
```
Greek:                                 0.04%
Latin:  ██████████████████████████     89.41%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Qwen/Qwen2.5-1.5B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 151,643 | 100% |
| **Greek Tokens** | 127 | 0.08% |
| **Latin Tokens** | 93,859 | 61.89% |

#### Language Distribution
```
Greek:                                 0.08%
Latin:  ██████████████████             61.89%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Qwen/Qwen3-0.6B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 151,643 | 100% |
| **Greek Tokens** | 127 | 0.08% |
| **Latin Tokens** | 93,859 | 61.89% |

#### Language Distribution
```
Greek:                                 0.08%
Latin:  ██████████████████             61.89%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Qwen/Qwen3-32B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 151,643 | 100% |
| **Greek Tokens** | 127 | 0.08% |
| **Latin Tokens** | 93,859 | 61.89% |

#### Language Distribution
```
Greek:                                 0.08%
Latin:  ██████████████████             61.89%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### Qwen/Qwen2.5-Omni-3B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 151,643 | 100% |
| **Greek Tokens** | 127 | 0.08% |
| **Latin Tokens** | 93,859 | 61.89% |

#### Language Distribution
```
Greek:                                 0.08%
Latin:  ██████████████████             61.89%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/gemma-2-2b-it

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 256,000 | 100% |
| **Greek Tokens** | 1,229 | 0.48% |
| **Latin Tokens** | 184,588 | 72.10% |

#### Language Distribution
```
Greek:                                 0.48%
Latin:  █████████████████████          72.10%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: ` τ`, `ου`, ` π`, ` κ`, ` σ`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/gemma-3-4b-it

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 262,144 | 100% |
| **Greek Tokens** | 1,409 | 0.54% |
| **Latin Tokens** | 151,739 | 57.88% |

#### Language Distribution
```
Greek:                                 0.54%
Latin:  █████████████████              57.88%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: ` τ`, `ου`, ` π`, ` σ`, ` κ`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### deepseek-ai/DeepSeek-V2.5-1210

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,000 | 100% |
| **Greek Tokens** | 86 | 0.09% |
| **Latin Tokens** | 70,489 | 70.49% |

#### Language Distribution
```
Greek:                                 0.09%
Latin:  █████████████████████          70.49%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `ι`, `τ`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/DeepSeek-R1

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 629 | 0.49% |
| **Latin Tokens** | 71,454 | 55.82% |

#### Language Distribution
```
Greek:                                 0.49%
Latin:  ████████████████               55.82%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `τ`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/DeepSeek-Prover-V2-671B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 629 | 0.49% |
| **Latin Tokens** | 71,454 | 55.82% |

#### Language Distribution
```
Greek:                                 0.49%
Latin:  ████████████████               55.82%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `τ`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### tngtech/DeepSeek-R1T-Chimera

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 629 | 0.49% |
| **Latin Tokens** | 71,454 | 55.82% |

#### Language Distribution
```
Greek:                                 0.49%
Latin:  ████████████████               55.82%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `τ`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### XiaomiMiMo/MiMo-7B-RL

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 151,643 | 100% |
| **Greek Tokens** | 127 | 0.08% |
| **Latin Tokens** | 93,859 | 61.89% |

#### Language Distribution
```
Greek:                                 0.08%
Latin:  ██████████████████             61.89%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Phi-3.5-mini-instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 32,000 | 100% |
| **Greek Tokens** | 63 | 0.20% |
| **Latin Tokens** | 25,624 | 80.08% |

#### Language Distribution
```
Greek:                                 0.20%
Latin:  ████████████████████████       80.08%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ος`, `α`, `ο`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### microsoft/phi-4

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,352 | 100% |
| **Greek Tokens** | 44 | 0.04% |
| **Latin Tokens** | 89,643 | 89.33% |

#### Language Distribution
```
Greek:                                 0.04%
Latin:  ██████████████████████████     89.33%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### microsoft/Phi-4-reasoning-plus

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 100,352 | 100% |
| **Greek Tokens** | 44 | 0.04% |
| **Latin Tokens** | 89,643 | 89.33% |

#### Language Distribution
```
Greek:                                 0.04%
Latin:  ██████████████████████████     89.33%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### microsoft/bitnet-b1.58-2B-4T

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 128,000 | 100% |
| **Greek Tokens** | 1,378 | 1.08% |
| **Latin Tokens** | 96,687 | 75.54% |

#### Language Distribution
```
Greek:                                 1.08%
Latin:  ██████████████████████         75.54%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### ibm-granite/granite-4.0-tiny-preview

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 49,152 | 100% |
| **Greek Tokens** | 42 | 0.09% |
| **Latin Tokens** | 40,302 | 81.99% |

#### Language Distribution
```
Greek:                                 0.09%
Latin:  ████████████████████████       81.99%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ν`, `ε`, `ο`, `ι`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### ibm-granite/granite-3.3-8b-instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Total Vocabulary** | 49,152 | 100% |
| **Greek Tokens** | 42 | 0.09% |
| **Latin Tokens** | 40,302 | 81.99% |

#### Language Distribution
```
Greek:                                 0.09%
Latin:  ████████████████████████       81.99%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ν`, `ε`, `ο`, `ι`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---


---
*Summary report generated on 2025-05-23 18:12:38 analyzing 29 models*