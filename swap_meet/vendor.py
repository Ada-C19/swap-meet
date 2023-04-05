class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
        else:    
            return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        # Does not execute swap if either item doesn't exist
        if (my_item not in self.inventory or 
                their_item not in other_vendor.inventory):
            return False

        # Gives vendor's item to other_vendor
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)

        # Receives other_vendor's item
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        try:
            # Returns True if swap executes
            return self.swap_items(other_vendor, self.inventory[0], 
                                    other_vendor.inventory[0])
        except IndexError:
            return False
        
    def get_by_category(self, category):
        # Returns a list of items in category
        return [item for item in self.inventory
                if item.get_category() == category]

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        try:
            # Returns item with best condition rating
            return max(category_items, key=lambda item: item.condition)
        except ValueError:
            return None

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        # Returns True if swap executes, returns False otherwise
        return self.swap_items(other_vendor, my_best, their_best)
    
    def swap_by_newest(self, other_vendor):
        try:
            my_newest = min(self.inventory, key=lambda item: item.age)
            their_newest = min(other_vendor.inventory, key=lambda item: item.age)
        except ValueError:
            return None
        # Returns True if swap executes, returns False otherwise
        return self.swap_items(other_vendor, my_newest, their_newest)