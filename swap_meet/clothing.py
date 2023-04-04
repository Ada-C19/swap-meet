from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category="Clothing", fabric="Unknown"):
        super().__init__(category) #check viability of super 
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def get_category(self):
        return f"{self.category}"
    