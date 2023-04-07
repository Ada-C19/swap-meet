from .item import Item

class Electronics(Item):
   def __init__(self, id=0, type = "Unknown", category="Electronics",condition=0):
       super().__init__(id, category, condition)
       self.type = type
      


   def __str__(self):
       item_descript = super().__str__()
       electronics_description = f'This is a {self.type} device.'
       return f"{item_descript} {electronics_description}"
