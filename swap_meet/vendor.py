class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, added_item):
        self.added_item = added_item
        (self.inventory).append(added_item)
        return added_item
    
    def remove(self,item_removed):
        self.item_removed = item_removed
        if item_removed not in self.inventory:
            return False
        else:
            for item in self.inventory:
                if item_removed == item:
                    (self.inventory).remove(item)
                    return item_removed
