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

    def test_valid_attributes(self):
        """Test valid instantiation of Rectangle."""
        r = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 100)

    def test_invalid_width(self):
        """Test invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 1, 2)

    def test_invalid_height(self):
        """Test invalid height."""
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 1, 2)

    def test_invalid_x(self):
        """Test invalid x."""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 2)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 2)

    def test_invalid_y(self):
        """Test invalid y."""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 1, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -2)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test display method."""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with redirect_stdout(StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(str(r), "[Rectangle] (100) 1/2 - 5/10")

    def test_update(self):
        """Test update method."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_kwargs(self):
        """Test update method with keyword arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(5, 10, 1, 2, 100)
        expected_dict = {'id': 100, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

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

    # Add your test cases for Square class here
