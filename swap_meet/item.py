import uuid

"""
    In Wave 2 we will create the Item class and the Vendor class' get_by_id method.
    There is a module (file) named item.py inside of the swap_meet package (folder)
    Inside this module, there is a class named Item
    Each Item will have an attribute named id, which is a unique integer by default
    There are many ways to generate numbers, but generating numbers without duplicates takes some care. 
    Happily, Python has a package called uuid that can help!
    With a little research we can use one of the functions uuid provides to create large unique numbers meant to be used as identifiers
    Specifically, you'll need to choose which of the uuid package's functions to use, so be sure to consider which function will work best for creating a unique integer
    Note that this package's functions return UUID objects, not integers as such, but UUID objects have an attribute int which allow us to access their value as an integer
    When we initialize an instance of Item, we can optionally pass in an integer with the keyword argument id to manually set the Item's id
    Each Item will have a function named get_category, which will return a string holding the name of the class
    Instances of Vendor have an instance method named get_by_id
    This method takes one argument: an integer, representing an Item's id
    This method returns the item with a matching id from the inventory
    If there is no matching item in the inventory, the method should explicitly return None

"""

class Item:

    # def add_to_list_ok(word, word_list=None):
    # word_list = word_list if word_list is not None else []
    def __init__(self, id=None, condition= 0.0):
        self.id = id if id is not None else int(uuid.uuid4())
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self, condition):
        int_condition = int(condition)
        condition_dict = {
            0: "Horrible",
            1: "Damaged",
            2: "Average",
            3: "Good",
            4: "Great",
            5: "Mint"
        }

        return condition_dict[int_condition]

    
    