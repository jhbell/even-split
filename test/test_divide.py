from src.divide import divide
from unittest import TestCase

class TestDivide(TestCase):
    """
    Test the divide function located in src/divide.py
    """
    def test_simple(self):
        self.assertEqual(divide(10, 2), 5)

    def test_decimal(self):
        self.assertEqual(divide(7.0, 4), 1.75)

    def test_divide_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(12, 0)
