import unittest
from feature1 import sum  # Importing the sum function from feature1

class TestFeature1(unittest.TestCase):
    def test_sum_positive_numbers(self):
        # Test for positive numbers
        self.assertEqual(sum(2, 3), 5, "Expected 5 for sum(2, 3)")
        self.assertEqual(sum(12, 23), 35, "Expected 35 for sum(12, 23)")

    def test_sum_negative_numbers(self):
        # Test for negative numbers
        self.assertEqual(sum(-2, -3), -5, "Expected -5 for sum(-2, -3)")

    def test_sum_zero(self):
        # Test for zero
        self.assertEqual(sum(0, 0), 0, "Expected 0 for sum(0, 0)")

if __name__ == '__main__':
    unittest.main()
