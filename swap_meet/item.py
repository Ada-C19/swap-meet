import uuid

class Item:
    
    def __init__(self, id= uuid.UUID.time_mid):
        self.id = id
    
    def get_category(self):
        return (f"{self.__class__.__name__}")