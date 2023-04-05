import uuid

class Item:
    def __init__(self, id=None, condition=0.0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return self.__class__.__name__ 
    
    def item_as_string(self):
        return self.__str__()
    
    def condition_description(self):
        if self.condition < 1.0:
            return "useless garbage"
        elif self.condition >= 1.0 and self.condition < 2.0:
            return "you probably don't need this in your life"
        elif self.condition >= 2.0 and self.condition < 3.0:
            return "catch & release"
        elif self.condition >= 3.0 and self.condition < 4.0:
            return "Okay but does it REALLY spark joy?"
        elif self.condition >= 4.0 and self.condition < 5.0:
            return "if we can't get it out of our mind...we will buy it"
        elif self.condition >= 5:
            return "TAKE MY MONEY"
        
        