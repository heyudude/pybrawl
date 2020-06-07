# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger docs for the official Brawl Stars API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pybrawl
from pybrawl.models.season_statistics import SeasonStatistics  # noqa: E501
from pybrawl.rest import ApiException


class TestSeasonStatistics(unittest.TestCase):
    """SeasonStatistics unit test stubs"""

    def testDefaults(self):
        model = SeasonStatistics()

    def testConstructorInitializers(self):
        model = SeasonStatistics(
            id='id',
            trophies='trophies',
            best_trophies='best_trophies'
        )

        assert model.id=='id'
        assert model.trophies=='trophies'
        assert model.best_trophies=='best_trophies'

    def testToDict(self):
        model = SeasonStatistics(
            id={'foo': 'bar'},
            trophies=SeasonStatistics(trophies=123),
            best_trophies=[SeasonStatistics(trophies='trophies')],
        )

        modelDict = model.to_dict()

        assert modelDict['id']['foo']=='bar'
        assert modelDict['trophies']['trophies']==123
        assert modelDict['best_trophies'][0]['trophies']=='trophies'

    def testToString(self):
        model = SeasonStatistics('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = SeasonStatistics('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = SeasonStatistics('A')
        model_a2 = SeasonStatistics('A')
        model_b  = SeasonStatistics('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
