from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id, fabric):
        super().__init__(id)
        self.fabric = fabric 


    def get_category(self):
        return "Item"
    
    def strigify(self):
        pass