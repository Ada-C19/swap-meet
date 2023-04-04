from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
        
    
    def __str__(self):
        my_string = f'{self.id}'
        return f"An object of type {self.get_category()} with id {my_string}. It is made from {self.fabric} fabric."
    
    

