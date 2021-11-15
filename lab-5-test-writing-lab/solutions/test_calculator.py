# Solutions to the calculator lab
import unittest
import calculator
from unittest import mock

class TestCalc(unittest.TestCase):
    # Write code here to test the add function
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-2, -7), -9)
        self.assertEqual(calculator.add(5.2, 0.03), 5.23)
        self.assertRaises(TypeError, calculator.add, "cat", "dog")
        self.assertRaises(TypeError, calculator.add, True, False)
        self.assertRaises(TypeError, calculator.add, [1, 2, 3], [2, 2, 2])

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-2, -7), 5)
        self.assertEqual(calculator.subtract(5.2, 0.03), 5.17)
        self.assertRaises(TypeError, calculator.subtract, "cat", "dog")
        self.assertRaises(TypeError, calculator.subtract, True, False)
        self.assertRaises(TypeError, calculator.subtract, [1, 2, 3], [2, 2, 2])

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-2, -7), 14)
        self.assertEqual(calculator.multiply(5.2, 0.03), 0.156)
        self.assertRaises(TypeError, calculator.multiply, "cat", "dog")
        self.assertRaises(TypeError, calculator.multiply, True, False)
        self.assertRaises(TypeError, calculator.multiply, [1, 2, 3], [2, 2, 2])

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(5, 2), 2.5)
        self.assertAlmostEqual(calculator.divide(5.2, 0.03), 173.3333333333)
        self.assertRaises(ValueError, calculator.divide, 10, 0)
        self.assertRaises(TypeError, calculator.divide, "cat", "dog")
        self.assertRaises(TypeError, calculator.divide, True, False)
        self.assertRaises(TypeError, calculator.divide, [1, 2, 3], [2, 2, 2])
    
    def test_tip(self):
        self.assertEqual(calculator.tip(100, 20), 120)
        self.assertEqual(calculator.tip(50, 18), 59)
        self.assertEqual(calculator.tip(23.50, 20), 28.20)
        self.assertEqual(calculator.tip(74.95, 22), 91.44)
        self.assertRaises(TypeError, calculator.tip, "cat", "dog")
        self.assertRaises(TypeError, calculator.tip, True, False)
        self.assertRaises(TypeError, calculator.tip, [1, 2, 3], [2, 2, 2])
        self.assertRaises(ValueError, calculator.tip, 50, -15)
        self.assertRaises(ValueError, calculator.tip, 50, 115)
        self.assertRaises(ValueError, calculator.tip, -50, 15)
    
    def test_scrabble_value(self):
        self.assertEqual(calculator.scrabble_value("cat"), 5)
        self.assertEqual(calculator.scrabble_value("AMAZE"), 16)
        self.assertEqual(calculator.scrabble_value("Quixotic"), 26)
        self.assertRaises(TypeError, calculator.scrabble_value, 17)
        self.assertRaises(TypeError, calculator.scrabble_value, True)
        self.assertRaises(TypeError, calculator.scrabble_value, ["cat", "dog"])
        self.assertRaises(ValueError, calculator.scrabble_value, "q")
        self.assertRaises(ValueError, calculator.scrabble_value, "trichotillomania")
        self.assertRaises(ValueError, calculator.scrabble_value, "hot dog")
        self.assertRaises(ValueError, calculator.scrabble_value, "pa$$word")
    
    def test_taxi(self):
        self.assertEqual(calculator.taxi(10, 5), 30)
        self.assertEqual(calculator.taxi(0.6, 1), 4.5)
        self.assertEqual(calculator.taxi(13.1, 0), 35.5)
        self.assertEqual(calculator.taxi(5.2, 2.25), 17)
        self.assertRaises(TypeError, calculator.taxi, "cat", "dog")
        self.assertRaises(TypeError, calculator.taxi, True, False)
        self.assertRaises(TypeError, calculator.taxi, [1, 2, 3], [2, 2, 2])
        self.assertRaises(ValueError, calculator.taxi, 50, -15)
        self.assertRaises(ValueError, calculator.taxi, -50, 15)

    def test_scientific_notation(self):
        self.assertEqual(calculator.scientific_notation(10000), "1.0*10**4")
        self.assertEqual(calculator.scientific_notation(1), "1.0*10**0")
        self.assertEqual(calculator.scientific_notation(0.00483), "4.83*10**-3")
        self.assertEqual(calculator.scientific_notation(829000), "8.29*10**5")
        self.assertEqual(calculator.scientific_notation(0.00000000000999), "9.99*10**-12")
        self.assertRaises(TypeError, calculator.scientific_notation, "cat")
        self.assertRaises(TypeError, calculator.scientific_notation, True)
        self.assertRaises(TypeError, calculator.scientific_notation, [1, 2, 3])
    
    # @mock.patch('calculator.input', create=True)
    # def test_get_numbers(self, mocked_input):
    #     mocked_input.side_effect = ['17', '42.81', 'cat', '17', 'False']
    #     self.assertEqual(calculator.get_numbers(), [17, 42.81])
    #     self.assertRaises(ValueError, calculator.get_numbers())
    #     self.assertRaises(ValueError, calculator.get_numbers())
    
    @mock.patch('calculator.input', create=True)
    def test_get_operation(self, mocked_input):
        mocked_input.side_effect = ['+', 'tip', 'sn', 'addition', 'scrabble_value']
        self.assertEqual(calculator.get_operation(), '+')
        self.assertEqual(calculator.get_operation(), 'tip')
        self.assertEqual(calculator.get_operation(), 'sn')
        with self.assertRaises(ValueError):
            calculator.get_operation()
        with self.assertRaises(ValueError):
            calculator.get_operation()

if __name__ == "__main__":
    unittest.main()