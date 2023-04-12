import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition
        #If no id is given create a random 32 digit, else use id given.
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    #get the category of an item: Electronics, Decor, Clothing
    def get_category(self):
        return self.__class__.__name__
    
    #creates a string that tells object type and id.
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."

    #defines the condition of each item on a 1-5 scale.
    def condition_description(self):
        if self.condition == 5.0:
            return "This item is a steal!"
        elif 4.0 <= self.condition < 5.0:
            return "Better than average!"
        elif 3.0 <= self.condition < 4.0:
            return "Average at best"
        elif 2.0 <= self.condition < 3.0:
            return "Needs some love"
        elif 1.0 <= self.condition < 2.0:
            return "Seen better days"
        else:
            return "Better off in the trash"