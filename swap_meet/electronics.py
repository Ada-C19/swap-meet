from swap_meet.item import Item
import uuid

class Electronics(Item):
    def __init__(self, id=uuid.uuid4().int, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        string = super().__str__() + f"This is a {self.type} device."
        return string
    
    
