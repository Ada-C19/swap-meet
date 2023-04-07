import uuid

class Item:
    def __init__(self, id = None, condition = None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
            
    def get_category(self):
        return Item.__name__
    
    def __str__(self):
        item_id = self.id
        return f"An object of type Item with id {item_id}."
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            return "fair"
        elif 1 <= self.condition < 2:
            return "good"
        elif 2 <= self.condition < 3:
            return "excellent"
        elif 3 <= self.condition < 4:
            return "near-mint"
        elif 4 <= self.condition <= 5:
            return "new"
        
        
    
    

