import uuid


class Item:
    def __init__(self, id = None, condition =0):
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition 

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return("Heavily used")
        elif self.condition == 1:
            return("Worn and torn")
        elif self.condition == 2:
            return("Mehhhh")
        elif self.condition == 3:
            return("Not too shabby")
        elif self.condition == 4:
            return("Almost new")
        elif self.condition == 5:
            return("Like new")