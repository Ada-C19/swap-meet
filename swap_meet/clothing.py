from swap_meet.item import Item

class Clothing(Item):
    
    # def __init__(self, id=None):
    #     if not id:
    #         id = uuid.uuid4().int
    #     self.id = id

    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric



    def __str__(self):
        first_sentence = super().__str__()
        # first_sentence = super().__str__(Item)
        # return f"{first_sentence} It is made from {self.fabric} fabric."

        # added return and was able to pass two more tests
        #  print(f"{first_sentence} It is made from {self.fabric} fabric.")
        return f"{first_sentence} It is made from {self.fabric} fabric."


        