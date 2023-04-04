from swap_meet.item import Item
class Vendor:
    # passing optional argument called inventory 
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        # self.item = Item(self.id, self.condition)
    # method that adds item to inventory 
    def add(self, item):
        if item:
            self.inventory.append(item)
        return item 
    # method that removes item from inventory if in inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item 

    def get_by_id(self, id):
        # if item is in inventory and matches item id the return item
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
            # check if items are in their respective inventories
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        # add item to other inventory and remove it from original inventory 
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        #remove first item from self.inventory and add to other_vendor.inventory
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
        return True

    def get_by_category(self, category):
        # items = []
        # for item in self.inventory:
        #     if item.get_category() == category:
        #         items.append(item)

        items = [item for item in self.inventory if item.get_category() == category]   

        # if not items:
        #     return None
        return items if items else None 
    
    def get_best_by_category(self, category):
        items_matching_category = self.get_by_category(category)
        if not items_matching_category: 
            return None
        highest_condition = max(items_matching_category, key=item.condition)
        return highest_condition
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        vendor_will_give = self.get_best_by_category(their_priority)
        other_vendor_gives = other_vendor.get_best_by_category(my_priority)
        if not vendor_will_give or not other_vendor_gives:
            return False
        swap_items_found = self.swap_items(other_vendor, vendor_will_give, other_vendor_gives)
        return True
