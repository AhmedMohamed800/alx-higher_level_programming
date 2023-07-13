#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """Test for Rectangle class"""
    def test_baisc_use(self):
        """Test id, width, heigth, x and y"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.y, 0)

    def test_width_height(self):
        """test all cases of width_height"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(TypeError):
            Rectangle("hello", -2)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello")
        with self.assertRaises(TypeError):
            Rectangle(None, -2)
        with self.assertRaises(TypeError):
            Rectangle(2, None)
        with self.assertRaises(TypeError):
            Rectangle(10.2, -2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2.3)
        with self.assertRaises(TypeError):
            Rectangle(10, -2.3)
        with self.assertRaises(TypeError):
            Rectangle(-2.3, 2.3)

    def test_x_y(self):
        """test all cases of x_y"""
        r1 = Rectangle(10, 23, 1)
        r2 = Rectangle(10, 23, 1, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 23, -1, 2)
        rl = Rectangle(10, 23, 0, 2)
        self.assertEqual(rl.x, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 23, 1, -1)
        rl2 = Rectangle(10, 23, 1, 0)
        self.assertEqual(rl2.y, 0)
        with self.assertRaises(TypeError):
            Rectangle(10)
