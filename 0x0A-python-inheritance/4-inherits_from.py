#!/usr/bin/python3
"""checks if object is an instance of a class
or an inherited class
"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits from
    """
    current_class = obj.__class__
    while current_class is not None:
        if current_class == a_class:
            return True
        current_class = current_class.__bases__[0] 
        if current_class.__bases__ else None
    return False
