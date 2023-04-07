import uuid
from swap_meet.item import Item
class Clothing:
    def __init__(self,id=None, fabric="Unknown", condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.fabric = fabric
        self.condition = condition


    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        descriptions = {
            0: "fair",
            1: "poor",
            2: "acceptable",
            3: "gently used",
            4: "Like new",
            5: "Mint Condition",
        }

        for key, value in descriptions.items():
            if key == self.condition:
                print(value)
