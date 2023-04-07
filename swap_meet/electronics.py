from swap_meet.item import Item

import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown", condition=0):
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return (f"An object of type Electronics with id { self.id }. This is a { self.type } device.")
