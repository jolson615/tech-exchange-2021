import unittest
from pets import Pet

class TestPet(unittest.TestCase):
    longMessage = False
    def setUp(self):
        #This code runs before every test
        self.pet1 = Pet("Spot", "dog", ["brown", "white"], 7)
        self.pet2 = Pet("Cleocatra", "cat", ["white", "orange"], 2)
        self.pet3 = Pet("Tweetheart", "Bird", ["green"], 1.5)
        self.pet4 = Pet("Nemo", "FISH", ["white", "orange"], 0.5)
        self.pet5 = Pet("Donatello", "turtle", ["green"], 13)

    def test00_init(self):
        #Check for accuracy
        self.assertEqual(self.pet1.name, "Spot")
        self.assertEqual(self.pet2.animal, "cat")
        self.assertEqual(self.pet3.colors[0], "green")
        self.assertEqual(self.pet4.colors[1], "orange")
        self.assertAlmostEqual(self.pet3.age, 1.5)

    def test01_init_types(self):
        # Check for type errors
        self.assertRaises(TypeError, Pet, False, "dog", ["brown", "white"], 7)
        self.assertRaises(TypeError, Pet, "Spot", 2, ["brown", "white"], 7)
        self.assertRaises(TypeError, Pet, "Spot", "dog", "black", 7)
        self.assertRaises(TypeError, Pet, "Spot", "dog", ["brown", "white"], "seven")
    
    def test02_init_values(self):
        # Check for value errors
        self.assertRaises(ValueError, Pet, name = "Fluffy", animal = "dog", colors = ["brown"], age = -3)
        self.assertRaises(ValueError, Pet, name = "Fluffy", animal = "dog", colors = ["brown"], age = 4000)

    def test03_nickname(self):
        # Check that the nickname is created correctly
        self.assertEqual(self.pet1.nickname, "fluffy wuffy Sposter", " secret error message")
        self.assertEqual(self.pet2.nickname, "fluffy wuffy Clester", " secret error message")
        self.assertEqual(self.pet4.nickname, "fluffy wuffy Nemster", " secret error message")
    
    def test04_call(self):
        # Check that the full name attribute is created correctly
        self.assertEqual(self.pet1.call(), "woof")
        self.assertEqual(self.pet2.call(), "meow")
        self.assertEqual(self.pet3.call(), "tweet")
        self.assertEqual(self.pet4.call(), "glub glub")
        self.assertEqual(self.pet5.call(), "silence")
    
    def test05_food(self):
        self.assertAlmostEqual(self.pet1.food(150), 5.75)
        self.assertAlmostEqual(self.pet1.food(30), 1.5)
        self.assertAlmostEqual(self.pet2.food(13), 0.5)
        self.assertAlmostEqual(self.pet4.food(0.1), "I am a baby! Check with a vet on how much to feed me")
        self.assertAlmostEqual(self.pet3.food(0.6), "Check with a vet on how much to feed me")

if __name__ == '__main__':
    unittest.main(failfast=True)