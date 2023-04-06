import uuid
from swap_meet.item import Item

# class Clothing(Item):
#     def __init__(self, id, condition, fabric = "Unknown"):
#         super().__init__(id, condition)
#         self.fabric = fabric
#         self.category = self.get_category()

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        # super().__init__(condition)
        if not id:
            id = uuid.uuid1().int
        self.id = id
        self.fabric = fabric
        self.condition = condition
        self.category = self.get_category()

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."