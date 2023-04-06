from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric 

    def get_category(self):
        return "Clothing"
        #change to get the actual name with a special method

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    
    # def condition_description(self):
    #     return super().condition_description(self.condition)
    def condition_description(self):
        # type_condition = super().condition_description()
        # return type_condition
        return super().condition_description()