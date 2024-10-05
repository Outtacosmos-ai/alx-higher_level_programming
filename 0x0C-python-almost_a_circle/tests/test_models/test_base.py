#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_none(self):
        """Test id as none"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_not_none(self):
        """Test id not none"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_multiple_instances(self):
        """Test multiple instances"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)


if __name__ == '__main__':
    unittest.main()
