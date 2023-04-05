from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, lenght = 0):
        super().__init__(id, condition)
        self.width = width
        self.lenght = lenght

    def get_category(self):
        return __class__.__name__

    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It takes up a {self.width} by {self.lenght} sized space."
    
    def condition_description(self):
        return super().condition_description()