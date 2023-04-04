import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0.0):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        if isinstance(self, Clothing):
            item_type = "Clothing" 
        return item_type
    
    def __str__(self):
        statement = f"An object of type Clothing with id " + str(self.id) + ". It is made from " + self.fabric + " fabric."
        print(statement)
        return statement
    