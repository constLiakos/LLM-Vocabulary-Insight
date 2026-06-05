# LLM Vocabulary Insight Report

[ℹ️ Project Info](README.dev.md)

## 🎯 Overview

This report presents a comprehensive analysis of Greek language tokenization capabilities across **50** Large Language Models (LLMs). The analysis evaluates how effectively different transformer-based models handle Greek text through their tokenizer vocabularies, providing insights into Greek language support, character coverage, and tokenization efficiency.

## Overall Statistics

| Metric | Value |
|--------|-------|
| **Total Models Analyzed** | 50 |
| **Combined Vocabulary Size** | 7,392,149 tokens |
| **Average Vocabulary Size** | 147,842 tokens |
| **Total Greek Tokens** | 105,595 (1.43%) |
| **Total Latin Tokens** | 4,758,538 (64.37%) |

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
🥇 **Most Tokens**: mlx-community/aya-expanse-32b-8bit - 173,699 tokens (68.12%)  
📉 **Fewest Tokens**: unsloth/mistral-7b-v0.3 - 25,723 tokens (78.50%)

#### By Percentage Coverage
🥇 **Highest %**: microsoft/phi-4 - 89.33% (89,643 tokens)  
📉 **Lowest %**: ilsp/Meltemi-7B-Instruct-v1.5 - 42.28% (25,948 tokens)

## Greek Performance Rankings

### By Token Count (Absolute Numbers)

| Rank | Model | Parameters | Greek Tokens | Total Vocabulary | Percentage |
|------|-------|------------|--------------|------------------|------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 28,162 | 61,366 | 45.89% |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 8B | 22,212 | 149,248 | 14.88% |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 32B | 7,547 | 255,000 | 2.96% |
| 4 | **1-800-LLMs/tiny-aya-earth** | 3B | 4,622 | 261,000 | 1.77% |
| 5 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 2,816 | 128,000 | 2.20% |
| 6 | **unsloth/Qwen3.5-27B** | 28B | 1,538 | 248,044 | 0.62% |
| 7 | **unsloth/Qwen3.5-122B-A10B** | 125B | 1,538 | 248,044 | 0.62% |
| 8 | **unsloth/Qwen3.6-35B-A3B** | 36B | 1,538 | 248,044 | 0.62% |
| 9 | **unsloth/Qwen3.6-27B** | 28B | 1,538 | 248,044 | 0.62% |
| 10 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 1,507 | 131,072 | 1.15% |
| 11 | **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 1,507 | 131,072 | 1.15% |
| 12 | **unsloth/Devstral-Small-2505** | 24B | 1,507 | 131,072 | 1.15% |
| 13 | **unsloth/Magistral-Small-2506** | 24B | 1,507 | 131,072 | 1.15% |
| 14 | **unsloth/Mistral-Medium-3.5-128B** | 128B | 1,507 | 131,072 | 1.15% |
| 15 | **unsloth/Mistral-Small-4-119B-2603** | 119B | 1,507 | 131,072 | 1.15% |
| 16 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 1,507 | 131,072 | 1.15% |
| 17 | **unsloth/gemma-3-27b-it** | 27B | 1,409 | 262,144 | 0.54% |
| 18 | **unsloth/gemma-4-12b-it** | 12B | 1,409 | 262,144 | 0.54% |
| 19 | **unsloth/gemma-4-12b** | 12B | 1,409 | 262,144 | 0.54% |
| 20 | **unsloth/gemma-4-E2B** | 5B | 1,409 | 262,144 | 0.54% |
| 21 | **unsloth/gemma-4-E4B** | 8B | 1,409 | 262,144 | 0.54% |
| 22 | **unsloth/gemma-4-31B** | 33B | 1,409 | 262,144 | 0.54% |
| 23 | **unsloth/Llama-3.2-3B-Instruct** | 3B | 1,378 | 128,000 | 1.08% |
| 24 | **unsloth/llama-3-8b** | 8B | 1,378 | 128,000 | 1.08% |
| 25 | **unsloth/Llama-3.3-70B-Instruct** | 71B | 1,378 | 128,000 | 1.08% |
| 26 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 1,378 | 128,000 | 1.08% |
| 27 | **microsoft/bitnet-b1.58-2B-4T** | 1B | 1,378 | 128,000 | 1.08% |
| 28 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 1,378 | 128,000 | 1.08% |
| 29 | **HuggingFaceTB/SmolLM3-3B** | 3B | 1,378 | 128,000 | 1.08% |
| 30 | **THUDM/GLM-4.1V-9B-Thinking** | 10B | 832 | 151,329 | 0.55% |
| 31 | **unsloth/Step-3.7-Flash** | 201B | 629 | 128,000 | 0.49% |
| 32 | **unsloth/DeepSeek-R1** | 684B | 629 | 128,000 | 0.49% |
| 33 | **unsloth/DeepSeek-R1-0528** | N/A | 629 | 128,000 | 0.49% |
| 34 | **unsloth/DeepSeek-Prover-V2-671B** | 671B | 629 | 128,000 | 0.49% |
| 35 | **tngtech/DeepSeek-R1T-Chimera** | 685B | 629 | 128,000 | 0.49% |
| 36 | **unsloth/LFM2.5-8B-A1B** | 8B | 430 | 124,893 | 0.34% |
| 37 | **openbmb/MiniCPM4-8B** | 8B | 143 | 73,440 | 0.19% |
| 38 | **Qwen/Qwen3-32B** | 33B | 127 | 151,643 | 0.08% |
| 39 | **Qwen/Qwen3-235B-A22B** | 235B | 127 | 151,643 | 0.08% |
| 40 | **Qwen/Qwen2.5-Omni-3B** | 6B | 127 | 151,643 | 0.08% |
| 41 | **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 86 | 100,000 | 0.09% |
| 42 | **unsloth/mistral-7b-v0.3** | 7B | 58 | 32,768 | 0.18% |
| 43 | **unsloth/Mistral-Small-Instruct-2409** | 22B | 58 | 32,768 | 0.18% |
| 44 | **microsoft/phi-4** | 15B | 44 | 100,352 | 0.04% |
| 45 | **unsloth/granite-4.1-30b** | 29B | 44 | 100,352 | 0.04% |
| 46 | **unsloth/granite-4.1-8b** | 9B | 44 | 100,352 | 0.04% |
| 47 | **unsloth/granite-4.1-30b** | 29B | 44 | 100,352 | 0.04% |
| 48 | **ibm-granite/granite-4.0-tiny-preview** | 7B | 42 | 49,152 | 0.09% |
| 49 | **ibm-granite/granite-3.3-8b-instruct** | 8B | 42 | 49,152 | 0.09% |
| 50 | **ibm-granite/granite-speech-3.3-8b** | 9B | 42 | 49,152 | 0.09% |


