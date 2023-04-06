import uuid #import just the uuid4()


class Item:
    def __init__(self, id = None, condition = 0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        if condition == 0:
            self.condition = 0
        else:
            self.condition = condition
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    #This is going to stringify the id in a sentence shown in the notes today
        
#need an instance where we pass on integer in the argument id which will manually set the value of id to the instance
#create function named get_category which will return a string holding the name of the class

    def get_category(self):
        return self.__class__.__name__

    def condition_description(self):
        if self.condition in range(0,1):
            return "This is basically trash!"
        elif self.condition in range(1,3):
            return "Not the worst"
        elif self.condition in range(3,6):
            return "You can work with this"