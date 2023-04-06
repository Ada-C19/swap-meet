from .item import Item
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

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_item, their_item)

        return True

    def get_by_category(self, category):
        return [item_obj for item_obj in self.inventory if item_obj.get_category() == category]

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None

        best_item = max(category_list, key=lambda item: item.condition)

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True