import sys
import unittest
from io import StringIO

# Add the parent directory of the models package to the Python path
sys.path.append('../')

# Now import Rectangle
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###"
        with StringIO() as out:
            r.display()
            captured_output = out.getvalue().strip()  # Capture the output
            self.assertEqual(captured_output, expected_output)

    def test_update(self):
        r = Rectangle(10, 12, 0, 0)
        r.update(1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 10/12")

if __name__ == '__main__':
    unittest.main()
