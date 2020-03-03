import unittest

from Calculator import Calculator
from Csvreader import csvreader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = csvreader('TestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = csvreader('TestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_times(self):
        test_data = csvreader('TestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div(self):
        test_data = csvreader('TestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square(self):
        test_data = csvreader('TestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data = csvreader('TestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
