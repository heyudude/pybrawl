from dateutil.parser import parse
import unittest

import config

import pybrawl
from pybrawl.rest import ApiException

configuration = config.getConfiguration()

class TestTournamentsApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.TournamentsApi(pybrawl.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_search_tournaments(self):
        tournaments = self.api.search_tournaments(name="a", limit="1").items

        assert len(tournaments) == 1

        tournament = tournaments[0]

        assert tournament.tag.startswith('#')
        assert tournament.type in ['open', 'passwordProtected']
        assert tournament.status in ['inProgress']
        assert isinstance(tournament.level_cap, int)
        assert isinstance(tournament.first_place_brawler_prize, int)
        assert isinstance(tournament.capacity, int)
        assert isinstance(tournament.max_capacity, int)
        assert tournament.capacity <= tournament.max_capacity
        assert isinstance(tournament.preparation_duration, int)
        assert isinstance(tournament.duration, int)
        assert tournament.created_time.startswith('20')
        try:
            parse(tournament.created_time)
            assert True
        except ValueError:
            assert False

        assert isinstance(tournament.game_mode.id, int)
        
if __name__ == '__main__':
    unittest.main()