# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
        
    def get_by_id(self, int):
        for item in self.inventory:
            if item.id == int:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory or my_item not in self.inventory:
            return False
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
        if their_item in other_vendor.inventory:
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        first_self_item = self.inventory[0]
        first_other_item = other_vendor.inventory[0]

        if first_self_item == self.inventory[0]:
            self.inventory.remove(first_self_item)
            other_vendor.inventory.append(first_self_item)
        if first_other_item == other_vendor.inventory[0]:
            other_vendor.inventory.remove(first_other_item)
            self.inventory.append(first_other_item)
        
        return True

    
