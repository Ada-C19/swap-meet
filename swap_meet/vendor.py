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
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        # Checks corresponding items are in inventories
        if (my_item not in self.inventory or 
                their_item not in other_vendor.inventory):
            return False
        
        # Gives vendor's item to other vendor
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)

        # Receives other vendor's item
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True
    
    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)

        return items

    def get_best_by_category(self, category):
        category_items = {}

        for item in self.inventory:
            if item.get_category() == category:
                category_items[item] = item.condition

        if not category_items:
            return None
        
        best_item = max(category_items, key=category_items.get)

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        
        if not my_best or not their_best:
            return False
        
        self.swap_items(other_vendor, my_best, their_best)
        
        return True