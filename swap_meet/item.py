import uuid

class Item:
    def __init__(self,id=None,condition=0):
        if id is None:

            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def condition_description(self):
        descriptions = {
            0: (0.0, "overused eww"),
            1: (1.0, "not great"),
            2: (2.0, "okay"),
            3: (3.0, "not bad"),
            4: (4.0, "great"),
            5: (5.0, "mint")
        }
        return descriptions.get(self.condition, "invalid condition value")[1]


    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def swap_items(self, other_item):
        self.id, other_item.id = other_item.id, self.id
