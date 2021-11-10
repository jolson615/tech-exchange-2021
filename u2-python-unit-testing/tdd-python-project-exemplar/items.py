#class to standardize attributes of all in game items
class Item:
    def __init__(self, name:str, attribute:str, rating:int):
        '''
        Set item attribute values.
        name (str) is an in-game description.
        attribute (str) correlates to a hero attribute the item modifies.
        rating (int) indicates how much the item modifies the relevant attribute
        '''
        if type(rating) not in [int,float]:
            raise TypeError("rating must be a non-negative real number")
        if rating < 0:
            raise ValueError("rating cannot be negative")
        if (type(name) is not str) or (type(attribute) is not str):
            raise TypeError("name and attribute must be strings")
        if attribute not in ["attack", "armor", "speed"]:
            raise ValueError("invalid attribute")
        self.name = name
        self.attribute = attribute
        self.rating = rating
    
#master list of items imported by rpg.py
item_master_list = [
    Item("sword","attack",3),
    Item("dagger","attack",1),
    Item("bow","attack",2),
    Item("chainmail","armor",3),
    Item("shield","armor",2),
    Item("helmet","armor",1),
    Item("winged boots","speed",2),
    Item("light cloak","speed",1),
]
