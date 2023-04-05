from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = 0, type = "Unnown"):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return __class__.__name__

    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. This is a {self.type} device."
    
    def condition_description(self):
        return super().condition_description()