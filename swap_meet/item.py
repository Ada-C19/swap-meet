import uuid

class Item:
    def __init__(self,id=None,condition=0):
        if id is None:

            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        self.condition_description = lambda: {
            0: (0.0, "overused eww"),
            1: (1.0, "not great"),
            2: (2.0, "okay"),
            3: (3.0, "not bad"),
            4: (4.0, "great"),
            5: (5.0, "mint")
        }.get(self.condition, "invalid condition value")


    def get_category(self):
        return self.__class__.__name__
    # For call to str(). Prints readable form
    # g4g example/
    # def __str__(self):
    #    return '%s + i%s' % (self.real, self.imag)  
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def swap_items(self, other_item):
        self.id, other_item.id = other_item.id, self.id


        #conditions 0-5
        # 0 being worst 5 best 
    #condition=0
    #condition_description
    #range 0-5





#item has attribute named id
#use uuid to provide num
#UUID4 uses pseudo-random number generators to generate UUID.
#initialize instance of item with keyword id.
#get_category returns string hold name of class(object.__class__.__name__)

#wave3
# stringify an instance of Item using str(), 
# it returns 
# "An object of type Item with id <id value>.", 
# where <id value> is the id of the 
# Item instance that str() was called on.