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
            # Configure Bearer authorization (JWT): JWT
       	    player = self.api.get_player('#200JUQP')
            print(player.tag, player.name, player.trophies)
            # assert player.tag == '#200JUQP'
            # assert player.name == 'Dude'
            # assert player.trophies >= 4000
            # assert.nameColor == '0xfff05637'
            # assert.trophies == 14320
            # assert.highestTrophies == 14490
            # assert.highestPowerPlayPoints == 86
            # assert.expLevel == 91
            # assert.expPoints == 44360
            # assert.isQualifiedFromChampionshipChallenge == False
            # assert.3vs3Victories == 827
            # assert.soloVictories == 382
            # assert.duoVictories == 59
            # assert.bestRoboRumbleTime == 5
            # assert.bestTimeAsBigBrawler == 0

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player(): %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()
