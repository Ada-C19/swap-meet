import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        return self.__class__.__name__ 
    
    def item_as_string(self):
        return self.__str__()
    
    def condition_description(self):
        if self.condition == 0:
            return "useless garbage"
        elif self.condition == 1:
            return "you probably don't need this in your life"
        elif self.condition == 2:
            return "catch & release"
        elif self.condition == 3:
            return "Okay but does it REALLY spark joy?"
        elif self.condition == 4:
            return "if we can't get it out of our mind...we will buy it"
        elif self.condition == 5:
            return "TAKE MY MONEY"
        
        