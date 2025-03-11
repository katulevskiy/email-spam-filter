import numpy as np
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
import cProfile

class NaiveBayesSpamFilter:
    def __init__(self):
        self.word_probs = {}
        self.spam_prob = 0.0
        self.ham_prob = 0.0

    def train(self, emails, labels):
        """Train the spam filter using naive Bayes algorithm."""
        n_spams = sum(labels)
        n_hams = len(labels) - n_spams
        
        # Initialize counts
        word_counts_spam = defaultdict(int)
        word_counts_ham = defaultdict(int)
        
        # Count words in spam and ham emails
        for email, label in zip(emails, labels):
            if label == 1:  # Spam
                for word in self._tokenize(email):
                    word_counts_spam[word] += 1
            else:  # Ham
                for word in self._tokenize(email):
                    word_counts_ham[word] += 1

        # Calculate probabilities
        total_words_spam = sum(word_counts_spam.values())
        total_words_ham = sum(word_counts_ham.values())

        self.spam_prob = n_spams / len(labels)
        self.ham_prob = n_hams / len(labels)

        self.word_probs['spam'] = {word: (count + 1) / (total_words_spam + len(word_counts_spam))
                                   for word, count in word_counts_spam.items()}
        
        self.word_probs['ham'] = {word: (count + 1) / (total_words_ham + len(word_counts_ham))
                                  for word, count in word_counts_ham.items()}

    def _tokenize(self, email):
        """Tokenize the email text into words."""
        return email.lower().split()

    def predict(self, emails):
        """Predict if emails are spam or ham."""
        with ProcessPoolExecutor() as executor:
            results = list(executor.map(self._predict_single_email, emails))
        return results

    def _predict_single_email(self, email):
        """Calculate probability for a single email being spam or ham."""
        words = self._tokenize(email)
        log_prob_spam = np.log(self.spam_prob)
        log_prob_ham = np.log(self.ham_prob)

        for word in words:
            prob_word_given_spam = self.word_probs['spam'].get(word, 1 / (sum(self.word_probs['spam'].values()) + len(words)))
            prob_word_given_ham = self.word_probs['ham'].get(word, 1 / (sum(self.word_probs['ham'].values()) + len(words)))

            log_prob_spam += np.log(prob_word_given_spam)
            log_prob_ham += np.log(prob_word_given_ham)

        return 1 if log_prob_spam > log_prob_ham else 0

    def profile_training(self, emails, labels):
        """Profile the training process to identify bottlenecks."""
        cProfile.runctx('self.train(emails, labels)', globals(), locals())