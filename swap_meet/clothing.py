from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric="Unknown", id=None, condition=0):
        self.fabric = fabric
        self.condition = condition
        super().__init__(id)

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        return super().condition_description(self.condition)