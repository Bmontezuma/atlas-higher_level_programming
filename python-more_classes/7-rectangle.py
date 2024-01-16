#!/usr/bin/python3
"""
Module for the Rectangle class
"""


class Rectangle:
    """
    Rectangle class

    Usage:
    >>> r1 = Rectangle(8, 4)
    >>> print(r1)
    ########
    ########
    ########
    ########
    >>> r1.print_symbol = "&"
    >>> print(r1)
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    >>> r2 = Rectangle(2, 1)
    >>> print(r2)
    ##
    >>> Rectangle.print_symbol = "C"
    >>> print(r2)
    CC
    >>> r3 = Rectangle(7, 3)
    >>> print(r3)
    CCCCCCC
    CCCCCCC
    CCCCCCC
    >>> r3.print_symbol = ["C", "is", "fun!"]
    >>> print(r3)
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    >>> del r1
    Bye rectangle...
    >>> del r2
    Bye rectangle...
    >>> del r3
    Bye rectangle...
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance

        Args:
            width (int): Width of the rectangle (default is 0)
            height (int): Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for width

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): Value to set as width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): Value to set as height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: String representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for eval()

        Returns:
            str: String representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

