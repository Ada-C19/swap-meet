from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, type="Unknown", id=None):
        super().__init__(id)
        self.type = type

    def get_category(self):
        if isinstance(self, Electronics):
            return "Electronics"
