import uuid
class Item:
    # randomized id and set it to an integer
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id is None else id
    # accessing the class name of self (item)
    def get_category(self):
        return self.__class__.__name__
<<<<<<< HEAD

=======
    
    def __str__(self, item):
        return(f"An object of type {item.get_category()} with id {item.id} ")
    
>>>>>>> ce2419b4b352e77f19e6f3dd23483b9b10fa35f4
