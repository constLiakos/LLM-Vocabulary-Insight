from transformers import PreTrainedTokenizerFast
import unicodedata
import json
from os import path, makedirs
import errno
from collections import Counter
from huggingface_hub import hf_hub_download, errors
from jinja2 import Environment, FileSystemLoader

from datetime import datetime

class Config():
    def __init__(self, model_name:str):
        self.model_name = model_name
        self.output_path = path.join("output", "generated", model_name)
        self.output_dir = path.join(self.output_path, self.model_name.replace('/', '_'))
        # Tokenizer File Path
        self.tokenizer_path = path.join("output", "modelfiles", model_name)
        self.tokenizer_filename = path.join(self.tokenizer_path, "tokenizer.json")
        # Output Reports path
        # self.reports_path = path.join("output", "reports", "greek")
        # Tokens Output Filename
        self.tokens_all_output_filename = path.join(self.output_path, "tokens-all.txt")
        self.tokens_all_json_output_filename = path.join(self.output_path, "tokens-all.json")
        self.tokens_greek_output_filename = path.join(self.output_path, "tokens-greek.txt")
        self.tokens_latin_output_filename = path.join(self.output_path, "tokens-latin.txt")
        self.tokens_greek_json_output_filename = path.join(self.output_path, "tokens-greek.json")
        self.tokens_latin_json_output_filename = path.join(self.output_path, "tokens-latin.json")
        self.tokens_statistics_filename=path.join(self.output_path, "tokens-statistics.json")

    @property
    def markdown_report_filename(self):
        return path.join(self.output_dir, f"{self.model_name.replace('/', '_')}_vocabulary_report.md")

def create_dirs(model_config:Config):
    makedirs(model_config.tokenizer_path, exist_ok=True)
    makedirs(model_config.output_path, exist_ok=True)
    # makedirs(model_config.reports_path, exist_ok=True)

def download_tokenizer(model_config:Config):
    if not path.exists(model_config.tokenizer_filename):
        try:
            hf_hub_download(repo_id=model_config.model_name, filename="tokenizer.json", local_dir=model_config.tokenizer_path)
        except errors.RepositoryNotFoundError:
            print(f"Repository Not Found for model: {model_config.model_name}")
            return False
        except:
            return False
    return True

def is_greek(token):
    """Check if a token contains any Greek characters."""
    for char in token:
        code_point = ord(char)
        # Greek ranges: 0x370-0x3FF
        is_greek_char = (0x370 <= code_point <= 0x3FF)
        if is_greek_char:
            return True
    return False

# def is_latin(token):
#     """Check if a token contains any Latin characters."""
#     for char in token:
#         code_point = ord(char)
#         # Basic Latin ranges: A-Z (65-90) and a-z (97-122)
#         is_latin_char = (65 <= code_point <= 90) or (97 <= code_point <= 122)
#         if is_latin_char:
#             return True
#     return False

def is_latin(token):
    """Check if token contains Latin characters and exclude special tokens with <> or []"""
    import re
    
    # Exclude tokens that are special tokens (entirely wrapped in <> or [])
    token_stripped = token.strip()
    if (token_stripped.startswith('<') and token_stripped.endswith('>')) or \
       (token_stripped.startswith('[') and token_stripped.endswith(']')):
        return False
    
    # Check for Latin characters (basic Latin alphabet)
    latin_pattern = re.compile(r'[a-zA-Z]')
    return bool(latin_pattern.search(token))

def tokens_alphabet_statistics(json_data:json):
    total_pairs = len(json_data)
    char_presence = Counter()
    
    # Count unique appearances in each string
    for text in json_data.values():
        # Convert string to set to count each character once
        unique_chars = set(text)
        for char in unique_chars:
            char_presence[char] += 1
    
    # Calculate percentage of presence
    char_statistics = {
        char: {
            'count': count,
            'percentage': "{:.2f}%".format((count/total_pairs) * 100)
        }
        for char, count in char_presence.items()
    }
    
    # Sort by frequency
    sorted_stats = dict(sorted(char_statistics.items(), 
                             key=lambda x: x[1]['count'], 
                             reverse=True))
    return sorted_stats

