#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxinteger(unittest.TestCase):
    """test max intger"""
    def test_use(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, 14)
        self.assertRaises(TypeError, max_integer, ["23", "hello", 12])
        self.assertRaises(TypeError, max_integer, "hello12")
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, [1.23, 12, 12.3])
