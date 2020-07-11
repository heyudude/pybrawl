# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pybrawl
from pybrawl.models.battles import Battles  # noqa: E501
from pybrawl.rest import ApiException

class TestBattles(unittest.TestCase):
    """Battles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Battles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pybrawl.models.battles.Battles()  # noqa: E501
        if include_optional :
            return Battles(
                battle_time = '0', 
                event = [
                    pybrawl.models.event.Event(
                        id = 56, 
                        mode = '0', 
                        map = '0', 
                        battle = [
                            pybrawl.models.battle.Battle(
                                mode = '0', 
                                type = '0', 
                                result = '0', 
                                duration = 56, 
                                trophy_change = 56, 
                                star_player = [
                                    pybrawl.models.star_player.starPlayer(
                                        tag = '0', 
                                        name = '0', 
                                        brawler = pybrawl.models.star_brawler.starBrawler(
                                            id = 56, 
                                            name = '0', 
                                            power = 56, 
                                            trophies = 56, ), )
                                    ], 
                                teams = [
                                    pybrawl.models.teams.teams(
                                        tag = '0', 
                                        name = '0', )
                                    ], )
                            ], )
                    ]
            )
        else :
            return Battles(
        )

    def testBattles(self):
        """Test Battles"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
