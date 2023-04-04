import uuid
class Item:
    def __init__(self, id = None, condition = 0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return f"{self.__class__.__name__}"    
    
    def condition_description(self):
        return str(self.condition)