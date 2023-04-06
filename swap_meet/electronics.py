from swap_meet.item import Item

class Electronics(Item):
        
    def __init__(self, id=None, type="Unknown"):
        super().__init__(id)
        self.type = type


    def __str__(self):
        first_sentence = super().__str__()
        print(f"{first_sentence} This is a {self.type} mobile device.")
