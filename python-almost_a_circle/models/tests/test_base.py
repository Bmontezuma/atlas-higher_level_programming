import os
import sys
import unittest
from io import StringIO
from contextlib import redirect_stdout

# Get the root directory of the project
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add the root directory to the Python path
sys.path.append(root_dir)

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_instance_creation(self):
        """Test creation of Base instances."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """Test to_json_string method."""
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = Base.to_json_string([dictionary])
        expected_output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_string, expected_output)

    def test_to_json_string_empty_list(self):
        """Test to_json_string method with empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_rectangle(self):
        """Test to_json_string method with list of Rectangle objects."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_string, expected_output)

    def test_to_json_string_square(self):
        """Test to_json_string method with list of Square objects."""
        s = Square(5, 3, 4)
        dictionary = s.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_output = '[{"id": 1, "size": 5, "x": 3, "y": 4}]'
        self.assertEqual(json_string, expected_output)

if __name__ == '__main__':
    unittest.main()

