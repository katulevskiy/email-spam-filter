"""Support module for Spam Detection using Support Vector Machine (SVM)."""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

class SVMSpamFilter:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = SVC(probability=True)

    def train(self, training_data, labels):
        """Train the SVM model with provided training data and labels."""
        features = self.vectorizer.fit_transform(training_data)
        self.model.fit(features, labels)

    def predict(self, email_content):
        """Predict whether an email is spam or not using the trained SVM model."""
        features = self.vectorizer.transform([email_content])
        prediction_probabilities = self.model.predict_proba(features)[0]
        return "spam" if prediction_probabilities[1] > 0.5 else "not_spam"

    def predict_with_confidence(self, email_content):
        """Predict whether an email is spam or not and provide confidence level."""
        features = self.vectorizer.transform([email_content])
        prediction_probabilities = self.model.predict_proba(features)[0]
        return ("spam", prediction_probabilities[1]) if prediction_probabilities[1] > 0.5 else ("not_spam", prediction_probabilities[0])

# Example usage:
# spam_filter = SVMSpamFilter()
# spam_filter.train(training_emails, labels)
# result = spam_filter.predict("Your free lottery ticket is waiting!")

This `svm.py` module defines a class `SVMSpamFilter`, which includes methods for training the SVM model on given data and predicting whether an email is spam or not. The module uses scikit-learn's `SVC` (Support Vector Classifier) to implement the spam detection logic. It includes functions for both prediction and obtaining confidence scores for predictions, making it versatile and user-friendly.