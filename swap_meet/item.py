import uuid


class Item:
   
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
  
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        conditions_dict = {
            0: "don't waste your money",
            1: "barely holding itself together",
            2: "used with obvious wear and tear",
            3: "used but acceptable",
            4: "barely used",
            5: "like new"
        }

        return conditions_dict.get(self.condition, "Invalid condition value")