### By Percentage (Relative Performance)

| Rank | Model | Parameters | Percentage | Greek Tokens | Total Vocabulary |
|------|-------|------------|------------|--------------|------------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 45.89% | 28,162 | 61,366 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 8B | 14.88% | 22,212 | 149,248 |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 32B | 2.96% | 7,547 | 255,000 |
| 4 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 2.20% | 2,816 | 128,000 |
| 5 | **1-800-LLMs/tiny-aya-earth** | 3B | 1.77% | 4,622 | 261,000 |
| 6 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 1.15% | 1,507 | 131,072 |
| 7 | **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 1.15% | 1,507 | 131,072 |
| 8 | **unsloth/Devstral-Small-2505** | 24B | 1.15% | 1,507 | 131,072 |
| 9 | **unsloth/Magistral-Small-2506** | 24B | 1.15% | 1,507 | 131,072 |
| 10 | **unsloth/Mistral-Medium-3.5-128B** | 128B | 1.15% | 1,507 | 131,072 |
| 11 | **unsloth/Mistral-Small-4-119B-2603** | 119B | 1.15% | 1,507 | 131,072 |
| 12 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 1.15% | 1,507 | 131,072 |
| 13 | **unsloth/Llama-3.2-3B-Instruct** | 3B | 1.08% | 1,378 | 128,000 |
| 14 | **unsloth/llama-3-8b** | 8B | 1.08% | 1,378 | 128,000 |
| 15 | **unsloth/Llama-3.3-70B-Instruct** | 71B | 1.08% | 1,378 | 128,000 |
| 16 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 1.08% | 1,378 | 128,000 |
| 17 | **microsoft/bitnet-b1.58-2B-4T** | 1B | 1.08% | 1,378 | 128,000 |
| 18 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 1.08% | 1,378 | 128,000 |
| 19 | **HuggingFaceTB/SmolLM3-3B** | 3B | 1.08% | 1,378 | 128,000 |
| 20 | **unsloth/Qwen3.5-27B** | 28B | 0.62% | 1,538 | 248,044 |
| 21 | **unsloth/Qwen3.5-122B-A10B** | 125B | 0.62% | 1,538 | 248,044 |
| 22 | **unsloth/Qwen3.6-35B-A3B** | 36B | 0.62% | 1,538 | 248,044 |
| 23 | **unsloth/Qwen3.6-27B** | 28B | 0.62% | 1,538 | 248,044 |
| 24 | **THUDM/GLM-4.1V-9B-Thinking** | 10B | 0.55% | 832 | 151,329 |
| 25 | **unsloth/gemma-3-27b-it** | 27B | 0.54% | 1,409 | 262,144 |
| 26 | **unsloth/gemma-4-12b-it** | 12B | 0.54% | 1,409 | 262,144 |
| 27 | **unsloth/gemma-4-12b** | 12B | 0.54% | 1,409 | 262,144 |
| 28 | **unsloth/gemma-4-E2B** | 5B | 0.54% | 1,409 | 262,144 |
| 29 | **unsloth/gemma-4-E4B** | 8B | 0.54% | 1,409 | 262,144 |
| 30 | **unsloth/gemma-4-31B** | 33B | 0.54% | 1,409 | 262,144 |
| 31 | **unsloth/Step-3.7-Flash** | 201B | 0.49% | 629 | 128,000 |
| 32 | **unsloth/DeepSeek-R1** | 684B | 0.49% | 629 | 128,000 |
| 33 | **unsloth/DeepSeek-R1-0528** | N/A | 0.49% | 629 | 128,000 |
| 34 | **unsloth/DeepSeek-Prover-V2-671B** | 671B | 0.49% | 629 | 128,000 |
| 35 | **tngtech/DeepSeek-R1T-Chimera** | 685B | 0.49% | 629 | 128,000 |
| 36 | **unsloth/LFM2.5-8B-A1B** | 8B | 0.34% | 430 | 124,893 |
| 37 | **openbmb/MiniCPM4-8B** | 8B | 0.19% | 143 | 73,440 |
| 38 | **unsloth/mistral-7b-v0.3** | 7B | 0.18% | 58 | 32,768 |
| 39 | **unsloth/Mistral-Small-Instruct-2409** | 22B | 0.18% | 58 | 32,768 |
| 40 | **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 0.09% | 86 | 100,000 |
| 41 | **ibm-granite/granite-4.0-tiny-preview** | 7B | 0.09% | 42 | 49,152 |
| 42 | **ibm-granite/granite-3.3-8b-instruct** | 8B | 0.09% | 42 | 49,152 |
| 43 | **ibm-granite/granite-speech-3.3-8b** | 9B | 0.09% | 42 | 49,152 |
| 44 | **Qwen/Qwen3-32B** | 33B | 0.08% | 127 | 151,643 |
| 45 | **Qwen/Qwen3-235B-A22B** | 235B | 0.08% | 127 | 151,643 |
| 46 | **Qwen/Qwen2.5-Omni-3B** | 6B | 0.08% | 127 | 151,643 |
| 47 | **microsoft/phi-4** | 15B | 0.04% | 44 | 100,352 |
| 48 | **unsloth/granite-4.1-30b** | 29B | 0.04% | 44 | 100,352 |
| 49 | **unsloth/granite-4.1-8b** | 9B | 0.04% | 44 | 100,352 |
| 50 | **unsloth/granite-4.1-30b** | 29B | 0.04% | 44 | 100,352 |


## Latin Performance Rankings

### By Token Count (Absolute Numbers)

