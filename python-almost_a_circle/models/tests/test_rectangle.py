import os
import sys
import unittest
from io import StringIO
from contextlib import redirect_stdout

# Get the absolute path to the models directory
models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the models directory to the Python path
sys.path.append(models_dir)

# Now import necessary classes from models package
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_to_json_string(self):
        """Test to_json_string method."""
        # Explicitly set the id attribute
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect_dict = rect1.to_dictionary()
        self.assertEqual(rect_dict, {'x': 2, 'y': 8, 'width': 10, 'height': 7, 'id': 1})

    def test_to_json_string_empty_list(self):
        """Test to_json_string method with an empty list."""
        json_string = Rectangle.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None."""
        json_string = Rectangle.to_json_string(None)
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_to_json_string(self):
        """Test to_json_string method."""
        square1 = Square(4, 2, 1, 12)
        square_dict = square1.to_dictionary()
        self.assertEqual(square_dict, {'id': 12, 'size': 4, 'x': 2, 'y': 1})

    def test_to_json_string_empty_list(self):
        """Test to_json_string method with an empty list."""
        json_string = Square.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None."""
        json_string = Square.to_json_string(None)
        self.assertEqual(json_string, "[]")

if __name__ == '__main__':
    unittest.main()
