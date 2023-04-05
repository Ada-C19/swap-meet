from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0, type="Unknown", id=None):
        super().__init__(condition, id)
        self.type = type
    
    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."