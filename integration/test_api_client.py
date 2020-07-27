# coding: utf-8

# flake8: noqa

"""
Run the tests.
$ pip install nose (optional)
$ cd OpenAPIetstore-python
$ nosetests -v
"""
import config
import configparser
from datetime import datetime
import gettext
import json
import locale
import logging
import requests
import copy
import os
import time
import atexit
import weakref
import unittest
from dateutil.parser import parse
from bstools.api_wrapper import ApiWrapper

import pybrawl
import pybrawl.configuration

HOST = 'https://api.brawlstars.com/v1'
# Create config dict with defaults
config_defaults = {
    'api': {
        'api_key': False,
        'club_id': False,
        'player_id': False,
        'proxy': '',
        'proxy_headers': ''
    },
    'paths': {
        'out': './bstools-out',
        'favicon': False,
        'club_logo': False,
        'description_html': False,
        'temp_dir_name': 'bstools',
        'use_fankit': False
    },
    'www': {
        'canonical_url': False
    },
    'activity': {
        'threshold_warn': 7,
        'threshold_kick': 21,
        'min_days_to_promote': 0
    },
    'score': {
        'min_club_size':               46,
        'threshold_promote':           160,
        'threshold_demote':            0,
        'threshold_kick':              0,
        'threshold_warn':              30,
        'new_member_grace_period_days': 3
    },
    'history': {
        'num_battles_to_track':            10
    },
    'members': {
        'blacklist': [],
        'no_promote': [],
        'kicked': [],
        'warned': [],
        'vacation': [],
        'safe': [],
        'custom': {}
    },
    'member_table': {
        'show_rank': True,
        'show_rank_previous': False,
        'show_name': True,
        'show_xp_level': False,
        'show_score': True,
        'show_trophies': True,
        'show_time_in_club': False,
        'show_last_seen': False,
        'show_days_inactive': True
    },
    'discord': {
        'webhook_default': '',
        'leaderboard_war': False,
        'leaderboard_donations': False,
        'webhook_war_nag': '',
        'warn_inactive': False,
        'scold_missed_war_battle': False,
        'scold_missed_collection_battle': False
    },
    'google_docs': {
        'api_key': '',
        'sheet_id': ''
    },
    'bstools': {
        'debug': False,
        'timestamp': datetime.utcnow(),
        'locale': 'en',
        'version': '0',
        'latest_version': '1',
        'update_available': False
    }
}

class ApiClientTests(unittest.TestCase):

    def test_configuration(self):
        self.api = pybrawl.PlayersApi(pybrawl.ApiClient(config.getConfiguration()))
    pass
    
if __name__ == '__main__':
    unittest.main()
