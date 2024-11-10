import unittest
from feature2 import dot  # Importing the dot function from feature2

class TestFeature2(unittest.TestCase):
    def test_dot_positive_numbers(self):
        # Test for positive numbers
        self.assertEqual(dot(2, 3), 6, "Expected 6 for dot(2, 3)")

    def test_dot_negative_numbers(self):
        # Test for negative numbers
        self.assertEqual(dot(-2, -3), 6, "Expected 6 for dot(-2, -3)")

    def test_dot_mixed_signs(self):
        # Test for mixed signs
        self.assertEqual(dot(-2, 3), -6, "Expected -6 for dot(-2, 3)")

    def test_dot_with_zero(self):
        # Test for multiplication with zero
        self.assertEqual(dot(0, 10), 0, "Expected 0 for dot(0, 10)")


if __name__ == '__main__':
    unittest.main()
