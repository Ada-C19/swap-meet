import uuid

class Item:
    def __init__(self, id = None, condition = 0, age = 0):
        '''
        If id does not exist, assign unique id with uuid
        If an invalid type is passed in as the id parameter, 
        a TypeError will be raised.
        '''
        self.age = age
        self.condition = condition

        if not id:
            self.id = int(uuid.uuid4())
        elif isinstance(id, int):
            self.id = id
        else:
            raise TypeError("ID must be an integer")


    def get_category(self):
        '''
        Function named `get_category` will return a string holding the name of the class
        '''
        return self.__class__.__name__
    
    def __str__(self):
        return "An object of type Item with id {}.".format(self.id)
        
    def condition_description(self):
        if self.condition == 0:
            return "That's Gross"
        elif self.condition == 1:
            return "No Thanks"
        elif self.condition == 2:
            return "Not Bad"
        elif self.condition == 3:
            return "Passable"
        elif self.condition == 4:
            return "Pretty Nice"
        elif self.condition == 5:
            return "I Need This!"
        else:
            return "Unknown"