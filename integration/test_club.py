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
            for member in club.members:
                if member.tag == '#9ULGLRCL':
                    assert member.name == 'Dude'
                    assert member.exp_level >= 13
                    assert member.exp_points >= 100
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
                print(member.name)
                if member.tag == '#200JUQP':
                    assert member.name == 'Dude'
                    # assert member.exp_level >= 12
                    # assert member.exp_points >= 100
                    assert member.trophies >= 14000
                    assert member.role.lower() in ['president', 'vicepresident', 'senior', 'member']

        except ApiException as e:
            print("Exception when calling BrawlersClub->get_club_members: %s\n" % e)
            assert False
  
if __name__ == '__main__':
    unittest.main()
