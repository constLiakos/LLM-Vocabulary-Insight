# LLM Vocabulary Insight Report

[ℹ️ Project Info](README.dev.md)

## 🎯 Overview

This report presents a comprehensive analysis of Greek language tokenization capabilities across **27** Large Language Models (LLMs). The analysis evaluates how effectively different transformer-based models handle Greek text through their tokenizer vocabularies, providing insights into Greek language support, character coverage, and tokenization efficiency.

## Overall Statistics

| Metric | Value |
|--------|-------|
| **Total Models Analyzed** | 27 |
| **Combined Vocabulary Size** | 3,211,615 tokens |
| **Average Vocabulary Size** | 118,948 tokens |
| **Total Greek Tokens** | 75,462 (2.35%) |
| **Total Latin Tokens** | 2,134,954 (66.48%) |

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

| Rank | Model | Greek Tokens | Total Vocabulary | Percentage |
|------|-------|--------------|------------------|------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 28,162 | 61,366 | 45.89% |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 22,212 | 149,248 | 14.88% |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 7,547 | 255,000 | 2.96% |
| 4 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2,816 | 128,000 | 2.20% |
| 5 | **unsloth/Devstral-Small-2505** | 1,507 | 131,072 | 1.15% |
| 6 | **unsloth/Magistral-Small-2506** | 1,507 | 131,072 | 1.15% |
| 7 | **unsloth/gemma-3-27b-it** | 1,409 | 262,144 | 0.54% |
| 8 | **unsloth/Llama-3.2-3B-Instruct** | 1,378 | 128,000 | 1.08% |
| 9 | **unsloth/llama-3-8b** | 1,378 | 128,000 | 1.08% |
| 10 | **unsloth/Llama-3.3-70B-Instruct** | 1,378 | 128,000 | 1.08% |
| 11 | **microsoft/bitnet-b1.58-2B-4T** | 1,378 | 128,000 | 1.08% |
| 12 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 1,378 | 128,000 | 1.08% |
| 13 | **unsloth/DeepSeek-R1** | 629 | 128,000 | 0.49% |
| 14 | **unsloth/DeepSeek-R1-0528** | 629 | 128,000 | 0.49% |
| 15 | **unsloth/DeepSeek-Prover-V2-671B** | 629 | 128,000 | 0.49% |
| 16 | **tngtech/DeepSeek-R1T-Chimera** | 629 | 128,000 | 0.49% |
| 17 | **openbmb/MiniCPM4-8B** | 143 | 73,440 | 0.19% |
| 18 | **Qwen/Qwen3-32B** | 127 | 151,643 | 0.08% |
| 19 | **Qwen/Qwen3-235B-A22B** | 127 | 151,643 | 0.08% |
| 20 | **Qwen/Qwen2.5-Omni-3B** | 127 | 151,643 | 0.08% |
| 21 | **deepseek-ai/DeepSeek-V2.5-1210** | 86 | 100,000 | 0.09% |
| 22 | **unsloth/mistral-7b-v0.3** | 58 | 32,768 | 0.18% |
| 23 | **unsloth/Mistral-Small-Instruct-2409** | 58 | 32,768 | 0.18% |
| 24 | **microsoft/phi-4** | 44 | 100,352 | 0.04% |
| 25 | **ibm-granite/granite-4.0-tiny-preview** | 42 | 49,152 | 0.09% |
| 26 | **ibm-granite/granite-3.3-8b-instruct** | 42 | 49,152 | 0.09% |
| 27 | **ibm-granite/granite-speech-3.3-8b** | 42 | 49,152 | 0.09% |


### By Percentage (Relative Performance)

