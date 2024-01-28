import sys
import unittest
from io import StringIO
from contextlib import redirect_stdout
# Add the parent directory of the models package to the Python path
sys.path.append('../')

# Now import Rectangle
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")

        r.update(y=1, width=2, x=3, id=89)  # Update the ID to 89
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")  # Ensure ID is updated in the string representation

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

if __name__ == '__main__':
    unittest.main()

