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

import pybrawl
from pybrawl.models.player_ranked import PlayerRanked  # noqa: E501
from pybrawl.rest import ApiException


class TestPlayerRanked(unittest.TestCase):
    """PlayerRanked unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = PlayerRanked()
        pass

    def testConstructorInitializers(self):
        model = PlayerRanked(
            tag='tag',
            name='name',
            exp_level='exp_level',
            trophies='trophies',
            rank='rank',
            previous_rank='previous_rank',
            clan='clan',
            arena='arena',
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.exp_level=='exp_level'
        assert model.trophies=='trophies'
        assert model.rank=='rank'
        assert model.previous_rank=='previous_rank'
        assert model.clan=='clan'
        assert model.arena=='arena'

    def testToDict(self):
        model = PlayerRanked(
            tag={'foo':'bar'},
            name=PlayerRanked(tag=123),
            exp_level=[PlayerRanked(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['name']['tag']==123
        assert modelDict['exp_level'][0]['name']=='name'

    def testToString(self):
        model = PlayerRanked('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = PlayerRanked('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = PlayerRanked('A')
        model_a2 = PlayerRanked('A')
        model_b  = PlayerRanked('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
