from swap_meet.item import Item
#from item import Item

class Clothing(Item):
    
    def __init__(self, id=0, condition=0, fabric=None):
        super().__init__(id, condition)
        self.fabric = fabric if fabric else "Unknown"
        self.condition = condition
        
    def get_category(self):
        return self.__class__.__name__   
    
    def __str__(self):
        base_str = super().__str__()
        new_str = f"It is made from {self.fabric} fabric."
        return " ".join([base_str, new_str])
    

