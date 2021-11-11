class Pet:
    '''A class to store information about the different pets from Pawsome Pets'''
    pass
    def __init__(self, name, animal, colors, age):
        self.name = name
        self.animal = animal
        self.colors = colors
        self.age = age
        if type(name) != str:
            raise TypeError("Name must be a string")
        if type(animal) != str:
            raise TypeError("Type of animal must be a string")