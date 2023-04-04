class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, object_id):
        for item in self.inventory:
            if item.id == object_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or\
        their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)    
        return True
            
    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        
        self.swap_items(other_vendor, self.inventory[0], \
        other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items
    
    def get_best_by_category(self, category):
        best_item = None
        best_item_rating = 0
        
        for item in self.inventory:
            if item.condition >= best_item_rating and \
            item.get_category() == category:
                best_item = item
                best_item_rating = item.condition
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_from_me = self.get_best_by_category(their_priority)
        item_from_them = other_vendor.get_best_by_category(my_priority)

        if item_from_me and item_from_them:
            self.swap_items(other_vendor, item_from_me, item_from_them)
            return True
        else:
            return False

        

