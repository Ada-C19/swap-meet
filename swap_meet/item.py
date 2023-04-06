from uuid import uuid4
import math

class Item:
    def __init__(self, age=0, id=None, condition=0):
        self.age = age
        self.id = uuid4().int if id is None else id
        self.condition = condition
        

    def get_category(self):
        # check if need to cast into str
        return "Item"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        CONDITION_DESCRIPTIONS = { 0: "awful. the worst item you can possibly imagine",
                                  1: "could be worse",
                                  2: "could be better",
                                  3: "fine. do u really want this tho",
                                  4: "pretty good tbqh",
                                  5: "get it before someone else does!!!!!!!!"}
        formatted_condition_value = math.floor(self.condition)
        
        return CONDITION_DESCRIPTIONS[formatted_condition_value]