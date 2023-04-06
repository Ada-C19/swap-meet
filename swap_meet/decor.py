from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, id = None, width = 0, length = 0, condition = 0.0):
        super().__init__(id)
        self.width = width
        self.length = length
        self.condition = condition

    def get_category(self):
        return super().get_category()
    
    def __str__(self):
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."
    
    def condition_description(self):
        return super().condition_description()
    

