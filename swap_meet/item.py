import uuid
# from swap_meet.vendor import Vendor

class Item:
    def __init__(self, id=0, category="Item",condition=0.0): 
        if id == 0:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.category = category
        self.condition = condition
        




    def get_category(self):
        
        return self.category
    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0.0:
            descript = "Uhm, why you selling this?"
        elif self.condition <= 1.0:
            descript = "A lil' musty"
        elif self.condition <= 2.0:
            descript = "Grimy but ok!"
        elif self.condition <= 3.0:
            descript = "Aiight"
        elif self.condition <= 4.0:
            descript = "This is.. good"
        elif self.condition <= 5:
            descript = "ooo almost brand new!"
        
        return descript