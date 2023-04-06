class Vendor:

    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory  = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    

    def get_by_id(self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        #if vendor inventory doesnt contain my item return false
        # if vendor doesnt contain their_item return false
        return True
    
    def swap_first_item(self,other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        # other_vendor.inventory.remove(self.item)
        

        self.inventory.remove(other_vendor.item)
        other_vendor.remove(self.item)

        self.inventory.add(other_vendor.item)
        other_vendor.add(self.item)



        return True