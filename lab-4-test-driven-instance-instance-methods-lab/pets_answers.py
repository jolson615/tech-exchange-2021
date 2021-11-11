class Pet:
    '''A class to store information about the different pets from Pawsome Pets'''
    adopted = False
    def __init__(self, name, animal, colors, age):
        if type(name) != str:
            raise TypeError("Name must be a string")
        if type(animal) != str:
            raise TypeError("Type of animal must be a string")
        if type(colors) != list:
            raise TypeError("Colors should be a list of animal shades")
        if type(age) not in [int, float]:
            raise TypeError("Age must be a number (int or float)")
        if age < 0 or age > 100:
            raise ValueError("Age must be a number between 0 and 100")
        self.name = name
        self.animal = animal
        self.colors = colors
        self.age = age
        self.nickname = 'fluffy wuffy {}ster'.format(self.name[0:3])
    def call(self):
        '''Gives the call that the pet most commonly makes as a string. No input.'''
        if self.animal.lower() == "cat":
            return "meow"
        elif self.animal.lower() == "dog":
            return "woof"
        elif self.animal.lower() =="bird":
            return "tweet"
        elif self.animal.lower() == "fish":
            return "glub glub"
        else:
            return "silence"
    def food(self, weight):
        '''Gives the amount of food (in cups) to feed the pet based on weight in pounds.'''
        # All animals younger than 1 and non-cats/dogs are referred to a vet. All cats older than 1 are give 1/2 cup of food. Dogs under 100 lbs are given cups equal to weight over 100. 
        if self.age < 1:
            return "I am a baby! Check with a vet on how much to feed me"
        elif self.animal == "cat":
            return 0.5
        elif self.animal == "dog":
            if weight < 100:
                return (weight/20.0)
            else:
                return 4.5 + (weight-100)/10*0.25
        else:
            return "Check with a vet on how much to feed me"

pet1 = Pet("Spot", "dog", ["brown", "white"], 7)
# print(pet1.food(150))
