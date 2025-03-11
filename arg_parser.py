import argparse
import json
import os

def load_config(file_path='config.json'):
    """Load configuration from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file {file_path} not found. Using default settings.")
    except json.JSONDecodeError:
        print("Error decoding the config.json file. Please check its format.")
    
    # Return a default configuration if file is missing or invalid
    return {
        'threshold': 0.7,
        'whitelist': [],
        'blacklist': []
    }

def validate_config(config):
    """Validate the configuration settings."""
    try:
        threshold = float(config.get('threshold', 0.7))
        whitelist = config.get('whitelist', [])
        blacklist = config.get('blacklist', [])

        if not (0 <= threshold <= 1):
            raise ValueError("Threshold must be between 0 and 1.")

        # Ensure whitelist and blacklist are lists
        if not isinstance(whitelist, list) or not all(isinstance(item, str) for item in whitelist):
            raise ValueError("Whitelist must be a list of strings.")
        
        if not isinstance(blacklist, list) or not all(isinstance(item, str) for item in blacklist):
            raise ValueError("Blacklist must be a list of strings.")

    except (ValueError, TypeError) as e:
        print(f"Configuration validation error: {e}")
        return False

    return {
        'threshold': threshold,
        'whitelist': whitelist,
        'blacklist': blacklist
    }

def main():
    parser = argparse.ArgumentParser(description='Email Spam Filter Configuration')
    
    # Add command-line arguments
    parser.add_argument('--config', type=str, help="Path to the configuration file", default='config.json')
    parser.add_argument('--threshold', type=float, help="Sensitivity threshold for spam detection")
    parser.add_argument('--whitelist', nargs='*', help="List of email addresses to whitelist")
    parser.add_argument('--blacklist', nargs='*', help="List of domains or emails to blacklist")

    args = parser.parse_args()

    # Load configuration from file
    config = load_config(args.config)

    # Override with environment variables if present
    env_threshold = os.getenv('THRESHOLD')
    env_whitelist = os.getenv('WHITELIST', '').split(',')
    env_blacklist = os.getenv('BLACKLIST', '').split(',')

    if env_threshold:
        try:
            config['threshold'] = float(env_threshold)
        except ValueError:
            print("Invalid threshold value in environment variable.")

    # Override with command-line arguments
    if args.threshold is not None:
        config['threshold'] = args.threshold

    if args.whitelist:
        config['whitelist'] = args.whitelist

    if args.blacklist:
        config['blacklist'] = args.blacklist

    # Validate the final configuration
    valid_config = validate_config(config)
    
    if valid_config:
        print(f"Configuration Loaded: {valid_config}")
    else:
        print("Using default settings due to configuration errors.")

if __name__ == "__main__":
    main()