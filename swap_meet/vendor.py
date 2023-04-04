class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, added_item):
        # self.added_item = added_item
        (self.inventory).append(added_item)
        return added_item
    
    def remove(self,item_removed):
        # self.item_removed = item_removed
        if item_removed not in self.inventory:
            return False
        else:
            for item in self.inventory:
                if item_removed == item:
                    (self.inventory).remove(item)
                    return item_removed

# not sure if code below belongs in the Item class
# passed all tests, so I guess iz ok
    def get_by_id(self, id_num):
        for item in self.inventory:
            if item.id == id_num:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        # self.other_vendor = other_vendor
        # self.my_item = my_item
        # self.their_item = their_item
        # if my_item not in other_vendor.inventory or their_item not in self.inventory:
        if my_item not in self.inventory or their_item not in other_vendor.inventory:

            return False
        else:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True