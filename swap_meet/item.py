from swap_meet import vendor
import uuid

class Item:
    def __init__(self, condition=0, id=None):
        if id is not None and not isinstance(id, int):
            raise ValueError("id must be an integer")    
        self.id = id or int(uuid.uuid4())
        self.condition = condition
    
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        self.condition = float(self.condition)
        
        if self.condition <=1.0:
            return "This item isn't in great condition, but may be a great DIY project."
        if self.condition <=2.0:
            return "Cool item!"
        if self.condition <=3.0:
            return "So neat! This item is in great condition."
        if self.condition <=4.0:
            return "Holy cow! This is an awesome item."
        if self.condition <=5.0:
            return "You must be in tears over the preciousness of this item, congrats :)"