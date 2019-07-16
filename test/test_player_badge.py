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
from pyroyale.models.player_badge import PlayerBadge  # noqa: E501
from pyroyale.rest import ApiException

class TestPlayerBadge(unittest.TestCase):
    """PlayerBadge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlayerBadge(self):
        """Test PlayerBadge"""
        # FIXME: construct object with mandatory attributes with example max_levels
        # model = PlayerBadge()  # noqa: E501
        pass

    def testDefaults(self):
        model = PlayerBadge()
        pass

    def testConstructorInitializers(self):
        model = PlayerBadge(
            name='name',
            level='level',
            max_level='max_level',
            progress='progress'
        )

        assert model.name=='name'
        assert model.level=='level'
        assert model.max_level=='max_level'
        assert model.progress=='progress'

    def testToDict(self):
        model = PlayerBadge(
            level=123,
            progress=[PlayerBadge(name='clanname')]
        )

        modelDict = model.to_dict()

        assert modelDict['level']==123
        assert modelDict['progress'][0]['name']=='clanname'

    def testToString(self):
        model = PlayerBadge('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = PlayerBadge('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = PlayerBadge('A')
        model_a2 = PlayerBadge('A')
        model_b  = PlayerBadge('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
