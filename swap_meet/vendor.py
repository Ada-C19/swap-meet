class Vendor():
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    # create instance method called add- takes in one item
    # add item to inventory list, return item

    def add(self, item):
        self.inventory.append(item)
        return item

    # create instance method called remove- takes in one item
    # removes matching item from inventory, return item
    # if no matching item in inventory, return False

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    # create instance method called get_by_id
    # takes one argument: an integer that represents an Item's id
    # return the the item with matching id from inventory
    # if no matching item in inventory, return None

    def get_by_id(self, id):
        
        for item in self.inventory:
            if id == item.id:
                return item
    
        return None
    
    # create instance method called swap_items- takes 3 arguments: other_vendor, my_item, their_item 
    # return False if either inventory doesn't contain my_item or their_item

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

    # we can use the add and remove instance methods we created above for this function
    # remove item from our inventory and add item to their inventory
    # remove item from their inveory and add to our inventory.
    # return True

        self.remove(my_item)
        other_vendor.add(my_item)
        
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    # create instance method called swap_first_item- takes one argument: other_vendor

    def swap_first_item(self, other_vendor):

        # if either inventory is empty, return False
        if not self.inventory or not other_vendor.inventory:
            return False
        
        # remove first item in our inventory and add to their inventory
        # remove first item in their inventory and add to our inventory
        # return True

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)
    
    # create method called get_by_category- takes in one argument: category (a string ex: 'Clothing')

    def get_by_category(self, category):

        # create empty list to place matching items

        items_in_category = []

        # iterate through each item in list

        for item in self.inventory:
            
            # if category of that item matches category argument, add that item to the empty list

            if category == item.get_category():
                items_in_category.append(item)

        # return the list 'items_in_category'
        # if no items match the category, return empty list

        return items_in_category
    
    # create instance method called get_best_by_category- takes in one argument: category (a string ex: 'Clothing')

    def get_best_by_category(self, category):

        # create variable to hold item with highest condition in matching category, assign as None
        # initialize highest_condition variable at 0- will use to keep track of highest condition value
        # create variable called list_items_in_category and use get_by_category method to create list of items that are of the same category

        best_item = None
        highest_condition = 0
        list_items_in_cat = self.get_by_category(category)

        # if no items of that category in list- return None

        if list_items_in_cat == []:
            return None
        
        # iterate through each item in list

        for item in list_items_in_cat:

            # if the condition associated with that item is higher than highest_condition variable, we want to reassign the highest_condition variable and best_item variable with that condition and item

            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item
    
    # create instance method called swap_best_by_category- takes 3 arguments: other_vendor, my_priority, their_priority
    # other_vendor: who we want to trade with
    # my_priority: category of item we want to receive
    # their_priority: category of item they want to receive

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        # we can use get_best_by_category method to assign my_item that we're trading, as our best item in the category they want to receive
        # we can use get_best_by_category method to assign their_item they're trading as their best item in the category we want to receive
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        # we can use swap_items method to remove the best item from each of our inventories
        # we can use swap_items method to add the best item to each of our inventories
        # swap_items method will return True

        return self.swap_items(other_vendor, my_item, their_item)
    
        # swap_items method will return False if there are no matching items

        # ****** original code below: ******
    
        # if my_item ==  None:
        #     return False
        # elif their_item ==  None:
        #     return False
        # else:
        #     self.inventory.remove(my_item)
        #     other_vendor.inventory.append(my_item)
        #     other_vendor.inventory.remove(their_item)
        #     self.inventory.append(their_item)
        #     return True
  