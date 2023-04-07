import uuid

class Item:

    # item constructor 
    def __init__(self, id = None, condition = 0.0):
        if not id: 
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
    
    # get by category method
    def get_category(self): 
        return self.__class__.__name__
    
    # stringify a method using dunder str
    def __str__(self): 
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self): 
        approx_value = round(self.condition)
        if approx_value == 5:
            return "New"
        elif approx_value == 4:
            return "Like New"
        elif approx_value == 3:
            return "Used"
        elif approx_value == 2:
            return "...Very Used"
        elif approx_value == 1:
            return "Barely Usable/Functional"
        else:
            return "Scrap Materials for DIY Project"

    