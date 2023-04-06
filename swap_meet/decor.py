from swap_meet.item import Item


class Decor(Item):
    """In addition to Item attributes, includes length and width.

    __str__ overrides Item's
    """

    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(condition=condition, id=id)
        self.width = width
        self.length = length

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
