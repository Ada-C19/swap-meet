from swap_meet.item import Item



class Decor(Item):
    
    # Wave 05
    def __init__(self, width=0, length=0, id=0, condition=0):

        super().__init__(category="Decor",condition=condition,id=id)

        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"


    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

