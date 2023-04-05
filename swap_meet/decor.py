import uuid
from swap_meet.item import Item
class Decor(Item):
    def __init__(self, id=None, width=None, length=None, condition=None):
        random_id = uuid.uuid4()
        self.id = int(random_id) if id is None else id
        self.width = 0 if width is None else width
        self.length = 0 if length is None else length
        self.condition = 0 if condition is None else condition
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
