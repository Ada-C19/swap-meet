
import uuid


class Item:
    

# Wave 02
    def __init__(self, category="", condition=0, id=0):
        if id is 0:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.category = category
        self.condition = condition


    def get_category(self):
        return f"{self.__class__.__name__}"


# Wave 03
    def __str__(self):
        return f"An object of type Item with id {self.id}."