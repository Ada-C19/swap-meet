class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        if item:
            self.inventory.append(item)
        
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            print(f"Error message: {err}")
            print(f"Unable to remove '{item}' from inventory.")
            return False