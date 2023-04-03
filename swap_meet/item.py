import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid1()
            self.id = int(id)
        else:
            self.id = id


    def get_category(self):
        # return "Item"
