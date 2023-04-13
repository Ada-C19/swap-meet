import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition
        self.category = "Item"  

    def __eq__(self, other):
            if isinstance(other, Item):
                return self.id == other.id
            return False

    def __str__(self):
        return f"An object of type Item with id {self.id}. It has a condition of {self.condition}."

    def get_category(self):
        return self.category  

    def condition_description(self):
        if self.condition <= 1:
            return "You probably want a glove for this one..."
        elif self.condition <= 2:
            return "Heavily used"
        elif self.condition <= 3:
            return "Fairly used"
        elif self.condition <= 4:
            return "Lightly used"
        elif self.condition <= 5:
            return "Mint condition"
        else:
            return "Unknown condition"
