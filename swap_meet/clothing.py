from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric=None):
        #if id is none, check at parent class and create id.
        if id is None:
            super().__init__()
        #otherwise, use given id as id.
        else:
            super().__init__(id=id)

        if fabric is None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric
    #override parent stringify to add the second portion of string."  
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    
    