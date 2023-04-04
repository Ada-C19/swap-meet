import uuid


class Item:
    
    def __init__(self, id=None, condition=0):
        # If user passes in custom id, set id to that number, otherwise generate one
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int
        
        self.condition = condition

    def get_category(self):
        """Output: the name of the Class"""
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self, value):
        if value == 5:
            return "This item is like brand new. Amazing!"
        elif value == 4:
            return "This item is in a pretty good condition."
        elif value == 3:
            return "This item is in a fair condition."
        elif value == 2:
            return "There's nothing to write home about here..."
        elif value == 1:
            return "This item is disintegrating as we speak!"
        elif value == 0:
            return "Ewww! Put that down right now and wash your hands!"


