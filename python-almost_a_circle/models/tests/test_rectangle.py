import sys
import unittest
sys.path.append('..')

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 2)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 2")
        s.update(10, 2, 4)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 2")
        s.update(10, 2, 4, 5)
        self.assertEqual(str(s), "[Square] (10) 5/3 - 2")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 5, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()

