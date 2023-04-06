class Vendor():
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item):        
        inventory = self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        inventory = self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        other_vendor.inventory
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.remove(their_item)
        self.inventory.append(their_item)
        return True
    
    def swap_first_item(self, other_vendor):
        my_first = ""
        their_first = "" 
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            my_first = self.inventory.pop(0)
            other_vendor.inventory.append(my_first)

            their_first = other_vendor.inventory.pop(0)
            self.inventory.append(their_first)                   
        return True
    
    def get_by_category(self, category):
        inventory_by_category = []
        for item in self.inventory:
            if item.get_category() == category: 
                inventory_by_category.append(item)
        return inventory_by_category

    def get_best_by_category(self, category):
        inventory_by_category = self.get_by_category(category)

        if not inventory_by_category:
            return None
        highest_condition = 0
        matching_category = inventory_by_category[0]
        for item in inventory_by_category:
            if item.condition > highest_condition:
                highest_condition = item.condition
                matching_category = item
        return matching_category
        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        other_vendor_priority = other_vendor.get_best_by_category(my_priority)
        my_item_priority = self.get_best_by_category(their_priority)
        return self.swap_items(other_vendor, my_item_priority, other_vendor_priority)