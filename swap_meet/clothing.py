from swap_meet.item import Item
class Clothing(Item):
    def _init_(self, fabric="Unknown"):
        self.fabric = fabric 
    def __str__(self): 
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric." 
                


    