import os
import sys
import unittest
from io import StringIO
from contextlib import redirect_stdout

# Add the parent directory of the models package to the Python path
sys.path.insert(0, '/atlas-higher_level_programming/python-almost_a_circle')

# Now import Square from models.square
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 2)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 2, 4)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 2, 4, 5)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 5, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()

