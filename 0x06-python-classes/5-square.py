#!/usr/bin/python3
class Square:
    """
    comments
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        @property
        def size(self):
            """Comments
            """
            return (self.__size)
        
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must bve >= o")
            self.__size = value
            
    def area(self):
        """
        comments
        """
        return (self.__size * self.__size)
    
    def my_print(self):
        """
        comments
        """
        for i in range(0, self.__size):
            # print("#")
            for i in range(0, self.__size):
                print("#", end="")
            print()


one = Square(7)
one.my_print()

        