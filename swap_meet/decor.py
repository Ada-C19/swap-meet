from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, width = 0, length = 0, condition = 0, age = 0):
        super().__init__(id, condition, age)    # Call the __init__() method of the parent class (Item) to set the ID attribute
        self.width = width      # Set the width attribute of the Decor object
        self.length = length    # Set the length attribute of the Decor object
    def __str__(self):
        # Call the __str__() method of the parent class (Item) to get the default string representation
        # of the Decor object, then add the dimensions to the end of the string
        return super().__str__() + f" It takes up a {self.width} by {self.length} sized space."
