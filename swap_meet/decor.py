from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, length = 0):
        super().__init__(id, condition)
        self.condition = condition
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"
    
    def __str__(self):
        decor_string = f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
        return decor_string
    
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