def vocabulary_extractor(model_config:Config):
    # Create directories if they dont exist
    create_dirs(model_config)
    tokenizer_loaded = download_tokenizer(model_config)
    if not tokenizer_loaded:
        print(f"Error loading tokenizer. Model: {model_config.model_name}")
        return
    # Load the tokenizer from the provided JSON file
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=model_config.tokenizer_filename)
    vocab_size = tokenizer.vocab_size

    # List to hold formatted token information
    tokens_all_formatted = []
    tokens_formatted_greek = []
    tokens_formatted_latin = []
    tokens_all_formatted_obj={}
    tokens_formatted_greek_obj = {}
    tokens_formatted_latin_obj = {}

    # Generate tokens and their corresponding decoded strings
    for i in range(1, vocab_size):
        token = tokenizer.decode(i)
        # Format each token into a string with index and token decoded form
        tokens_all_formatted.append(f"{i}: {token}")
        tokens_all_formatted_obj[i]=token

        if is_greek(token):
            tokens_formatted_greek.append(f"{i}: {token}")
            tokens_formatted_greek_obj[i] = token

        if is_latin(token):
            tokens_formatted_latin.append(f"{i}: {token}")
            tokens_formatted_latin_obj[i] = token

    vocabulary_greek_size = len(tokens_formatted_greek_obj.keys())
    vocabulary_latin_size = len(tokens_formatted_latin_obj.keys())
    greek_percentage = (vocabulary_greek_size/vocab_size)*100
    latin_percentage = (vocabulary_latin_size/vocab_size)*100
    
    model_statistics = {
        "vocab_all_size": vocab_size,
        "vocab_greek_size": vocabulary_greek_size,
        "vocab_latin_size": vocabulary_latin_size,
        "vocabulary_greek_percentage": "{:.2f}%".format(greek_percentage),
        "vocabulary_latin_percentage": "{:.2f}%".format(latin_percentage),
        "greek_percentage_raw": greek_percentage,
        "latin_percentage_raw": latin_percentage,
        "stats_greek": tokens_alphabet_statistics(tokens_formatted_greek_obj)
    }

    # Join the formatted tokens into one text file
    tokens_all_range_joined = "\n".join(tokens_all_formatted)
    token_greek_range_joined = "\n".join(tokens_formatted_greek)
    token_latin_range_joined = "\n".join(tokens_formatted_latin)
    tokens_greek_json_dump = json.dumps(tokens_formatted_greek_obj,indent=4, ensure_ascii=False)
    tokens_latin_json_dump = json.dumps(tokens_formatted_latin_obj,indent=4, ensure_ascii=False)
    tokens_all_json_dump = json.dumps(tokens_all_formatted_obj,indent=4, ensure_ascii=False)

    model_statistics_str = json.dumps(model_statistics,indent=4, ensure_ascii=False)

    # Write the formatted tokens to the output filename
    # All
    with open(model_config.tokens_all_output_filename, "w") as f:
        f.write(tokens_all_range_joined)
    with open(model_config.tokens_all_json_output_filename, "w") as f:
        f.write(tokens_all_json_dump)
    # Greek
    with open(model_config.tokens_greek_output_filename, "w") as f:
        f.write(token_greek_range_joined)
    with open(model_config.tokens_greek_json_output_filename, "w") as f:
        f.write(tokens_greek_json_dump)
    # Latin
    with open(model_config.tokens_latin_output_filename, "w") as f:
        f.write(token_latin_range_joined)
    with open(model_config.tokens_latin_json_output_filename, "w") as f:
        f.write(tokens_latin_json_dump)
    # Statistics
    with open(model_config.tokens_statistics_filename, "w") as f:
        f.write(model_statistics_str)

    generate_markdown_report(model_config, model_statistics, 
                           tokens_formatted_greek_obj, 
                           tokens_formatted_latin_obj)
    
    # Return model data for summary report
    return {
        'model_name': model_config.model_name,
        'stats': model_statistics,
        'greek_tokens': tokens_formatted_greek_obj,
        'latin_tokens': tokens_formatted_latin_obj,
        'files': {
            'tokens_all_output': model_config.tokens_all_output_filename,
            'tokens_all_json_output': model_config.tokens_all_json_output_filename,
            'tokens_greek_output': model_config.tokens_greek_output_filename,
            'tokens_greek_json_output': model_config.tokens_greek_json_output_filename,
            'tokens_latin_output': model_config.tokens_latin_output_filename,
            'tokens_latin_json_output': model_config.tokens_latin_json_output_filename,
            'tokens_statistics': model_config.tokens_statistics_filename
        }
    }

