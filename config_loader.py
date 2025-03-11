import os
import json
import argparse

def load_config(config_file='config.json'):
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {config_file} not found. Using default configuration.")
        return {}
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in the config file.")

def validate_config(config):
    required_keys = ['threshold', 'whitelist', 'blacklist']
    
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required configuration key: {key}")

    if not isinstance(config['threshold'], (int, float)) or not 0 <= config['threshold'] <= 1:
        raise ValueError("Threshold must be a number between 0 and 1.")

    if not isinstance(config['whitelist'], list) or not all(isinstance(item, str) for item in config['whitelist']):
        raise ValueError("Whitelist must be a list of strings.")
    
    if not isinstance(config['blacklist'], list) or not all(isinstance(item, str) for item in config['blacklist']):
        raise ValueError("Blacklist must be a list of strings.")

def get_config_from_env():
    env_config = {
        'threshold': os.getenv('THRESHOLD'),
        'whitelist': os.getenv('WHITELIST', '').split(','),
        'blacklist': os.getenv('BLACKLIST', '').split(',')
    }
    
    # Convert threshold to float if it's set
    if env_config['threshold']:
        try:
            env_config['threshold'] = float(env_config['threshold'])
        except ValueError:
            raise ValueError("Threshold from environment variable must be a number.")
            
    return {k: v for k, v in env_config.items() if v}

def get_config_from_args():
    parser = argparse.ArgumentParser(description='Email Spam Filter Configuration')
    
    parser.add_argument('--threshold', type=float, help='Sensitivity threshold for filtering emails.')
    parser.add_argument('--whitelist', nargs='+', help='List of email addresses to never mark as spam.')
    parser.add_argument('--blacklist', nargs='+', help='Addresses or domains to always be marked as spam.')

    args = parser.parse_args()
    
    return {k: v for k, v in vars(args).items() if v is not None}

def merge_configs(configs):
    final_config = {}
    keys_to_merge = ['threshold', 'whitelist', 'blacklist']
    
    # Override priority: command-line > environment > config file
    for key in keys_to_merge:
        if key in configs['args']:
            final_config[key] = configs['args'][key]
        elif key in configs['env']:
            final_config[key] = configs['env'][key]
        else:
            final_config[key] = configs['file'].get(key, None)

    return final_config

def main():
    # Load configurations
    file_config = load_config()
    env_config = get_config_from_env()
    args_config = get_config_from_args()

    configs = {
        'file': file_config,
        'env': env_config,
        'args': args_config
    }

    # Merge configurations with priority: command-line > environment > config file
    final_config = merge_configs(configs)

    try:
        validate_config(final_config)
    except (KeyError, ValueError) as e:
        print(f"Configuration error: {e}")
        return

    # Use the validated and merged configuration for further processing
    print("Final Configuration:", final_config)

if __name__ == "__main__":
    main()