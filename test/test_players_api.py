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
from pybrawl.api.players_api import PlayersApi  # noqa: E501
from pybrawl.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = pybrawl.api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_player_battles(self):
        """Test case for get_player_battles

        Get log of recent battles for a player  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
