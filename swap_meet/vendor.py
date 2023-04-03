class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            removed_item = item
            self.inventory.remove(item)
            return removed_item
        else:
            return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item_id == item.id:
                return item