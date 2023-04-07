class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_by_category(self, category):
        category_list = []

        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list

    def get_best_by_category(self, category):
        if len(self.get_by_category(category)) == 0:
            return None

        best_item, best_condition = "", 0
        for item in self.get_by_category(category):
            if item.condition >= best_condition:
                best_item, best_condition = item, item.condition

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if (
            len(self.get_by_category(their_priority)) == 0
            or len(other_vendor.get_by_category(my_priority)) == 0
        ):
            return False

        my_swap_item = self.get_best_by_category(their_priority)
        other_swap_item = other_vendor.get_best_by_category(my_priority)

        self.swap_items(other_vendor, my_swap_item, other_swap_item)
        return True

    def swap_by_newest(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_newest, my_age = self.inventory[0], self.inventory[0].age
        their_newest, their_age = (
            other_vendor.inventory[0],
            other_vendor.inventory[0].age,
        )

        for item in self.inventory:
            if item.age <= my_age:
                my_newest, my_age = item, item.age

        for item in other_vendor.inventory:
            if item.age <= their_age:
                their_newest, their_age = item, item.age

        self.swap_items(other_vendor, my_newest, their_newest)
        return True
