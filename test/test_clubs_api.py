# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pybrawl
from pybrawl.api.clubs_api import ClubsApi  # noqa: E501
from pybrawl.rest import ApiException


class TestClubsApi(unittest.TestCase):
    """ClubsApi unit test stubs"""

    def setUp(self):
        self.api = pybrawl.api.clubs_api.ClubsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_getclub(self):
        """Test case for getclub

        Get club information  # noqa: E501
        """
        pass

    def test_getclub_members(self):
        """Test case for getclub_members

        List club members  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
