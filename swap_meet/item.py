import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            id = uuid.uuid4()
            self.id = int(id)
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        #convert to a dict later?
        condition_dict = {}

        if self.condition == 0:
            return "Questionable matter...maybe buy it new..."
        elif self.condition == 1:
            return "Decent..."
        elif self.condition == 2:
            return "It's alright...."
        elif self.condition == 3:
            return "Great"
        elif self.condition == 4:
            return "This is beautiful :,)"
        else:
            return "Wow!!! Buy it NOW!!!"
