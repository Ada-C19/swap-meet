from swap_meet.item import Item

class Clothing(Item):
    # category = "Clothing"

    def __init__(self, condition=0, fabric="Unknown", id=None, category="Clothing"):
        super().__init__(condition=condition, id=id)
        self.fabric = fabric
        self.category = category
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def get_category(self):
        return self.category
    
    def condition_description(self):
        return super().condition_description()
