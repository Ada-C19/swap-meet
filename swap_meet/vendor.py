class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        # Add an item to inventory
        if item:
            self.inventory.append(item)
        return item

    def remove(self, item):
        # Remove an item from inventory
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            print(f"{err}. Unable to remove '{item}' from inventory.")
            return False

    def get_by_id(self, id):
        # Return item that matches target id
        try:
            for item in self.inventory:
                if item.id == id:
                    return item
        except IndexError as err:
            print(f"{err}. Could not retrieve item '{id}' from inventory.")
            return None

    def swap_items(self, other_vendor, my_item, their_item):
        # Check if swap is even possible
        if (my_item not in self.inventory or their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        # Get first item in each inventory and swap them
        try:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        except IndexError as err:
            print(f"{err}. Item does not exist.")
            return False

    def get_by_category(self, category):
        # Return list of items that match target category
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        # Get list of items that match the target category
        inventory_of_category = self.get_by_category(category)

        if not inventory_of_category:
            return None # List was empty

        # Return item with the highest condition from the list
        return max(inventory_of_category, key=lambda i: i.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # Get our best items that match the others' priority
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        # Swap the best items
        return self.swap_items(other_vendor, my_best, their_best)

    def swap_by_newest(self, other_vendor):
        # Get our youngest items from each inventory
        try:
            my_newest = min(self.inventory, key=lambda i: i.age)
            their_newest = min(other_vendor.inventory, key=lambda i: i.age)
        except ValueError as err:
            print(f"{err}. One or more inventories are missing.")
            return None

        # Swap the newest items
        return self.swap_items(other_vendor, my_newest, their_newest)

