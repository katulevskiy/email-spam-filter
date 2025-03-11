import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class NaiveBayesSpamFilter:
    def __init__(self):
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())

    def train(self, emails, labels):
        """Train the Naive Bayes spam filter model with labeled data."""
        self.model.fit(emails, labels)

    def predict(self, email):
        """Predict whether a single email is spam or not.
        
        Args:
            email (str): The content of the email to classify.

        Returns:
            str: 'spam' if the email is predicted as spam, else 'ham'.
        """
        prediction = self.model.predict([email])
        return 'spam' if prediction[0] == 1 else 'ham'

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    emails = [
        "Congratulations! You've won a free ticket to Bahamas.",
        "Hi Bob, are we still on for the meeting tomorrow?",
        "Get cheap loans now with no credit check!",
        "Don't forget about the team outing this Friday."
    ]
    
    labels = [1, 0, 1, 0]  # 1 indicates spam, 0 indicates ham

    filter = NaiveBayesSpamFilter()
    filter.train(emails, labels)

    test_email = "Win a free vacation to the Maldives!"
    print(filter.predict(test_email))  # Output: 'spam'

This script defines a `NaiveBayesSpamFilter` class that leverages Scikit-learn's `MultinomialNB` for spam detection. The implementation includes methods to train the model and predict whether an email is spam. It also provides an example usage section demonstrating how to use this class with sample data.