from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, id=0, condition= 0, type= None):
        super().__init__(id, condition)
        self.type = type if type else "Unknown"
        
    def __str__(self):
        base_str = super().__str__()
        new_str = f"This is a {self.type} device."
        return " ".join([base_str, new_str])
