from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0.0):
        super().__init__(id)
        self.fabric = fabric 
        self.condition = condition
    
    def __str__(self):
        category_message = super().__str__()
        return f"{category_message} It is made from {self.fabric} fabric."
        
