import uuid

condition_descriptions = {
    0: "Ewww! Put that down right now and wash your hands!",
    1: "This item is disintegrating as we speak!",
    2: "There's nothing to write home about here...",
    3: "This item is in a pretty good condition.",
    4: "This item is in a pretty good condition.",
    5: "This item is like brand new. Amazing!",
}


class Item:
    
    def __init__(self, id=None, condition=0):
        # If user passes in custom id, set id to that number, otherwise generate one
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        
        self.condition = condition
        self.category = "Item"
        
    def get_category(self):
        """Output: the name of the Class"""
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        return condition_descriptions[self.condition]



