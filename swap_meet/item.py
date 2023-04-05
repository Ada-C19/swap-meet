import uuid

class Item:

    def __init__(self, id= None, condition=0):
        if not id: 
            id = uuid.uuid4().int
        self.id = id 
        self.condition = condition
    
    def __str__(self): 
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def get_category(self):
        return self.__class__.__name__
    
    def condition_description(self):
        self.item_condition = {5: "Brand new with tag/box/case",
                               4: "Like new but not quite",
                               3: "Gently used condition", 
                               2: "May come with flaws", 
                               1: "Comes with many flaws",
                               0: "You sure you want to buy this?"}
        
        return self.item_condition[self.condition]
        
