from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, fabric="Unknown", id=None):
        super().__init__(id)
        self.fabric = fabric

    def get_category(self):
        if isinstance(self, Clothing):
            return "Clothing"