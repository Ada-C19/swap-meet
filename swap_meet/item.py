import uuid 

class Item:
    def __init__(self, id=None, condition=0):
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        description = ""
        if self.condition >= 0 and self.condition <1:
            description = "This item should not even be allowed to be here."
        if self.condition >= 1 and self.condition <2:
            description = "This item has seen better days."
        if self.condition >= 3 and self.condition <4:  
            description = "This item is not the best but also not the worst"
        if self.condition >= 4 and self.condition <5:
            description = "This item is the best there is."

        return description