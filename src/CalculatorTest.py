import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

     def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)
     def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(Calculator.result, 4)





if __name__ == 'main':
    unittest.main()
