import uuid

class Item:
    def __init__(self):
        # self.id = uuid.int_()
        # self.id = uuid.uuid1().int
        self.id = uuid.uuid4().int
        print(f"{self.id = }")
        print(f"{type(self.id) = }")



test_item = Item()
print(f"{test_item.id = }")
test_item1 = Item()
print(f"{test_item1.id = }")
test_item2 = Item()
print(f"{test_item2.id = }")
test_item3 = Item()
print(f"{test_item3.id = }")

### Wave 2

# class Item:
# def __init__ (self, id): we can optionally pass in an integer with the keyword argument `id` to manually set the `Item`'s `id`
# self.id = int (unique)

# def get_category(self):
# return class name in a string

# import the [`uuid` package](https://docs.python.org/3/library/uuid.html) in `item.py` to create large ***unique*** numbers 
# `UUID` objects have [an attribute `int`](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) which allow us to access their value as an integer

