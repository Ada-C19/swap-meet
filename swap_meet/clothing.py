import uuid
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, id=uuid.uuid4().int, fabric="Unknown", condition=0, age=0):
        Item.__init__(self, id, condition, age)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."
