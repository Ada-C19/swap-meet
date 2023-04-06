import uuid

class Item:
    
    def __init__(self, id=None, condition=0, age=10):

        '''
        Constructor of the class Item, represents objects that Vendor can hold in tis parameter inventory
        Parameters: 
            id - int unique identifier or the object created, if nothing is passed unique id will be created
            condition - int from 0 to 5 showing in what condition the Item is. 0 lowest rating and 5 is the highest rating
                it defaults to zero
        '''

        # If no id is given then a unique id is created by using  uuid4 from the uuid library

        if not id:
            id = int(uuid.uuid4())

        self.id = id 
        self.condition = condition
        self.age = age
    

    def get_category(self):

        return (f"{self.__class__.__name__}")
    
    
    def __str__(self):

        return (f"An object of type {self.get_category()} with id {self.id}.")
    


    def condition_description(self):

        if self.condition == 0:
            return "Trash"
        if self.condition == 1:
            return "Has lived"
        if self.condition == 2:
            return "Trashy but classic"
        if self.condition == 3:
            return "Above Average"
        if self.condition == 4:
            return "Almost New"
        return "Like New"
        
