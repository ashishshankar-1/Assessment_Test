#!/usr/bin/python3

import unittest
from validate_format_PostCode import *

class TestToValidateThePostCode(unittest.TestCase):
    def test_to_validate_postcode(self):
        # Test for valid postcode
        self.assertTrue(validatePostcode("RG27 9HW"))

        # Test for invalid post code
        self.assertFalse(validatePostcode("CR2 20D"))

class TestToQueryPostcode(unittest.TestCase):
    def test_to_query_postcode(self):
        # Test for query with valid postcode
        self.assertEqual(type(queryPostcode("RG27 9HW")), type(list()))

        # Test for query with invalid  postcode like 'PXSJ 123'
        self.assertEqual(queryPostcode("PXSJ 123"), None)

class TestToGetAutoCompletePostcode(unittest.TestCase):
    def test_to_query_postcode(self):
        # Test to get auto complete with valid postcode
        self.assertEqual(type(getAutoCompletePostcode("RG27 9HW")), type(list()))

        # Test to get auto complete with invalid  postcode like 'PXSJ 123'
        self.assertEqual(getAutoCompletePostcode("PXSJ 123"), None)


if __name__ == '__main__':
    unittest.main()
