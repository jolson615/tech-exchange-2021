import unittest
from hero import Hero

#python3 -m unittest test_hero
class TestHero(unittest.TestCase):
    def test_argument_values(self):
        self.assertRaises(ValueError, Hero.check_death, self, -1)

    def test_argument_types(self):
        self.assertRaises(TypeError, Hero, 3)
        self.assertRaises(TypeError, Hero, None)
        self.assertRaises(TypeError, Hero.get_item, self, "test")
        self.assertRaises(TypeError, Hero.get_item, self, 1)
        self.assertRaises(TypeError, Hero.check_death, self, "Test")
        self.assertRaises(TypeError, Hero.check_death, self, None)