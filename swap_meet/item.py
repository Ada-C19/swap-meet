import uuid #import just the uuid4()


class Item:
    def __init__(self, id = None):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    #This is going to stringify the id in a sentence shown in the notes today
        
#need an instance where we pass on integer in the argument id which will manually set the value of id to the instance
#create function named get_category which will return a string holding the name of the class

    def get_category(self):
        self.item = Item()
        return self.__class__.__name__


