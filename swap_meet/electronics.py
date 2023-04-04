from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None, condition=0.0):
        super().__init__(id, condition)

        if not type:
                type = "Unknown"
        self.type = type
    
    def __str__(self):
        return (super().__str__() + ' This is a ' + 
                str(self.type) + ' device.')
