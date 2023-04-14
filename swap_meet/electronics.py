from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition = 0, age = 0):
        # call the superclass constructor to set the id attribute
        super().__init__(id, condition, age)
        
        # set the type attribute
        self.type = type

    def __str__(self):
        # call the superclass __str__ method to get the id string
        # and concatenate it with the device type string
        return super().__str__() + f" This is a {self.type} device."
