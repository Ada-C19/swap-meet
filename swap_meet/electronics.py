from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None):
        super().__init__(id)

        if not type:
                type = "Unknown"
        self.type = type
    
    def __str__(self):
        return (super().__str__() + ' This is a ' + 
                str(self.type) + ' device.')
