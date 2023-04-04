import uuid

class Item:
    def __init__(self, id = None, condition = 0, age = 0):
        self.id =  int(uuid.uuid4()) if id is None else id
        self.condition = condition
        self.age = age
        
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "The condition is 0, heavily discounted for a reason. It's probably stained with something you don't want to know."
        if self.condition == 1:
            return "The condition is 1, moderately discounted for a reason. It may have been forgotten for many years in a musty basement."
        if self.condition == 2:
            return "The condition is 2, somewhat discounted for a reason. Only a little bit haunted."
        if self.condition == 3:
            return "The condition is 3, a little discounted for a reason. The last owner may or may not have died, but it's not haunted, don't worry."
        if self.condition == 4:
            return "The condition is 4, barely discounted for a reason. Honestly, look at it. That's in nice condition."
        if self.condition == 5:
            return "The condition is 5, there is no discount for a reason. Honestly, look at it. That's in pristine condition."

