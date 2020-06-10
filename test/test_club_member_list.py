# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pybrawl
from pybrawl.models.club_member_list import ClubMemberList  # noqa: E501
from pybrawl.rest import ApiException

class TestClubMemberList(unittest.TestCase):
    """ClubMemberList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClubMemberList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pybrawl.models.club_member_list.ClubMemberList()  # noqa: E501
        if include_optional :
            return ClubMemberList(
                items = [
                    pybrawl.models.club_member.clubMember(
                        tag = '0', 
                        name = '0', 
                        exp_level = 56, 
                        trophies = 56, 
                        arena = pybrawl.models.arena.Arena(
                            id = 56, 
                            name = '0', ), 
                        role = '0', 
                        last_seen = '0', 
                        club_rank = 56, 
                        previousclub_rank = 56, 
                        donations = 56, 
                        donations_received = 56, 
                        club_chest_points = 56, )
                    ], 
                paging = pybrawl.models.search_paging.SearchPaging(
                    cursors = pybrawl.models.search_paging_cursors.SearchPaging_cursors(
                        after = '0', 
                        before = '0', ), )
            )
        else :
            return ClubMemberList(
        )

    def testClubMemberList(self):
        """Test ClubMemberList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
