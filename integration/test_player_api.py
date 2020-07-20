from __future__ import absolute_import

import unittest

import config

import pybrawl
from pybrawl.api.players_api import PlayersApi  # noqa: E501
from pybrawl.rest import ApiException

configuration = config.getConfiguration()

class TestPlayersApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.api.players_api.PlayersApi()  # noqa: E501
        pass
        
    def tearDown(self):
        pass

    def test_player_Dude(self):
        try:
            player = self.api.get_player('#200JUQP')
            assert player.tag == '#200JUQP'
            assert player.name == 'Dude'
            assert player.explevel >= 13
            assert player.trophies >= 4000
            assert player.best_trophies >= 4000
            assert player.wins >= 7000
            assert player.losses >= 7000
            assert player.battle_count >= 20000
            assert player.role.lower() in ['President', 'vicepresident', 'Vice-President', 'member']
            assert player.donations >= 0
            assert player.donations_received >= 0
            assert player.Club.tag == '#RLUP2C'
            assert player.Club.name == '18Plussers'
            assert player.Club.badge_id >= 16000000
            assert len(player.badges) > 5
            assert len(player.achievements) > 5
            assert len(player.cards) > 50
            assert len(player.current_favourite_card.name) > 2
            assert player.current_favourite_card.id >= 26000000
            assert player.current_favourite_card.max_level > 4
            assert player.current_favourite_card.icon_urls.medium.startswith('https://')
            assert player.star_points >= 0

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player(): %s\n" % e)
            assert False

    def test_player_Dude_battle_log(self):
        try:
            battles = self.api.get_player_battles('#200JUQP')

            assert len(battles) >= 1

            battle = battles[0]

            assert battle.type in ['PvP', 'clubWarWarDay', 'clubWarCollectionDay', 'challenge']

            assert len(battle.team) >= 1
            assert len(battle.opponent) >= 1
            assert battle.game_mode.id >= 72000000
            assert len(battle.game_mode.name) >= 2

        except ApiException as e:
            print("Exception when calling PlayersApi.get_player_battles(): %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()