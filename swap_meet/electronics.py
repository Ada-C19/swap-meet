import uuid
from .item import Item
class Electronics(Item):
    def __init__(self, id=uuid.uuid1().int, type="Unknown", condition=0):
        self.id = id
        self.type = type
        self.condition = condition
    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return (f'An object of type Electronics with id {self.id}.' 
                f'This is a {self.type} device.')
