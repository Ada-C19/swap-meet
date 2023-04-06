import uuid


class Clothing:

    def __init__(self, id=None, fabric="Unknown", condition=0):
        self.fabric = fabric
        if id:
            self.id = id
        else:
            self.id = int(uuid.uuid4())
        self.condition = condition

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def condition_description(self):
        if self.condition == 0:
            return "cannot reuse"
        elif self.condition == 1:
            return "poor"
        elif self.condition == 2:
            return "heavily used"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "like-new"
        elif self.condition == 5:
            return "new"
