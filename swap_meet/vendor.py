class Vendor:
    def __init__(self, id, inventory, add_item, remove_item):
        self.id = id
        self.inventory = []
        self.add_item = add_item
        self.remove_item = remove_item
    def add_item():
        return #item that was added
    
    def remove_item(): 
        return #item that was removed
    




    
    
#each vendor will have an attribute named :inventory (an empty list)
#when we instantiate the instance of vendor, we can pass in a list with the argument inventory
#every instance of vendor has an instance menthod .add()
#.add() take is 1 item and adds it to inventory
#returns the item that was added
# every instance of vendor has a instance method .remove()
# .remove() takes in one item and removes matching item from inventory
#returns the item that was removed
#If no matching item found in inventory it returns False

# ---------------- WAVE 2 --------------------
#create get_by_id method
#instances of vendor have an instance method named get_by_id
#takes in one argument (int) which reps items id 
#this method returns item with matching id from inventory
#if there is no item with matching id, the method should return None