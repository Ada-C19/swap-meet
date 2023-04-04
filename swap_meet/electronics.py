import uuid
from swap_meet.item import Item
    
class Electronics(Item):

    def __init__(self, id=None, type="Unknown",condition= 0.0):
        self.id = id if id is not None else int(uuid.uuid4())
        self.type = type
        self.condition = condition



    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    def condition_description(self, condition):
        
        condition_dict = {
            0: "Horrible",
            1: "Damaged",
            2: "Average",
            3: "Good",
            4: "Great",
            5: "Mint"
        }

        return condition_dict[int(condition)]