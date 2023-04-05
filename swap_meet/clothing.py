from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition = 0, fabric = "Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        clothing_string = f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
        return clothing_string
    
    def condition_description(self):
        if self.condition == 0:
            return "Garbage"
        elif self.condition == 1:
            return "Could be worse"
        elif self.condition == 2:
            return "Meh"
        elif self.condition == 3:
            return "It's fine"
        elif self.condition == 4:
            return "My grandma would love this"
        elif self.condition == 5:
            return "Perfection on earth"
