from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, width=0, length=0, id=None):
        super().__init__(id)
        self.width = width
        self.length = length

    def get_category(self):
        if isinstance(self, Decor):
            return "Decor"