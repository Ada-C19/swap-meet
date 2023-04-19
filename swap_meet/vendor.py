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
        self.inventory.remove(item)
        return item
        
    def get_by_id(self, int):
        for item in self.inventory:
            if item.id == int:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if their_item not in other_vendor.inventory \
            or my_item not in self.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
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

    def get_by_category(self, category):
        category_list = [item for item in self.inventory if item.get_category() == category]
        return category_list

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        highest_condition = 0
        highest_condition_item = category_list[0]
        for item in category_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_condition_item = item
        return highest_condition_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        other_vendors_item = other_vendor.get_best_by_category(my_priority)
        vendors_item = self.get_best_by_category(their_priority)
        if not vendors_item or not other_vendors_item:
            return False
        return self.swap_items(other_vendor, vendors_item, other_vendors_item)