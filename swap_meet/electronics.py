import uuid
    
class Electronics:

    def __init__(self, id=None, type="Unknown"):
        self.id = id if id is not None else int(uuid.uuid4())
        self.type = type
    



    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."