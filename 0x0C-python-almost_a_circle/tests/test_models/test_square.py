#!/usr/bin/python3

import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
	def test_pep8_conformance_square(self):
		"""Test that we conform to PEP8."""
		pep8style = pep8.StyleGuide(quiet=True)
		result = pep8style.check_files(['models/square.py'])
		self.assertEqual(result.total_errors, 0,
						"Found code style errors (and warnings).")

	def test_getter(self):
		r1 = Square(5)
		self.assertEqual(r1.size, 5)

	def test_setter(self):
		r1 = Square(5)
		r1.size = 8
		self.assertEqual(r1.size, 8)

	def test_string(self):
		r1 = Square(3)
		with self.assertRaises(TypeError):
			r1.size = "Hi"

	def test_negative(self):
		r1 = Square(6)
		with self.assertRaises(ValueError):
			r1.size = -5

	def test_zero(self):
		r1 = Square(6)
		with self.assertRaises(ValueError):
			r1.size = 0

	def test_zero(self):
		r1 = Square(6)
		with self.assertRaises(TypeError):
			r1.size = 1.5

	def test_tupla(self):
		r1 = Square(7)
		with self.assertRaises(TypeError):
			r1.size = (2, 8)

	def test_empty(self):
		r1 = Square(7)
		with self.assertRaises(TypeError):
			r1.size = ""

	def test_none(self):
		r1 = Square(5)
		with self.assertRaises(TypeError):
			r1.size = None

	def test_list(self):
		r1 = Square(4)
		with self.assertRaises(TypeError):
			r1.size = [4, 7]

	def test_dict(self):
		r1 = Square(5)
		with self.assertRaises(TypeError):
			r1.size = {"hi": 5, "world": 8}

	def test_width(self):
		r1 = Square(5)
		r1.size = 6
		self.assertEqual(r1.width, 6)
		self.assertEqual(r1.height, 6)



            
if __name__ == "_main_":
   unittest.main()
