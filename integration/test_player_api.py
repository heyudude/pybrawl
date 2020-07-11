import unittest

import config

import pybrawl
from pybrawl.rest import ApiException

configuration = config.getConfiguration()

class TestPlayersApi(unittest.TestCase):
    def foo(self):
        print('foo')

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.PlayersApi(pybrawl.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_player_Dude(self):
        try:
            player = self.api.get_player('#200JUQP')
            assert player.tag == '#200JUQP'
            assert player.name == 'Dude'
            assert player.exp_level >= 13
            assert player.trophies >= 4000
            assert player.best_trophies >= 4000
            assert player.wins >= 7000
            assert player.losses >= 7000
            assert player.battle_count >= 20000
            assert player.role.lower() in ['leader', 'coleader', 'elder', 'member']
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

a = TestPlayersApi()
a.setUp()
a.test_player_Dude()
a.foo()