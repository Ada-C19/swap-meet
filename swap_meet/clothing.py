from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, fabric="Unknown", id=None, condition = 0):
        # Initialize a new instance of Clothing
        super().__init__(id, condition)
        self.fabric = fabric
    
    def __str__(self):
        # Return a string representation of the Clothing object
        return super().__str__() + f" It is made from {self.fabric} fabric."
