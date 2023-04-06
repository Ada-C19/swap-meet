from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, id=None, width=0, length=0):
        super().__init__(id)
        self.width = width
        self.length = length


    def __str__(self):
        first_sentence = super().__str__()
        print(f"{first_sentence} It takes up a {self.width} by {self.length} sized space.")