import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        # setting id to be an optional argument
        # passing in large random int if no id being passed by user
        # allowing id to be overwritten if id being passed by user
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
    
    def get_category(self):
        # returns any objects name
        return self.__class__.__name__
    
    def __repr__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if 0 <= self.condition <=2:
            return "Poor condition"
        elif self.condition == 3:
            return "Average condition"
        elif self.condition == 4:
            return "Almost as good as new."
        elif self.condition == 5:
            return "As good as new! Mint condition."
        

    