| Rank | Model | Parameters | Latin Tokens | Total Vocabulary | Percentage |
|------|-------|------------|--------------|------------------|------------|
| 1 | **mlx-community/aya-expanse-32b-8bit** | 32B | 173,699 | 255,000 | 68.12% |
| 2 | **1-800-LLMs/tiny-aya-earth** | 3B | 153,473 | 261,000 | 58.80% |
| 3 | **unsloth/gemma-3-27b-it** | 27B | 151,739 | 262,144 | 57.88% |
| 4 | **unsloth/gemma-4-12b-it** | 12B | 151,739 | 262,144 | 57.88% |
| 5 | **unsloth/gemma-4-12b** | 12B | 151,739 | 262,144 | 57.88% |
| 6 | **unsloth/gemma-4-E2B** | 5B | 151,739 | 262,144 | 57.88% |
| 7 | **unsloth/gemma-4-E4B** | 8B | 151,739 | 262,144 | 57.88% |
| 8 | **unsloth/gemma-4-31B** | 33B | 151,739 | 262,144 | 57.88% |
| 9 | **unsloth/Qwen3.5-27B** | 28B | 137,780 | 248,044 | 55.55% |
| 10 | **unsloth/Qwen3.5-122B-A10B** | 125B | 137,780 | 248,044 | 55.55% |
| 11 | **unsloth/Qwen3.6-35B-A3B** | 36B | 137,780 | 248,044 | 55.55% |
| 12 | **unsloth/Qwen3.6-27B** | 28B | 137,780 | 248,044 | 55.55% |
| 13 | **THUDM/GLM-4.1V-9B-Thinking** | 10B | 100,326 | 151,329 | 66.30% |
| 14 | **ilsp/Llama-Krikri-8B-Instruct** | 8B | 96,699 | 149,248 | 64.79% |
| 15 | **unsloth/Llama-3.2-3B-Instruct** | 3B | 96,687 | 128,000 | 75.54% |
| 16 | **unsloth/llama-3-8b** | 8B | 96,687 | 128,000 | 75.54% |
| 17 | **unsloth/Llama-3.3-70B-Instruct** | 71B | 96,687 | 128,000 | 75.54% |
| 18 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 96,687 | 128,000 | 75.54% |
| 19 | **microsoft/bitnet-b1.58-2B-4T** | 1B | 96,687 | 128,000 | 75.54% |
| 20 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 96,687 | 128,000 | 75.54% |
| 21 | **HuggingFaceTB/SmolLM3-3B** | 3B | 96,687 | 128,000 | 75.54% |
| 22 | **Qwen/Qwen3-32B** | 33B | 93,859 | 151,643 | 61.89% |
| 23 | **Qwen/Qwen3-235B-A22B** | 235B | 93,859 | 151,643 | 61.89% |
| 24 | **Qwen/Qwen2.5-Omni-3B** | 6B | 93,859 | 151,643 | 61.89% |
| 25 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 91,179 | 128,000 | 71.23% |
| 26 | **microsoft/phi-4** | 15B | 89,643 | 100,352 | 89.33% |
| 27 | **unsloth/granite-4.1-30b** | 29B | 89,643 | 100,352 | 89.33% |
| 28 | **unsloth/granite-4.1-8b** | 9B | 89,643 | 100,352 | 89.33% |
| 29 | **unsloth/granite-4.1-30b** | 29B | 89,643 | 100,352 | 89.33% |
| 30 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 87,986 | 131,072 | 67.13% |
| 31 | **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 87,986 | 131,072 | 67.13% |
| 32 | **unsloth/Devstral-Small-2505** | 24B | 87,986 | 131,072 | 67.13% |
| 33 | **unsloth/Magistral-Small-2506** | 24B | 87,986 | 131,072 | 67.13% |
| 34 | **unsloth/Mistral-Medium-3.5-128B** | 128B | 87,986 | 131,072 | 67.13% |
| 35 | **unsloth/Mistral-Small-4-119B-2603** | 119B | 87,986 | 131,072 | 67.13% |
| 36 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 87,986 | 131,072 | 67.13% |
| 37 | **unsloth/LFM2.5-8B-A1B** | 8B | 86,283 | 124,893 | 69.09% |
| 38 | **unsloth/Step-3.7-Flash** | 201B | 71,454 | 128,000 | 55.82% |
| 39 | **unsloth/DeepSeek-R1** | 684B | 71,454 | 128,000 | 55.82% |
| 40 | **unsloth/DeepSeek-R1-0528** | N/A | 71,454 | 128,000 | 55.82% |
| 41 | **unsloth/DeepSeek-Prover-V2-671B** | 671B | 71,454 | 128,000 | 55.82% |
| 42 | **tngtech/DeepSeek-R1T-Chimera** | 685B | 71,454 | 128,000 | 55.82% |
| 43 | **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 70,489 | 100,000 | 70.49% |
| 44 | **ibm-granite/granite-4.0-tiny-preview** | 7B | 40,302 | 49,152 | 81.99% |
| 45 | **ibm-granite/granite-3.3-8b-instruct** | 8B | 40,302 | 49,152 | 81.99% |
| 46 | **ibm-granite/granite-speech-3.3-8b** | 9B | 40,302 | 49,152 | 81.99% |
| 47 | **openbmb/MiniCPM4-8B** | 8B | 36,406 | 73,440 | 49.57% |
| 48 | **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 25,948 | 61,366 | 42.28% |
| 49 | **unsloth/mistral-7b-v0.3** | 7B | 25,723 | 32,768 | 78.50% |
| 50 | **unsloth/Mistral-Small-Instruct-2409** | 22B | 25,723 | 32,768 | 78.50% |


### By Percentage (Relative Performance)

