
class Vendor:

    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory  = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    

    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        #if vendor inventory doesnt contain my item return false
        # if vendor doesnt contain their_item return false
        return True
    
    def swap_first_item(self,other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        other_vendor.add(self.inventory[0])

        self.add(other_vendor.inventory[0])

        self.remove(self.inventory[0])

        other_vendor.remove(other_vendor.inventory[0])

        return True
    
    def get_by_category(self,category):

        self.category = category
        
        objects = []

        for stuff in self.inventory:
            if stuff.get_category() == category:
                objects.append(stuff)

        return objects
    
    def get_best_by_category(self, category_condition):

        self.category_condition = category_condition

        best_condition = 0

        for stuff in self.inventory(category_condition):
            if stuff.condition_description() < best_condition:
                best_condition = category_condition
                return

            return 




