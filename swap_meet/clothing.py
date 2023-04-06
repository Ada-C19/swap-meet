from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition = None, age=None, name = None, fabric = None):
        super().__init__(id, condition, age, name = "Clothing")
        self.fabric = fabric if fabric else "Unknown"
    
    def __str__(self):
        return f"{Item.__str__(self)} It is made from {self.fabric} fabric."