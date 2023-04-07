
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

    def stringify(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

# calling the stringfy method
    def __str__(self):
        return self.stringify()
