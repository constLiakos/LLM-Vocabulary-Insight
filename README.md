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

### Best Greek Support
🥇 **ilsp/Meltemi-7B-Instruct-v1.5** - 45.89% Greek tokens

### Lowest Greek Support
📉 **microsoft/phi-4** - 0.04% Greek tokens

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


## Comparative Analysis

### Vocabulary Size Distribution

unsloth/gemma-3-4b-it: ███ 262,144

unsloth/gemma-2-2b-it: ███ 256,000

Qwen/Qwen2.5-1.5B-Instruct: ██ 151,643

Qwen/Qwen3-0.6B: ██ 151,643

Qwen/Qwen3-32B: ██ 151,643

Qwen/Qwen2.5-Omni-3B: ██ 151,643

XiaomiMiMo/MiMo-7B-RL: ██ 151,643

ilsp/Llama-Krikri-8B-Instruct: ██ 149,248

unsloth/Llama-3.2-3B-Instruct: █ 128,000

unsloth/llama-3-8b: █ 128,000

unsloth/Llama-3.3-70B-Instruct: █ 128,000

kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit: █ 128,000

unsloth/DeepSeek-R1: █ 128,000

unsloth/DeepSeek-Prover-V2-671B: █ 128,000

tngtech/DeepSeek-R1T-Chimera: █ 128,000

microsoft/bitnet-b1.58-2B-4T: █ 128,000

microsoft/phi-4: █ 100,352

microsoft/Phi-4-reasoning-plus: █ 100,352

Xenova/gpt-4: █ 100,263

Xenova/text-embedding-ada-002: █ 100,261

Xenova/gpt-3.5-turbo-16k: █ 100,261

deepseek-ai/DeepSeek-V2.5-1210: █ 100,000

ilsp/Meltemi-7B-Instruct-v1.5:  61,366

unsloth/SmolLM2-1.7B-Instruct:  49,152

ibm-granite/granite-4.0-tiny-preview:  49,152

ibm-granite/granite-3.3-8b-instruct:  49,152

unsloth/mistral-7b-v0.3:  32,768

unsloth/Mistral-Small-Instruct-2409:  32,768

unsloth/Phi-3.5-mini-instruct:  32,000


### Greek Support Ranking

1. **ilsp/Meltemi-7B-Instruct-v1.5**: 45.89% (28,162 tokens)

2. **ilsp/Llama-Krikri-8B-Instruct**: 14.88% (22,212 tokens)

3. **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit**: 2.20% (2,816 tokens)

4. **unsloth/gemma-3-4b-it**: 0.54% (1,409 tokens)

5. **unsloth/Llama-3.2-3B-Instruct**: 1.08% (1,378 tokens)

6. **unsloth/llama-3-8b**: 1.08% (1,378 tokens)

7. **unsloth/Llama-3.3-70B-Instruct**: 1.08% (1,378 tokens)

8. **microsoft/bitnet-b1.58-2B-4T**: 1.08% (1,378 tokens)

9. **unsloth/gemma-2-2b-it**: 0.48% (1,229 tokens)

10. **unsloth/DeepSeek-R1**: 0.49% (629 tokens)

11. **unsloth/DeepSeek-Prover-V2-671B**: 0.49% (629 tokens)

12. **tngtech/DeepSeek-R1T-Chimera**: 0.49% (629 tokens)

13. **Qwen/Qwen2.5-1.5B-Instruct**: 0.08% (127 tokens)

14. **Qwen/Qwen3-0.6B**: 0.08% (127 tokens)

15. **Qwen/Qwen3-32B**: 0.08% (127 tokens)

16. **Qwen/Qwen2.5-Omni-3B**: 0.08% (127 tokens)

17. **XiaomiMiMo/MiMo-7B-RL**: 0.08% (127 tokens)

18. **deepseek-ai/DeepSeek-V2.5-1210**: 0.09% (86 tokens)

19. **unsloth/Phi-3.5-mini-instruct**: 0.20% (63 tokens)

20. **unsloth/SmolLM2-1.7B-Instruct**: 0.12% (60 tokens)

21. **unsloth/mistral-7b-v0.3**: 0.18% (58 tokens)

22. **unsloth/Mistral-Small-Instruct-2409**: 0.18% (58 tokens)

23. **Xenova/gpt-4**: 0.04% (44 tokens)

24. **Xenova/text-embedding-ada-002**: 0.04% (44 tokens)

25. **Xenova/gpt-3.5-turbo-16k**: 0.04% (44 tokens)

26. **microsoft/phi-4**: 0.04% (44 tokens)

27. **microsoft/Phi-4-reasoning-plus**: 0.04% (44 tokens)

28. **ibm-granite/granite-4.0-tiny-preview**: 0.09% (42 tokens)

29. **ibm-granite/granite-3.3-8b-instruct**: 0.09% (42 tokens)


### Latin Support Ranking

1. **unsloth/gemma-2-2b-it**: 72.10% (184,588 tokens)

2. **unsloth/gemma-3-4b-it**: 57.88% (151,739 tokens)

