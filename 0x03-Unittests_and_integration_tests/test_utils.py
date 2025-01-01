#!/usr/bin/env python3
"""Module"""
import unittest
import unittest.mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any

from utils import memoize
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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """tests if access_nested_map raises a keyError on specific inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """a class that tests the utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}, ),
        ("http://holberton.io", {"payload": False}, ),
    ])
    @unittest.mock.patch("requests.get", return_value=unittest.mock.Mock())
    def test_get_json(self, url: str, playload: Mapping,
                      mockk: unittest.mock.Mock) -> None:
        """Function that tests utils.get_json"""
        new_mock = unittest.mock.Mock()
        new_mock.json.return_value = playload
        mockk.return_value = new_mock

        self.assertEqual(get_json(url), playload)
        self.assertEqual(mockk.call_count, 1)


class TestMemoize(unittest.TestCase):
    """testing the memoize function"""
    class TestClass:
        """a testing class"""
        def a_method(self):
            """first method"""
            return 42

        @memoize
        def a_property(self):
            """wrapper method"""
            return self.a_method()

    def test_memoize(self):
        """testing the memoize with mock and patch"""
        with unittest.mock.patch(f"{__name__}.TestMemoize.TestClass.a_method",
                                 return_value=42) as mockk:
            instance = self.TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(mockk.call_count, 1)
