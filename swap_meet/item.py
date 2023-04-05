from uuid import uuid1

class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.id = uuid1().int if id is None else id
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return "Item"
    
    def condition_description(self):
        condition_description_list = [
            "Busted", 
            "Bad", 
            "Used", 
            "Good", 
            "Like New", 
            "Mint"
            ]

        return (f"{condition_description_list[self.condition]}")