import uuid 

class Vendor:
    def __init__(self, id=None,inventory=[]):
        self.id = uuid.uuid4().int
        self.inventory = inventory #each vendor will have an attribute named :inventory (an empty list)
        
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
        print(item)
        return item 
    
    def remove(self, item): 
        #when this happens: remove takes in one item and removes matching item from inventory
        # for current_item in self.inventory:
        #     if current_item == item:
        #         self.inventory.remove(item)
        #         return item #If no matching item found in inventory it returns False
        #     else:
        #         return False #item that was removed
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        return self.id
    
# vendor = Vendor()
# item = "new item"
# result = vendor.add(item)
# print(result)
# print(vendor.inventory)
# ---------------- WAVE 2 --------------------
#create get_by_id method
#instances of vendor have an instance method named get_by_id
#takes in one argument (int) which reps items id 
#this method returns item with matching id from inventory
#if there is no item with matching id, the method should return None