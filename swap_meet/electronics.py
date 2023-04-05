from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id= None, condition = 0, type = "Unknown"):
        super().__init__(id, condition)
        self.type = type
    
    # def get_category is already defined in Item

    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."

    
    # def condition_description(self):
        # return super().condition_description()