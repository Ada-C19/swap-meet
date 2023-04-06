import uuid

#Dictionary stores the value and it's respective description. Used in condition_description method 
CONDITION_VALUE__DESCRIPTION_DICT = {
            0 : "Questionable matter...maybe buy it new...",
            1 : "It's alright....",
            2 : "Decent...",
            3 : "Great",
            4 : "This is beautiful :,)",
            5 : "Wow!!! Buy it NOW!!!"
        }

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
        return CONDITION_VALUE__DESCRIPTION_DICT[self.condition]