| Rank | Model | Parameters | Percentage | Latin Tokens | Total Vocabulary |
|------|-------|------------|------------|--------------|------------------|
| 1 | **microsoft/phi-4** | 15B | 89.33% | 89,643 | 100,352 |
| 2 | **unsloth/granite-4.1-30b** | 29B | 89.33% | 89,643 | 100,352 |
| 3 | **unsloth/granite-4.1-8b** | 9B | 89.33% | 89,643 | 100,352 |
| 4 | **unsloth/granite-4.1-30b** | 29B | 89.33% | 89,643 | 100,352 |
| 5 | **ibm-granite/granite-4.0-tiny-preview** | 7B | 81.99% | 40,302 | 49,152 |
| 6 | **ibm-granite/granite-3.3-8b-instruct** | 8B | 81.99% | 40,302 | 49,152 |
| 7 | **ibm-granite/granite-speech-3.3-8b** | 9B | 81.99% | 40,302 | 49,152 |
| 8 | **unsloth/mistral-7b-v0.3** | 7B | 78.50% | 25,723 | 32,768 |
| 9 | **unsloth/Mistral-Small-Instruct-2409** | 22B | 78.50% | 25,723 | 32,768 |
| 10 | **unsloth/Llama-3.2-3B-Instruct** | 3B | 75.54% | 96,687 | 128,000 |
| 11 | **unsloth/llama-3-8b** | 8B | 75.54% | 96,687 | 128,000 |
| 12 | **unsloth/Llama-3.3-70B-Instruct** | 71B | 75.54% | 96,687 | 128,000 |
| 13 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 75.54% | 96,687 | 128,000 |
| 14 | **microsoft/bitnet-b1.58-2B-4T** | 1B | 75.54% | 96,687 | 128,000 |
| 15 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 75.54% | 96,687 | 128,000 |
| 16 | **HuggingFaceTB/SmolLM3-3B** | 3B | 75.54% | 96,687 | 128,000 |
| 17 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 71.23% | 91,179 | 128,000 |
| 18 | **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 70.49% | 70,489 | 100,000 |
| 19 | **unsloth/LFM2.5-8B-A1B** | 8B | 69.09% | 86,283 | 124,893 |
| 20 | **mlx-community/aya-expanse-32b-8bit** | 32B | 68.12% | 173,699 | 255,000 |
| 21 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 67.13% | 87,986 | 131,072 |
| 22 | **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 67.13% | 87,986 | 131,072 |
| 23 | **unsloth/Devstral-Small-2505** | 24B | 67.13% | 87,986 | 131,072 |
| 24 | **unsloth/Magistral-Small-2506** | 24B | 67.13% | 87,986 | 131,072 |
| 25 | **unsloth/Mistral-Medium-3.5-128B** | 128B | 67.13% | 87,986 | 131,072 |
| 26 | **unsloth/Mistral-Small-4-119B-2603** | 119B | 67.13% | 87,986 | 131,072 |
| 27 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 67.13% | 87,986 | 131,072 |
| 28 | **THUDM/GLM-4.1V-9B-Thinking** | 10B | 66.30% | 100,326 | 151,329 |
| 29 | **ilsp/Llama-Krikri-8B-Instruct** | 8B | 64.79% | 96,699 | 149,248 |
| 30 | **Qwen/Qwen3-32B** | 33B | 61.89% | 93,859 | 151,643 |
| 31 | **Qwen/Qwen3-235B-A22B** | 235B | 61.89% | 93,859 | 151,643 |
| 32 | **Qwen/Qwen2.5-Omni-3B** | 6B | 61.89% | 93,859 | 151,643 |
| 33 | **1-800-LLMs/tiny-aya-earth** | 3B | 58.80% | 153,473 | 261,000 |
| 34 | **unsloth/gemma-3-27b-it** | 27B | 57.88% | 151,739 | 262,144 |
| 35 | **unsloth/gemma-4-12b-it** | 12B | 57.88% | 151,739 | 262,144 |
| 36 | **unsloth/gemma-4-12b** | 12B | 57.88% | 151,739 | 262,144 |
| 37 | **unsloth/gemma-4-E2B** | 5B | 57.88% | 151,739 | 262,144 |
| 38 | **unsloth/gemma-4-E4B** | 8B | 57.88% | 151,739 | 262,144 |
| 39 | **unsloth/gemma-4-31B** | 33B | 57.88% | 151,739 | 262,144 |
| 40 | **unsloth/Step-3.7-Flash** | 201B | 55.82% | 71,454 | 128,000 |
| 41 | **unsloth/DeepSeek-R1** | 684B | 55.82% | 71,454 | 128,000 |
| 42 | **unsloth/DeepSeek-R1-0528** | N/A | 55.82% | 71,454 | 128,000 |
| 43 | **unsloth/DeepSeek-Prover-V2-671B** | 671B | 55.82% | 71,454 | 128,000 |
| 44 | **tngtech/DeepSeek-R1T-Chimera** | 685B | 55.82% | 71,454 | 128,000 |
| 45 | **unsloth/Qwen3.5-27B** | 28B | 55.55% | 137,780 | 248,044 |
| 46 | **unsloth/Qwen3.5-122B-A10B** | 125B | 55.55% | 137,780 | 248,044 |
| 47 | **unsloth/Qwen3.6-35B-A3B** | 36B | 55.55% | 137,780 | 248,044 |
| 48 | **unsloth/Qwen3.6-27B** | 28B | 55.55% | 137,780 | 248,044 |
| 49 | **openbmb/MiniCPM4-8B** | 8B | 49.57% | 36,406 | 73,440 |
| 50 | **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 42.28% | 25,948 | 61,366 |


## Comparative Analysis

### Vocabulary Size Distribution

