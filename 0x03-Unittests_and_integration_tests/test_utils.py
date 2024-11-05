#!/usr/bin/env python3
"""Module"""
import unittest
import unittest.mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """unit testing class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """a function to test the access_nested_map function"""

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    # python3 -c 'print(__import__("test_utils").TestAccessNestedMap.test_access_nested_map_exception.__doc__)'
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """tests if access_nested_map raises a keyError on specific inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

# class TestGetJson(unittest.TestCase):
#     """a class that tests the utils.get_json"""
#     @parameterized.expand([
#         ("http://example.com", {"payload": True}, ),
#         ("http://holberton.io", {"payload": False}, ),
#     ])
#     @unittest.mock.patch("requests.get", return_value=unittest.mock.Mock())
#     def test_get_json(self, url: str) -> None:
#         pass