| Rank | Model | Percentage | Greek Tokens | Total Vocabulary |
|------|-------|------------|--------------|------------------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 45.89% | 28,162 | 61,366 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 14.88% | 22,212 | 149,248 |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 2.96% | 7,547 | 255,000 |
| 4 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2.20% | 2,816 | 128,000 |
| 5 | **unsloth/Devstral-Small-2505** | 1.15% | 1,507 | 131,072 |
| 6 | **unsloth/Magistral-Small-2506** | 1.15% | 1,507 | 131,072 |
| 7 | **unsloth/Llama-3.2-3B-Instruct** | 1.08% | 1,378 | 128,000 |
| 8 | **unsloth/llama-3-8b** | 1.08% | 1,378 | 128,000 |
| 9 | **unsloth/Llama-3.3-70B-Instruct** | 1.08% | 1,378 | 128,000 |
| 10 | **microsoft/bitnet-b1.58-2B-4T** | 1.08% | 1,378 | 128,000 |
| 11 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 1.08% | 1,378 | 128,000 |
| 12 | **unsloth/gemma-3-27b-it** | 0.54% | 1,409 | 262,144 |
| 13 | **unsloth/DeepSeek-R1** | 0.49% | 629 | 128,000 |
| 14 | **unsloth/DeepSeek-R1-0528** | 0.49% | 629 | 128,000 |
| 15 | **unsloth/DeepSeek-Prover-V2-671B** | 0.49% | 629 | 128,000 |
| 16 | **tngtech/DeepSeek-R1T-Chimera** | 0.49% | 629 | 128,000 |
| 17 | **openbmb/MiniCPM4-8B** | 0.19% | 143 | 73,440 |
| 18 | **unsloth/mistral-7b-v0.3** | 0.18% | 58 | 32,768 |
| 19 | **unsloth/Mistral-Small-Instruct-2409** | 0.18% | 58 | 32,768 |
| 20 | **deepseek-ai/DeepSeek-V2.5-1210** | 0.09% | 86 | 100,000 |
| 21 | **ibm-granite/granite-4.0-tiny-preview** | 0.09% | 42 | 49,152 |
| 22 | **ibm-granite/granite-3.3-8b-instruct** | 0.09% | 42 | 49,152 |
| 23 | **ibm-granite/granite-speech-3.3-8b** | 0.09% | 42 | 49,152 |
| 24 | **Qwen/Qwen3-32B** | 0.08% | 127 | 151,643 |
| 25 | **Qwen/Qwen3-235B-A22B** | 0.08% | 127 | 151,643 |
| 26 | **Qwen/Qwen2.5-Omni-3B** | 0.08% | 127 | 151,643 |
| 27 | **microsoft/phi-4** | 0.04% | 44 | 100,352 |


## Latin Performance Rankings

### By Token Count (Absolute Numbers)

| Rank | Model | Latin Tokens | Total Vocabulary | Percentage |
|------|-------|--------------|------------------|------------|
| 1 | **mlx-community/aya-expanse-32b-8bit** | 173,699 | 255,000 | 68.12% |
| 2 | **unsloth/gemma-3-27b-it** | 151,739 | 262,144 | 57.88% |
| 3 | **ilsp/Llama-Krikri-8B-Instruct** | 96,699 | 149,248 | 64.79% |
| 4 | **unsloth/Llama-3.2-3B-Instruct** | 96,687 | 128,000 | 75.54% |
| 5 | **unsloth/llama-3-8b** | 96,687 | 128,000 | 75.54% |
| 6 | **unsloth/Llama-3.3-70B-Instruct** | 96,687 | 128,000 | 75.54% |
| 7 | **microsoft/bitnet-b1.58-2B-4T** | 96,687 | 128,000 | 75.54% |
| 8 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 96,687 | 128,000 | 75.54% |
| 9 | **Qwen/Qwen3-32B** | 93,859 | 151,643 | 61.89% |
| 10 | **Qwen/Qwen3-235B-A22B** | 93,859 | 151,643 | 61.89% |
| 11 | **Qwen/Qwen2.5-Omni-3B** | 93,859 | 151,643 | 61.89% |
| 12 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 91,179 | 128,000 | 71.23% |
| 13 | **microsoft/phi-4** | 89,643 | 100,352 | 89.33% |
| 14 | **unsloth/Devstral-Small-2505** | 87,986 | 131,072 | 67.13% |
| 15 | **unsloth/Magistral-Small-2506** | 87,986 | 131,072 | 67.13% |
| 16 | **unsloth/DeepSeek-R1** | 71,454 | 128,000 | 55.82% |
| 17 | **unsloth/DeepSeek-R1-0528** | 71,454 | 128,000 | 55.82% |
| 18 | **unsloth/DeepSeek-Prover-V2-671B** | 71,454 | 128,000 | 55.82% |
| 19 | **tngtech/DeepSeek-R1T-Chimera** | 71,454 | 128,000 | 55.82% |
| 20 | **deepseek-ai/DeepSeek-V2.5-1210** | 70,489 | 100,000 | 70.49% |
| 21 | **ibm-granite/granite-4.0-tiny-preview** | 40,302 | 49,152 | 81.99% |
| 22 | **ibm-granite/granite-3.3-8b-instruct** | 40,302 | 49,152 | 81.99% |
| 23 | **ibm-granite/granite-speech-3.3-8b** | 40,302 | 49,152 | 81.99% |
| 24 | **openbmb/MiniCPM4-8B** | 36,406 | 73,440 | 49.57% |
| 25 | **ilsp/Meltemi-7B-Instruct-v1.5** | 25,948 | 61,366 | 42.28% |
| 26 | **unsloth/mistral-7b-v0.3** | 25,723 | 32,768 | 78.50% |
| 27 | **unsloth/Mistral-Small-Instruct-2409** | 25,723 | 32,768 | 78.50% |


