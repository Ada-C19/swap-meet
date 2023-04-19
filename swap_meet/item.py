import uuid

class Item():

    def __init__(self, id=None, condition=0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
        self.condition = condition
    
    def get_category(self):
        return "Item"


    def __str__(self) -> str:
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        item_condition = ["mint", "like new", "gently used", "vintage", "heavily used", "worn"]
        return item_condition[int(self.condition)]

