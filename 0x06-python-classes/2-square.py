#!/usr/bin/python3
class Square:
    """
    comments
    """
    def __init__(self, size=0):
        self.size = size #private instance attribute
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

# one = Square("a")
# print(one.size)
two = Square(-2)
print(two.size)