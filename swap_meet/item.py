from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition >= 4:
            condition_str = "Near Mint! That's a good pick!"
        elif self.condition >= 3:
            condition_str = "Decent pick. Almost near mint."
        elif self.condition >= 2:
            condition_str =  "Moderately Used. It's aight."
        elif self.condition >= 1:
            condition_str = "You might want to reconsider."
        else:
            condition_str = "This is TRAASHHHHH!!"
        return condition_str

    

