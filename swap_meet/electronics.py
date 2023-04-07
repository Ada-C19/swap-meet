from swap_meet.item import Item

class Electronics(Item):
        
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type


    def __str__(self):
        first_sentence = super().__str__()

        return f"{first_sentence} This is a {self.type} device."
