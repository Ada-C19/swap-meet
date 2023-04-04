from swap_meet.item import Item
class Clothing:
    def __init__(self, category="Clothing", condition=0, fabric="Unknown"):
        super().__init__(category, condition) #check viability of super 
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    