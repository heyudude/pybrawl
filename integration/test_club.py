import unittest

import config

import pybrawl
from pybrawl.rest import ApiException

configuration = config.getConfiguration()

class TestClubsApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.ClubsApi(pybrawl.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_club_agrassar(self):
        try:
            Club = self.api.get_club('#JY8YVV')
            assert Club.club_war_trophies > 0
            for member in Club.member_list:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'AaronTraas'
                    assert member.exp_level >= 13
                    assert member.trophies >= 4000
                    assert member.arena.id >= 54000000
                    assert member.role.lower() in ['leader', 'coleader', 'elder', 'member']
                    assert member.club_rank in range(1,50)
                    assert member.previous_club_rank in range(1,50)
                    assert member.donations >= 0
                    assert member.donations_received >= 0
                    assert member.club_chest_points >= 0

        except ApiException as e:
            print("Exception when calling CardsClub->get_club: %s\n" % e)
            assert False


    def test_club_agrassar_members(self):
        try:
            members = self.api.get_club_members('#JY8YVV')
            for member in members.items:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'AaronTraas'
                    assert member.exp_level >= 13
                    assert member.trophies >= 4000
                    assert member.arena.id >= 54000000
                    assert member.role.lower() in ['leader', 'coleader', 'elder', 'member']
                    assert member.club_rank in range(1,50)
                    assert member.previous_club_rank in range(1,50)
                    assert member.donations >= 0
                    assert member.donations_received >= 0
                    assert member.club_chest_points >= 0

        except ApiException as e:
            print("Exception when calling CardsClub->get_club_members: %s\n" % e)
            assert False

    def test_club_agrassar_warlog(self):
        try:
            warlog = self.api.get_club_war_log('#JY8YVV')
            assert len(warlog.items) in range(0,11)
            for war in warlog.items:
                assert war.season_id > 0
                assert len(war.participants) in range(1,50)
                assert len(war.standings) in range(1,50)
                for standing in war.standings:
                    if standing.Club.tag == '#JY8YVV':
                        assert standing.Club.name.lower() == 'agrassar'
                    assert standing.Club.badge_id > 0
                    assert standing.Club.club_score >= 0
                    assert standing.Club.participants in range(1,50)
                    assert standing.Club.battles_played in range(0,50)
                    assert standing.Club.wins >= 0
                    assert standing.Club.crowns >= 0

        except ApiException as e:
            print("Exception when calling CardsClub->get_club_members: %s\n" % e)
            assert False

    def test_club_agrassar_current_war(self):
        try:
            war = self.api.get_current_war('#JY8YVV')
            assert war.state in ['notInWar','collectionDay','warDay']

        except ApiException as e:
            print("Exception when calling CardsClub->get_club_members: %s\n" % e)
            assert False

    def test_club_search_agrassar(self):
        try:
            clubs = self.api.search_clubs(name='agrassar')
            assert len(clubs.items) >= 1
            found = False
            for Club in clubs.items:
                if Club.tag == '#JY8YVV':
                    assert Club.name == 'Agrassar'
                    found = True
            assert found

        except ApiException as e:
            print("Exception when calling CardsClub->get_club_members: %s\n" % e)
            assert False

