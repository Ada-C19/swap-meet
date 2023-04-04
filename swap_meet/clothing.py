from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, fabric="Unknown", id=None, condition=0):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        if isinstance(self, Clothing):
            return "Clothing"