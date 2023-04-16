from swap_meet.item import Item

class Decor (Item):
    def __init__(self, condition=0, width, length):
        super().__init__(id)
        self.condition = condition
        self.width = width
        self.length = length
        

    def condition_description(self):
        pass

# ------------------ WAVE 5 -----------------------
# Has an attribute id that is by default a unique integer
# Holds 2 integer attributes width and length
# Both of these values should be 0 by default
# When we instantiate an instance of Decor, we can optionally pass in integers with the keyword arguments width and length
# Has a function get_category that returns "Decor"
# Has a stringify method that returns "An object of type Decor with id <id value>. It takes up a <width value> by <length value> sized space."
# For example, if we had a Decor instance with an id of 123435, width of 3, and length of 7, its stringify method should return "An object of type Decor with id 12345. It takes up a 3 by 7 sized space."