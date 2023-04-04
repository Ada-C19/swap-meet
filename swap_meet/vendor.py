from swap_meet.item import Item

class Vendor:

    # need attribute called inventory: empty list by default
    # self.iventory
    # instantiate vendor with keyword argument 'inventory'/pass in list
    
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    # create instance method called add that takes in one item
    # add that item to inventory via the instance method and return item

    def add(self, item):
        self.inventory.append(item)
        return item

    # create instance method called remove that takes in one item
    # method removes the matching item from inventory
    # return item
    # if no matching item, return false

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    # create instance method called get_by_id
    # takes one argument: an integer that represents an Item's id
    # method returns item with matching id from inventory 
    # if no matching item in inventory, return None.

    def get_by_id(self, id):
        
        for item in self.inventory:
            if id == item.id:
                return item
    
        return None


    # create method called swap_items
    # takes 3 arguments: other_vendor, my_item, their_item
    # remove my_item and add to their inventory
    # remove their item and add to my inventory
    # return Tru
    # if item not in either inventories, return False

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)

            other_vendor.remove(their_item)
            self.add(their_item)
            return True


    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, my_first_item, their_first_item)




