#!/usr/bin/env python3

import types
import unittest
from print_numbers import display_the_nos

class TestCaseToCheckTheReturnValue(unittest.TestCase):
    # Below function to check whether the return type is GeneratorType or not
    def test_check_return_value(self):
        self.assertIsInstance(display_the_nos(100), types.GeneratorType)
    
if __name__ == '__main__':
    unittest.main()
