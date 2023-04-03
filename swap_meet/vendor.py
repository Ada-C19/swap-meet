class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        if item:
            self.inventory.append(item.lower())
        
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item.lower())
            return item
        except ValueError as err:
            print(f"Unable to remove '{item}' from inventory.")
            return False