### By Percentage (Relative Performance)

| Rank | Model | Percentage | Latin Tokens | Total Vocabulary |
|------|-------|------------|--------------|------------------|
| 1 | **microsoft/phi-4** | 89.33% | 89,643 | 100,352 |
| 2 | **ibm-granite/granite-4.0-tiny-preview** | 81.99% | 40,302 | 49,152 |
| 3 | **ibm-granite/granite-3.3-8b-instruct** | 81.99% | 40,302 | 49,152 |
| 4 | **ibm-granite/granite-speech-3.3-8b** | 81.99% | 40,302 | 49,152 |
| 5 | **unsloth/mistral-7b-v0.3** | 78.50% | 25,723 | 32,768 |
| 6 | **unsloth/Mistral-Small-Instruct-2409** | 78.50% | 25,723 | 32,768 |
| 7 | **unsloth/Llama-3.2-3B-Instruct** | 75.54% | 96,687 | 128,000 |
| 8 | **unsloth/llama-3-8b** | 75.54% | 96,687 | 128,000 |
| 9 | **unsloth/Llama-3.3-70B-Instruct** | 75.54% | 96,687 | 128,000 |
| 10 | **microsoft/bitnet-b1.58-2B-4T** | 75.54% | 96,687 | 128,000 |
| 11 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 75.54% | 96,687 | 128,000 |
| 12 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 71.23% | 91,179 | 128,000 |
| 13 | **deepseek-ai/DeepSeek-V2.5-1210** | 70.49% | 70,489 | 100,000 |
| 14 | **mlx-community/aya-expanse-32b-8bit** | 68.12% | 173,699 | 255,000 |
| 15 | **unsloth/Devstral-Small-2505** | 67.13% | 87,986 | 131,072 |
| 16 | **unsloth/Magistral-Small-2506** | 67.13% | 87,986 | 131,072 |
| 17 | **ilsp/Llama-Krikri-8B-Instruct** | 64.79% | 96,699 | 149,248 |
| 18 | **Qwen/Qwen3-32B** | 61.89% | 93,859 | 151,643 |
| 19 | **Qwen/Qwen3-235B-A22B** | 61.89% | 93,859 | 151,643 |
| 20 | **Qwen/Qwen2.5-Omni-3B** | 61.89% | 93,859 | 151,643 |
| 21 | **unsloth/gemma-3-27b-it** | 57.88% | 151,739 | 262,144 |
| 22 | **unsloth/DeepSeek-R1** | 55.82% | 71,454 | 128,000 |
| 23 | **unsloth/DeepSeek-R1-0528** | 55.82% | 71,454 | 128,000 |
| 24 | **unsloth/DeepSeek-Prover-V2-671B** | 55.82% | 71,454 | 128,000 |
| 25 | **tngtech/DeepSeek-R1T-Chimera** | 55.82% | 71,454 | 128,000 |
| 26 | **openbmb/MiniCPM4-8B** | 49.57% | 36,406 | 73,440 |
| 27 | **ilsp/Meltemi-7B-Instruct-v1.5** | 42.28% | 25,948 | 61,366 |


## Comparative Analysis

### Vocabulary Size Distribution

