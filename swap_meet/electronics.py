import uuid
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=uuid.uuid4().int, type="Unknown", condition=0, age=0):
        Item.__init__(self, id, condition, age)
        self.type = type
    
    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."