import uuid
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,id=None, type=None, condition=None):
        random_id = uuid.uuid4()
        self.id = int(random_id) if id is None else id
        self.type = "Unknown" if type is None else type
        self.condition = 0 if condition is None else condition
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."