import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if not id:
            self.id = int(uuid.uuid4())
        else:
            self.id = id 
        self.category = "Item"
        self.condition = condition

    def get_category(self):
        return self.category

    def __str__(self):
        description_string = f"An object of type {self.get_category()} with id {self.id}."
        return description_string
        
    def condition_description(self):
        if self.condition == 0:
            return "Garbage"
        elif self.condition == 1:
            return "Could be worse"
        elif self.condition == 2:
            return "Meh"
        elif self.condition == 3:
            return "It's fine"
        elif self.condition == 4:
            return "My grandma would love this"
        elif self.condition == 5:
            return "Perfection on earth"
