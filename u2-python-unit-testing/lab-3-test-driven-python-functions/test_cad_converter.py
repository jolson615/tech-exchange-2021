import unittest
from converters import cad_converter

class TestCadConverter(unittest.TestCase):
    def test_conversion_rate(self):
        self.assertAlmostEqual(cad_converter(1),1.2397)
        self.assertAlmostEqual(cad_converter(0.05),0.061985)
        self.assertAlmostEqual(cad_converter(100),123.97)
        self.assertAlmostEqual(cad_converter(2.1),2.60337)
        self.assertAlmostEqual(cad_converter(0),0.0)

    def test_input_values(self):
        self.assertRaises(ValueError, cad_converter, -1)

    def test_types(self):
        self.assertRaises(TypeError, cad_converter, "test")
        self.assertRaises(TypeError, cad_converter, False)
        self.assertRaises(TypeError, cad_converter, None)
        self.assertRaises(TypeError, cad_converter, 3+1j)

