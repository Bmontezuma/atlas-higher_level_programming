#!/usr/bin/python3
"""My Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """My Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
