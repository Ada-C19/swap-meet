from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    #     self.inventory = inventory
    #     word_list = [] if word_list is None else word_list
    # word_list.append(word)
    
    def add(self, item): #this method will add item to the list of self.inventory
        self.inventory.append(item)
        return item
    
    def remove(self, item): #this method will remove the item is present in self.inventory
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id = None): #this method is going to return the item is the id is present in self.inventory
        for item in self.inventory:
            if item.id == id:
                return item 
            # else:
        return None
        
    def swap_items(self, other_vendor,my_item, their_item):
    #other_vender = instance of Vendor() 
    #my_item = instance of Item()
    #their_item = instance of Item() that Vendor() plans to give them
        if self.get_by_id(my_item.id) == None or other_vendor.get_by_id(their_item.id) == None:
            return False #get_by_id is None if the item is not in the inventory
        self.add(their_item) #adding their item to my inventory
        other_vendor.add(my_item) #adding my item in their inventory
        self.remove(my_item) #removing my item from my inventory
        other_vendor.remove(their_item) #removing their item from their inventory
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        self.add(other_vendor.inventory[0])
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])
        return True



