class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        return item
    
    def remove_item(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory or their_item in other_vendor:
            item_for_friend = self.remove_item(my_item)
            other_vendor.add_item(item_for_friend)
            
            item_for_me = other_vendor.remove_item(their_item)
            self.add_item(item_for_me)
            return True
        
        else:
            return False
