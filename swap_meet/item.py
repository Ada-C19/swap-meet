import uuid
class Item:
    def __init__(self,id = None, condition = 0):
        id = uuid.uuid4().int if id is None else id
        self.id = id
        self.condition = int(condition)
    
    def get_category(self):
        return "Item"
   
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        conditon_dict = {0: "Terrible", 1: "Bad" , 2: "Kind of bad", 3: "Fair", 4: "Good", 5: "Excellent"}
        return conditon_dict.get(self.condition)

