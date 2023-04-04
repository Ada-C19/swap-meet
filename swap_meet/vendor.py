#from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
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
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        items_of_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_of_category.append(item)
        return items_of_category   

    def get_best_by_category(self, category):
        items_of_category = self.get_by_category(category)
        if not items_of_category:
            return None
        best_condition = items_of_category[0].condition
        best_item = None
        for item in items_of_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        # if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
        #     return False
        their_best = other_vendor.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        self.swap_items(other_vendor, my_best, their_best)

        return True