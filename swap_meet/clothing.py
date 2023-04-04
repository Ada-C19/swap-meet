from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    def get_category(self):
        return super().get_category()
    
    def __str__(self):
        my_string = f'{self.id}'
        return f"An object of type {self.get_category()} with id {my_string}. It is made from {self.fabric} fabric."
    
        



