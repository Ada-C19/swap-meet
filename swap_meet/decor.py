from swap_meet.item import Item

class Decor(Item):
    # category = "Decor"

    def __init__(self, condition=0, id=None, width=0, length=0, category = "Decor"):
        # super().__init__(category=Decor.category, condition=condition, id=id)
        super().__init__(condition=condition, id=id)

        self.width = width
        self.length = length
        self.category = category

    def condition_description(self):
        return super().condition_description()

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def get_category(self):
        return self.category
