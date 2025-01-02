#!/usr/bin/env python3
"""Module"""
import unittest
from unittest.mock import PropertyMock, patch, Mock
import unittest.mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any

from utils import memoize
from client import GithubOrgClient
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestGithubOrgClient(unittest.TestCase):
    """a clss for testing client.py"""
    @parameterized.expand([
        ("google", {}),
        ("abc", {}),
    ])
    @patch("requests.get", return_value=Mock())
    def test_org(self, org: str, ret: Mapping, MK1: Mock):
        """testing org of GithubOrgClient class"""
        new_mock = Mock()
        new_mock.json.return_value = ret
        MK1.return_value = new_mock

        self.assertEqual(GithubOrgClient(org).org, ret)
        self.assertEqual(MK1.call_count, 1)

    @parameterized.expand([
        ("google", "great"),
        ("abc", "great"),
    ])
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, url: str, ret: str, MK_ret: Mock):
        """"""
        MK_ret.return_value = {"repos_url": "great"}
        self.assertEqual(GithubOrgClient(url)._public_repos_url, ret)
