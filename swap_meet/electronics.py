from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, type, condition=0):
        super().__init__(id)
        self.type = None
        self.condition = condition

    def get_category(self):    
        pass
        
    def condition_description(self):
        pass
    
        #electronics = "Stereo" key="type"


# ------------------ WAVE 5 -----------------------
# Has an attribute id that is by default a unique integer
# Has an attribute type that is by default the string "Unknown"
# This attribute describes what kind of electronic device this is. Some example values might be “Kitchen Appliance”, “Game Console”, or “Health Tracker”
# When we initialize an instance of Electronics, we can optionally pass in a string with the keyword argument type
# Has an function get_category that returns "Electronics"
# Has a stringify method that returns "An object of type Electronics with id <id value>. This is a <type value> device."
