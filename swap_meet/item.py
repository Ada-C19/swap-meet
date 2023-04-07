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
            0: "Trash",
            1: "Yikes",
            2: "Meh",
            3: "Okay",
            4: "Pretty good",
            5: "Brilliant, incredible, amazing, show stopping, spectacular, never the same, totally unique, completely not ever been done before"
        }

        if self.condition in condition_dict:
            return condition_dict[self.condition]