import uuid

class Item:
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = int(uuid.uuid4())
        print({self.id})

    def get_category(self):
        class_name = Item()
        return class_name.__class__.__name__
