import uuid

class Item:
    def __init__(self, id = None):
        
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return __class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with {self.id}"

# class Item
# def __str__(self, item):
# returns `"An object of type Item with id <id value>."`
# For example, if we had an `Item` instance `item_a = Item(id=12345)`


# class Vendor

# def swap_items(self, other_vendor, my_item, their_item): -> my_item plans to give
# remove my_item from self.vendor append to other_vendor
# remove their_item from other_vendor append self.vendor[]
# return True

# if not my_item in vendor or not their_item in other_vendor:
# return False