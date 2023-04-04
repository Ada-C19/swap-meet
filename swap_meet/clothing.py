from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric=None, condition=0.0):
        super().__init__(id, condition)

        if not fabric:
                fabric = "Unknown"
        self.fabric = fabric
    
    def __str__(self):
        return (super().__str__() + ' It is made from ' + 
                str(self.fabric) + ' fabric.')
    
# clothing = Clothing(id=12345)
# print(clothing.id)
# str_clothing_id = str(clothing.id)
# print(len(str_clothing_id))
