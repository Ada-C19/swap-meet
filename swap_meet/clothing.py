from .item import Item


class Clothing(Item):
    def __init__(self, fabric):
        super().__init__(self,id=0)

        self.fabric = "Unknown" if fabric is None else fabric 
        
        
    def get_category(self):
        item = Item()
        return item.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."