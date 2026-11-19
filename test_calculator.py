# https://github.com/423453465/lab10-OS-ML
# Partner 1: Owen Staples
# Partner 2: Chengxi Li

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-4,-6), -10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 4), -1)
        self.assertEqual(sub(-3,-2), -1)
        self.assertEqual(sub(0, 5), -5)

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

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 5)
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-2, 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(144), 12)

# Do not touch this
if __name__ == "__main__":
    unittest.main()