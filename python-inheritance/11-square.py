# 11-square.py
from rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new instance of the Square class."""
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.width ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.width}/{self.height}"
