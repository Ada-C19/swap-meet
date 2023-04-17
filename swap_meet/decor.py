from swap_meet.item import Item

class Decor (Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
        

    def condition_description(self):
        if self.condition == 0:
            return f"Item condition is rated 0. This item is barely holding on!"
        elif self.condition == 1:
            return f"Items condition is rated 1. This item is hanging on by a thread!"
        elif self.condition == 2:
            return f"Items condition is rated 2. This item is living on a prayer."
        elif self.condition == 3:
            return f"Items condition is rated 3. This item is in working order."
        elif self.condition == 4:
            return f"Items condition is rated 4. This item is in good condition."
        else:
            return f"Items condition is rated 5. This item is in excellent condition."

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."

# ------------------ WAVE 5 -----------------------
# Has an attribute id that is by default a unique integer
# Holds 2 integer attributes width and length
# Both of these values should be 0 by default
# When we instantiate an instance of Decor, we can optionally pass in integers with the keyword arguments width and length
# Has a function get_category that returns "Decor"
# Has a stringify method that returns "An object of type Decor with id <id value>. It takes up a <width value> by <length value> sized space."
# For example, if we had a Decor instance with an id of 123435, width of 3, and length of 7, its stringify method should return "An object of type Decor with id 12345. It takes up a 3 by 7 sized space."