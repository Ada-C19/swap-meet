import uuid

class Item:
    # Define attributes for Item instances
    def __init__(self, id = None, condition = None):
        # If no value provided for id, attribute id takes on randomly generated unique number
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        
        # If no value provided for condition, attribute condition takes on 0    
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
            
    def get_category(self):
        # Return class name "Item"
        return Item.__name__
    
    # Stringify Item instances
    def __str__(self):
        # Read id attribute
        item_id = self.id
        # Return expected string
        return f"An object of type Item with id {item_id}."
    
    # Read condition attribute and return a string corresponding to attribute value
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
        
        
    
    

