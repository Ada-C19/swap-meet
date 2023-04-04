import uuid

class Item:
    def __init__(self, id = None):
        if not id:
            id = uuid.uuid4().int
        self.id = id

    def get_category(self):
        if isinstance(self, Item):
            item_type = "Item"
        # elif isinstance(self, Clothing):
        #     item_type = "Clothing" 
        # elif isinstance(item, Electronics):
        #     item_type = "Electronics"        
        # elif isinstance(self, Decor):
        #     item_type = "Decor"      
        return item_type
    
    def __str__(self):
        statement = f"An object of type Item with id " + str(self.id) + "."
        print(statement)
        return statement