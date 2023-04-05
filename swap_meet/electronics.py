from swap_meet.item import Item


class Electronics(Item):

    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
        self.category = "Electronics"

    def __str__(self):
        category_id_description = super().__str__()
        return f"{category_id_description} This is a {self.type} device."
