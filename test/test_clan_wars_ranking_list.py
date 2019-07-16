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
from pyroyale.models.clan_wars_ranking_list import ClanWarsRankingList  # noqa: E501
from pyroyale.rest import ApiException


class TestClanWarsRankingList(unittest.TestCase):
    """ClanWarsRankingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = ClanWarsRankingList()
        pass

    def testConstructorInitializers(self):
        model = ClanWarsRankingList(
            items='items'
        )

        assert model.items=='items'

    def testToDict(self):
        model = ClanWarsRankingList(
            items='items'
        )
        modelDict = model.to_dict()

        assert modelDict['items']=='items'

        model = ClanWarsRankingList(
            items=123,
        )
        modelDict = model.to_dict()

        assert modelDict['items']==123

        model = ClanWarsRankingList(
            items=ClanWarsRankingList(items='items'),
        )
        modelDict = model.to_dict()

        assert modelDict['items']['items']=='items'

    def testToString(self):
        model = ClanWarsRankingList('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ClanWarsRankingList('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ClanWarsRankingList('A')
        model_a2 = ClanWarsRankingList('A')
        model_b  = ClanWarsRankingList('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
