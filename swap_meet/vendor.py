
class Vendor:
    
# Wave 01
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
    
        self.inventory.remove(vendor_first_item)
        self.inventory.append(other_vendor_first_item)
        other_vendor.inventory.remove(other_vendor_first_item)
        other_vendor.inventory.append(vendor_first_item)
        return True


    # Wave 05

    # clothing.py
    # def get_category(self):
    #     return "Clothing"
    

    def condition_description(self):
        if self.condition == 5:
            return "Thrift Gem!"
        if self. condition == 4:
            return "Still has the tag"
        if self.condition == 3:
            return "Sustainable"
        if self.condition == 2:
            return "Fair trade"
        if self. condition == 1:
            return "Only a dollar"
        else:
            return "Thrift Bust"


    # decor.py
    # def get_category(self):
    #     return "Decor"
    

    def condition_description(self):
        if self.condition == 5:
            return "Brand spankin new to you!"
        if self. condition == 4:
            return "I can fix that"
        if self.condition == 3:
            return "Faded but it's a look"
        if self.condition == 2:
            return  "Mmm interesting"
        if self. condition == 1:
            return "Might give me health issues"
        else:
            return "Don't do it"


    # electronics.py
    # def get_category(self):
    #     return "Electronics"
    

    def condition_description(self):
        if self.condition == 5:
            return "Great find!"
        if self. condition == 4:
            return "Twas in good care"
        if self.condition == 3:
            return "Morally right"
        if self.condition == 2:
            return "Do it for the turtles"
        if self. condition == 1:
            return "Rethinking thrifting"
        else:
            return "I mean it's free"




