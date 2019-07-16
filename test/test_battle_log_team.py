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
from pyroyale.models.battle_log_team import BattleLogTeam  # noqa: E501
from pyroyale.rest import ApiException


class TestBattleLogTeam(unittest.TestCase):
    """BattleLogTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBattleLogTeam(self):
        """Test BattleLogTeam"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BattleLogTeam()  # noqa: E501
        pass

    def testDefaults(self):
        model = BattleLogTeam()
        pass

    def testConstructorInitializers(self):
        model = BattleLogTeam(
            tag='tag',
            name='name',
            starting_trophies='starting_trophies',
            trophy_change='trophy_change',
            crowns='crowns',
            clan='clan',
            cards='cards'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.starting_trophies=='starting_trophies'
        assert model.trophy_change=='trophy_change'
        assert model.crowns=='crowns'
        assert model.clan=='clan'
        assert model.cards=='cards'

    def testToDict(self):
        model = BattleLogTeam(
            tag='tag',
            starting_trophies=123,
            clan=BattleLogTeam(tag='tag'),
        )

        modelDict = model.to_dict()

        assert modelDict['tag']=='tag'
        assert modelDict['starting_trophies']==123
        assert modelDict['clan']['tag']=='tag'

    def testToString(self):
        model = BattleLogTeam('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = BattleLogTeam('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = BattleLogTeam('A')
        model_a2 = BattleLogTeam('A')
        model_b  = BattleLogTeam('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
