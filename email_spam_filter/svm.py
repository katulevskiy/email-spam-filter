import numpy as np
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from concurrent.futures import ProcessPoolExecutor
import cProfile

class SpamFilterSVM:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = None
    
    def fit(self, X_train, y_train):
        """
        Train the SVM model on the provided data.

        Args:
            X_train: Training features (list of emails).
            y_train: Training labels (list of 0s and 1s indicating non-spam/spam).

        Returns:
            self
        """
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        self.model = svm.SVC(kernel='linear', probability=True)
        self.model.fit(X_train_tfidf, y_train)
        return self

    def predict(self, emails):
        """
        Predict if the given list of emails are spam or not.

        Args:
            emails: List of emails to classify.

        Returns:
            List of predictions (0 for non-spam, 1 for spam).
        """
        emails_tfidf = self.vectorizer.transform(emails)
        return self.model.predict(emails_tfidf)

    def predict_parallel(self, emails):
        """
        Predict if the given list of emails are spam or not using parallel processing.

        Args:
            emails: List of emails to classify.

        Returns:
            List of predictions (0 for non-spam, 1 for spam).
        """
        num_chunks = min(8, len(emails))  # Adjust based on your CPU
        chunk_size = len(emails) // num_chunks

        with ProcessPoolExecutor() as executor:
            results = list(executor.map(
                self._process_chunk,
                [emails[i:i + chunk_size] for i in range(0, len(emails), chunk_size)]
            ))

        # Flatten the result
        return [pred for sublist in results for pred in sublist]

    def _process_chunk(self, emails_chunk):
        """
        Process a chunk of emails to classify them.

        Args:
            emails_chunk: List of emails in this chunk.

        Returns:
            List of predictions (0 for non-spam, 1 for spam) for the chunk.
        """
        return self.predict(emails_chunk)

def profile_fit_predict():
    """
    Profile the fit and predict operations using cProfile.
    """
    # Example data
    X_train = ["spam email content here", "normal email content"]
    y_train = [1, 0]
    emails_to_classify = ["email to classify", "another one"]

    spam_filter = SpamFilterSVM()
    
    profiler = cProfile.Profile()
    profiler.enable()

    # Fit the model
    spam_filter.fit(X_train, y_train)
    
    # Predict using parallel processing
    predictions = spam_filter.predict_parallel(emails_to_classify)

    profiler.disable()
    profiler.print_stats(sort='time')

# If used as a script to test the profiling
if __name__ == "__main__":
    profile_fit_predict()

This code defines an SVM-based spam filter class in `spam_filter_svm.py`. It includes methods for training (`fit`), making predictions (`predict`), and predicting using parallel processing (`predict_parallel`). The `_process_chunk` method helps with dividing the work among processes. Profiling is included to identify bottlenecks during fitting and prediction, which can be run by executing the script.