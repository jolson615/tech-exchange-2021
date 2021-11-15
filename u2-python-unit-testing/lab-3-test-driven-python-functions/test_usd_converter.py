import unittest
from converters import usd_converter

class TestUsdConverter(unittest.TestCase):
    def test_conversion_rate(self):
        self.assertAlmostEqual(usd_converter("CHINA", 1), 0.15612802498)
        self.assertAlmostEqual(usd_converter("China", 1), 0.15612802498)
        self.assertAlmostEqual(usd_converter("china", 1), 0.15612802498)
        
        self.assertAlmostEqual(usd_converter("CHINA", 0.05), 0.00780640124902)
        self.assertAlmostEqual(usd_converter("CHINA", 2.1), 0.327868852459)
        self.assertAlmostEqual(usd_converter("CHINA", 0),0.0)

        self.assertAlmostEqual(usd_converter("CANADA",100), 80.664676938)
        self.assertAlmostEqual(usd_converter("CHINA",100), 15.612802498)
        self.assertAlmostEqual(usd_converter("INDIA",100), 1.33333333333)
        self.assertAlmostEqual(usd_converter("JAPAN",100), 0.876962202929)
        self.assertAlmostEqual(usd_converter("MEXICO", 100), 4.8659432631)
        self.assertAlmostEqual(usd_converter("SOUTH KOREA", 100), 0.0851107290585)
        self.assertAlmostEqual(usd_converter("TAIWAN", 100), 3.59324469996)
        self.assertAlmostEqual(usd_converter("UNITED KINGDOM", 100), 73.0673681134)
        self.assertAlmostEqual(usd_converter("UNITED STATES", 100), 100)

    def test_input_values(self):
        self.assertRaises(ValueError, usd_converter, "CHINA", -1)
        self.assertRaises(ValueError, usd_converter, "", 1)
        self.assertRaises(ValueError, usd_converter, "test", 1)

    def test_types(self):
        self.assertRaises(TypeError, usd_converter, "CHINA", "true")
        self.assertRaises(TypeError, usd_converter, "CHINA", False)
        self.assertRaises(TypeError, usd_converter, "CHINA", None)
        self.assertRaises(TypeError, usd_converter, "CHINA", 3+1j)

        self.assertRaises(TypeError, usd_converter, 100, 100)
        self.assertRaises(TypeError, usd_converter, 0.05, 100)
        self.assertRaises(TypeError, usd_converter, 3+1j, 100)
        self.assertRaises(TypeError, usd_converter, False, 100)
        self.assertRaises(TypeError, usd_converter, None, 100)

