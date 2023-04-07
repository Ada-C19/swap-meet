# from swap_meet.item import Item


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
        else:
            return False

    def get_by_id(self, item_id):
        self.item_id = item_id
        for item in self.inventory:
            if self.item_id == item.id:
                return item
        else:
            return None

    def swap_items(self, other_vendor, my_item, their_item):
        if self.inventory == [] or other_vendor.inventory == []:
            return False

        if their_item not in other_vendor.inventory:
            return False

        if my_item not in self.inventory:
            return False

        other_vendor.add(my_item)
        self.add(their_item)

        self.remove(my_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):

        if self.inventory == [] or other_vendor.inventory == []:
            return False

        their_item = other_vendor.inventory[0]
        my_item = self.inventory[0]
        a = self.swap_items(other_vendor, my_item, their_item)

        return a

    def get_by_category(self, category):
        list_of_objects = []

        for item in self.inventory:
            if category == item.get_category():
                list_of_objects.append(item)
        return list_of_objects

    def get_best_by_category(self, category):

        highest_condition = 0
        best_item = None

        for item in self.inventory:
            if category == item.get_category() and item.condition > highest_condition:
                best_item = item
                highest_condition = item.condition
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item:
            return False
        if not their_best_item:
            return False

        self.remove(my_best_item)
        other_vendor.remove(their_best_item)

        self.add(their_best_item)
        other_vendor.add(my_best_item)

        return True
