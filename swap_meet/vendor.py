class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        their_first_item = other_vendor.inventory[0]
        my_first_item = self.inventory[0]
        self.swap_items(other_vendor, my_first_item, their_first_item)
        return True

    def get_by_category(self, category):
        objects_of_category = []
        for item in self.inventory:
            if item.get_category() == category:
                objects_of_category.append(item)
        return objects_of_category

    def get_best_by_category(self, category):
        best_item = None
        best_item_condition = 0
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > best_item_condition:
                    best_item = item
                    best_item_condition = item.condition
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item_for_them = self.get_best_by_category(their_priority)
        their_item_for_me = other_vendor.get_best_by_category(my_priority)
        if my_item_for_them is None or their_item_for_me is None:
            return False
        self.swap_items(other_vendor, my_item_for_them, their_item_for_me)
        return True
