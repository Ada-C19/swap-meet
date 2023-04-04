from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id, name, fabric = None):
        super().__init__(id, name = "Clothing")
        
        self.fabric = fabric if fabric else "Unknown"
    
    