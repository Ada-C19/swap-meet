class Vendor:
    def __init__(self):
        self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        try:
            self.inventory.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.inventory.append(their_item)
            return True
        except ValueError:
            return False
        