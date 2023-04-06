class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
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
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(other_vendor.remove(their_item))
            other_vendor.add(self.remove(my_item))
            return True
        else:
            return False        
  
    def swap_first_item(self, other_vendor):
            if not self.inventory or not other_vendor.inventory:
                return False
        
            first_item = self.inventory[0]
            friends_first_item = other_vendor.inventory[0]

            other_vendor.inventory.append(first_item)
            self.inventory.append(friends_first_item)
            other_vendor.inventory.remove(friends_first_item)
            self.inventory.remove(first_item)
            return True
            
    def get_by_category(self, category):
        objects_in_inventory = []

        for item in self.inventory:
            if item.get_category() == category:
                objects_in_inventory.append(item)
        return objects_in_inventory
    
    def get_best_by_category(self, category):
        highest_condition = 0
        item_w_highest_condition = None
        
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    item_w_highest_condition = item
        return item_w_highest_condition

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_best = other_vendor.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not their_best or not my_best:
            return False
        
        other_vendor.inventory.append(my_best)
        self.inventory.append(their_best)
        other_vendor.inventory.remove(their_best)
        self.inventory.remove(my_best)
        return True


            


        
        


