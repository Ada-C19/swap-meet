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
        list_by_category = []
        for element in self.inventory:
            if category == element.get_category():
                list_by_category.append(element)

        return list_by_category