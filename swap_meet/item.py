import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        id = uuid.uuid4().int if id is None else id
        self.id = id
        self.condition = condition

    def __repr__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return self.__class__.__name__
    
    def condition_description(self):
        descriptions = ["heavily used", "fair","good","like new","never worn","new with tag"]
        return descriptions[self.condition]
    


    
    


