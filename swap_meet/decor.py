from swap_meet.item import Item

class Decor(Item):

    def __init__(self, id= None, condition=0, width=0, length=0):
        '''
        Constructor of the class Decor child class of Item
        Represents an Item that is used to decorate a space 
        Parameter from Item: 
            id - int unique identifier or the object created, if nothing is passed unique id will be created
            condition - int from 0 to 5 showing in what condition the Item is. 0 lowest rating and 5 is the highest rating 
        New parameters: 
            width - int, initialized to zero if nothing is passed
            length - int, initialized to zero if nothing is passed 

        '''

        super().__init__(id,condition)

        self.width=width
        self.length=length
    
    def __str__(self):
        '''
        input:
            self - 
        output: 
            str "It takes up a {self.width} by {self.length} sized space."
        '''
        return super().__str__() + f" It takes up a {self.width} by {self.length} sized space."
