import uuid
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, id = None, fabric = None, condition = None): 
        super().__init__(id, condition)       
        if fabric is None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric
        
    def get_category(self):
        return Clothing.__name__
    
    def __str__(self):
        id_value = self.id
        fabric_value = self.fabric
        return f"An object of type Clothing with id {id_value}. It is made from {fabric_value} fabric."
        

    