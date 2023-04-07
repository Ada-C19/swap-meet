from swap_meet import item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            return item
        else:
            return False
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False 
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
            
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else: 
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True

    def get_by_category(self, category):
        self.category = category

        list_of_items_in_category = []

        for item in self.inventory:
            if category == item.get_category():
                list_of_items_in_category.append(item)
        return list_of_items_in_category
            

    def get_best_by_category(self, category):
        self.category = category

        best_condition = 0.0
        best_item = None
        for item in self.inventory:
            if category == item.get_category():
                if item.condition >= best_condition:
                    best_item = item
                    best_condition = item.condition
        return best_item


        
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
    
        if self.get_best_by_category(their_priority) == None:
            return False 
        
        if other_vendor.get_best_by_category(my_priority) == None:
            return False

        for_them = self.get_best_by_category(their_priority)
        other_vendor.inventory.append(for_them)
        self.inventory.remove(for_them)
        for_me = other_vendor.get_best_by_category(my_priority) 
        self.inventory.append(for_me)
        other_vendor.inventory.remove(for_me)
        return True
            
