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

    def test_club_test(self):
        try:
            club = self.api.get_club('#RLUP2C')
            assert club.club_war_trophies > 0
            for member in club.member_list:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'Dude'
                    assert member.explevel >= 13
                    assert member.trophies >= 14000
                    assert member.role.lower() in ['President', 'vice president', 'Senior', 'member']
                    assert member.club_rank in range(1,50)

        except ApiException as e:
            print("Exception when calling CardsClub->get_club: %s\n" % e)
            assert False


    def test_club_test_members(self):
        try:
            members = self.api.get_club_members('#RLUP2C')
            for member in members.items:
                if member.tag == '#200JUQP':
                    assert member.name == 'Dude'
                    assert member.explevel >= 1
                    assert member.trophies >= 14000
                    assert member.role.lower() in ['President', 'vice president', 'Senior', 'member']
                    assert member.club_rank in range(1,50)

        except ApiException as e:
            print("Exception when calling BrawlersClub->get_club_members: %s\n" % e)
            assert False
  
    def test_club_search_18plussers(self):
        try:
            clubs = self.api.search_clubs(name='18plussers')
            assert len(clubs.items) >= 1
            found = False
            for Club in clubs.items:
                if Club.tag == '#JY8YVV':
                    assert Club.name == '18Plussers'
                    found = True
            assert found

        except ApiException as e:
            print("Exception when calling BrawlersClub->get_club_members: %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()