| Model | Total Vocabulary | Visual Scale | Relative Size |
|-------|------------------|--------------|---------------|
| **unsloth/gemma-3-27b-it** | 262,144 |  | 220.4% of avg |
| **mlx-community/aya-expanse-32b-8bit** | 255,000 |  | 214.4% of avg |
| **Qwen/Qwen3-32B** | 151,643 |  | 127.5% of avg |
| **Qwen/Qwen3-235B-A22B** | 151,643 |  | 127.5% of avg |
| **Qwen/Qwen2.5-Omni-3B** | 151,643 |  | 127.5% of avg |
| **ilsp/Llama-Krikri-8B-Instruct** | 149,248 |  | 125.5% of avg |
| **unsloth/Devstral-Small-2505** | 131,072 |  | 110.2% of avg |
| **unsloth/Magistral-Small-2506** | 131,072 |  | 110.2% of avg |
| **unsloth/Llama-3.2-3B-Instruct** | 128,000 |  | 107.6% of avg |
| **unsloth/llama-3-8b** | 128,000 |  | 107.6% of avg |
| **unsloth/Llama-3.3-70B-Instruct** | 128,000 |  | 107.6% of avg |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 128,000 |  | 107.6% of avg |
| **unsloth/DeepSeek-R1** | 128,000 |  | 107.6% of avg |
| **unsloth/DeepSeek-R1-0528** | 128,000 |  | 107.6% of avg |
| **unsloth/DeepSeek-Prover-V2-671B** | 128,000 |  | 107.6% of avg |
| **tngtech/DeepSeek-R1T-Chimera** | 128,000 |  | 107.6% of avg |
| **microsoft/bitnet-b1.58-2B-4T** | 128,000 |  | 107.6% of avg |
| **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 128,000 |  | 107.6% of avg |
| **microsoft/phi-4** | 100,352 |  | 84.4% of avg |
| **deepseek-ai/DeepSeek-V2.5-1210** | 100,000 |  | 84.1% of avg |
| **openbmb/MiniCPM4-8B** | 73,440 |  | 61.7% of avg |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 61,366 |  | 51.6% of avg |
| **ibm-granite/granite-4.0-tiny-preview** | 49,152 |  | 41.3% of avg |
| **ibm-granite/granite-3.3-8b-instruct** | 49,152 |  | 41.3% of avg |
| **ibm-granite/granite-speech-3.3-8b** | 49,152 |  | 41.3% of avg |
| **unsloth/mistral-7b-v0.3** | 32,768 |  | 27.5% of avg |
| **unsloth/Mistral-Small-Instruct-2409** | 32,768 |  | 27.5% of avg |


### Greek Support Comparison

| Rank | Model | Greek Percentage | Greek Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **ilsp/Meltemi-7B-Instruct-v1.5** | 45.89% | 28,162 | 🟩🟩🟩🟩🟩 |
| 2 | **ilsp/Llama-Krikri-8B-Instruct** | 14.88% | 22,212 | 🟩🟩🟩🟩🟩 |
| 3 | **mlx-community/aya-expanse-32b-8bit** | 2.96% | 7,547 | 🟩🟩🟩🟩🟩 |
| 4 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 2.20% | 2,816 | 🟩🟩🟩🟩🟩 |
| 5 | **unsloth/Devstral-Small-2505** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 6 | **unsloth/Magistral-Small-2506** | 1.15% | 1,507 | 🟩🟩🟩⬜⬜ |
| 7 | **unsloth/gemma-3-27b-it** | 0.54% | 1,409 | 🟩🟩⬜⬜⬜ |
| 8 | **unsloth/Llama-3.2-3B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 9 | **unsloth/llama-3-8b** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 10 | **unsloth/Llama-3.3-70B-Instruct** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 11 | **microsoft/bitnet-b1.58-2B-4T** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 12 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 1.08% | 1,378 | 🟩🟩⬜⬜⬜ |
| 13 | **unsloth/DeepSeek-R1** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 14 | **unsloth/DeepSeek-R1-0528** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 15 | **unsloth/DeepSeek-Prover-V2-671B** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 16 | **tngtech/DeepSeek-R1T-Chimera** | 0.49% | 629 | 🟩⬜⬜⬜⬜ |
| 17 | **openbmb/MiniCPM4-8B** | 0.19% | 143 | ⬜⬜⬜⬜⬜ |
| 18 | **Qwen/Qwen3-32B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 19 | **Qwen/Qwen3-235B-A22B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 20 | **Qwen/Qwen2.5-Omni-3B** | 0.08% | 127 | ⬜⬜⬜⬜⬜ |
| 21 | **deepseek-ai/DeepSeek-V2.5-1210** | 0.09% | 86 | ⬜⬜⬜⬜⬜ |
| 22 | **unsloth/mistral-7b-v0.3** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 23 | **unsloth/Mistral-Small-Instruct-2409** | 0.18% | 58 | ⬜⬜⬜⬜⬜ |
| 24 | **microsoft/phi-4** | 0.04% | 44 | ⬜⬜⬜⬜⬜ |
| 25 | **ibm-granite/granite-4.0-tiny-preview** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |
| 26 | **ibm-granite/granite-3.3-8b-instruct** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |
| 27 | **ibm-granite/granite-speech-3.3-8b** | 0.09% | 42 | ⬜⬜⬜⬜⬜ |


