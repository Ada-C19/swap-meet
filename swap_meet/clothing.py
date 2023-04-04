from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category="Clothing",condition=0,fabric="Unknown", id=None):
        super().__init__(category, condition, id)    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def get_category(self):
        return f"{self.category}"
    
    def condition_description(self):
        return super().condition_description()
    
    