import uuid

class Item:
    # each item will have an attribute named id
    #initialize an instance of item optionally pass in an int
    def __init__(self, id=None, condition=0):
        if id is None:
            # func provides unique numbers to be used to id
            # create a unique int
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        # return a string holding the name of the class 
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
            # condition = {0:'Trendy', 1: 'heavily used', 2:'incredible', 3:'outrageous', 4:'cute', 5:'ugly'}

            if self.condition == 0:
                return 'Trendy'
            if self.condition  == 1:
                return 'heavily used'
            if self.condition  == 2:
                return'incredible'
            if self.condition  == 3:
                return'outrageous'
            if self.condition == 4:
                return'cute'
            if self.condition  == 5:
                return'ugly'
            
            