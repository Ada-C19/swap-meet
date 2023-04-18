#Wave 1
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
        
#Wave2
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item

        return None

#Wave3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or \
           their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
        
#Wave4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(
            other_vendor, 
            self.inventory[0], 
            other_vendor.inventory[0]
        )
        return True
    
#Wave6
    def get_by_category(self, category):
        inv = self.inventory
        return list(filter(lambda item: item.get_category() == category, inv))
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        return max(items, default=None, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False
        
        self.swap_items(other_vendor, my_best, their_best)
        return True
    
#Bonus
    def swap_by_newest(self, other_vendor):
        if not self.inventory or not  other_vendor.inventory:
            return False
        
        my_newest = min(self.inventory, key=lambda item: item.age)
        their_newest = min(other_vendor.inventory, key=lambda item: item.age)
        self.swap_items(other_vendor, my_newest, their_newest)
        return True