from swap_meet.item import Item

import uuid
class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0):
        id = uuid.uuid4().int if id is None else id
        self.id = id

        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
