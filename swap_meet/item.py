import uuid
class Item:
    def __init__(self,condition =0, id = None, age = 0):
        self.category = self.__class__.__name__
        id = uuid.uuid4().int if id is None else id
        self.id = id
        self.condition = condition
        self.age = age

        
    
    def get_category(self):
        return self.category
        
   
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        conditon_dict = {0: "Terrible", 1: "Bad" , 2: "Kind of bad", 3: "Fair", 4: "Good", 5: "Excellent"}
        return conditon_dict.get(self.condition)
