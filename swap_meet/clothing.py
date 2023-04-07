from swap_meet.item import Item

import uuid

class Clothing:
    def __init__(self, id=None, fabric="Unknown", condition=0):
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        self.fabric = fabric
        self.condition = condition
    
    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return (f"An object of type Clothing with id { self.id }. It is made from { self.fabric } fabric.")
    
    def condition_description(self):
        if self.condition == 0:
            return "Old"
        elif self.condition == 1:
            return "Used"
        elif self.condition == 2:
            return "Lightly used"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Very good"
        elif self.condition == 5:
            return "Excellent"