| Model | Parameters | Total Vocabulary | Visual Scale | Relative Size |
|-------|------------|------------------|--------------|---------------|
| **unsloth/gemma-3-27b-it** | 27B | 262,144 |  | 177.3% of avg |
| **unsloth/gemma-4-12b-it** | 12B | 262,144 |  | 177.3% of avg |
| **unsloth/gemma-4-12b** | 12B | 262,144 |  | 177.3% of avg |
| **unsloth/gemma-4-E2B** | 5B | 262,144 |  | 177.3% of avg |
| **unsloth/gemma-4-E4B** | 8B | 262,144 |  | 177.3% of avg |
| **unsloth/gemma-4-31B** | 33B | 262,144 |  | 177.3% of avg |
| **1-800-LLMs/tiny-aya-earth** | 3B | 261,000 |  | 176.5% of avg |
| **mlx-community/aya-expanse-32b-8bit** | 32B | 255,000 |  | 172.5% of avg |
| **unsloth/Qwen3.5-27B** | 28B | 248,044 |  | 167.8% of avg |
| **unsloth/Qwen3.5-122B-A10B** | 125B | 248,044 |  | 167.8% of avg |
| **unsloth/Qwen3.6-35B-A3B** | 36B | 248,044 |  | 167.8% of avg |
| **unsloth/Qwen3.6-27B** | 28B | 248,044 |  | 167.8% of avg |
| **Qwen/Qwen3-32B** | 33B | 151,643 |  | 102.6% of avg |
| **Qwen/Qwen3-235B-A22B** | 235B | 151,643 |  | 102.6% of avg |
| **Qwen/Qwen2.5-Omni-3B** | 6B | 151,643 |  | 102.6% of avg |
| **THUDM/GLM-4.1V-9B-Thinking** | 10B | 151,329 |  | 102.4% of avg |
| **ilsp/Llama-Krikri-8B-Instruct** | 8B | 149,248 |  | 101.0% of avg |
| **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 131,072 |  | 88.7% of avg |
| **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 131,072 |  | 88.7% of avg |
| **unsloth/Devstral-Small-2505** | 24B | 131,072 |  | 88.7% of avg |
| **unsloth/Magistral-Small-2506** | 24B | 131,072 |  | 88.7% of avg |
| **unsloth/Mistral-Medium-3.5-128B** | 128B | 131,072 |  | 88.7% of avg |
| **unsloth/Mistral-Small-4-119B-2603** | 119B | 131,072 |  | 88.7% of avg |
| **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 131,072 |  | 88.7% of avg |
| **unsloth/Llama-3.2-3B-Instruct** | 3B | 128,000 |  | 86.6% of avg |
| **unsloth/llama-3-8b** | 8B | 128,000 |  | 86.6% of avg |
| **unsloth/Llama-3.3-70B-Instruct** | 71B | 128,000 |  | 86.6% of avg |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 128,000 |  | 86.6% of avg |
| **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 128,000 |  | 86.6% of avg |
| **unsloth/Step-3.7-Flash** | 201B | 128,000 |  | 86.6% of avg |
| **unsloth/DeepSeek-R1** | 684B | 128,000 |  | 86.6% of avg |
| **unsloth/DeepSeek-R1-0528** | N/A | 128,000 |  | 86.6% of avg |
| **unsloth/DeepSeek-Prover-V2-671B** | 671B | 128,000 |  | 86.6% of avg |
| **tngtech/DeepSeek-R1T-Chimera** | 685B | 128,000 |  | 86.6% of avg |
| **microsoft/bitnet-b1.58-2B-4T** | 1B | 128,000 |  | 86.6% of avg |
| **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 128,000 |  | 86.6% of avg |
| **HuggingFaceTB/SmolLM3-3B** | 3B | 128,000 |  | 86.6% of avg |
| **unsloth/LFM2.5-8B-A1B** | 8B | 124,893 |  | 84.5% of avg |
| **microsoft/phi-4** | 15B | 100,352 |  | 67.9% of avg |
| **unsloth/granite-4.1-30b** | 29B | 100,352 |  | 67.9% of avg |
| **unsloth/granite-4.1-8b** | 9B | 100,352 |  | 67.9% of avg |
| **unsloth/granite-4.1-30b** | 29B | 100,352 |  | 67.9% of avg |
| **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 100,000 |  | 67.6% of avg |
| **openbmb/MiniCPM4-8B** | 8B | 73,440 |  | 49.7% of avg |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 61,366 |  | 41.5% of avg |
| **ibm-granite/granite-4.0-tiny-preview** | 7B | 49,152 |  | 33.2% of avg |
| **ibm-granite/granite-3.3-8b-instruct** | 8B | 49,152 |  | 33.2% of avg |
| **ibm-granite/granite-speech-3.3-8b** | 9B | 49,152 |  | 33.2% of avg |
| **unsloth/mistral-7b-v0.3** | 7B | 32,768 |  | 22.2% of avg |
| **unsloth/Mistral-Small-Instruct-2409** | 22B | 32,768 |  | 22.2% of avg |


### Greek Support Comparison

| Rank | Model | Greek Percentage | Greek Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 45.89% | 28,162 | 🟩🟩🟩🟩🟩 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 14.88% | 22,212 | 🟩🟩🟩🟩🟩 |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 2.96% | 7,547 | 🟩🟩🟩🟩🟩 |
| 4 | **1-800-LLMs/tiny-aya-earth** | 1.77% | 4,622 | 🟩🟩🟩🟩🟩 |
| 5 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2.20% | 2,816 | 🟩🟩🟩🟩🟩 |
| 6 | **unsloth/Qwen3.5-27B** | 0.62% | 1,538 | 🟩🟩🟩⬜⬜ |
| 7 | **unsloth/Qwen3.5-122B-A10B** | 0.62% | 1,538 | 🟩🟩🟩⬜⬜ |
| 8 | **unsloth/Qwen3.6-35B-A3B** | 0.62% | 1,538 | 🟩🟩🟩⬜⬜ |
| 9 | **unsloth/Qwen3.6-27B** | 0.62% | 1,538 | 🟩🟩🟩⬜⬜ |
| 10 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 11 | **unsloth/Nemotron-3-Nano-30B-A3B** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 12 | **unsloth/Devstral-Small-2505** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 13 | **unsloth/Magistral-Small-2506** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 14 | **unsloth/Mistral-Medium-3.5-128B** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 15 | **unsloth/Mistral-Small-4-119B-2603** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 16 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 17 | **unsloth/gemma-3-27b-it** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 18 | **unsloth/gemma-4-12b-it** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 19 | **unsloth/gemma-4-12b** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 20 | **unsloth/gemma-4-E2B** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 21 | **unsloth/gemma-4-E4B** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 22 | **unsloth/gemma-4-31B** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 23 | **unsloth/Llama-3.2-3B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 24 | **unsloth/llama-3-8b** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 25 | **unsloth/Llama-3.3-70B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 26 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 27 | **microsoft/bitnet-b1.58-2B-4T** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 28 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 29 | **HuggingFaceTB/SmolLM3-3B** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 30 | **THUDM/GLM-4.1V-9B-Thinking** | 0.55% | 832 | 🟩⬜⬜⬜⬜ |
| 31 | **unsloth/Step-3.7-Flash** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 32 | **unsloth/DeepSeek-R1** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 33 | **unsloth/DeepSeek-R1-0528** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 34 | **unsloth/DeepSeek-Prover-V2-671B** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 35 | **tngtech/DeepSeek-R1T-Chimera** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 36 | **unsloth/LFM2.5-8B-A1B** | 0.34% | 430 | ⬜⬜⬜⬜⬜ |
| 37 | **openbmb/MiniCPM4-8B** | 0.19% | 143 | ⬜⬜⬜⬜⬜ |
| 38 | **Qwen/Qwen3-32B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 39 | **Qwen/Qwen3-235B-A22B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 40 | **Qwen/Qwen2.5-Omni-3B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 41 | **deepseek-ai/DeepSeek-V2.5-1210** | 0.09% | 86 | ⬜⬜⬜⬜⬜ |
| 42 | **unsloth/mistral-7b-v0.3** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 43 | **unsloth/Mistral-Small-Instruct-2409** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 44 | **microsoft/phi-4** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 45 | **unsloth/granite-4.1-30b** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 46 | **unsloth/granite-4.1-8b** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 47 | **unsloth/granite-4.1-30b** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 48 | **ibm-granite/granite-4.0-tiny-preview** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |
| 49 | **ibm-granite/granite-3.3-8b-instruct** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |
| 50 | **ibm-granite/granite-speech-3.3-8b** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |


