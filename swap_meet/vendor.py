class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
        return False
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            # we do not need to import id bc we're not inheriting anything
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        '''
        other_vendor reps the friend that the vendor(self) is swapping with
        my_item reps the item I am giving away
        their_item reps item other_vendor plans to give
        '''
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        # remove my_item from inv
        self.remove(my_item)
        # add my_item to other_vendor
        other_vendor.add(my_item)
        # remove their_item from the other Vendors inv
        other_vendor.remove(their_item)
        # add their_item to my inv
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor,my_first_item, their_first_item)

        return True
    
    def get_by_category(self, category_type):
        category_objects = []

        for object in self.inventory:
            if object.get_category() == category_type:
                category_objects.append(object)
        return category_objects

    def get_best_by_category(self, category_type):
        best_item = None
        best_condition = -1

        for object in self.inventory:
            if object.get_category() == category_type:
                if best_condition < object.condition:
                    best_condition = object.condition
                    best_item = object
                
        return None if best_item == None else best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        '''
        Best item in my inv matches their_priority is swapped with the best
        item in other_vendor's inv that matches my priority
        Swap does NOT happen if:
        vendor has no item that matches their_priority
        other_vendor has no item that matches my_priority
        '''
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True  
        return False  