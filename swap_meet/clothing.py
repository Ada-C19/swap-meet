from swap_meet.item import Item


class Clothing(Item):


    def __init__(self, id=None, age=10, condition=0, fabric='Unknown'):
        '''
        Constructor of the class Clothing child class of Item
        Represents a type of Item that can be worn by vendors 
        Parameter from Item: 
                id - int unique identifier or the object created, if nothing is passed unique id will be created
                condition - int from 0 to 5 showing in what condition the Item is. 0 lowest rating and 5 is the highest rating 
                    it defaults to zero 
        New parameters: 
            fabric - str saves the type of fabric with which the clothing is made. If no argument is given it will default to 'Unknown' 
        '''
        super().__init__(id,condition,age)
        self.fabric = fabric


    def __str__(self):
        '''
        input:
            self - 
        output: 
            str - " It is made from {self.fabric} fabric."
        '''
        return super().__str__() + f" It is made from {self.fabric} fabric."
