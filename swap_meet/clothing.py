
import uuid


class Clothing:
    def __init__(self, fabric="Unknown", id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.fabric = fabric

    def get_category(self):
        return "Clothing"
