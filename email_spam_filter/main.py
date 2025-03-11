"""Main module for email-spam-filter."""

import os

class SpamFilter:
    """Class for handling multiple spam detection algorithms."""
    
    def __init__(self, algorithm='naive_bayes'):
        """Initialize with a default or specified algorithm."""
        self.algorithm = algorithm
        self.algorithms = {
            'naive_bayes': self._naive_bayes_filter,
            'svm': self._svm_filter,
            # Additional algorithms can be added here
        }
    
    def run_spam_filter(self, email_content):
        """Run the selected spam detection algorithm on the given content."""
        if self.algorithm in self.algorithms:
            return self.algorithms[self.algorithm](email_content)
        else:
            raise ValueError(f"Algorithm '{self.algorithm}' is not supported.")
    
    def _naive_bayes_filter(self, email_content):
        """Placeholder for Naive Bayes spam detection logic."""
        # Future implementation of naive bayes filtering logic goes here.
        pass
    
    def _svm_filter(self, email_content):
        """Placeholder for SVM spam detection logic."""
        # Future implementation of svm filtering logic goes here.
        pass

def print_greeting():
    """Print a greeting message."""
    print("Hello from email-spam-filter!")

def main():
    """Run the main functions for the application."""
    spam_filter = SpamFilter(algorithm='naive_bayes')
    
    # Example usage with placeholder content
    example_email_content = "This is an example email content."
    try:
        result = spam_filter.run_spam_filter(example_email_content)
        print(f"Spam detection result: {result}")
    except ValueError as e:
        print(e)

    print_greeting()

if __name__ == "__main__":
    main()