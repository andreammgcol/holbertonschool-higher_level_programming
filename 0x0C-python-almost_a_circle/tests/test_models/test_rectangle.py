#!/usr/bin/python3

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class Testrectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class
    """

    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def set_Up(self):
        """
        Redirect the stdout to check the output
        """
        sys.stdout = StringIO()

    def reset_clean(self):
        """
        Reset the nb_objects and clean everything
        """
        Base._Base__nb_objects = 0
        sys.stdout = sys.__stdout__

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_docstring(self):
        """
        Test docstring
        """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_documentation(self):
        """
        Test documentation is correct and created
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "create"))
        self.assertTrue(Rectangle.create.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_json_string"))
        self.assertTrue(Rectangle.to_json_string.__doc__)
        self.assertTrue(hasattr(Rectangle, "from_json_string"))
        self.assertTrue(Rectangle.from_json_string.__doc__)
        self.assertTrue(hasattr(Rectangle, "save_to_file"))
        self.assertTrue(Rectangle.save_to_file.__doc__)
        self.assertTrue(hasattr(Rectangle, "load_from_file"))
        self.assertTrue(Rectangle.load_from_file.__doc__)

    def test_parameters(self):

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def is_string(self):
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)

    def test_type_param(self):
        """ width instance testing """
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
            raise TypeError()
        with self.assertRaises(ValueError):
            R2 = Rectangle(-234234242, 45)
            raise ValueError()
        with self.assertRaises(TypeError):
            R3 = Rectangle("", 4)
            raise TypeError()
        with self.assertRaises(TypeError):
            R4 = Rectangle(True, 4)
            raise TypeError()

        """ height instance testing """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1.76)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, "Hello")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, -4798576398576)
            raise ValueError()

        """ x instance testing """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1.50)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 7, -4798576398576)
            raise ValueError()

        """ y instance testing """
        with self.assertRaises(TypeError):
            H1 = Rectangle(5, 1, 1, 1.53)
            raise TypeError()
        with self.assertRaises(TypeError):
            H2 = Rectangle(5, 6, 5, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            H3 = Rectangle(5, 7, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            H1 = Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()

    def test_rectangle_area(self):
        """
        Test area method
        """
        r = Rectangle(1, 2)
        r1 = Rectangle(3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9)
        r3 = Rectangle(10, 11, 12, 13, 14)
        r4 = Rectangle(9999999999999, 9999999999999)
        self.assertEqual(r.area(), 2)
        self.assertEqual(r1.area(), 3 * 4)
        self.assertEqual(r2.area(), 6 * 7)
        self.assertEqual(r3.area(), 10 * 11)
        self.assertEqual(r4.area(), 9999999999999 * 9999999999999)
