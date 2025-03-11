import unittest
from email_spam_filter import SpamFilter

class TestSpamFilterAlgorithms(unittest.TestCase):
    
    def setUp(self):
        # Setup common data for tests
        self.sample_emails = [
            {"subject": "Win a free vacation", "body": "Click here to claim now!"},
            {"subject": "Meeting at 10 AM", "body": "Please be on time."},
            {"subject": "You've won $1000!", "body": "Call this number immediately."}
        ]
        
    def test_naive_bayes_algorithm(self):
        """Test spam detection using Naive Bayes algorithm."""
        filter = SpamFilter(algorithm='naive_bayes')
        for email in self.sample_emails:
            result = filter.detect(email)
            # Replace 'expected_result' with the actual expected result based on your training data
            expected_result = True if "win" in email["body"].lower() else False
            self.assertEqual(result, expected_result)

    def test_svm_algorithm(self):
        """Test spam detection using SVM algorithm."""
        filter = SpamFilter(algorithm='svm')
        for email in self.sample_emails:
            result = filter.detect(email)
            # Replace 'expected_result' with the actual expected result based on your training data
            expected_result = True if "win" in email["body"].lower() or "call this number immediately" in email["body"].lower() else False
            self.assertEqual(result, expected_result)

    def test_rnn_algorithm(self):
        """Test spam detection using RNN algorithm."""
        filter = SpamFilter(algorithm='rnn')
        for email in self.sample_emails:
            result = filter.detect(email)
            # Replace 'expected_result' with the actual expected result based on your training data
            expected_result = True if "win" in email["body"].lower() or "call this number immediately" in email["body"].lower() else False
            self.assertEqual(result, expected_result)

    def test_cnn_algorithm(self):
        """Test spam detection using CNN algorithm."""
        filter = SpamFilter(algorithm='cnn')
        for email in self.sample_emails:
            result = filter.detect(email)
            # Replace 'expected_result' with the actual expected result based on your training data
            expected_result = True if "win" in email["body"].lower() or "call this number immediately" in email["body"].lower() else False
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()