from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id=None, condition=0, age= 10, type="Unknown"):

        '''
        Constructor of the class Electronics child class of Item
        Represents an Item that is used by vendors 
        Parameter from Item: 
            id - int unique identifier or the object created, if nothing is passed unique id will be created
            condition - int from 0 to 5 showing in what condition the Item is. 0 lowest rating and 5 is the highest rating
                it defaults to zero 
        New parameters: 
            type - str showing the category of electronic that the object is. If no argument is given
                it will default to "Unknown" 
        '''

        super().__init__(id,condition,age)
        self.type=type


    
    def __str__(self):

        return super().__str__() + f" This is a {self.type} device."