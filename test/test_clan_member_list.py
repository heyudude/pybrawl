# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.clan_member_list import ClanMemberList  # noqa: E501
from pyroyale.rest import ApiException


class TestClanMemberList(unittest.TestCase):
    """ClanMemberList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = ClanMemberList()
        pass

    def testConstructorInitializers(self):
        model = ClanMemberList(
            items='items'
        )

        assert model.items=='items'

    def testToDict(self):
        model = ClanMemberList(
            items='items'
        )
        modelDict = model.to_dict()

        assert modelDict['items']=='items'

        model = ClanMemberList(
            items=123,
        )
        modelDict = model.to_dict()

        assert modelDict['items']==123

        model = ClanMemberList(
            items=ClanMemberList(items='items'),
        )
        modelDict = model.to_dict()

        assert modelDict['items']['items']=='items'

    def testToString(self):
        model = ClanMemberList('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ClanMemberList('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ClanMemberList('A')
        model_a2 = ClanMemberList('A')
        model_b  = ClanMemberList('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