3. **ilsp/Llama-Krikri-8B-Instruct**: 64.79% (96,699 tokens)

4. **unsloth/Llama-3.2-3B-Instruct**: 75.54% (96,687 tokens)

5. **unsloth/llama-3-8b**: 75.54% (96,687 tokens)

6. **unsloth/Llama-3.3-70B-Instruct**: 75.54% (96,687 tokens)

7. **microsoft/bitnet-b1.58-2B-4T**: 75.54% (96,687 tokens)

8. **Qwen/Qwen2.5-1.5B-Instruct**: 61.89% (93,859 tokens)

9. **Qwen/Qwen3-0.6B**: 61.89% (93,859 tokens)

10. **Qwen/Qwen3-32B**: 61.89% (93,859 tokens)

11. **Qwen/Qwen2.5-Omni-3B**: 61.89% (93,859 tokens)

12. **XiaomiMiMo/MiMo-7B-RL**: 61.89% (93,859 tokens)

13. **kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit**: 71.23% (91,179 tokens)

14. **Xenova/gpt-4**: 89.41% (89,643 tokens)

15. **Xenova/text-embedding-ada-002**: 89.41% (89,643 tokens)

16. **Xenova/gpt-3.5-turbo-16k**: 89.41% (89,643 tokens)

17. **microsoft/phi-4**: 89.33% (89,643 tokens)

18. **microsoft/Phi-4-reasoning-plus**: 89.33% (89,643 tokens)

19. **unsloth/DeepSeek-R1**: 55.82% (71,454 tokens)

20. **unsloth/DeepSeek-Prover-V2-671B**: 55.82% (71,454 tokens)

21. **tngtech/DeepSeek-R1T-Chimera**: 55.82% (71,454 tokens)

22. **deepseek-ai/DeepSeek-V2.5-1210**: 70.49% (70,489 tokens)

23. **unsloth/SmolLM2-1.7B-Instruct**: 95.94% (47,156 tokens)

24. **ibm-granite/granite-4.0-tiny-preview**: 81.99% (40,302 tokens)

25. **ibm-granite/granite-3.3-8b-instruct**: 81.99% (40,302 tokens)

26. **ilsp/Meltemi-7B-Instruct-v1.5**: 42.28% (25,948 tokens)

27. **unsloth/mistral-7b-v0.3**: 78.50% (25,723 tokens)

28. **unsloth/Mistral-Small-Instruct-2409**: 78.50% (25,723 tokens)

29. **unsloth/Phi-3.5-mini-instruct**: 80.08% (25,624 tokens)


## Generated Files by Model


### unsloth/Llama-3.2-3B-Instruct
- 📄 [All Tokens (Text)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/Llama-3.2-3B-Instruct/tokens-statistics.json)


### unsloth/llama-3-8b
- 📄 [All Tokens (Text)](output/generated/unsloth/llama-3-8b/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/llama-3-8b/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/llama-3-8b/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/llama-3-8b/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/llama-3-8b/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/llama-3-8b/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/llama-3-8b/tokens-statistics.json)


### unsloth/Llama-3.3-70B-Instruct
- 📄 [All Tokens (Text)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/Llama-3.3-70B-Instruct/tokens-statistics.json)


### kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit
- 📄 [All Tokens (Text)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/kaitchup/EuroLLM-9B-Instruct-AutoRound-GPTQ-4bit/tokens-statistics.json)


### ilsp/Meltemi-7B-Instruct-v1.5
- 📄 [All Tokens (Text)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/ilsp/Meltemi-7B-Instruct-v1.5/tokens-statistics.json)


### ilsp/Llama-Krikri-8B-Instruct
- 📄 [All Tokens (Text)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/ilsp/Llama-Krikri-8B-Instruct/tokens-statistics.json)


### unsloth/mistral-7b-v0.3
- 📄 [All Tokens (Text)](output/generated/unsloth/mistral-7b-v0.3/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/mistral-7b-v0.3/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/mistral-7b-v0.3/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/mistral-7b-v0.3/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/mistral-7b-v0.3/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/mistral-7b-v0.3/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/mistral-7b-v0.3/tokens-statistics.json)


### unsloth/Mistral-Small-Instruct-2409
- 📄 [All Tokens (Text)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/Mistral-Small-Instruct-2409/tokens-statistics.json)


### unsloth/SmolLM2-1.7B-Instruct
- 📄 [All Tokens (Text)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/SmolLM2-1.7B-Instruct/tokens-statistics.json)


### Xenova/gpt-4
- 📄 [All Tokens (Text)](output/generated/Xenova/gpt-4/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Xenova/gpt-4/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Xenova/gpt-4/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Xenova/gpt-4/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Xenova/gpt-4/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Xenova/gpt-4/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Xenova/gpt-4/tokens-statistics.json)


