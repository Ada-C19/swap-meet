# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None): 
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.name = "Vendor"
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False 
        
        self.inventory.remove(item)
        return item

    def get_by_id(self, current_id):
        # item_id = Item().id
        for item in self.inventory:
            if current_id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        other_vendor_inventory = other_vendor.inventory
        current_vendor_inventory = self.inventory

        if my_item not in current_vendor_inventory or their_item not in other_vendor_inventory:
            return False
        
        
        my_index = current_vendor_inventory.index(my_item)
        their_index = other_vendor_inventory.index(their_item)

        other_vendor_inventory.append(current_vendor_inventory.pop(my_index))
        current_vendor_inventory.append(other_vendor_inventory.pop(their_index))
        
        # current_vendor_inventory.remove(my_item)
        # other_vendor_inventory.append(my_item)
        # other_vendor_inventory.remove(their_item)
        # current_vendor_inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        current_vendor_inventory = self.inventory
        other_vendor_inventory = other_vendor.inventory

        if len(current_vendor_inventory) ==0  or len(other_vendor_inventory) ==0:
            return False
        
        current_vendor_inventory.append(other_vendor_inventory.pop(0))
        other_vendor_inventory.append(current_vendor_inventory.pop(0))

        return True

    def get_by_category(self, category):
        same_category_list = []

        for item in self.inventory:
            if category == item.get_category():
                same_category_list.append(item)

        return same_category_list
    
    def get_best_by_category(self, category):
        highest_score = 0
        highest_item = ""
        for item in self.inventory:
            if item.condition >= highest_score and category == item.get_category():
                highest_score = item.condition
                highest_item = item

        if not highest_item:
            return None
        
        return highest_item   
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        current_vendor_inventory = self.inventory
        other_vendor_inventory = other_vendor.inventory

        if not current_vendor_inventory or not other_vendor_inventory:
            return False

        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        my_best_index = current_vendor_inventory.index(my_best_item)
        their_best_index = other_vendor_inventory.index(their_best_item)

        other_vendor_inventory.append(current_vendor_inventory.pop(my_best_index))
        current_vendor_inventory.append(other_vendor_inventory.pop(their_best_index))

        return True