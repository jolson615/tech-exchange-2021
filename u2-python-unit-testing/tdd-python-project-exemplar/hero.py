from random import randint
from items import Item

#class to organize properties of the player character
class Hero:
    def __init__(self, name:str):
        '''
        Set initial hero attribute values.
        name (str) is a player input.
        Numeric values are a static default.
        inventory is an empty array for collected items.
        '''
        if (type(name) is not str):
            raise TypeError("name must be a string")
        self.name = name
        self.level = 1
        self.attack = 1
        self.armor = 0
        self.speed = 0
        self.hp = 4
        self.inventory = []

    def get_item(self, item:Item):
        '''
        When the hero collects an item (Item), print its stats and add it to inventory.
        Then adjust hero attributes based on the attribute and rating.
        '''
        if (type(item) is not Item):
            raise TypeError("item must be an Item object")
        self.inventory.append(item)
        print(self.name + " found a " + item.name)
        print(f"The {item.name} improves {self.name}'s {item.attribute} by {item.rating}")
        
        if item.attribute == "attack":
            self.attack += item.rating
        elif item.attribute == "armor":
            self.armor += item.rating
        else:
            self.speed += item.rating

    def show_details(self):
        '''Print player stats and inventory'''
        print(f"{self.name} is level {self.level} with {self.hp} HP.")
        print(f"Attack: {self.attack}, Armor: {self.armor}, Speed: {self.speed}")
        item_list = []
        for object in self.inventory:
            item_list.append(object.name)
        print(f"{self.name} is carrying: {item_list}")

    def strike(self):
        '''
        Resolve player attack value based on attack attribute and random variable
        Returns total attack value as an integer
        '''
        print(self.name + " attacks!")
        return self.attack + randint(0,2)

    def check_death(self,damage:int):
        '''
        Resolve whether a skeleton attack kills the hero, is deflected by armor, or does damage (int)
        Returns a boolean representing whether the hero died.
        '''
        if type(damage) not in [int,float]:
            raise TypeError("damage must be a non-negative real number")
        if damage < 0:
            raise ValueError("damage cannot be negative")
        if damage >= (self.hp+self.armor):
            print(self.name + " collapses in exhaustion!")
            return True
        else:
            damage -= self.armor
            if damage < 1:
                print(self.name + " blocks the attack!")
                return False
            else:
                self.hp -= damage
                print(self.name + " staggers from the blow!")
                return False


                