### Latin Support Comparison

| Rank | Model | Latin Percentage | Latin Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **mlx-community/aya-expanse-32b-8bit** | 68.12% | 173,699 | 🟦🟦🟦🟦🟦 |
| 2 | **1-800-LLMs/tiny-aya-earth** | 58.80% | 153,473 | 🟦🟦🟦🟦🟦 |
| 3 | **unsloth/gemma-3-27b-it** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 4 | **unsloth/gemma-4-12b-it** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 5 | **unsloth/gemma-4-12b** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 6 | **unsloth/gemma-4-E2B** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 7 | **unsloth/gemma-4-E4B** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 8 | **unsloth/gemma-4-31B** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 9 | **unsloth/Qwen3.5-27B** | 55.55% | 137,780 | 🟦🟦🟦🟦🟦 |
| 10 | **unsloth/Qwen3.5-122B-A10B** | 55.55% | 137,780 | 🟦🟦🟦🟦🟦 |
| 11 | **unsloth/Qwen3.6-35B-A3B** | 55.55% | 137,780 | 🟦🟦🟦🟦🟦 |
| 12 | **unsloth/Qwen3.6-27B** | 55.55% | 137,780 | 🟦🟦🟦🟦🟦 |
| 13 | **THUDM/GLM-4.1V-9B-Thinking** | 66.30% | 100,326 | 🟦🟦🟦🟦🟦 |
| 14 | **ilsp/Llama-Krikri-8B-Instruct** | 64.79% | 96,699 | 🟦🟦🟦🟦🟦 |
| 15 | **unsloth/Llama-3.2-3B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 16 | **unsloth/llama-3-8b** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 17 | **unsloth/Llama-3.3-70B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 18 | **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 19 | **microsoft/bitnet-b1.58-2B-4T** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 20 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 21 | **HuggingFaceTB/SmolLM3-3B** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 22 | **Qwen/Qwen3-32B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 23 | **Qwen/Qwen3-235B-A22B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 24 | **Qwen/Qwen2.5-Omni-3B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 25 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 71.23% | 91,179 | 🟦🟦🟦🟦🟦 |
| 26 | **microsoft/phi-4** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 27 | **unsloth/granite-4.1-30b** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 28 | **unsloth/granite-4.1-8b** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 29 | **unsloth/granite-4.1-30b** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 30 | **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 31 | **unsloth/Nemotron-3-Nano-30B-A3B** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 32 | **unsloth/Devstral-Small-2505** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 33 | **unsloth/Magistral-Small-2506** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 34 | **unsloth/Mistral-Medium-3.5-128B** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 35 | **unsloth/Mistral-Small-4-119B-2603** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 36 | **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 37 | **unsloth/LFM2.5-8B-A1B** | 69.09% | 86,283 | 🟦🟦🟦🟦🟦 |
| 38 | **unsloth/Step-3.7-Flash** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 39 | **unsloth/DeepSeek-R1** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 40 | **unsloth/DeepSeek-R1-0528** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 41 | **unsloth/DeepSeek-Prover-V2-671B** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 42 | **tngtech/DeepSeek-R1T-Chimera** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 43 | **deepseek-ai/DeepSeek-V2.5-1210** | 70.49% | 70,489 | 🟦🟦🟦🟦🟦 |
| 44 | **ibm-granite/granite-4.0-tiny-preview** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 45 | **ibm-granite/granite-3.3-8b-instruct** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 46 | **ibm-granite/granite-speech-3.3-8b** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 47 | **openbmb/MiniCPM4-8B** | 49.57% | 36,406 | 🟦🟦🟦🟦🟦 |
| 48 | **ilsp/Meltemi-7B-Instruct-v1.5** | 42.28% | 25,948 | 🟦🟦🟦🟦🟦 |
| 49 | **unsloth/mistral-7b-v0.3** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |
| 50 | **unsloth/Mistral-Small-Instruct-2409** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |


### Cross-Language Performance Matrix

