from swap_meet.item import Item

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
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        
    def swap_first_item(self,other_vendor):
        if  not self.inventory or not other_vendor.inventory:
            return False
        inventory_first = self.inventory[0]
        friends_first = other_vendor.inventory[0]

        Vendor.remove(self, inventory_first)
        Vendor.remove(other_vendor, friends_first)
        Vendor.add(self,friends_first)
        Vendor.add(other_vendor, inventory_first)
        return True
    def get_by_category(self,category):
        objects_in_inventory = []

        for i in self.inventory:
            if Item.get_category(i) == category:
                objects_in_inventory.append(i)
        
        return objects_in_inventory
    
    def get_best_by_category(self, category):
        objects_in_inventory = Vendor.get_by_category(self, category)
        
        if not objects_in_inventory:
            return None
        else:
            
            for i in objects_in_inventory:
                max_i = max(i.condition for i in objects_in_inventory)
                if i.condition == max_i:
                    return i
                else:
                    continue
    

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_item = Vendor.get_best_by_category(other_vendor, my_priority)
        their_item = Vendor.get_best_by_category(self, their_priority)
        if other_vendor == [] or self.inventory == [] or my_priority == their_priority or not my_item or not their_item:
                return False
        if self.inventory[0] == my_item and other_vendor.inventory[0] == their_item:
            Vendor.swap_first_item(self, other_vendor)
        else:
            Vendor.remove(self, their_item)
            Vendor.remove(other_vendor, my_item)

            Vendor.add(self,my_item)
            Vendor.add(other_vendor, their_item)

        return True
    