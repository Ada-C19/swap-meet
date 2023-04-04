""" Initiation of class Electronics """
from .item import Item

class Electronics(Item):
    """ Represents electronic items. """
    def __init__(self, type="Unknown", id=None, condition=0.0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."



#  `Electronics`
#   - Has an attribute `id` that is by default a unique integer
#   - Has an attribute `type` that is by default the string "Unknown"
#     - This attribute describes what kind of electronic device this is. Some example values might be `“Kitchen Appliance”`, `“Game Console”`, or `“Health Tracker”`
#     - When we initialize an instance of `Electronics`, we can optionally pass in a string with the keyword argument `type`
#   - Has an function `get_category` that returns `"Electronics"`
#   - Has a stringify method that returns `"An object of type Electronics with id <id value>. This is a <type value> device."`
#     - For example, if we had an `Electronics` instance with an `id` of `123435` and `type` attribute of `"Mobile Phone"`, its stringify method should return 
# `"An object of type Electronics with id 12345. This is a Mobile Phone device."`