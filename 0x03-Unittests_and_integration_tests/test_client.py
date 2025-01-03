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
# get_json = __import__('utils').get_json


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

    @patch("client.get_json", return_value=[{"name": "get_json"}])
    def test_public_repos(self, mk: Mock):
        """Test public_repos"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = "get"
            self.assertEqual(GithubOrgClient("url").public_repos(),
                             ["get_json"])
            # self.assertEqual(mock_public_url.call_count, 1)
            # self.assertEqual(mk.call_count, 1)
            mock_public_url.assert_called_once()
            mk.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Mapping, license_key: str, eval: bool):
        self.assertEqual(GithubOrgClient("url").has_license(repo, license_key), eval)