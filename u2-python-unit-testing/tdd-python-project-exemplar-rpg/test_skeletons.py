import unittest
from skeletons import Skeleton

#run the following in your console to test:
#python -m unittest test_skeletons
class TestSkeleton(unittest.TestCase):
    def test_argument_values(self):
        self.assertRaises(ValueError, Skeleton.check_death, self, -1)

    def test_argument_types(self):
        self.assertRaises(TypeError, Skeleton, "test")
        self.assertRaises(TypeError, Skeleton, None)
        self.assertRaises(TypeError, Skeleton.check_death, self, "Test")
        self.assertRaises(TypeError, Skeleton.check_death, self, None)