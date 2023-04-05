# ######################## WAVE 2 #############################
import uuid

# # uuid4() creates a random UUID
# test = uuid.uuid4()
# print(uuid.uuid4, test.int())
# # do I need this???????
# # from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, id=uuid.uuid4()):
        self.id = id

        # self.id.int()


    # each item has this function
    def get_category(self, name=""):
        self.name = name
        return Item.self.name 
        # return Item.name


    # this was moved to vendor.py
    # def get_by_id(self, id):
    #     if id in self.inventory:
    #         return self.item
    #     else:
    #         return None