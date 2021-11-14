import unittest
from profit_calculator import calculate_funding, calculate_campaign_costs, calculate_personnel_costs, calculate_printing_costs, calculate_profit

class TestProfitCalculator(unittest.TestCase):
    
    def test_funding_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_funding(backers=100,unit_cost=30.0),3000.0)
        self.assertAlmostEqual(calculate_funding(backers=0,unit_cost=30.0),0.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_funding, backers=-1, unit_cost=30.0)
        self.assertRaises(ValueError, calculate_funding, backers=100, unit_cost=-1.0)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_funding, backers="test")
        self.assertRaises(TypeError, calculate_funding, backers=None)
        self.assertRaises(TypeError, calculate_funding, backers=False)
        self.assertRaises(TypeError, calculate_funding, unit_cost="test")
        self.assertRaises(TypeError, calculate_funding, unit_cost=None)
        self.assertRaises(TypeError, calculate_funding, unit_cost=False)

    def test_campaign_cost_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_campaign_costs(10000),1500.0)
        self.assertAlmostEqual(calculate_campaign_costs(100),510.0)
        self.assertAlmostEqual(calculate_campaign_costs(0),500.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_campaign_costs, -1)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_campaign_costs, "test")
        self.assertRaises(TypeError, calculate_campaign_costs, None)
        self.assertRaises(TypeError, calculate_campaign_costs, False)

    def test_personnel_cost_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_personnel_costs(10000),4000.0)
        self.assertAlmostEqual(calculate_personnel_costs(100),3010.0)
        self.assertAlmostEqual(calculate_personnel_costs(0),3000.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_personnel_costs, -1)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_personnel_costs, "test")
        self.assertRaises(TypeError, calculate_personnel_costs, None)
        self.assertRaises(TypeError, calculate_personnel_costs, False)

    def test_printing_cost_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_printing_costs(1000),13250.0)
        self.assertAlmostEqual(calculate_printing_costs(10),1370.0)
        self.assertAlmostEqual(calculate_printing_costs(0),1250.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_printing_costs, -1)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_printing_costs, "test")
        self.assertRaises(TypeError, calculate_printing_costs, None)
        self.assertRaises(TypeError, calculate_printing_costs, False)

    def test_profit_calculator(self):
        #test accuracy of calculation
        self.assertAlmostEqual(calculate_profit(backers=1000,unit_cost=30.0),7250.0)
        self.assertAlmostEqual(calculate_profit(backers=0,unit_cost=30.0),-4750.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_profit, backers=-1, unit_cost=30.0)
        self.assertRaises(ValueError, calculate_profit, backers=100, unit_cost=-1.0)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_profit, backers="test")
        self.assertRaises(TypeError, calculate_profit, backers=None)
        self.assertRaises(TypeError, calculate_profit, backers=False)
        self.assertRaises(TypeError, calculate_profit, unit_cost="test")
        self.assertRaises(TypeError, calculate_profit, unit_cost=None)
        self.assertRaises(TypeError, calculate_profit, unit_cost=False)