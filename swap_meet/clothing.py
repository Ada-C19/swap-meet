from swap_meet.item import Item

class Clothing(Item):
    
    # def __init__(self, id=None):
    #     if not id:
    #         id = uuid.uuid4().int
    #     self.id = id

    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric 


    # check item file!!!!!!!!
    def __str__(self):
        first_sentence = super().__str__()
        # first_sentence = super().__str__(Item)
        # return f"{first_sentence} It is made from {self.fabric} fabric."

        print("*****************")
        print(f"{first_sentence} It is made from {self.fabric} fabric.")



        