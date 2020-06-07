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

import pybrawl
from pybrawl.models.player_ranking_list import PlayerRankingList  # noqa: E501
from pybrawl.rest import ApiException


class TestPlayerRankingList(unittest.TestCase):
    """PlayerRankingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = PlayerRankingList()
        pass

    def testConstructorInitializers(self):
        model = PlayerRankingList(
            items='items',
            paging='paging'
        )

        assert model.items=='items'
        assert model.paging=='paging'

    def testToDict(self):
        model = PlayerRankingList(
            items=PlayerRankingList(items='items', paging=123),
            paging=[PlayerRankingList(items={'foo': 'bar'})]
        )
        modelDict = model.to_dict()

        assert modelDict['items']['items']=='items'
        assert modelDict['items']['paging']==123
        assert modelDict['paging'][0]['items']['foo']=='bar'

    def testToString(self):
        model = PlayerRankingList('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = PlayerRankingList('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = PlayerRankingList('A')
        model_a2 = PlayerRankingList('A')
        model_b  = PlayerRankingList('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
