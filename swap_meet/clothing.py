from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition = 0, fabric = "Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        # get_category = super().get_category()
        # return get_category
        return __class__.__name__

    
    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It is made from {self.fabric}."

    # def condition_description(self):
    #     return super().condition_description()