import uuid
from swap_meet.item import Item


class Decor(Item):
    def __init__(self, id=uuid.uuid4().int, width=0, length=0, condition=0, age=0):
        Item.__init__(self, id, condition, age)
        self.width = width
        self.length = length

    def get_category(self):
        """This function returns the category of the item"""
        return "Decor"

    def __str__(self):
        """This function returns a string with the type of the object and it's id"""
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
