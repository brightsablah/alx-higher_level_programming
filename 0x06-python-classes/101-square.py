#!/usr/bin/python3
"""New Module contains Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        area = self.size * self.size
        return area

    def my_print(self):
        if self.size == 0:
            print()
            return

        # vertical padding (position[1])
        for i in range(self.position[1]):
            print()

        # square with hosrizontal padding (position[0])
        for j in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    # print same thing as my_print
    def __str__(self):
        if self.size == 0:
            print()
            return

        # vertical padding (position[1])
        for i in range(self.position[1]):
            print()

        # square with hosrizontal padding (position[0])
        for j in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)