def generate_markdown_report(model_config: Config, stats: dict, 
                           greek_tokens: dict, latin_tokens: dict):
    """Generate a comprehensive markdown report using Jinja2"""
    
    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader('templates'),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    # Add custom filters
    def number_format(value):
        return f"{value:,}"
    
    env.filters['number_format'] = number_format
    
    # Load template
    template = env.get_template('model_report.md.j2')
    
    # Prepare template data
    template_data = {
        'model_name': model_config.model_name,
        'stats': stats,
        'greek_sample': list(greek_tokens.items())[:20],
        'latin_sample': list(latin_tokens.items())[:20],
        'generation_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'files': {
            'tokens_all_output': path.basename(model_config.tokens_all_output_filename),
            'tokens_all_json_output': path.basename(model_config.tokens_all_json_output_filename),
            'tokens_greek_output': path.basename(model_config.tokens_greek_output_filename),
            'tokens_greek_json_output': path.basename(model_config.tokens_greek_json_output_filename),
            'tokens_latin_output': path.basename(model_config.tokens_latin_output_filename),
            'tokens_latin_json_output': path.basename(model_config.tokens_latin_json_output_filename),
            'tokens_statistics': path.basename(model_config.tokens_statistics_filename)
        }
    }
    
    # Render template
    markdown_content = template.render(**template_data)
    
    # Write markdown file
    markdown_filename = path.join(
        path.dirname(model_config.tokens_statistics_filename),
        f"{model_config.model_name.replace('/', '_')}_vocabulary_report.md"
    )
    
    with open(markdown_filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print(f"✅ Markdown report generated: {markdown_filename}")
    return markdown_filename

def create_summarization_report(models_data, output_filename):
    """Generate a comprehensive markdown report for all models"""
    from jinja2 import Environment, FileSystemLoader
    from datetime import datetime
    import os
    
    # Setup Jinja2 environment
    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(os.path.join(template_dir, 'templates')))
    
    # Add number formatting filter
    def number_format(value):
        return f"{value:,}"
    
    env.filters['number_format'] = number_format
    
    # Load the summary template
    template = env.get_template('models_summary_report.md.j2')
    
    # Calculate overall statistics
    total_models = len(models_data)
    total_vocab_size = sum(model['stats']['vocab_all_size'] for model in models_data)
    total_greek_tokens = sum(model['stats']['vocab_greek_size'] for model in models_data)
    total_latin_tokens = sum(model['stats']['vocab_latin_size'] for model in models_data)
    
    # Find model with highest/lowest Greek percentage
    greek_percentages = [(model['model_name'], model['stats']['vocab_greek_size'] / model['stats']['vocab_all_size'] * 100) 
                        for model in models_data]
    best_greek_model = max(greek_percentages, key=lambda x: x[1])
    worst_greek_model = min(greek_percentages, key=lambda x: x[1])
    
    overall_stats = {
        'total_models': total_models,
        'total_vocab_size': total_vocab_size,
        'total_greek_tokens': total_greek_tokens,
        'total_latin_tokens': total_latin_tokens,
        'avg_vocab_size': total_vocab_size // total_models if total_models > 0 else 0,
        'avg_greek_percentage': (total_greek_tokens / total_vocab_size * 100) if total_vocab_size > 0 else 0,
        'avg_latin_percentage': (total_latin_tokens / total_vocab_size * 100) if total_vocab_size > 0 else 0,
        'best_greek_model': best_greek_model,
        'worst_greek_model': worst_greek_model
    }
    
    # Render the template
    rendered = template.render(
        models=models_data,
        overall_stats=overall_stats,
        generation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    
    # Write the report
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(rendered)
    
    print(f"✅ Summary report generated: {output_filename}")

def main():
    models_data = []
    
    # Read models from file like the original
    with open("models.txt", "r") as file:
        for line in file:
            model_name = line.strip()
            if model_name and not model_name.startswith('#'):  # Skip empty lines and comments
                model_config = Config(model_name)
                print(f"Processing model: {model_name}")
                
                model_data = vocabulary_extractor(model_config)
                if model_data:
                    models_data.append(model_data)
    
    # Generate the summary report
    if models_data:
        report_file = path.join("README.md")
        create_summarization_report(models_data, report_file)
        print(f"✅ Processed {len(models_data)} models successfully")
    else:
        print("❌ No models were processed successfully")

if __name__ == "__main__":
    main()
