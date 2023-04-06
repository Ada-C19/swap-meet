from uuid import uuid4
from uuid import getnode

class Item:
    def __init__(self, id = None, condition = 0, age = 0):
        self.id = id if id else uuid4().int
        # self.id = int(uuid4())
        self.condition = condition
        self.conditions_dict = {
            0: "There is a very evil, ancient spirit attached to this item",
            1: "We unearthed this from a haunted gravesite",
            2:"We unearthed this from an unhaunted gravesite",
            3:"This item has never been buried in a gravesite",
            4:"This item is used, but has never been haunted",
            5:"This item is brand new and has had no opportunity to be touched by the spirits...yet"}
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        return self.conditions_dict[self.condition]
        