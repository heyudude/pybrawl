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
from pyroyale.models.war_current import WarCurrent  # noqa: E501
from pyroyale.rest import ApiException


class TestWarCurrent(unittest.TestCase):
    """WarCurrent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConstructorInitializers(self):
        model = WarCurrent(
            state='state',
            war_end_time='war_end_time',
            collection_end_time='collection_end_time',
            clan='clan',
            participants='participants',
            clans='clans'
        )

        assert model.state=='state'
        assert model.war_end_time=='war_end_time'
        assert model.collection_end_time=='collection_end_time'
        assert model.clan=='clan'
        assert model.participants=='participants'
        assert model.clans=='clans'

    def testToDict(self):
        model = WarCurrent(
            collection_end_time='collection_end_time',
            clan=123,
            participants={'foo':'bar'},
            clans=[WarCurrent(collection_end_time='collection_end_time')]
        )

        modelDict = model.to_dict()

        assert modelDict['collection_end_time']=='collection_end_time'
        assert modelDict['participants']['foo']=='bar'
        assert modelDict['clan']==123
        assert modelDict['clans'][0]['collection_end_time']=='collection_end_time'

    def testToString(self):
        model = WarCurrent('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = WarCurrent('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = WarCurrent('A')
        model_a2 = WarCurrent('A')
        model_b  = WarCurrent('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()