from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, width=0, length=0, id=None, condition=0, age=0):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length

    def __str__(self):
        return super().__str__() + f" It takes up a {self.width} by {self.length} sized space."

    def get_category(self):
        return "Decor"