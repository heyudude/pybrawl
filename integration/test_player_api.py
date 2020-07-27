from __future__ import absolute_import

import unittest

import config
import pybrawl
import logging
from pybrawl.api.players_api import PlayersApi
from pybrawl.rest import ApiException
logger = logging.getLogger(__name__)

#configuration = config.getConfiguration()

class TestPlayersApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.PlayersApi(pybrawl.ApiClient(config.getConfiguration()))

    def tearDown(self):
        pass

    def test_player_Dude(self):
        try:
            #print(self.api.api_client.configuration.api_key['authorization'])
       	    player = self.api.get_player('#200JUQP')
            assert player.tag == '#200JUQP'
            assert player.name == 'Dude'
            assert player.explevel >= 13
            assert player.trophies >= 4000
            assert player.best_trophies >= 4000
            assert player.battle_count >= 20000
            assert player.role.lower() in ['President', 'Vice President', 'Senior', 'Member']
            assert player.donations >= 0
            assert player.donations_received >= 0
            assert player.Club.tag == '#RLUP2C'
            assert player.Club.name == '18Plussers'
            assert player.Club.badge_id >= 16000000
            assert player.star_points >= 0

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player(): %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()
