import uuid

class Item:
    def __init__(self, id = None, condition=0):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "YIKES"
        elif self.condition == 1:
            return "Gross, but not the grossest"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Mid"
        elif self.condition == 4:
            return "Pretty good"
        else:
            return "Peak"

# #class Item:
#     def __init__(self, id = None, condition = 0, category = None):
#         self.category = category
#         self.condition = condition
#         self.id = id #or uuid.uuid4()
