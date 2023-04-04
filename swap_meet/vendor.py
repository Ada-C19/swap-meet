
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

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
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        result = self.swap_items(other_vendor, my_first_item, their_first_item)
        return result

    def get_by_category(self, category):
        category_items_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_items_list.append(item)
        return category_items_list

    def get_best_by_category(self, category):
        category_items_list = self.get_by_category(category)
        if category_items_list:
            best_item = max(category_items_list,
                            key=lambda item: item.condition)
            return best_item
        return None

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        result = self.swap_items(other_vendor, my_best_item, their_best_item)

        return result

    def get_newest_item(self):
        if self.inventory:
            return min(self.inventory, key=lambda item: item.age)
        return None

    def swap_by_newest(self, other_vendor):
        my_newest_item = self.get_newest_item()
        their_newest_item = other_vendor.get_newest_item()

        result = self.swap_items(
            other_vendor, my_newest_item, their_newest_item)

        return result
