from swap_meet.item import Item

class Decor(Item):
<<<<<<< HEAD
    pass
    def __init__(self, id=None, width=0, length=0):
        super().__init__(id)
        self.width = width
        self.length = length

def get_category(self):
    return self.__class__.__name__


def __str__(self):
    type_and_id_msg = super().__str__()
    width_and_length_msg = f"It takes up a {self.width} by {self.length} sized space."
    return f"{type_and_id_msg}{width_and_length_msg}"
    
=======
    pass
>>>>>>> 1b69ed7e0962ae8895d004327e672a5b88cd82f3
