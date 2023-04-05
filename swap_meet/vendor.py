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
    
    #WaveZ
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or 
            their_item not in other_vendor.inventory):
                return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    #Wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.remove(my_first_item)
        other_vendor.add(my_first_item)
        
        other_vendor.remove(their_first_item)
        self.add(their_first_item)
        
        return True
    
    #Wave 6

    def get_best_by_category(self, category):
        items_with_category = self.get_by_category(category)
        if len(items_with_category) == 0:
            return None
        best_item = max(items_with_category, key=lambda x: x.condition)
        return best_item