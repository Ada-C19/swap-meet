from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
        
    
    def __str__(self):
        my_string = f'{self.id}'
        return f"An object of type {self.get_category()} with id {my_string}. This is a {self.type} device."
    
