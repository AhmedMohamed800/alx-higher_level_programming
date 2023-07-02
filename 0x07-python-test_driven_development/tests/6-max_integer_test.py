#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxinteger(unittest.TestCase):
    """test max intger"""

    def test_use(self):
        """Regual tests """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        """Type check"""
        self.assertRaises(TypeError, max_integer, 14)
        self.assertRaises(TypeError, max_integer, ["23", "hello", 12])
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, None)

    def test_empty(self):
        """empty tests"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_negative(self):
        """test_negatives"""
        self.assertEqual(max_integer([-1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -7]), -1)

    def test_float(self):
        """test floats"""
        self.assertEqual(max_integer([-1.2, -1.1, -7]), -1.1)

    def test_strings(self):
        """test_strings"""
        self.assertEqual(max_integer(["hello world", "meow"]), "meow")
        self.assertEqual(max_integer("hello"), "o")
        
