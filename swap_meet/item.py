import uuid

class Item:

    # create attribute called 'id': unique integer by default
    # generate numbers with a package called uuid
    # use one of their functions to create large unique numbers meant to be used as identifiers
    # package returns uuid objects not integers but they do have an attribute int that we can assess the value as an integer
    # when initializing an instance of Item, pass in an integer with the keyword argument id to mannually set the items id.

    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid4().int
        self.id = id

    # each Item has a function called get_category: returns string holding name of class.

    def get_category(self):   
        return __class__.__name__
    
    # write method to stringify (convert to string) an Item using str() 
    # write method called swap items

    def __str__(self):
        return f'An object of type Item with id {self.id}.'
    
  



# When we stringify an instance of Item using str(), it returns "An object of type Item with id <id value>.", where <id value> is the id of the Item instance that str() was called on.
# For example, if we had an Item instance item_a = Item(id=12345), the output of str(item_a) should be "An object of type Item with id 12345.".
# To accomplish this, you'll want to investigate what calling str() on a class instance does and how you can override such a method. This type of overriding is known as "operator overloading", put simply, it means that the same method exhibits different behavior across instances of different classes. A simple example would be something like + which for strings means "concatenate" but for numbers, means "add", or for lists, means "combine".