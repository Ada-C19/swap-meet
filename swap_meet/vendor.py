#   In Wave 1 we will create the Vendor class.
class Vendor:
    

    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        # This method returns the item that was added
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            # This method returns the item that was removed
            return item
        else:

            return False


#Instances of Vendor have an instance method named get_by_id
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None


        


















