import uuid
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        # Notes: default arguments need to go to the end of this line.
        # Do we need to set id=uuid or id= None again if we inherit id from our parent class alreay? 
        # why we need to set default to condition=0 again too?
        # will id=None override our manually set id?
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."