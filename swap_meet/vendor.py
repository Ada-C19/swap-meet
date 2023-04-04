class Vendor:
    def __init__(self, inventory=None):
        # If inventory is not None, whatever 'inventory' is passed in will be assigned to self.inventory
        # if inv IS None, then [] will be assigned to self.inventory
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
            # python doesnt know .id exists but it is still going to try it
            # we do not need to import bc we're not inheriting anything
            if item.id == item_id:
                return item
        return None