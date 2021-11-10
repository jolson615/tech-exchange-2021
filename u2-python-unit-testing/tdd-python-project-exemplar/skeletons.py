from random import choice, randint

#class to organize attributes of the enemy characters
class Skeleton:
    def __init__(self, level:int):
        '''
        Set initial skeleton attribute values scaled from hero level (int).
        Numeric values are random integers in a given range.
        description is a randomly chosen string.
        '''
        if type(level) not in [int,float]:
            raise TypeError("level must be a non-negative real number")
        if level < 0:
            raise ValueError("level cannot be negative")
        self.attack = randint(1,(level*2))
        self.armor = randint(0,level)
        self.speed = randint(0,(level*2))
        self.hp = randint(1,(level+1))
        self.description = self.random_description()
        print("You see a " + self.description + " skeleton!")
        self.show_details()

    def random_description(self):
        '''Give the skeleton a random descriptive adjective'''
        words = ["scary"," hair-raising"," terrifying"," petrifying"," spine-chilling"," blood-curdling"," chilling"," horrifying"," alarming"," daunting"," formidable"," fearsome"," nerve-racking"," unnerving"]
        return choice(words)

    def show_details(self):
        '''Print skeleton stats'''
        print(f"Skeleton HP: {self.hp}, Skeleton Attack: {self.attack}, Skeleton Armor: {self.armor}, Skeleton Speed: {self.speed}")
    
    def strike(self):
        '''
        Resolve skeleton attack value based on attack attribute and random variable
        Returns total attack value as an integer
        '''
        print("The " + self.description + " skeleton attacks!")
        return self.attack + randint(0,2)

    def check_death(self,damage:int):
        '''
        Resolve whether a hero attack destroys the skeleton, is deflected by armor, or does damage (int)
        Returns a boolean representing whether the skeleton died.
        '''
        if type(damage) not in [int,float]:
            raise TypeError("damage must be a non-negative real number")
        if damage < 0:
            raise ValueError("damage cannot be negative")
        if damage>= self.hp:
            print("The " + self.description + " skeleton is destroyed!")
            return True
        else:
            self.hp -= damage
            print("The " + self.description + " skeleton staggers from the blow!")
            return False