### Latin Support Comparison

| Rank | Model | Latin Percentage | Latin Tokens | Visual |
|------|-------|------------------|--------------|--------|
| 1 | **mlx-community/aya-expanse-32b-8bit** | 68.12% | 173,699 | 🟦🟦🟦🟦🟦 |
| 2 | **unsloth/gemma-3-27b-it** | 57.88% | 151,739 | 🟦🟦🟦🟦🟦 |
| 3 | **ilsp/Llama-Krikri-8B-Instruct** | 64.79% | 96,699 | 🟦🟦🟦🟦🟦 |
| 4 | **unsloth/Llama-3.2-3B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 5 | **unsloth/llama-3-8b** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 6 | **unsloth/Llama-3.3-70B-Instruct** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 7 | **microsoft/bitnet-b1.58-2B-4T** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 8 | **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 75.54% | 96,687 | 🟦🟦🟦🟦🟦 |
| 9 | **Qwen/Qwen3-32B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 10 | **Qwen/Qwen3-235B-A22B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 11 | **Qwen/Qwen2.5-Omni-3B** | 61.89% | 93,859 | 🟦🟦🟦🟦🟦 |
| 12 | **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 71.23% | 91,179 | 🟦🟦🟦🟦🟦 |
| 13 | **microsoft/phi-4** | 89.33% | 89,643 | 🟦🟦🟦🟦🟦 |
| 14 | **unsloth/Devstral-Small-2505** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 15 | **unsloth/Magistral-Small-2506** | 67.13% | 87,986 | 🟦🟦🟦🟦🟦 |
| 16 | **unsloth/DeepSeek-R1** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 17 | **unsloth/DeepSeek-R1-0528** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 18 | **unsloth/DeepSeek-Prover-V2-671B** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 19 | **tngtech/DeepSeek-R1T-Chimera** | 55.82% | 71,454 | 🟦🟦🟦🟦🟦 |
| 20 | **deepseek-ai/DeepSeek-V2.5-1210** | 70.49% | 70,489 | 🟦🟦🟦🟦🟦 |
| 21 | **ibm-granite/granite-4.0-tiny-preview** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 22 | **ibm-granite/granite-3.3-8b-instruct** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 23 | **ibm-granite/granite-speech-3.3-8b** | 81.99% | 40,302 | 🟦🟦🟦🟦🟦 |
| 24 | **openbmb/MiniCPM4-8B** | 49.57% | 36,406 | 🟦🟦🟦🟦🟦 |
| 25 | **ilsp/Meltemi-7B-Instruct-v1.5** | 42.28% | 25,948 | 🟦🟦🟦🟦🟦 |
| 26 | **unsloth/mistral-7b-v0.3** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |
| 27 | **unsloth/Mistral-Small-Instruct-2409** | 78.50% | 25,723 | 🟦🟦🟦🟦🟦 |


### Cross-Language Performance Matrix

