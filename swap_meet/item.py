import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return "Item"
    

# #class Item:
#     def __init__(self, id = None, condition = 0, category = None):
#         self.category = category
#         self.condition = condition
#         self.id = id #or uuid.uuid4()

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
    def __init__(self, id = None, condition=0):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        if self.condition == 0:
            return "This item is in terrible condition"
        elif self.condition == 1:
            return "This item is in very bad condition"
        elif self.condition == 2:
            return "This item is in bad condition"
        elif self.condition == 3:
            return "This item is in good condition"
        elif self.condition == 4:
            return "This item is in very good condition"
        elif self.condition == 5:
            return "This item is in excellent condition"