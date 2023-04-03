import swap_meet.item as Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None: 
            self.inventory = []
        else: 
            inventory

    # adds single item to inventory and returns item added
    def add(self, item):  
        self.inventory.append(item)
        return item
    
    # removes single item from invetory, returns item removed | if not matching item in inventory, method should return False
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        return False
    
    # returns item with matching id from inventory | if no matching item, then explicitly return None
    def get_by_id(self, id):
        for item_instance in self.inventory: 
            if item_instance.id == id:  
                return item_instance
            else: 
                return None
