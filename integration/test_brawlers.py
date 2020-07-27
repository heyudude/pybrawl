import unittest

import config

import pybrawl
from pybrawl.rest import ApiException

class TestBrawlersApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.PlayersApi(pybrawl.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_brawlers(self):
        try:
            # Get list of available brawlers
            brawlerList = self.api.get_brawlers()
            #print(brawlerList)
            assert type(brawlerList.items) == list
            for brawler in brawlerList.items:
                if brawler.id == '26000000':
                    assert brawler.name == 'Bo'
                    assert brawler.power == 7
        except ApiException as e:
            print("Exception when calling BrawlersApi->get_brawlers: %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()
