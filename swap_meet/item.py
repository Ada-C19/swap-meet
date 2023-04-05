import uuid

#Wave 2
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
        if self.condition == 0:
            return "don't waste your money"
        elif self.condition == 1:
            return "barely holding itself together"
        elif self.condition == 2:
            return "used with obvious wear and tear"
        elif self.condition == 3:
            return "used but acceptable"
        elif self.condition == 4:
            return "barely used"
        elif self.condition == 5:
            return "like new"
        else:
            return "Please include a condition value between 0 and 5."
