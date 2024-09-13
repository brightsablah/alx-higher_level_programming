#!/usr/bin/python3
"""New Module contains Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        #details to be setup later. tomorrow
        print() # just to stop indent problem for next function

    
    def area(self):
        area = self.size*self.size
        return area

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
