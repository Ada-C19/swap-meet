import uuid


class Item:
    def __init__(self, id):
        self.id = uuid4() 

    
#need an instance where we pass on integer in the argument id which will manually set the value of id to the instance
#create function named get_category which will return a string holding the name of the class

    def get_category(self, item):
        self.item = Item(item)
        return self.__class__.__name__


