from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=[]):
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