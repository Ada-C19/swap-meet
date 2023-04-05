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
    
    def get_by_id(self, id):
        try:
            for item in self.inventory:
                if item.id == id:
                    return item
        except ValueError as err:
            print(f"Error message: {err}")
            print(f"Could not retrieve item {id} from inventory.")
            return None
        
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or
                their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        # Check if either inventory is empty
        if not self.inventory or not other_vendor.inventory:
            return False
        
        # Swap first item of each vendor's inventory
        self.swap_items(other_vendor,
                        self.inventory[0],
                        other_vendor.inventory[0])
        
        return True
    
    def get_by_category(self, category):
        return [item for item in self.inventory if 
                item.get_category() == category]
    
    def get_best_by_category(self, category):
        inventory_of_category = self.get_by_category(category)

        if not inventory_of_category:
            return None

        best_item = None
        for item in inventory_of_category:
            if not best_item or item.condition > best_item.condition:
                best_item = item
        
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False
        
        self.swap_items(other_vendor, my_best, their_best)
        return True