from swap_meet.item import Item

#import uuid

    # Wave 05
class Clothing(Item):

    def __init__(self, condition=0, id=0, fabric="Unknown"):

        super().__init__(category="Clothing", condition=condition, id=id)

        self.fabric = fabric
        #self.category = "Clothing"

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    
    def condition_description(self):
        if self.condition == 5:
            return "Thrift Gem!"
        if self. condition == 4:
            return "Still has the tag"
        if self.condition == 3:
            return "Sustainable"
        if self.condition == 2:
            return "Fair trade"
        if self. condition == 1:
            return "Only a dollar"
        else:
            return "Thrift Bust"
        




