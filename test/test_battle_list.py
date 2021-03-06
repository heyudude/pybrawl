# coding: utf-8

"""
    Brawl_Stars_API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/heyudude/brawlstars-swagger
"""


from __future__ import absolute_import

import unittest
import datetime

import pybrawl
from pybrawl.models.battle_list import BattleList  # noqa: E501
from pybrawl.rest import ApiException

class TestBattleList(unittest.TestCase):
    """BattleList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BattleList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pybrawl.models.battle_list.BattleList()  # noqa: E501
        if include_optional :
            return BattleList(
                battle_time = '0', 
                event = [
                    pybrawl.models.event.Event(
                        id = 56, 
                        mode = '0', 
                        map = '0', )
                    ], 
                battle = [
                    pybrawl.models.battle.Battle(
                        mode = '0', 
                        type = '0', 
                        rank = 56, 
                        trophy_change = 56, 
                        players = [
                            pybrawl.models.battle_log_team.BattleLogTeam(
                                tag = '0', 
                                name = '0', 
                                brawler = [
                                    pybrawl.models.battle_log_brawler.BattleLogBrawler(
                                        id = 56, 
                                        name = '0', 
                                        power = 56, 
                                        trophies = 56, 
                                        paging = pybrawl.models.search_paging.SearchPaging(
                                            cursors = pybrawl.models.search_paging_cursors.SearchPaging_cursors(
                                                after = '0', 
                                                before = '0', ), ), )
                                    ], )
                            ], )
                    ]
            )
        else :
            return BattleList(
        )

    def testBattleList(self):
        """Test BattleList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
