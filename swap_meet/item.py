import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition        
        #if id is not manually assigned
        if id == None:
            self.id = uuid.uuid4().int
        #if id is manually assigned
        else:
            self.id = id
        
        
    def get_category(self):
        return self.__class__.__name__
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."    

def condition_description(self):
        if self.condition == 0:
            return f"Item condition is rated 0. This item is barely holding on!"
        elif self.condition == 1:
            return f"Items condition is rated 1. This item is hanging on by a thread!"
        elif self.condition == 2:
            return f"Items condition is rated 2. This item is living on a prayer."
        elif self.condition == 3:
            return f"Items condition is rated 3. This item is in working order."
        elif self.condition == 4:
            return f"Items condition is rated 4. This item is in good condition."
        else:
            return f"Items condition is rated 5. This item is in excellent condition."
