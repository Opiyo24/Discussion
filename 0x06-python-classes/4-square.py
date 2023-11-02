#!/usr/bin/python3
class Square:
    """
    comments
    """
    def __init__(self, size=0):
        self.__size = size #private instance attribute
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        @property
        def size(self):
            return (self.__size)
        
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    
    def area(self):
        """
        Area ya square
        """
        return(self.__size * self.__size)

one = Square(5)
one.area()