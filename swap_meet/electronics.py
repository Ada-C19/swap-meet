from .item import Item

class Electronics(Item):
    
    def __init__(self, age=0, id=None, condition=0, type="Unknown"):
        super().__init__(age, id, condition)
        self.type = type
    

    def get_category(self):
        return "Electronics"


    def __str__(self):
        line1 = super().__str__()
        line2 = f"This is a {self.type} device."
        return " ".join((line1, line2))