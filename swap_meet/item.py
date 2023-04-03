# Item class
# Each item will have a atrribute named ID
# uuid package import? to avoid duplicate #'s
# keyword arg ID and optional int passed in to manually set ID 
# def get_category that returns a string holding the name of the class
# def get_by_id takes in int(item ID) and returns item with matching ID 
# if none matchiing return None
import uuid
class Item:
    # randomized id and set it to an integer
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id
    # accessing the class name of self (item)
    def get_category(self):
        return self.__class__.__name__
    
