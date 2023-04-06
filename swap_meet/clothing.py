from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric



    def __str__(self):
        first_sentence = super().__str__()

        return f"{first_sentence} It is made from {self.fabric} fabric."


