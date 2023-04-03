import uuid

class Item:
    def __init__(self, id = None):
        self.id =  int(uuid.uuid4()) if id is None else id
        
    def get_category(self):
        return "Item"
    
#     In Wave 3 we will write a method to stringify (convert to a string) an Item using str() and write the method swap_items.
    def __str__(self):
        return f"An object of type Item with id {self.id}."

# When we stringify an instance of Item using str(), it returns "An object of type Item with id <id value>.", where <id value> is the id of the Item instance that str() was called on.
# For example, if we had an Item instance item_a = Item(id=12345), the output of str(item_a) should be "An object of type Item with id 12345.".
# To accomplish this, you'll want to investigate what calling str() on a class instance does and how you can override such a method. This type of overriding is known as "operator overloading", put simply, it means that the same method exhibits different behavior across instances of different classes. A simple example would be something like + which for strings means "concatenate" but for numbers, means "add", or for lists, means "combine".
# The remaining tests in wave 3 imply:

# Instances of Vendor have an instance method named swap_items
# It takes 3 arguments:
# swap_items takes 3 arguments:
# an instance of another Vendor (other_vendor), representing the friend that the vendor is swapping with
# an instance of an Item (my_item), representing the item this Vendor instance plans to give
# an instance of an Item (their_item), representing the item the friend Vendor plans to give
# The method removes my_item from this Vendor's inventory, and adds it to the friend's inventory
# The method removes their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
# The method returns True
# If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False
