from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        # if this item in in inventory with matchind ID. return the item
        for item in self.inventory:
            if id == item.id:
                return item
        return None