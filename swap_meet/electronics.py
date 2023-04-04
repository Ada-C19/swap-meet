from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = None, name = None, type = None):
        # super().__init__(id, name = "Clothing")
        self.type= type if type else "Unknown"
        Item.__init__(self, id, condition, name = "Electronics")
    
    def __str__(self):
        return f"{Item.__str__(self)} This is a {self.type} device."
