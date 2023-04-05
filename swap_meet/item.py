import uuid

class Item:
    def __init__(self, id=None, condition = None):
        self.id = int(uuid.uuid4()) if id is None else id
        self.condition = 0 if condition == None else condition

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return f"{self.__class__.__name__}"
    
    def condition_description(self):
        if self.condition == 0:
            return "..."
        elif 0 < self.condition <= 1:
            return ",,,"
        elif  1 < self.condition <= 2:
            return ":|"
        elif 2 < self.condition <= 3:
            return ":)"
        elif 3 < self.condition <= 4:
            return ":O)"
        else:
            return "BUY IT!"
