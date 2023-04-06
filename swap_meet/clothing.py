from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0, age = 0):
        super().__init__(id, condition, age)
        self.fabric = fabric
        
    def get_category(self):
        return super().get_category()

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def condition_description(self):
        return super().condition_description()
