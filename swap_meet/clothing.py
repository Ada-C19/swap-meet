from swap_meet.item import Item
import uuid

# parent class: Item
# child class: Clothing

class Clothing(Item):
    
    def __init__(self, id = None, fabric = None, condition = None):
        # access parent class with super().
        super().__init__(id = None, condition = None)
        if id == None:
            id = uuid.uuid4().int
        self.id = id
        self.fabric = fabric if fabric else 'Unknown'
        self.condition = condition if condition else 0

    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric.'
    
    def get_category(self):
        return __class__.__name__
    
    # inherit condition_description method from the parent class Item
    
    def condition_description(self):
        return super().condition_description()
