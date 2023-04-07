class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        """This function adds an item to the inventory"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """This function removes an item from the inventory"""
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        """This function returns an item by it's id"""
        for item in self.inventory:
            if id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        """This function swaps an item from the inventory with another vendor's item from their inventory"""
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        return True

    def swap_first_item(self, other_vendor):
        """This function swaps the item first in the inventory list"""
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_by_category(self, category):
        """This function returns a list of items in the inventory of a specific category"""
        category_list = []

        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list

    def get_best_by_category(self, category):
        """This function returns the item with the best condition by category"""
        if not self.get_by_category(category):
            return None

        return max(self.get_by_category(category), key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """This function swaps the item with the best condition by category with another vendor's"""
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(
            my_priority
        ):
            return False

        my_swap_item = self.get_best_by_category(their_priority)
        other_swap_item = other_vendor.get_best_by_category(my_priority)

        self.swap_items(other_vendor, my_swap_item, other_swap_item)
        return True

    def swap_by_newest(self, other_vendor):
        """This function swaps the newest item with another vendor's newest item"""
        if not self.inventory or not other_vendor.inventory:
            return False

        my_newest = min(self.inventory, key=lambda item: item.age)
        their_newest = min(other_vendor.inventory, key=lambda item: item.age)

        self.swap_items(other_vendor, my_newest, their_newest)
        return True
