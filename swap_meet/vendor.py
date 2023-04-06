class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

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
        if not (my_item in self.inventory and their_item in other_vendor.inventory):
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        return result

    def get_best_by_category(self, category):
        items_matching_category = self.get_by_category(category)
        current_max = -1
        result = None
        for item in items_matching_category:
            if item.condition > current_max:
                current_max = item.condition
                result = item
        return result
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        return False
