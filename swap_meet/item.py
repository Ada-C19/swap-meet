# ######################## WAVE 2 #############################
import uuid

# # uuid4() creates a random UUID
# test = uuid.uuid4()
# print(uuid.uuid4, test.int())
# # do I need this???????
# # from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int
        self.id = id

    # def __init__(self, id=uuid.uuid4().int):
    #     self.id = id

        # if len(id) >= 32:
            


        # self.id.int()


# each item has this function
    def get_category(self, name=""):

        name = Item("name")

        return type(name).__name__

        # return name


        # if name == Item():
        #     return None
        # name = Item()
        # return name

        # name = Item("")

        # if name == self.item:

        # return name
        # item = Item.__name__

        # self.name = name
        # return Item.self.name 
    


        # if len(id) >= 32:
        #     return 


    # this was moved to vendor.py
    # def get_by_id(self, id):
    #     if id in self.inventory:
    #         return self.item
    #     else:
    #         return None