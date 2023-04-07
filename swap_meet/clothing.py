
import uuid


class Clothing:
    def __init__(self, fabric="Unknown", condition=0, id=None):
        if id:
            self.id = id
        else:
            # using uuid to generate random id
            self.id = int(uuid.uuid4())

        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"

    def stringify(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."

# calling the stringfy method
    def __str__(self):
        return self.stringify()

    def condition_description(self):
        if self.condition == 0:
            return "very bad"
        elif self.condition == 1:
            return "bad"
        elif self.condition == 2:
            return "fair"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 5:
            return "great"

        return "not acceptable"
