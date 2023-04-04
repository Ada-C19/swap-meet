from swap_meet.item import Item
class Clothing(Item):
	def __init__(self, id, fabric=None):
		self.fabric = "Unknown" if fabric is None else fabric
		super().__init__(id)
        
	def get_category(self):
		return self.item.get_category(self)
        
	def __str__(self):
		return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
	