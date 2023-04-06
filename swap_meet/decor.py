from swap_meet.item import Item
import uuid

class Decor(Item):
    
    def __init__(self, id = None, width = None, length = None, condition = None):
        super().__init__(id = None, condition = None)
        if id == None:
            id = uuid.uuid4().int
        self.id = id
        self.width = width if width else 0
        self.length = length if length else 0
        self.condition = condition if condition else 0

    def get_category(self):
        return __class__.__name__
    
    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space.'
    
    def condition_description(self):
        return super().condition_description()
