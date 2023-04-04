from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=None):
        if not inventory:
            inventory=[]
        self.inventory=inventory

    def add(self,new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, old_item):
        if old_item in self.inventory:
            self.inventory.remove(old_item)
            return old_item
        else: 
            return False
    
    def get_by_id(self,items_id):
        for item in self.inventory:
            if items_id == item.id: 
                return item
        return  
    
    def swap_items(self,other_vendor,my_item,others_item):

        if my_item in self.inventory and others_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.remove(others_item)
            self.inventory.append(others_item)
            other_vendor.inventory.append(my_item)
            return True 
        return False
    
    def swap_first_item(self,other_vendor):
        if len(self.inventory) and len (other_vendor.inventory):
            my_item=self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.inventory[0]=their_item
            other_vendor.inventory[0]=my_item
            return True 
        
        return False 