from swap_meet.item import Item
class Clothing(Item):
	def __init__(self, id, fabric=“Unknown”):
		super().__init__(id)
        self.fabric = fabric if fabric is fabric else "Unknown"
	
    def get_category(self):