| Model | Total Vocab | Greek % | Greek Tokens | Latin % | Latin Tokens | Greek/Latin Ratio |
|-------|-------------|---------|--------------|---------|--------------|-------------------|
| **unsloth/Llama-3.2-3B-Instruct** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/llama-3-8b** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **unsloth/Llama-3.3-70B-Instruct** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit** | 128,000 | 2.20% | 2,816 | 71.23% | 91,179 | 0.03 |
| **ilsp/Meltemi-7B-Instruct-v1.5** | 61,366 | 45.89% | 28,162 | 42.28% | 25,948 | 1.09 |
| **ilsp/Llama-Krikri-8B-Instruct** | 149,248 | 14.88% | 22,212 | 64.79% | 96,699 | 0.23 |
| **Qwen/Qwen3-32B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen3-235B-A22B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **Qwen/Qwen2.5-Omni-3B** | 151,643 | 0.08% | 127 | 61.89% | 93,859 | 0.00 |
| **unsloth/gemma-3-27b-it** | 262,144 | 0.54% | 1,409 | 57.88% | 151,739 | 0.01 |
| **deepseek-ai/DeepSeek-V2.5-1210** | 100,000 | 0.09% | 86 | 70.49% | 70,489 | 0.00 |
| **unsloth/DeepSeek-R1** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **unsloth/DeepSeek-R1-0528** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **unsloth/DeepSeek-Prover-V2-671B** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **tngtech/DeepSeek-R1T-Chimera** | 128,000 | 0.49% | 629 | 55.82% | 71,454 | 0.01 |
| **microsoft/phi-4** | 100,352 | 0.04% | 44 | 89.33% | 89,643 | 0.00 |
| **microsoft/bitnet-b1.58-2B-4T** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **ibm-granite/granite-4.0-tiny-preview** | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **ibm-granite/granite-3.3-8b-instruct** | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **ibm-granite/granite-speech-3.3-8b** | 49,152 | 0.09% | 42 | 81.99% | 40,302 | 0.00 |
| **mlx-community/aya-expanse-32b-8bit** | 255,000 | 2.96% | 7,547 | 68.12% | 173,699 | 0.04 |
| **nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1** | 128,000 | 1.08% | 1,378 | 75.54% | 96,687 | 0.01 |
| **openbmb/MiniCPM4-8B** | 73,440 | 0.19% | 143 | 49.57% | 36,406 | 0.00 |
| **unsloth/Devstral-Small-2505** | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/Magistral-Small-2506** | 131,072 | 1.15% | 1,507 | 67.13% | 87,986 | 0.02 |
| **unsloth/mistral-7b-v0.3** | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |
| **unsloth/Mistral-Small-Instruct-2409** | 32,768 | 0.18% | 58 | 78.50% | 25,723 | 0.00 |


### Performance Categories

| High Greek Support (>1%) | Medium Greek Support (0.1-1%) | Low Greek Support (<0.1%) |
|---------------------------|--------------------------------|---------------------------|
| unsloth/Llama-3.2-3B-Instruct (1.08%) | unsloth/gemma-3-27b-it (0.54%) | Qwen/Qwen3-32B (0.08%) |
| unsloth/llama-3-8b (1.08%) | unsloth/DeepSeek-R1 (0.49%) | Qwen/Qwen3-235B-A22B (0.08%) |
| unsloth/Llama-3.3-70B-Instruct (1.08%) | unsloth/DeepSeek-R1-0528 (0.49%) | Qwen/Qwen2.5-Omni-3B (0.08%) |
| kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit (2.20%) | unsloth/DeepSeek-Prover-V2-671B (0.49%) | deepseek-ai/DeepSeek-V2.5-1210 (0.09%) |
| ilsp/Meltemi-7B-Instruct-v1.5 (45.89%) | tngtech/DeepSeek-R1T-Chimera (0.49%) | microsoft/phi-4 (0.04%) |
| ilsp/Llama-Krikri-8B-Instruct (14.88%) | openbmb/MiniCPM4-8B (0.19%) | ibm-granite/granite-4.0-tiny-preview (0.09%) |
| microsoft/bitnet-b1.58-2B-4T (1.08%) | unsloth/mistral-7b-v0.3 (0.18%) | ibm-granite/granite-3.3-8b-instruct (0.09%) |
| mlx-community/aya-expanse-32b-8bit (2.96%) | unsloth/Mistral-Small-Instruct-2409 (0.18%) | ibm-granite/granite-speech-3.3-8b (0.09%) |
| nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1 (1.08%) |  |  |
| unsloth/Devstral-Small-2505 (1.15%) |  |  |
| unsloth/Magistral-Small-2506 (1.15%) |  |  |


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

### Qwen/Qwen3-235B-A22B

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

### unsloth/gemma-3-27b-it

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

### unsloth/DeepSeek-R1-0528

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

### ibm-granite/granite-speech-3.3-8b

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

### mlx-community/aya-expanse-32b-8bit

| Metric | Value | Percentage |
|--------|-------|------------|
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


---
*Summary report generated on 2025-06-12 17:07:43 analyzing 27 models*