import uuid

class Item:
    def __init__(self, id = None):
        if not id:
            random_id = uuid.uuid4() # Since id does not need date/time or netword card MAC address in which it was created (such as UUID1), 
            # decided to go with UUID4 which gives a unique id that is generated randomly 
            self.id = random_id.int
        else:
            self.id = id
    
    def get_category(self):
        ''' Returns the category of self, which represents the instance of the class
    as a string'''
        return self.__class__.__name__
        # self is the instance of the class itself, 'Item'

        # __class__ is the class to which the instance 'Item' belongs. It is set
        # to point to the 'Item' class object 

        # __name__  provides the name of the class, which is 'Item'. When the 
        # class instance is instantiated, the name attribute of the class is then assigned to 
        # the name 'Item'

    def __str__(item):
        ''' Returns a string that provides details of the object and ID'''
        return f"An object of type Item with id {item.id}."