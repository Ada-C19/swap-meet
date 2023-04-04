class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        if item in self.inventory:
            return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        if item not in self.inventory:
            return item
    
    def get_by_id(self, search_id):
        for item in self.inventory:
            if item.id == search_id:
                return item
        return None   
