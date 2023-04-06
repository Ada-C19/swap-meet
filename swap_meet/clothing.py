
import uuid 

class Clothing:
    def __init__(self,id = None, fabric = "Unknown"):
        if not id:
            id = int(uuid.uuid4())
            
        self.fabric = fabric

        pass