import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
    

    def get_category(self):
        # returns any objects name
        return self.__class__.__name__
    

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    

    def condition_description(self):
        if not 0 <= self.condition <= 5:
            return None
        elif 0 <= self.condition <=2:
            return "Poor condition"
        elif self.condition == 3:
            return "Average condition"
        elif self.condition == 4:
            return "Almost as good as new."
        elif self.condition == 5:
            return "As good as new! Mint condition."