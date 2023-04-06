from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        self.type = type
        super().__init__(id, condition)

    def get_category(self):
        # return "Electronics"
        return type(self).__name__
    
    def __str__(self):
        return f'An object of type Electronics with id {self.id}. This is a {self.type} device.'
    
    def condition_description(self):
        some_condition = super().condition_description()
        return some_condition