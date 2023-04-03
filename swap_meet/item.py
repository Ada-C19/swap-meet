import uuid


class Item:
    
    def __init__(self, id=None):
        # If user passes in custom id, set id to that number, otherwise generate one
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().int

    def get_category(self):
        """Output: the name of the Class"""
        return self.__class__.__name__




