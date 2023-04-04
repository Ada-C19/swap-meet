class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, added_item):
        (self.inventory).append(added_item)
        return added_item
    
    def remove(self,item_removed):
        if item_removed not in self.inventory:
            return False
        else:
            for item in self.inventory:
                if item_removed == item:
                    (self.inventory).remove(item)
                    return item_removed

    def get_by_id(self, id_num):
        for item in self.inventory:
            if item.id == id_num:
                return item
            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True