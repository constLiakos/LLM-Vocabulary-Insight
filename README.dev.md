# LLM Vocabulary Insight

A comprehensive tokenizer analysis tool that evaluates multilingual capabilities of Large Language Models (LLMs) by examining their vocabulary distributions across different languages.

## 🎯 Overview

LLM Vocabulary Insight provides deep analysis of how well different transformer-based models handle various languages through their tokenizer vocabularies. The tool generates detailed reports on token distribution and character coverage.

## ✨ Features

- **Greek Language Analysis**: Comprehensive Greek alphabet and character support
- **Comprehensive Reports**: Individual model reports and comparative summaries
- **Token Classification**: Automatic categorization of tokens by Greek script detection
- **Statistical Analysis**: Character distribution, coverage percentages, and performance metrics
- **Multiple Output Formats**: JSON data files and markdown reports
- **Batch Processing**: Analyze multiple models simultaneously
- **Future Support**: Planned expansion to Latin, Cyrillic, and other alphabets

## 📊 Language Reports

### Currently Available
- 🇬🇷 [Greek Vocabulary Analysis](reports/greek/models_summary.md)

### 🚧 Coming Soon
- 🇮🇹 Latin alphabet analysis
- 🇷🇺 Cyrillic script support
- 🌍 Multilingual comparative analysis
- 🔤 Additional writing systems

## 🚀 Quick Start

### Prerequisites
```bash
pip install transformers huggingface_hub jinja2
```

### Basic Usage
1. Add model names to `models.txt` (one per line):
```
ilsp/Meltemi-7B-Instruct-v1.5
ilsp/Llama-Krikri-8B-Instruct
Qwen/Qwen3-0.6B
```

2. Run the analysis:
```bash
python llm_vocabulary_insight.py
```

3. View generated reports in the `output/reports/` directory

## 📁 Project Structure

```
├── llm_vocabulary_insight.py          # Main analysis script
├── models.txt                      # List of models to analyze
├── templates/                      # Jinja2 report templates
│   ├── model_report.md.j2         # Individual model template
│   └── models_summary_report.md.j2 # Summary report template
└── output/
    ├── reports/                    # Generated markdown reports
    │   └── greek/                  # Greek language analysis
    ├── generated/                  # Raw token data (JSON/TXT)
    └── modelfiles/               # Downloaded tokenizer files
```

## 📈 What You Get

### For Each Model:
- **Vocabulary Statistics**: Total size, Greek token distribution percentages
- **Token Samples**: Examples of Greek tokens with their IDs
- **Character Analysis**: Most common Greek characters and their frequencies
- **Visual Charts**: ASCII-based distribution visualizations

### Summary Reports:
- **Performance Rankings**: Models ranked by Greek language support
- **Comparative Analysis**: Side-by-side vocabulary comparisons
- **Overall Statistics**: Aggregate metrics across all analyzed models

## 🔧 Configuration

Currently optimized for Greek analysis. Future versions will support:

```python
# Planned multi-language support
config = Config(model_name, target_languages=['greek', 'latin', 'cyrillic'])

# Customize output directories
config.reports_dir = "custom_reports/"
```

## 🤝 Contributing

1. Fork the repository
2. Help add support for new languages by creating detection functions
3. Enhance templates for better visualizations
4. Submit pull requests with improvements

**Particularly welcome contributions for:**
- Latin alphabet detection logic
- Cyrillic script analysis
- Additional writing systems (Arabic, Chinese, etc.)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Transformers](https://huggingface.co/transformers/) library
- Report generation powered by [Jinja2](https://jinja.palletsprojects.com/)
- Model downloads via [Hugging Face Hub](https://huggingface.co/docs/huggingface_hub/)

---

**Star ⭐ this repository if you find it useful for your Greek NLP research!**