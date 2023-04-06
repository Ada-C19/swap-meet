from swap_meet.item import Item

#import uuid

    # Wave 05
class Clothing(Item):
    # Has an attribute id that is by default a unique integer
    # Has an attribute fabric that is by default the string "Unknown"
    def __init__(self, condition=0, id=0, fabric="Unknown"):

        super().__init__(category="Clothing", condition=condition, id=id)

        self.fabric = fabric
        #self.category = "Clothing"

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    




