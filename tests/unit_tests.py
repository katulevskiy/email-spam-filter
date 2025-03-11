import unittest

class TestExample(unittest.TestCase):
    
    def setUp(self):
        # Setup code before each test method is called
        self.example_data = [1, 2, 3, 4, 5]

    def tearDown(self):
        # Cleanup code after each test method is executed
        pass

    def test_sum(self):
        """Test that the sum of example data is correct."""
        result = sum(self.example_data)
        expected = 15
        self.assertEqual(result, expected)

    def test_max_value(self):
        """Test that the maximum value in the list is correct."""
        result = max(self.example_data)
        expected = 5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()