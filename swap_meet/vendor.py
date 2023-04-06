class Vendor:
    """Create a Vendor that has inventory which can be changed or swapped with other vendors."""

    def __init__(self, inventory=None):
        self.inventory = inventory
        if not self.inventory:
            self.inventory = []

    def add(self, item):
        """Add an item to inventory."""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Remove an item from inventory."""
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_id(self, id):
        """Return an item given the item's id."""
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        """Exchange items between vendors."""
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        """Exchange first items between vendors."""
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, other_vendor_first_item)
        return True

    def get_by_category(self, category):
        """Return a list of items in inventory given a category."""
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        """Return the best quality item in inventory in a specific category."""
        options = self.get_by_category(category)
        if options:
            best_condition_avail = max(option.condition for option in options)
        else:
            return None
        for option in options:
            if option.condition == best_condition_avail:
                return option

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """Exchange best quality items between vendors given a preferred category."""
        item_other_vendor_wants = self.get_best_by_category(their_priority)
        item_self_wants = other_vendor.get_best_by_category(my_priority)
        if item_other_vendor_wants and item_self_wants:
            self.swap_items(other_vendor, item_other_vendor_wants, item_self_wants)
            return True
        else:
            return False
