# Email Spam Detection Guide

Welcome to the comprehensive guide for using the Email Spam Filter. This document provides detailed usage scenarios and examples designed to help you make the most of this tool in real-world applications. We cover everything from basic setup to advanced integration with popular email clients and automated workflows.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Filtering Example](#basic-filtering-example)
3. **[Integration with Email Clients](#integration-with-email-clients)**
    - Gmail Integration
    - Outlook Integration
4. [Automated Workflows](#automated-workflows)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Getting Started

Before you begin, ensure that Python 3.6 or higher is installed on your system and that the email spam filter package is installed using:

pip install -e .

Next, create a `config.json` file in the root directory of your project with the following structure to customize the behavior of the filter:

{
    "threshold": 0.7,
    "whitelist": ["trusted@example.com"],
    "blacklist": ["spammydomain.com"]
}

## Basic Filtering Example

To perform basic email filtering, follow these steps:

1. **Import and Initialize**: Import the main module from your package.

   ```python
   from email_spam_filter import main
   ```

2. **Run the Filter**: Execute the filter function to classify emails as spam or not based on your configuration.

   ```python
   main.main()
   ```

## Integration with Email Clients

### Gmail Integration

To integrate the spam filter with Gmail, use Google Apps Script:

1. Open Google Drive and create a new Google Apps Script.
2. Use the following script to connect your email filtering logic.

   ```javascript
   function filterSpam() {
       var threads = GmailApp.search('is:unread');
       for (var i = 0; i < threads.length; i++) {
           var messages = threads[i].getMessages();
           for (var j = 0; j < messages.length; j++) {
               var emailBody = messages[j].getPlainBody();
               
               // Call the Python script or an equivalent API endpoint
               if (isSpam(emailBody)) { // Define isSpam to call your filter logic
                   GmailApp.moveThreadToArchive(threads[i]);
                   Logger.log('Archived: ' + threads[i].getMessages()[0].getSubject());
               }
           }
       }
   }

   function isSpam(body) {
       // Implement a call to the Python script or use an external API
       return body.includes('spammy'); // Simplified logic for demonstration purposes
   }
   ```

3. Run `filterSpam` from the Apps Script editor to classify and archive spam emails.

### Outlook Integration

For Outlook users, leverage Microsoft Power Automate:

1. Create a new flow in Power Automate.
2. Set up an action that triggers on receiving a new email.
3. Use a custom connector or HTTP request to run your filter logic on the email body.
4. Conditionally move emails marked as spam to a specific folder.

## Automated Workflows

To automate spam filtering, consider setting up cron jobs (on Unix-like systems) or Task Scheduler tasks (on Windows):

1. **Cron Job Example**:

   Create a shell script `run_filter.sh` with the following content:

   ```bash
   #!/bin/bash
   python -m email_spam_filter.main
   ```

2. Schedule the script to run at regular intervals by adding an entry to your crontab:

   ```bash
   0 * * * * /path/to/run_filter.sh
   ```

## Troubleshooting Common Issues

### Installation Issues

- Ensure you have Python 3.6 or higher installed.
- Use a virtual environment for dependency management.

### Configuration Errors

- Double-check your `config.json` file for syntax errors and valid JSON structure.
- Verify that all configuration parameters are correctly defined and correspond to the expected data types.

### Filtering Accuracy

- Adjust the spam filter threshold in `config.json` if you experience false positives or negatives.
- Regularly update whitelists and blacklists to improve accuracy.

By following these guidelines, you should be able to effectively use and customize the Email Spam Filter for your specific needs. If further issues arise, consider reaching out through community forums or issue trackers associated with this tool.