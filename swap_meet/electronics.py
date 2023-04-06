from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0, age = 0):
        super().__init__(id, condition, age)
        self.type = type

    def get_category(self):
        return super().get_category()
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self):
        return super().condition_description()