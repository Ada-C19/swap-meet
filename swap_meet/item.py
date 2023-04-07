import uuid


class Item:

    def __init__(self, id = None, condition = 0):
        if not id:
            id = int(uuid.uuid4())
        self.id = id
        self.condition = condition

    def condition_description(self):
        if self.condition == 0:
            return 'this is Garbage!'
        elif 1 <= self.condition < 2:
            return 'ITS A SCAM'
        elif 2 <= self.condition < 3:
            return "not bad! It's your money though"
        elif 3 <= self.condition <= 5:
            return "OMG GET IT!"
        


    def get_category(self):
        return (self.__class__.__name__)
    

    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'



