import uuid
from swap_meet.item import Item
    
class Electronics(Item):

    def __init__(self, id=None, type="Unknown", condition= 0.0):
        self.id = id if id is not None else int(uuid.uuid4())
        self.type = type
        self.condition = condition

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
