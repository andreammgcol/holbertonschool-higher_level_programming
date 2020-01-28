#!/usr/bin/python3
"""
Module unittest for the Base class
"""
import unittest
import sys
import os
import json
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
	"""
    Test cases for the Base class
    """

	def test_pep8_conformance_base(self):
		"""Test that we conform to PEP8."""
		pep8style = pep8.StyleGuide(quiet=True)
		result = pep8style.check_files(['models/base.py'])
		self.assertEqual(result.total_errors, 0,
				"Found code style errors (and warnings).")


	def test_id_positive(self):
		bo = Base(23)
		self.assertEqual(bo.id, 23)
		bo = Base(34)
		self.assertEqual(bo.id, 34)

	def test_id_negative(self):
		bo = Base(-4)
		self.assertEqual(bo.id, -4)
		bo = Base(-10)
		self.assertEqual(bo.id, -10)

	def test_id_none(self):
		bo = Base()
		self.assertEqual(bo.id, 1)
		bo = Base(None)
		self.assertEqual(bo.id, 2)

	def test_id_string(self):
		bo = Base("st")
		self.assertEqual(bo.id, "st")
		bo = Base("st2")
		self.assertEqual(bo.id, "st2")

	def test_id_float(self):
		bo = Base(0.5)
		self.assertEqual(bo.id, 0.5)
		bo = Base(2.4)
		self.assertEqual(bo.id, 2.4)

	def test_from_json_string(self):
		string_js = '[{"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}, \
			{"id": 7, "width": 1, "height": 7, "x": 6, "y": 5}]'
		jsonconv = Base.from_json_string(string_js)
		self.assertTrue(type(jsonconv) is list)
		self.assertEqual(len(jsonconv), 2)



if __name__ == "_main_":
   unittest.main()