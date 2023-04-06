from swap_meet.item import Item

class Electronics(Item):
    
    # Wave 05
    def __init__(self, condition=0, id=0, type="Unknown"):
        super().__init__(category="Electronics",condition=condition,id=id)

        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
