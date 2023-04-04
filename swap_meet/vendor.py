from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


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
            if item.id == item_id:
                return item
        return None
      
    def swap_items(self, other_vendor, my_item, their_item):

        # verify each item is in their corresponding inventory
        # else return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # remove my_item from our own inventory and add to the other vendor's inventory
        self.remove(my_item)
        other_vendor.add(my_item)

        # remove their_item from other vendor's inventory and add to ours
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.get_category() == category]
        return items
    
    def get_best_by_category(self, category):
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if best_item == None or item.condition > best_item.condition:
                    best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):     
        my_best_item = self.get_best_by_category(their_priority) 
        their_best_item = other_vendor.get_best_by_category(my_priority) 
    
        if my_best_item == None or their_best_item == None:
            return False
        return self.swap_items(other_vendor, my_best_item, their_best_item)
    
    def get_newest_item(self):
        if not self.inventory:
            return False
        
        newest_item_age = self.inventory[0].age
        newest_item = None
        
        for item in self.inventory:
            if item.age < newest_item_age:
                newest_item_age = item.age
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor):
        if not (self.inventory and other_vendor.inventory):
            return False
        
        their_newest_item = other_vendor.get_newest_item()
        my_newest_item = self.get_newest_item()

        return self.swap_items(other_vendor, my_newest_item, their_newest_item)

