import uuid

class Item:
    def __init__(self, id = None, condition=0, age=0):
        self.id = uuid.uuid1().int if id is None else id
        self.condition = condition
        self.age = age
    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        try:
            condition = {
            5:"Mint condition",
            4:"Great",
            3:"Decent",
            2:"It's okay",
            1:"Needs TLC",
            0:"Pass on this"
        }
            print(condition[self.condition])
            return condition[self.condition]
        except KeyError: 
            print("That is not a valid condition rating.")