| Model | Parameters | Total Vocab | Greek % | Greek Tokens | Latin % | Latin Tokens | Greek/Latin Ratio |
|-------|------------|-------------|---------|--------------|---------|--------------|-------------------|
| **unsloth/Llama-3.2-3B-Instruct** | 3B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/llama-3-8b** | 8B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/Llama-3.3-70B-Instruct** | 71B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 9B | 128,000 | 2.20% | 2,816 | 71.23% | 91,179 | 0.03 |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 7B | 61,366 | 45.89% | 28,162 | 42.28% | 25,948 | 1.09 |
| **ilsp/Llama-Krikri-8B-Instruct** | 8B | 149,248 | 14.88% | 22,212 | 64.79% | 96,699 | 0.23 |
| **Qwen/Qwen3-32B** | 33B | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen3-235B-A22B** | 235B | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen2.5-Omni-3B** | 6B | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **unsloth/Qwen3.5-27B** | 28B | 248,044 | 0.62% | 1,538 | 55.55% | 137,780 | 0.01 |
| **unsloth/Qwen3.5-122B-A10B** | 125B | 248,044 | 0.62% | 1,538 | 55.55% | 137,780 | 0.01 |
| **unsloth/Qwen3.6-35B-A3B** | 36B | 248,044 | 0.62% | 1,538 | 55.55% | 137,780 | 0.01 |
| **unsloth/Qwen3.6-27B** | 28B | 248,044 | 0.62% | 1,538 | 55.55% | 137,780 | 0.01 |
| **unsloth/Llama-3.1-Nemotron-Nano-8B-v1** | 8B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/NVIDIA-Nemotron-3-Nano-4B** | 4B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/Nemotron-3-Nano-30B-A3B** | 32B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/gemma-3-27b-it** | 27B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/gemma-4-12b-it** | 12B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/gemma-4-12b** | 12B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/gemma-4-E2B** | 5B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/gemma-4-E4B** | 8B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/gemma-4-31B** | 33B | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **unsloth/Step-3.7-Flash** | 201B | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **deepseek-ai/DeepSeek-V2.5-1210** | 236B | 100,000 | 0.09% | 86 | 70.49% | 70,489 | 0.00 |
| **unsloth/DeepSeek-R1** | 684B | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **unsloth/DeepSeek-R1-0528** | N/A | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **unsloth/DeepSeek-Prover-V2-671B** | 671B | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **tngtech/DeepSeek-R1T-Chimera** | 685B | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **microsoft/phi-4** | 15B | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **microsoft/bitnet-b1.58-2B-4T** | 1B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **ibm-granite/granite-4.0-tiny-preview** | 7B | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **ibm-granite/granite-3.3-8b-instruct** | 8B | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **ibm-granite/granite-speech-3.3-8b** | 9B | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **mlx-community/aya-expanse-32b-8bit** | 32B | 255,000 | 2.96% | 7,547 | 68.12% | 173,699 | 0.04 |
| **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 9B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **openbmb/MiniCPM4-8B** | 8B | 73,440 | 0.19% | 143 | 49.57% | 36,406 | 0.00 |
| **unsloth/Devstral-Small-2505** | 24B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/Magistral-Small-2506** | 24B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/mistral-7b-v0.3** | 7B | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |
| **unsloth/Mistral-Small-Instruct-2409** | 22B | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |
| **unsloth/Mistral-Medium-3.5-128B** | 128B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/Mistral-Small-4-119B-2603** | 119B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/Mistral-Small-3.2-24B-Instruct-2506** | 24B | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/granite-4.1-30b** | 29B | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **HuggingFaceTB/SmolLM3-3B** | 3B | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **THUDM/GLM-4.1V-9B-Thinking** | 10B | 151,329 | 0.55% | 832 | 66.30% | 100,326 | 0.01 |
| **unsloth/LFM2.5-8B-A1B** | 8B | 124,893 | 0.34% | 430 | 69.09% | 86,283 | 0.00 |
| **unsloth/granite-4.1-8b** | 9B | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **unsloth/granite-4.1-30b** | 29B | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **1-800-LLMs/tiny-aya-earth** | 3B | 261,000 | 1.77% | 4,622 | 58.80% | 153,473 | 0.03 |


### Performance Categories

| High Greek Support (>1%) | Medium Greek Support (0.1-1%) | Low Greek Support (<0.1%) |
|---------------------------|--------------------------------|---------------------------|
| unsloth/Llama-3.2-3B-Instruct (1.08%) | unsloth/Qwen3.5-27B (0.62%) | Qwen/Qwen3-32B (0.08%) |
| unsloth/llama-3-8b (1.08%) | unsloth/Qwen3.5-122B-A10B (0.62%) | Qwen/Qwen3-235B-A22B (0.08%) |
| unsloth/Llama-3.3-70B-Instruct (1.08%) | unsloth/Qwen3.6-35B-A3B (0.62%) | Qwen/Qwen2.5-Omni-3B (0.08%) |
| kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit (2.20%) | unsloth/Qwen3.6-27B (0.62%) | deepseek-ai/DeepSeek-V2.5-1210 (0.09%) |
| ilsp/Meltemi-7B-Instruct-v1.5 (45.89%) | unsloth/gemma-3-27b-it (0.54%) | microsoft/phi-4 (0.04%) |
| ilsp/Llama-Krikri-8B-Instruct (14.88%) | unsloth/gemma-4-12b-it (0.54%) | ibm-granite/granite-4.0-tiny-preview (0.09%) |
| unsloth/Llama-3.1-Nemotron-Nano-8B-v1 (1.08%) | unsloth/gemma-4-12b (0.54%) | ibm-granite/granite-3.3-8b-instruct (0.09%) |
| unsloth/NVIDIA-Nemotron-3-Nano-4B (1.15%) | unsloth/gemma-4-E2B (0.54%) | ibm-granite/granite-speech-3.3-8b (0.09%) |
| unsloth/Nemotron-3-Nano-30B-A3B (1.15%) | unsloth/gemma-4-E4B (0.54%) | unsloth/granite-4.1-30b (0.04%) |
| microsoft/bitnet-b1.58-2B-4T (1.08%) | unsloth/gemma-4-31B (0.54%) | unsloth/granite-4.1-8b (0.04%) |
| mlx-community/aya-expanse-32b-8bit (2.96%) | unsloth/Step-3.7-Flash (0.49%) | unsloth/granite-4.1-30b (0.04%) |
| nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1 (1.08%) | unsloth/DeepSeek-R1 (0.49%) |  |
| unsloth/Devstral-Small-2505 (1.15%) | unsloth/DeepSeek-R1-0528 (0.49%) |  |
| unsloth/Magistral-Small-2506 (1.15%) | unsloth/DeepSeek-Prover-V2-671B (0.49%) |  |
| unsloth/Mistral-Medium-3.5-128B (1.15%) | tngtech/DeepSeek-R1T-Chimera (0.49%) |  |
| unsloth/Mistral-Small-4-119B-2603 (1.15%) | openbmb/MiniCPM4-8B (0.19%) |  |
| unsloth/Mistral-Small-3.2-24B-Instruct-2506 (1.15%) | unsloth/mistral-7b-v0.3 (0.18%) |  |
| HuggingFaceTB/SmolLM3-3B (1.08%) | unsloth/Mistral-Small-Instruct-2409 (0.18%) |  |
| 1-800-LLMs/tiny-aya-earth (1.77%) | THUDM/GLM-4.1V-9B-Thinking (0.55%) |  |
|  | unsloth/LFM2.5-8B-A1B (0.34%) |  |


## Individual Model Analysis


