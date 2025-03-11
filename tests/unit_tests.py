import unittest

class TestExample(unittest.TestCase):
    
    def setUp(self):
        # Setup common data for tests
        self.example_data = list(range(1, 6))

    def test_sum(self):
        """Ensure sum of example data matches expected value."""
        result = sum(self.example_data)
        expected = 15
        self.assertEqual(result, expected)

    def test_max_value(self):
        """Verify the maximum value in the list is correct."""
        result = max(self.example_data)
        expected = 5
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()