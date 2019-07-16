# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.clan_war_ranked import ClanWarRanked  # noqa: E501
from pyroyale.rest import ApiException


class TestClanWarRanked(unittest.TestCase):
    """ClanWarRanked unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = ClanWarRanked()
        pass

    def testConstructorInitializers(self):
        model = ClanWarRanked(
            tag='tag',
            name='name',
            rank='rank',
            previous_rank='previous_rank',
            badge_id='badge_id',
            clan_score='clan_score',
            members='members',
            location='location'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.previous_rank=='previous_rank'
        assert model.badge_id=='badge_id'
        assert model.badge_id=='badge_id'
        assert model.clan_score=='clan_score'
        assert model.members=='members'
        assert model.location=='location'

    def testToDict(self):
        model = ClanWarRanked(
            tag='tag',
            clan_score=123,
            members=[ClanWarRanked(name='clanname')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']=='tag'
        assert modelDict['clan_score']==123
        assert modelDict['members'][0]['name']=='clanname'

    def testToString(self):
        model = ClanWarRanked('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ClanWarRanked('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ClanWarRanked('A')
        model_a2 = ClanWarRanked('A')
        model_b  = ClanWarRanked('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
