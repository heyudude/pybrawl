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
from pybrawl.models.arena import Arena  # noqa: E501
from pybrawl.rest import ApiException


class TestArena(unittest.TestCase):
    """Arena unit test stubs"""

    def testDefaults(self):
        model = Arena()
        assert True

    def testConstructorInitializers(self):
        model = Arena(
            id='id',
            name='name'
        )

        assert model.id=='id'
        assert model.name=='name'

    def testToDict(self):
        model = Arena(
            id=123,
            name=Arena(name='name')
        )

        modelDict = model.to_dict()

        assert modelDict['id']==123
        assert modelDict['name']['name']=='name'

        model = Arena(
            id={'foo':'bar'},
            name=[Arena(id='id')]
        )

        modelDict = model.to_dict()

        assert modelDict['id']['foo']=='bar'
        assert modelDict['name'][0]['id']=='id'

    def testToString(self):
        model = Arena('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = Arena('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = Arena('A')
        model_a2 = Arena('A')
        model_b  = Arena('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
