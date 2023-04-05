import uuid
class Item:
    def __init__(self, id = None, condition = 0):
        self.condition = condition
    
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
    

    def get_category(self):
        return "Item"
    

    def __str__(self):
        return f"An object of type Item with id {self.id}."


    def condition_description(self):
        if self.condition == 5:
            return "Brand new with tags"
        elif self.condition == 4:
            return "Like new"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 1:
            return "Heavily used"
        else:
            return "Poor"