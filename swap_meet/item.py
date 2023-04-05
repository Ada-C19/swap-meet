import uuid
class Item:
    # randomized id and set it to an integer
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
    # accessing the class name of self (item)
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return(f"An object of type {self.get_category()} with id {self.id}.")
    
    def condition_description(self):
        if self.condition == 0:
            return "Really really bad"
        elif self.condition == 1:
            return "Kinda bad"
        elif self.condition == 2:
            return "So So"
        elif self.condition == 3:
            return "Kinda nice"
        elif self.condition == 4:
            return "Almost new"
        elif self.condition == 5:
            return "Brand spankin' new!"