from swap_meet.item import Item 
class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
        
    def add(self, item):
        self.inventory.append(item)
        if item in self.inventory:
            return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        if item not in self.inventory:
            return item
    
    def get_by_id(self, search_id):
        for item in self.inventory:
            if item.id == search_id:
                return item
        return None   
    
    def swap_items(self, other_vendor, my_item, their_item):
        their_inventory = other_vendor.inventory
        if not (my_item in self.inventory and their_item in their_inventory):
            return False   
        their_inventory.append(my_item)
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        their_inventory.remove(their_item)
        return True 
        
    def swap_first_item(self, other_vendor):
        thier_inventory = other_vendor.inventory
        if not (self.inventory and thier_inventory):
            return False 
        instance_first_item = self.inventory[0]
        other_vendor_first_item = thier_inventory[0]
        
        self.inventory[0] = other_vendor_first_item
        thier_inventory[0] = instance_first_item       
        return True 
    
    def get_by_category(self, category):
        inventory_by_category = []
        for element in self.inventory:
            if category == element.get_category():
                inventory_by_category.append(element)
        return inventory_by_category
    
    def get_best_by_category(self, category):
        inventory_by_category = self.get_by_category(category)
        if not inventory_by_category:
            return None 
        highest_condition = 0.0
        item_best_condition = None
        for element in inventory_by_category:
            if element.condition > highest_condition:
                highest_condition = element.condition
                item_best_condition = element 
        return item_best_condition   
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not (self.get_by_category(their_priority) and other_vendor.get_by_category(my_priority)):
            return False 
        
        vendor_best_item = self.get_best_by_category(their_priority)
        other_vendor_best_item = other_vendor.get_best_by_category(my_priority)

        self.swap_items(other_vendor, vendor_best_item, other_vendor_best_item)
        return True 