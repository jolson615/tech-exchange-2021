import unittest
from pets_answers import Pet

class TestPet(unittest.TestCase):
    longMessage = False
    def setUp(self):
        #This code runs before every test
        try:
            self.pet1 = Pet("Clifford", "dog", ["brown", "white"], 7)
        except:
            print("\nYou must edit the pet class to be initialized with 4 instance variables: name, animal, colors, and age")
            raise
        self.pet2 = Pet("Cleocatra", "cat", ["white", "orange"], 2)
        self.pet3 = Pet("Tweetheart", "Bird", ["green"], 1.5)
        self.pet4 = Pet("Nemo", "FISH", ["white", "orange"], 0.5)
        self.pet5 = Pet("Donatello", "turtle", ["green"], 13)

    def test00_init(self):
        #Check for accuracy
        self.assertEqual(self.pet1.name, "Clifford")
        self.assertEqual(self.pet2.animal, "cat")
        self.assertEqual(self.pet3.colors[0], "green")
        self.assertEqual(self.pet4.colors[1], "orange")
        self.assertAlmostEqual(self.pet3.age, 1.5)
        try:
            self.assertEqual(self.pet1.adopted, False)
        except AttributeError:
            print("\n'adopted' is a class variable representing whether each pet has been adopted or not. The value should be set to False for all pets and can be updated once they find their forever homes.")
            raise

    def test01_init_types(self):
        self.assertRaises(TypeError, Pet, False, "dog", ["brown", "white"], 7)
        self.assertRaises(TypeError, Pet, "Clifford", 2, ["brown", "white"], 7)
        try:
            self.assertRaises(TypeError, Pet, "Clifford", "dog", "black", 7)
        except AssertionError as e:
            print("\n colors must be a list, not a string. Raise a TypeError if the user inputs a string")
            raise
        self.assertRaises(TypeError, Pet, "Clifford", "dog", ["brown", "white"], "seven")
    
    def test02_init_values(self):
        # Check for value errors
        self.assertRaises(ValueError, Pet, name = "Fluffy", animal = "dog", colors = ["brown"], age = -3)
        self.assertRaises(ValueError, Pet, name = "Fluffy", animal = "dog", colors = ["brown"], age = 4000)

    def test03_nickname(self):
        # Check that the nickname is created correctly
        try:
            self.assertEqual(self.pet1.nickname, "fluffy wuffy Clifster")
        except AttributeError as e:
            print("\nYou must define an attribute called nickname, using the first 4 letters of the pet's name as shown in the test example")
            raise
        except AssertionError as e:
            raise
        self.assertEqual(self.pet2.nickname, "fluffy wuffy Cleoster")
        self.assertEqual(self.pet4.nickname, "fluffy wuffy Nemoster")
    
    def test04_call(self):
        # Check that the full name attribute is created correctly
        try:
            self.assertEqual(self.pet1.call(), "woof")
        except AttributeError as e:
            print('\nYou will need to define a new method called call(), which represents the sound that each animal makes')
            raise
        self.assertEqual(self.pet2.call(), "meow")
        try:
            self.assertEqual(self.pet3.call(), "tweet")
        except AssertionError as e:
            print('\nHint: pet3 is being called as: self.pet3 = Pet("Tweetheart", "Bird", ["green"], 1.5)')
            raise
        try:
            self.assertEqual(self.pet4.call(), "glub glub")
        except AssertionError as e:
            print('\nHint: pet4 is being called as: self.pet4 = Pet("Nemo", "FISH", ["white", "orange"], 0.5)')
            raise
        self.assertEqual(self.pet5.call(), "silence")
    
    def test05_food_amount(self):
        try:
            self.assertAlmostEqual(self.pet1.food_amount(150), 5.75)
        except AttributeError:
            print("\nNow you will need to define a method called food_amount which takes in the pet's weight and returns the amount of food, in cups, to feed the pet. All animals younger than 1 and non-cats/dogs are referred to a vet. All cats older than 1 are given 1/2 cup of food. Dogs under 100 lbs are given cups equal to their weight divided by 20. Dogs over 100 lbs are given 4.5 cups plus an extra quarter cup for each 10 pounds over 100.")
            raise
        self.assertAlmostEqual(self.pet1.food_amount(30), 1.5)
        self.assertAlmostEqual(self.pet2.food_amount(13), 0.5)
        self.assertEqual(self.pet4.food_amount(0.1), "I am a baby! Check with a vet on how much to feed me")
        self.assertEqual(self.pet3.food_amount(0.6), "Check with a vet on how much to feed me")

    def test06_human_age(self):
        try:
            self.assertAlmostEqual(self.pet1.human_age(), 49)
        except:
            print("\nYou must define a method called human_age which calculates the equivalent age that the pet would be if they were human. For dogs, age is multiplied by 7. For cats, by 6. For birds, by 10. For other animals, return None")
            raise
        self.assertAlmostEqual(self.pet2.human_age(), 12)
        self.assertAlmostEqual(self.pet3.human_age(), 15)
        self.assertEqual(self.pet4.human_age(), None)
if __name__ == '__main__':
    unittest.main(failfast=True)