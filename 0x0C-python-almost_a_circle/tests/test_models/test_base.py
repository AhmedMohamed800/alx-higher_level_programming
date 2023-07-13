#!/usr/bin/python3
"""Unittest for Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test for Base"""
    def test_create_id(self):
        """test id's values"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(1.4)
        b6 = Base(-2)
        b7 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 1.4)
        self.assertEqual(b6.id, -2)
        self.assertEqual(b7.id, 0)
