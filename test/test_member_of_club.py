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
from pybrawl.models.member_of_club import MemberOfClub  # noqa: E501
from pybrawl.rest import ApiException

class TestMemberOfClub(unittest.TestCase):
    """MemberOfClub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MemberOfClub
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pybrawl.models.member_of_club.MemberOfClub()  # noqa: E501
        if include_optional :
            return MemberOfClub(
                tag = '0', 
                name = '0'
            )
        else :
            return MemberOfClub(
        )

    def testMemberOfClub(self):
        """Test MemberOfClub"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
