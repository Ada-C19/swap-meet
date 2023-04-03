import uuid as uuid

# We can use uuid.uuid4() which will return an object
# We can then use an attribute
# class Item:
#     def __init__(self, id):
#         self.id = id

#     def get_category(): 
#         pass
        # return str of the name of the class

class Item:
    def __init__(self, category="", condition=0.0, id=None):
        self.category = category
        self.condition = condition
        # if there is no id
        if id is None:
            # generate uniquie id as an int
            self.id = uuid.uuid4().int
        else:
            self.id = id
    # Each `Item` will have function named `get_category`
    def get_category(self):
        # return a string holding the name of the class
        return self.__class__.__name__


# when initializing an instance of Item, can optionally pass in an intger with a keyword arg id to manually set id
# item = Item(id)

    # this is described as a function and not a method - why? 
    def get_by_id(self, item_id):
        # for each item in my inventory
        for item_id in self.inventory:
            # if id in question matches any item_id i have,
            if item_id == item_id:
        # return item with matching id from inventory
                return item_id
            # if no matching item, then return None
            return None  
        

    def swap_items(self, other_vendor, my_item, their_item):
        # if i have item to give and they have their item to give 
        if my_item in self.inventory and their_item in other_vendor.inventory:
            # remove item from my list to...
            self.remove(my_item)
            # add to the other vendor's list then...
            other_vendor.add(my_item)
            # removes their item to give from their list
            other_vendor.remove(their_item)
            # and adds their item to my list
            self.add(their_item)
            return True
        return False
import swap_meet.vendor as Vendor
import uuid 

# We can use uuid.uuid4() which will return an object
# which will look like this - UUID('16fd2706-8baf-433b-82eb-8c7fada847da')
# We can then use an attribute to get the actual integer called 'int'

# Example: id = uuid.uuid4() | then: id_int = id.int


class Item:
    def __init__(self, id=None):
        if id == None: 
            self.id = uuid.uuid4().int
        else: 
            id = None

    def get_category(self): 
        return self.__class__.__name__
