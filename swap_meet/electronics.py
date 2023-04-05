from swap_meet.item import Item

class Electronics(Item):
    category = "Electronics"

    def __init__(self, condition=0, type="Unknown", id=None):
        super().__init__(condition=condition, id=id)
        self.type = type

    def __str__(self):
        if self.type != "Unknown":
            return f"An object of type Electronics with id {self.id}. It is a {self.type} device."
        else:
            return f"An object of type Electronics with id {self.id}. It is an {self.type} device."

    def get_category(self):
        return Electronics.category

    def condition_description(self):
        return super().condition_description()
