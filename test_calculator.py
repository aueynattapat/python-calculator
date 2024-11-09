import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self): #a + b
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(18, 18), 36)
        self.assertEqual(self.calc.add(18, 2), 20)

    def test_subtract(self): 
        self.assertEqual(self.calc.subtract(55, 15), 40)
        self.assertEqual(self.calc.subtract(27, 18), 9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 8), 40)
        self.assertEqual(self.calc.multiply(12, 9), 108)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(18, 6), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(18, 5), 3)
        self.assertEqual(self.calc.modulo(27, 3), 0)


if __name__ == '__main__':
    unittest.main()