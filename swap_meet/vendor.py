


class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.invenory = inventory

    # def add(self, item):
    #     self.inventory.append(item)
    #     return item
    
    # def remove(self,item):
    #     if item in self.inventory:
    #         self.inventory.remove(item)
    #         return item
    #     else:
    #         return False