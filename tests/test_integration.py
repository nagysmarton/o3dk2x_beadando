import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_and_multiply(self):
        calc = Calculator()
        result = calc.multiply(calc.add(2, 3), 4)
        self.assertEqual(result, 20)

if __name__ == "__main__":
    unittest.main()
