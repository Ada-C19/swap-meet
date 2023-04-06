import uuid 

class Item:
    def __init__(self, id = None, condition=0):
        self.id = id
        self.condition = condition

        if id == None: 
            self.id = uuid.uuid4().int
        else: 
            self.id
        

    def get_category(self): 
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    

    def condition_description(self): 
        if self.condition <= 1: 
            return "You probably want a glove for this one..."
        elif self.condition <= 3: 
            return "It's aight."
        elif self.condition <= 5: 
            return "Practically brand new, almost."