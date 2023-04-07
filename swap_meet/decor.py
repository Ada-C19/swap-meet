from .item import Item

class Decor(Item):
    def __init__(self, condition, id=0, width = None, length = None, category="Decor"):
       super().__init__(id, category, condition)
       self.width = 0 if width is None else width
       self.length = 0 if width is None else length


    def __str__(self):
       item_descript = super().__str__()
       decor_description = f'It takes up a {self.width} by {self.length} sized space.'
       return f"{item_descript} {decor_description}"