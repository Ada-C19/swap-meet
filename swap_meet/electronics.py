from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):    
        return self.__class__.__name__
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."
        
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

        #electronics = "Stereo" key="type"


# ------------------ WAVE 5 -----------------------
# Has an attribute id that is by default a unique integer
# Has an attribute type that is by default the string "Unknown"
# This attribute describes what kind of electronic device this is. Some example values might be “Kitchen Appliance”, “Game Console”, or “Health Tracker”
# When we initialize an instance of Electronics, we can optionally pass in a string with the keyword argument type
# Has an function get_category that returns "Electronics"
# Has a stringify method that returns "An object of type Electronics with id <id value>. This is a <type value> device."
