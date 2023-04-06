from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric 
        

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."
#         return f"An object of type Clothing with id {self.__annotations__}"
    
# "An object of type Clothing with id <id value>. It is made from <fabric value> fabric."


# try out __name__ 
# type(self).__name__