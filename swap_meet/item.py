import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        condition_dict = {
            1: "Bad",
            2: "Not good",
            3: "Okay",
            4: "Good",
            5: "Great"
        }

        if self.condition in condition_dict:
            return condition_dict[self.condition]