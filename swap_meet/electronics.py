from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0.0):
        super().__init__(id)
        self.type = type
        self.condition = condition

    def get_category(self):
        return super().get_category()
    
    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."
    
    def condition_description(self):
        return super().condition_description()