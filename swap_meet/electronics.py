from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, id=0, condition= 0, type= None):
        super().__init__(id, condition)
        self.type = type if type else "Unknown"
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {str(self.id)}. This is a {self.type} device."
