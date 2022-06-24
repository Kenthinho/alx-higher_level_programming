#!/usr/bin/python3
"""A Unittest module for max_integer function.
"""
import unittest
from importlib import import_module


class TestMaxInteger(unittest.TestCase):
    '''Test the max_integer function.
    '''
    def test_area(self):
        '''The equality test for the max_integer function
        '''
        max_integer = import_module('6-max_integer', '..').max_integer
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-7, -2, -45, -6]), -2)
        self.assertEqual(max_integer([7, 2, 45, 6]), 45)
