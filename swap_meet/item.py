import uuid

class Item:
    def __init__(self, id=None):
    
        # if id is not manually assigned
        if id is None:
            self.id = uuid.uuid4().int
        #if id is manually assigned
        else:
            self.id = id
        
    def get_category(self):
        return self.__class__.__name__
        
        

    # def swap_meets(self, other_vendor, my_item, their_item):
    #     if not self.inventory(my_item) or not self.inventory(their_item): 
    #         return False
    #     else:
    #         self.inventory.add(their_item)
    #         self.inventory.remove(my_item)
    #         #self.inventory.append(their_item)
    #         return True 
    # # these functions will return uuid objects **(not int)**  
