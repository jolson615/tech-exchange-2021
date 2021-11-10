import unittest
from items import Item

#python -m unittest test_items
class TestItems(unittest.TestCase):
    def test_argument_values(self):
        self.assertRaises(ValueError, Item, "sword", "attack", -1)
        self.assertRaises(ValueError, Item, "sword", "test", 3)

    def test_argument_types(self):
        self.assertRaises(TypeError, Item, "sword", "attack", "test")
        self.assertRaises(TypeError, Item, "sword", "attack", (3+1j))
        self.assertRaises(TypeError, Item, 1, "attack", 3)
        self.assertRaises(TypeError, Item, "sword", 1 , 3)