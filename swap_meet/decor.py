from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0.0, age=0.0):
        super().__init__(id, condition, age)

        self.width = width
        self.length = length
    
    def __str__(self):
        return (super().__str__() + ' It takes up a ' + 
                str(self.width) + ' by ' + str(self.length) +
                ' sized space.')