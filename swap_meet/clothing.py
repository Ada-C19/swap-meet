

class Clothing:

    def __init__(self, id=None, fabric="unknown"):
        self.id = uuid.uuid4().int
        if not fabric == "unknown":
            self.fabric = fabric
        else:
            self.fabric = user_input

    def clothing(self):
        self.clothing = self.fabric   

    def get_category(self):
        return self.clothing 
    


# ------------------ WAVE 5 -----------------------
# Clothing

# Has an attribute id that is by default a unique integer
# Has an attribute fabric that is by default the string "Unknown"
# This attribute describes what fabric the clothing is made from; some example values might be "Striped", "Cotton", or "Floral"
# When we instantiate an instance of Clothing, we can optionally pass in a string with the keyword argument fabric
# Has a function get_category that returns "Clothing"
# Has a stringify method that returns "An object of type Clothing with id <id value>. It is made from <fabric value> fabric."

    

    