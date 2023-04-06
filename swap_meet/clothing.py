from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0.0):
        super().__init__(id, condition)
        self.fabric = fabric
    #override parent stringify to add the second portion of string."  
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    
    