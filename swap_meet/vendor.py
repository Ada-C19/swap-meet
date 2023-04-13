from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None
        best_item = max(items, key=lambda item: item.condition)
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    def get_by_id(self, item_id):
            for item in self.inventory:
                if item.id == item_id:
                    return item
            return None
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
        return True