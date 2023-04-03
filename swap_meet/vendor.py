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
    
    def add(self, item):
        self.inventory.append(item)
        return  item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id = None):
        for item in self.inventory:
            if item.id == id:
                return item 
            # else:
        return None
    #this is iterating through the instances of item
        
    def swap_items(other_vendor,my_item, their_item):
        print(f"An object of type Item with id")
    #other_vender = instance of Vendor() 
    #my_item = instance of Item()
    #their_item = instance of Item() that Vendor() plans to give them


    #removes my_item from Vendor inventory and add it to their friend's inventory Return TRUE
    #removes thier_item from other vendor's inventory and adds it to the vendor's inventory return TRUE
    #if vendor inventory doesn't contain my_item or friend's inventory doesn't contain their_item then return False
