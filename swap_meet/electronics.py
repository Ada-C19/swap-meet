from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = 0, type = "Unknown"):
        super().__init__(id, condition)
        self.condition = condition
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        electronics_string = f"An object of type Electronics with id {self.id}. This is a {self.type} device."
        return electronics_string
    
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
