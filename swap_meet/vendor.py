from swap_meet.item import Item 
"""
Module that contains class Vendor with attribute inventory and instance methods: add, remove.
Other instance methods:
To get items in inventory by Item object attribute: get_by_id, get_by_category, get_best_by_category, get_newest_by_category 
To swap items by attribute: swap_best_by_category, , swap_newest_by_category. 
"""
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
        if not (my_item in self.inventory and their_item in other_vendor.inventory):
            return False   
        #Add their item to my inventory, add my item to their inventory 
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        #Remove their item from their inventory, remove my item from my inventory
        self.inventory.remove(my_item)   
        other_vendor.inventory.remove(their_item)
        return True 
        
    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False 
        my_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_first_item, other_vendor_first_item)       
        return True 
    
    def get_by_category(self, category):
        inventory_by_category = [item for item in self.inventory if category == item.get_category()]
        return inventory_by_category
    
    #Returns item with highest value for condition attribute. 
    def get_best_by_category(self, category):
        inventory_by_category = self.get_by_category(category)
        if not inventory_by_category:
            return None 
        item_best_condition = max(inventory_by_category, key=lambda item: item.condition)
        return item_best_condition   
    
    #Returns true if item with highest value for condition is swapped between vendors.
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not (self.get_by_category(their_priority) and other_vendor.get_by_category(my_priority)):
            return False 
        
        vendor_best_item = self.get_best_by_category(their_priority)
        other_vendor_best_item = other_vendor.get_best_by_category(my_priority)
        self.swap_items(other_vendor, vendor_best_item, other_vendor.get_best_by_category(my_priority))
        return True 
    
    def get_newest_by_category(self, category):
        inventory_by_category = self.get_by_category(category)
        if not inventory_by_category:
            return None 
        item_newest = min(inventory_by_category, key=lambda item: item.age)
        return item_newest
    
    def swap_newest_by_category(self, other_vendor, my_priority, their_priority):
        if not (self.get_by_category(their_priority) and other_vendor.get_by_category(my_priority)):
            return False 
        
        vendor_newest_item = self.get_newest_by_category(their_priority)
        other_vendor_newest_item = other_vendor.get_newest_by_category(my_priority)
        self.swap_items(other_vendor, vendor_newest_item, other_vendor_newest_item)
        return True 
    
    #This is a possible higher order function to combine swap by age or condition and category.
    #It is commented out to not change test_wave_06
    #
    # def swap_modifier_by_category(self, other_vendor, my_priority, their_priority, swap_modifier):
    #     if not (self.get_by_category(their_priority) and other_vendor.get_by_category(my_priority)):
    #         return False 
    #     vendor_item = swap_modifier(self, their_priority)
    #     other_vendor_item = swap_modifier(other_vendor, my_priority)
    #     self.swap_items(other_vendor, vendor_item, other_vendor_item)
    #     return True