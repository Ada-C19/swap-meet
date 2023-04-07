import uuid
from swap_meet.item import Item
class Decor(Item):
    def __init__(self,id=None, width=0,length=0, condition=0):
        self.width = width
        self.length = length 

        super().__init__(id, condition)
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def condition_desciption(self):

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