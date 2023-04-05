import uuid
# from swap_meet import Vendor


class Item:
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

    def get_category(self):
        return "Item"
