from swap_meet.item import Item
class Electronics:
    def __init__(self, category="Electronics", type="Unknown"):
        super().__init__(category)
        self.type = type
        
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    def get_category(self):
        return f"{self.category}"
