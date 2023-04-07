from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None , condition = 0, type = None):
        super().__init__(id = id, condition = condition)
        if type is None:
            type = "Unknown"
        self.type = type
    
    
    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."