from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type=None):
        #if id is none, check at parent class and create id.
        if id is None:
            super().__init__()
        #otherwise, use given id as id.
        else:
            super().__init__(id=id)

        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
    #override parent stringify to add the second portion of string."  
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. This is a {self.type} device."
    
    