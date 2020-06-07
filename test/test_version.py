from __future__ import absolute_import

import pybrawl
from pybrawl._version import __version__
import unittest

def testVersion():
    assert len(__version__) >= 5

