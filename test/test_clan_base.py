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
from pyroyale.models.clan_base import ClanBase  # noqa: E501
from pyroyale.rest import ApiException


class TestClanBase(unittest.TestCase):
    """ClanBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClanBase(self):
        """Test ClanBase"""
        # FIXME: construct object with mandatory attributes with example values
        pass

    def testDefaults(self):
        model = ClanBase()
        pass

    def testConstructorInitializers(self):
        model = ClanBase(
            tag='tag',
            name='name',
            badge_id='badge_id'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.badge_id=='badge_id'

    def testToDict(self):
        model = ClanBase(
            tag={'foo':'bar'},
            name=[ClanBase()],
            badge_id=123
        )

        clanDict = model.to_dict()

        assert clanDict['tag']['foo']=='bar'
        assert clanDict['badge_id']==123

    def testToString(self):
        model = ClanBase(tag='TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = ClanBase(tag='TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = ClanBase('A')
        model_a2 = ClanBase('A')
        model_b  = ClanBase('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