### unsloth/Llama-3.2-3B-Instruct

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 3B | - |
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
| **Parameters** | 8B | - |
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
| **Parameters** | 71B | - |
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
| **Parameters** | 9B | - |
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
| **Parameters** | 7B | - |
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
| **Parameters** | 8B | - |
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

### Qwen/Qwen3-32B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 33B | - |
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

### Qwen/Qwen3-235B-A22B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 235B | - |
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
| **Parameters** | 6B | - |
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

### unsloth/Qwen3.5-27B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 28B | - |
| **Total Vocabulary** | 248,044 | 100% |
| **Greek Tokens** | 1,538 | 0.62% |
| **Latin Tokens** | 137,780 | 55.55% |

#### Language Distribution
```
Greek:                                 0.62%
Latin:  ████████████████               55.55%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Qwen3.5-122B-A10B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 125B | - |
| **Total Vocabulary** | 248,044 | 100% |
| **Greek Tokens** | 1,538 | 0.62% |
| **Latin Tokens** | 137,780 | 55.55% |

#### Language Distribution
```
Greek:                                 0.62%
Latin:  ████████████████               55.55%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Qwen3.6-35B-A3B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 36B | - |
| **Total Vocabulary** | 248,044 | 100% |
| **Greek Tokens** | 1,538 | 0.62% |
| **Latin Tokens** | 137,780 | 55.55% |

#### Language Distribution
```
Greek:                                 0.62%
Latin:  ████████████████               55.55%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Qwen3.6-27B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 28B | - |
| **Total Vocabulary** | 248,044 | 100% |
| **Greek Tokens** | 1,538 | 0.62% |
| **Latin Tokens** | 137,780 | 55.55% |

#### Language Distribution
```
Greek:                                 0.62%
Latin:  ████████████████               55.55%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Llama-3.1-Nemotron-Nano-8B-v1

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 8B | - |
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

### unsloth/NVIDIA-Nemotron-3-Nano-4B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 4B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Nemotron-3-Nano-30B-A3B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 32B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/gemma-3-27b-it

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 27B | - |
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

### unsloth/gemma-4-12b-it

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 12B | - |
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

### unsloth/gemma-4-12b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 12B | - |
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

### unsloth/gemma-4-E2B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 5B | - |
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

### unsloth/gemma-4-E4B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 8B | - |
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

### unsloth/gemma-4-31B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 33B | - |
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

### unsloth/Step-3.7-Flash

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 201B | - |
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

### deepseek-ai/DeepSeek-V2.5-1210

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 236B | - |
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
| **Parameters** | 684B | - |
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

### unsloth/DeepSeek-R1-0528

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | N/A | - |
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
| **Parameters** | 671B | - |
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
| **Parameters** | 685B | - |
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

### microsoft/phi-4

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 15B | - |
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
| **Parameters** | 1B | - |
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
| **Parameters** | 7B | - |
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
| **Parameters** | 8B | - |
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

### ibm-granite/granite-speech-3.3-8b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 9B | - |
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

### mlx-community/aya-expanse-32b-8bit

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 32B | - |
| **Total Vocabulary** | 255,000 | 100% |
| **Greek Tokens** | 7,547 | 2.96% |
| **Latin Tokens** | 173,699 | 68.12% |

#### Language Distribution
```
Greek:                                 2.96%
Latin:  ████████████████████           68.12%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `ο`, `α`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 9B | - |
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

### openbmb/MiniCPM4-8B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 8B | - |
| **Total Vocabulary** | 73,440 | 100% |
| **Greek Tokens** | 143 | 0.19% |
| **Latin Tokens** | 36,406 | 49.57% |

#### Language Distribution
```
Greek:                                 0.19%
Latin:  ██████████████                 49.57%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `μ`, `β`, `θ`, `π`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Devstral-Small-2505

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 24B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Magistral-Small-2506

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 24B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/mistral-7b-v0.3

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 7B | - |
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
| **Parameters** | 22B | - |
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

### unsloth/Mistral-Medium-3.5-128B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 128B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Mistral-Small-4-119B-2603

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 119B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/Mistral-Small-3.2-24B-Instruct-2506

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 24B | - |
| **Total Vocabulary** | 131,072 | 100% |
| **Greek Tokens** | 1,507 | 1.15% |
| **Latin Tokens** | 87,986 | 67.13% |

#### Language Distribution
```
Greek:                                 1.15%
Latin:  ████████████████████           67.13%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `τ`, `α`, `ο`, `ι`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/granite-4.1-30b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 29B | - |
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

### HuggingFaceTB/SmolLM3-3B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 3B | - |
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

### THUDM/GLM-4.1V-9B-Thinking

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 10B | - |
| **Total Vocabulary** | 151,329 | 100% |
| **Greek Tokens** | 832 | 0.55% |
| **Latin Tokens** | 100,326 | 66.30% |

#### Language Distribution
```
Greek:                                 0.55%
Latin:  ███████████████████            66.30%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, ` α`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/LFM2.5-8B-A1B

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 8B | - |
| **Total Vocabulary** | 124,893 | 100% |
| **Greek Tokens** | 430 | 0.34% |
| **Latin Tokens** | 86,283 | 69.09% |

#### Language Distribution
```
Greek:                                 0.34%
Latin:  ████████████████████           69.09%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `ο`, `β`, `μ`, `ν`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---

### unsloth/granite-4.1-8b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 9B | - |
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

### unsloth/granite-4.1-30b

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 29B | - |
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

### 1-800-LLMs/tiny-aya-earth

| Metric | Value | Percentage |
|--------|-------|------------|
| **Parameters** | 3B | - |
| **Total Vocabulary** | 261,000 | 100% |
| **Greek Tokens** | 4,622 | 1.77% |
| **Latin Tokens** | 153,473 | 58.80% |

#### Language Distribution
```
Greek:                                 1.77%
Latin:  █████████████████              58.80%
```


#### Greek Character Statistics
- **Total Greek Characters**: 
- **Unique Characters**: 
- **Most Common**: `` ( times)


#### Sample Tokens
**Greek**: `α`, `τ`, `ο`, `ι`, `ε`...

**Latin**: `A`, `B`, `C`, `D`, `E`...

---


---
*Summary report generated on 2026-06-05 13:52:48 analyzing 50 models*