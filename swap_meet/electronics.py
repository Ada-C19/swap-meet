from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0.0):
        super().__init__(id)
        self.type = type
        self.condition = condition

    def __str__(self):
        category_message = super().__str__()
        return f"{category_message} This is a {self.type} device."

