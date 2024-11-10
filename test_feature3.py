import unittest
from feature3 import divide  # Importing the divide function from feature3

class TestFeature3(unittest.TestCase):
    def test_divide_positive_numbers(self):
        # Test for positive numbers
        self.assertEqual(divide(6, 3), 2, "Expected 2 for divide(6, 3)")

    def test_divide_negative_numbers(self):
        # Test for negative numbers
        self.assertEqual(divide(-6, -3), 2, "Expected 2 for divide(-6, -3)")

    def test_divide_mixed_signs(self):
        # Test for mixed signs
        self.assertEqual(divide(-6, 3), -2, "Expected -2 for divide(-6, 3)")

    def test_divide_float_result(self):
        # Test for float result
        self.assertAlmostEqual(divide(7, 2), 3.5, "Expected 3.5 for divide(7, 2)")

    def test_divide_by_zero(self):
        # Test for division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()
