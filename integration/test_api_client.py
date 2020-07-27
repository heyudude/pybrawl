# coding: utf-8

# flake8: noqa

"""
Run the tests.
$ pip install nose (optional)
$ cd OpenAPIetstore-python
$ nosetests -v
"""
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

    def SetUp(self):
        #self.api = pybrawl.PlayersApi(pybrawl.ApiClient(config.getConfiguration())) 
        config = load_config_file('../../.bstools')
        print("setup")

    def __parse_value(self, new_value, template_value):
        value = new_value
        if isinstance(template_value, list):
            value = value.split(',')
            value = [x.strip() for x in value]
        else:
            # if the value represents an integer, convert from string to int
            try:
             value = int(value)
            except ValueError:
                pass

        # if set to "true" or "false" or similar, convert to boolean
        if isinstance(value, str):
            if value.lower() in ['true', 'yes', 'on']:
                value = True
            elif value.lower() in ['false', 'no', 'off']:
                value = False
        return value

    def load_config_file(self, config_file_name=None, check_for_update=False, locale=None):
        """ Look for config file. If config file exists, load it, and try to
        extract config from config file"""

        config = copy.deepcopy(config_defaults)

        if config_file_name and os.path.isfile(config_file_name):
            parser = configparser.ConfigParser()
            parser.read(config_file_name)
            sections = parser.sections()
            a = self.__parse_value('a', 'b')
            # Map the contents of the ini file with the structure for the config object found above.
            for section in sections:
                section_key = section.lower()
                
                if section_key in config:
                    for (key, value) in parser.items(section):
                        if key in config[section_key]:
                            config[section_key][key] = self.__parse_value(value, config[section_key][key])
                            
        #config = __validate_paths(config)
        #config = __validate_bstools_settings(config)
        #config = __process_special_status(config)

        # Augment from Google Sheet
        #config = gdoc.get_member_data_from_sheets(config)

        if check_for_update:
            config = __get_version_info(config)

        if locale:
            config['bstools']['locale'] = locale

        #config['strings'] = __localize_strings(config['bstools']['locale'])

        return config

    def test_configuration(self):
        config = self.load_config_file('../../.bstools')      
        
        api = ApiWrapper(config)
        player = api.get_data_from_api()

if __name__ == '__main__':
    unittest.main()
