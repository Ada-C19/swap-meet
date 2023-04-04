from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None , name = None, fabric = None):
        # super().__init__(id, name = "Clothing")
        self.fabric = fabric if fabric else "Unknown"
        Item.__init__(self, id, name = "Clothing")
    
    def __str__(self):
        return f"{Item.__str__(self)} It is made from {self.fabric} fabric."