import sys
import os
import unittest

# Add the parent directory of the models package to the Python path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(root_dir)

# Now import Base and Rectangle from the models package
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id(self):
        """Test id initialization."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_to_json_string(self):
        """Test to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8, 1)  # Explicitly set ID to 1
        r2 = Rectangle(2, 4, 0, 0, 2)    # Explicitly set ID to 2
        actual_json = Base.to_json_string(sorted([r1.to_dictionary(), r2.to_dictionary()], key=lambda x: x['id']))
        expected_json = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},' + \
                        ' {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
        self.assertEqual(actual_json, expected_json)

    def test_from_json_string(self):
        """Test from_json_string method."""
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()

