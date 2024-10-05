#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_init(self):
        """Test initialization"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)

    def test_validation(self):
        """Test attribute validation"""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(TypeError):
            Square(5, "2")
        with self.assertRaises(ValueError):
            Square(5, -2)
        with self.assertRaises(TypeError):
            Square(5, 2, "3")
        with self.assertRaises(ValueError):
            Square(5, 2, -3)

    def test_area(self):
        """Test area method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.area(), 9)

    def test_display(self):
        """Test display method"""
        s1 = Square(2)
        s1.display()
        self.assertEqual(self.captured_output.getvalue(), "##\n##\n")
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

        s2 = Square(2, 2, 2)
        s2.display()
        self.assertEqual(self.captured_output.getvalue(), "\n\n  ##\n  ##\n")

    def test_str(self):
        """Test __str__ method"""
        s1 = Square(5, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 5")
        s2 = Square(3, 1, 3)
        self.assertEqual(str(s2), "[Square] (1) 1/3 - 3")

    def test_update(self):
        """Test update method"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)
        self.assertEqual(type(s1_dictionary), dict)


if __name__ == "__main__":
    unittest.main()
