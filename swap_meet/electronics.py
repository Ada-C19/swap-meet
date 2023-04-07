import uuid
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        self.type = type
        super().__init__(id, condition)

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
   
    def condition_description(self):
        descriptions = {0: "fair",
                        1: "poor",
                        2: "acceptable",
                        3: "gently used",
                        4: "Like new",
                        5: "Mint Condition",
        }

        for key, value in descriptions.items():
            if key == self.condition:
                print(value)