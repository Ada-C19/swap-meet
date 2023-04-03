import uuid
# returns an UUID object, not an int, but has an int attribute

class Item:
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid1().int
        self.id = id

    def get_category(class_type):
        return class_type.__class__.__name__

# when calling a function from a class use ClassName.FunctionName() 
# don't understand "When calling a function bound to an instance of
#  a class, the first argument passed in to the function is the instance
#  itself. These are known as methods"