# simon? -- or whoever may be grading this project, please disregard
# this commit I am working on the projects over the break to do 
#corrections pls lmk if I should wait until after already graded that
# I can go over them thank you!

class Vendor:
    
# Wave 01
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False


# Wave 02
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None



# Wave 03 
    def swap_items(self, other_vendor, my_item, their_item):
        #
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        
        return False


# Wave 04
    
    def swap_first_item(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False

        vendor_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]

        if not vendor_first_item or not other_vendor_first_item:
            return False
    
        # self.inventory.remove(vendor_first_item)
        # self.inventory.append(other_vendor_first_item)
        # other_vendor.inventory.remove(other_vendor_first_item)
        # other_vendor.inventory.append(vendor_first_item)
        # my attempt to drying code with swap_items
        # test_swap_first_item_returns_true does not pass
        # self.swap_items(vendor_first_item, other_vendor_first_item)
        # passed
        self.swap_items(other_vendor, vendor_first_item, other_vendor_first_item)
        return True


    # Wave 05 -- not passing 1 assert

    # moved conditionals to respective modules, doesn't make a difference
    # but makes vendor.py cleaner
    # trying to get last test to pass, 

    # clothing.py
    # decor.py
    # electronics.py
    

    # Wave 06 -- not passing 4 asserts

    def get_by_category(self, category=""):
        #list of obj in the inventory with that category
        # no items in the inventory that match the category
        # argument the method returns an empty list
        item_in_category = []
        # check vendor inventory by item
        for item in self.inventory:
            #if item in inventory 
            if item.category == category:
                # return item in in a list
                item_in_category.append(item)
        return item_in_category


    # method takes argument category str
    def get_best_by_category(self, category=""):
            
            # if there is no items in inventory return None
            best_item = None
            # look thru inventory for item 
            for item in self.inventory:
                # matching category
                if item.category == category:
                    # if there is no items in inventory return None
                    #it returns a single item even if there are dupes
                    if best_item is None or item.condition > best_item.condition:
                        best_item = item
            # returns this item with highest conditin and matching category
            return best_item
            

    def swap_best_by_category(self,  other_vendor,my_priority,their_priority):
        # my_best_item = self.get_best_by_category(their_priority)
        # their_best_item = self.get_best_by_category(my_priority)
        # think this would be part of a solution to the asserts i am not
        # passing but couldn't get it to work before due date will try later
        # as im trying to swap best item by category
        my_best_item = None
        their_best_item = None
        # check best item in my inventory that matches their_priority category
        for item in self.inventory:
            if item.category == their_priority:
            # If the Vendor has no item that matches their_priority category, it returns False
                if my_best_item is None:
                    my_best_item = item
            #  check best item in other_vendor's inventory that matches my_priority
            for item in other_vendor.inventory:
                if item.category == my_priority:
                # If other_vendor has no item that matches my_priority category, it returns False
                    if their_best_item is None:
                        their_best_item = item

                # if it is in inventory swap items
                if my_best_item is not None and their_best_item is not None:
                    # self.inventory.remove(my_best_item)
                    # other_vendor.inventory.append(my_best_item)
                    # other_vendor.inventory.remove(their_best_item)
                    # self.inventory.append(their_best_item)
                    # my attempt to drying code with swap_items
                    self.swap_items(other_vendor, my_best_item, their_best_item)
                    return True

        return False
