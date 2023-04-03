import uuid

class Item:
    def __init__(self,id):
        self.id = uuid4()

    def get_category(self, item):
        self.item = Item(item):