### Xenova/text-embedding-ada-002
- 📄 [All Tokens (Text)](output/generated/Xenova/text-embedding-ada-002/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Xenova/text-embedding-ada-002/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Xenova/text-embedding-ada-002/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Xenova/text-embedding-ada-002/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Xenova/text-embedding-ada-002/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Xenova/text-embedding-ada-002/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Xenova/text-embedding-ada-002/tokens-statistics.json)


### Xenova/gpt-3.5-turbo-16k
- 📄 [All Tokens (Text)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Xenova/gpt-3.5-turbo-16k/tokens-statistics.json)


### Qwen/Qwen2.5-1.5B-Instruct
- 📄 [All Tokens (Text)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Qwen/Qwen2.5-1.5B-Instruct/tokens-statistics.json)


### Qwen/Qwen3-0.6B
- 📄 [All Tokens (Text)](output/generated/Qwen/Qwen3-0.6B/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Qwen/Qwen3-0.6B/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Qwen/Qwen3-0.6B/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Qwen/Qwen3-0.6B/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Qwen/Qwen3-0.6B/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Qwen/Qwen3-0.6B/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Qwen/Qwen3-0.6B/tokens-statistics.json)


### Qwen/Qwen3-32B
- 📄 [All Tokens (Text)](output/generated/Qwen/Qwen3-32B/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Qwen/Qwen3-32B/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Qwen/Qwen3-32B/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Qwen/Qwen3-32B/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Qwen/Qwen3-32B/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Qwen/Qwen3-32B/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Qwen/Qwen3-32B/tokens-statistics.json)


### Qwen/Qwen2.5-Omni-3B
- 📄 [All Tokens (Text)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/Qwen/Qwen2.5-Omni-3B/tokens-statistics.json)


### unsloth/gemma-2-2b-it
- 📄 [All Tokens (Text)](output/generated/unsloth/gemma-2-2b-it/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/gemma-2-2b-it/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/gemma-2-2b-it/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/gemma-2-2b-it/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/gemma-2-2b-it/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/gemma-2-2b-it/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/gemma-2-2b-it/tokens-statistics.json)


### unsloth/gemma-3-4b-it
- 📄 [All Tokens (Text)](output/generated/unsloth/gemma-3-4b-it/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/gemma-3-4b-it/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/gemma-3-4b-it/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/gemma-3-4b-it/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/gemma-3-4b-it/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/gemma-3-4b-it/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/gemma-3-4b-it/tokens-statistics.json)


### deepseek-ai/DeepSeek-V2.5-1210
- 📄 [All Tokens (Text)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/deepseek-ai/DeepSeek-V2.5-1210/tokens-statistics.json)


### unsloth/DeepSeek-R1
- 📄 [All Tokens (Text)](output/generated/unsloth/DeepSeek-R1/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/DeepSeek-R1/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/DeepSeek-R1/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/DeepSeek-R1/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/DeepSeek-R1/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/DeepSeek-R1/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/DeepSeek-R1/tokens-statistics.json)


### unsloth/DeepSeek-Prover-V2-671B
- 📄 [All Tokens (Text)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/DeepSeek-Prover-V2-671B/tokens-statistics.json)


### tngtech/DeepSeek-R1T-Chimera
- 📄 [All Tokens (Text)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/tngtech/DeepSeek-R1T-Chimera/tokens-statistics.json)


### XiaomiMiMo/MiMo-7B-RL
- 📄 [All Tokens (Text)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/XiaomiMiMo/MiMo-7B-RL/tokens-statistics.json)


### unsloth/Phi-3.5-mini-instruct
- 📄 [All Tokens (Text)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/unsloth/Phi-3.5-mini-instruct/tokens-statistics.json)


### microsoft/phi-4
- 📄 [All Tokens (Text)](output/generated/microsoft/phi-4/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/microsoft/phi-4/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/microsoft/phi-4/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/microsoft/phi-4/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/microsoft/phi-4/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/microsoft/phi-4/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/microsoft/phi-4/tokens-statistics.json)


### microsoft/Phi-4-reasoning-plus
- 📄 [All Tokens (Text)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/microsoft/Phi-4-reasoning-plus/tokens-statistics.json)


### microsoft/bitnet-b1.58-2B-4T
- 📄 [All Tokens (Text)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/microsoft/bitnet-b1.58-2B-4T/tokens-statistics.json)


### ibm-granite/granite-4.0-tiny-preview
- 📄 [All Tokens (Text)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/ibm-granite/granite-4.0-tiny-preview/tokens-statistics.json)


### ibm-granite/granite-3.3-8b-instruct
- 📄 [All Tokens (Text)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-all.txt)
- 📄 [All Tokens (JSON)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-all.json)
- 🇬🇷 [Greek Tokens (Text)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-greek.txt)
- 🇬🇷 [Greek Tokens (JSON)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-greek.json)
- 🇮🇹 [Latin Tokens (Text)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-latin.txt)
- 🇮🇹 [Latin Tokens (JSON)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-latin.json)
- 📊 [Statistics (JSON)](output/generated/ibm-granite/granite-3.3-8b-instruct/tokens-statistics.json)



---
*Summary report generated on 2025-05-23 17:08:52 analyzing 29 models*