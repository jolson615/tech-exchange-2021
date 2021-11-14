import unittest
from converters import two_currency_converter

class TestTwoCurrencyConverter(unittest.TestCase):
    def test_conversion_rate(self):
        self.assertAlmostEqual(two_currency_converter("CHINA", 1, "UNITED STATES"), 0.15612802498)
        self.assertAlmostEqual(two_currency_converter("china", 1, "united states"), 0.15612802498)
        self.assertAlmostEqual(two_currency_converter("China", 1, "United States"), 0.15612802498)

        self.assertAlmostEqual(two_currency_converter("CHINA", 0.05, "UNITED STATES"), 0.00780640124902)
        self.assertAlmostEqual(two_currency_converter("CHINA", 2.1, "UNITED STATES"), 0.327868852459)
        self.assertAlmostEqual(two_currency_converter("CHINA", 0, "UNITED STATES"),0.0)

        self.assertAlmostEqual(two_currency_converter("CANADA", 100, "CHINA"), 516.657255788)
        self.assertAlmostEqual(two_currency_converter("CHINA", 100, "INDIA"), 1170.96018735)
        self.assertAlmostEqual(two_currency_converter("INDIA", 100, "JAPAN"), 152.04)
        self.assertAlmostEqual(two_currency_converter("JAPAN", 100, "MEXICO"), 18.0224502324)
        self.assertAlmostEqual(two_currency_converter("MEXICO", 100, "SOUTH KOREA"), 5717.19137755)
        self.assertAlmostEqual(two_currency_converter("SOUTH KOREA", 100, "TAIWAN"), 2.3686315897)
        self.assertAlmostEqual(two_currency_converter("TAIWAN", 100, "UNITED KINGDOM"), 4.91771469637)
        self.assertAlmostEqual(two_currency_converter("UNITED KINGDOM", 100, "UNITED STATES"), 73.0673681134)
        self.assertAlmostEqual(two_currency_converter("UNITED STATES", 100, "CANADA"), 123.97)

    def test_input_values(self):
        self.assertRaises(ValueError, two_currency_converter, "CHINA", -1, "UNITED STATES")
        self.assertRaises(ValueError, two_currency_converter, "", 1, "UNITED STATES")
        self.assertRaises(ValueError, two_currency_converter, "test", 1, "UNITED STATES")
        self.assertRaises(ValueError, two_currency_converter, "CHINA", 1, "")
        self.assertRaises(ValueError, two_currency_converter, "CHINA", 1, "test")

    def test_types(self):
        self.assertRaises(TypeError, two_currency_converter, "CHINA", "true", "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, "CHINA", False, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, "CHINA", None, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, "CHINA", 3+1j, "UNITED STATES")

        self.assertRaises(TypeError, two_currency_converter, 100, 100, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, 0.05, 100, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, 3+1j, 100, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, False, 100, "UNITED STATES")
        self.assertRaises(TypeError, two_currency_converter, None, 100, "UNITED STATES")

        self.assertRaises(TypeError, two_currency_converter, "CHINA", 100, 100)
        self.assertRaises(TypeError, two_currency_converter, "CHINA", 100, 0.05)
        self.assertRaises(TypeError, two_currency_converter, "CHINA", 100, 3+1j)
        self.assertRaises(TypeError, two_currency_converter, "CHINA", 100, False)
        self.assertRaises(TypeError, two_currency_converter, "CHINA", 100, None)

