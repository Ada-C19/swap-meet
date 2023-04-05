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
    
