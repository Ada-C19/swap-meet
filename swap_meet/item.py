import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    
    def get_category(self):
        return "Item"
        # class_name = __class__.__name__
        
    def condition_description(self):
        condition_status = ["bad", "heavily used", "acceptable", "good", "like new", "new"]
        return condition_status[self.condition]
        
    
    


    
