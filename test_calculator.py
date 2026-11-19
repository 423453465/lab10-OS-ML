# https://github.com/423453465/lab10-OS-ML

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertAlmostEqual(multiply(2, 3), 6)
        self.assertAlmostEqual(multiply(-2, 3), -6)
        self.assertAlmostEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(-10, 2), -5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(144), 12)

# Do not touch this
if __name__ == "__main__":
    unittest.main()