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
from pybrawl.models.ranking_club_list import RankingClubList  # noqa: E501
from pybrawl.rest import ApiException

class TestRankingClubList(unittest.TestCase):
    """RankingClubList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RankingClubList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pybrawl.models.ranking_club_list.RankingClubList()  # noqa: E501
        if include_optional :
            return RankingClubList(
                tag = '0', 
                name = '0', 
                trophies = 56, 
                rank = 56, 
                membercount = 56, 
                paging = pybrawl.models.search_paging.SearchPaging(
                    cursors = pybrawl.models.search_paging_cursors.SearchPaging_cursors(
                        after = '0', 
                        before = '0', ), )
            )
        else :
            return RankingClubList(
        )

    def testRankingClubList(self):
        """Test RankingClubList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
