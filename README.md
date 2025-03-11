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

#### Basic Filtering

1. **Run the filter on a set of emails**:
   - Load your email data into the system.
   - Execute the spam filter to categorize them as spam or not.

2. **Custom Configuration**:
   - Edit `config.json` with specific rules.
   - Observe how these settings affect email classification.

#### Integration with Email Clients

- **Integrate with Gmail**:

  1. Set up a Google Cloud Project and enable the Gmail API.
  2. Install the necessary client library: 
     ```bash
     pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
     ```
  3. Use OAuth to authenticate and access your Gmail account.
  4. Filter incoming emails through the spam filter before they reach your inbox.

- **Integrate with Outlook**:

  1. Create an app registration in Azure Active Directory for accessing Microsoft Graph API.
  2. Install MSAL (Microsoft Authentication Library) for Python:
     ```bash
     pip install msal
     ```
  3. Use OAuth to authenticate and access your Outlook account.
  4. Apply the spam filter to incoming emails using the Microsoft Graph API.

#### Automated Workflows

- **Setup with Cron Jobs**:

  1. Write a script that pulls new emails from your mailbox at regular intervals.
  2. Use cron jobs to schedule this script:
     ```bash
     crontab -e
     ```
  3. Add a line to execute the script every hour, for example:
     ```bash
     0 * * * * /usr/bin/python3 /path/to/your/script.py
     ```

- **Using Zapier**:

  1. Create a Zap that triggers on new emails in Gmail.
  2. Use Webhooks by Zapier to send email data to your filter.
  3. Process the emails and update their status based on the spam filter's output.

### Troubleshooting Tips

- **Installation Issues**: Ensure you have the correct Python version installed. Check for any missing dependencies in the error messages and install them using pip.

- **Configuration Errors**: Double-check syntax in your configuration file. Make sure JSON is properly formatted, with matching braces and quotes.

- **Filtering Performance**: Experiment with different threshold values to fine-tune performance. Adjust the sensitivity settings based on the spam characteristics of your email traffic.

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