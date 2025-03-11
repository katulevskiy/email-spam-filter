# Email Spam Filter

Email spam filter designed to help you manage and reduce unwanted emails effectively.

## Installation

To install this package, use the following command:

pip install -e .

Ensure that Python 3.6 or higher is installed on your system before proceeding with the installation.

## Usage

The basic usage of the email spam filter can be demonstrated as follows:

from email_spam_filter import main
main.main()

### Configuration Options

You can customize the behavior of the email spam filter by setting various options. Here are some common configuration settings you might adjust in your `config.json` file (or equivalent):

- **Threshold**: Adjusts sensitivity for filtering emails.
- **Whitelist**: A list of email addresses to never mark as spam.
- **Blacklist**: Addresses or domains to always be marked as spam.

Example `config.json`:

{
    "threshold": 0.7,
    "whitelist": ["trusted@example.com"],
    "blacklist": ["spammydomain.com"]
}

### Example Use Cases

1. **Basic Filtering**:
   - Run the filter on a set of emails to categorize them as spam or not.

2. **Custom Configuration**:
   - Set up specific rules in your configuration file and see how they affect email classification.

3. **Integration with Email Clients**:
   - Use this library in conjunction with popular email clients for automated spam filtering.

### Troubleshooting Tips

- **Installation Issues**: Ensure you have the correct Python version installed.
- **Configuration Errors**: Double-check syntax in your configuration file.
- **Filtering Performance**: Experiment with different threshold values to fine-tune performance.

## Testing Suite

To ensure reliability and catch regressions early, we've established a comprehensive testing suite:

### Unit Tests

Unit tests cover individual functions within the library. You can run them using:

pytest test/unit_tests.py

### Integration Tests

Integration tests verify that different parts of the application work together correctly.

Run integration tests with:

pytest test/integration_tests.py

### End-to-End Tests

For end-to-end testing, which simulates real-world usage scenarios:

pytest test/e2e_tests.py

To set up and run all tests, ensure you have `pytest` installed:

pip install pytest

Then execute the following to run the entire suite:

pytest

## Contribution

We welcome contributions from the community. If you'd like to contribute, please fork this repository and submit a pull request.

Thank you for using the Email Spam Filter!