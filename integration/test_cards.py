import unittest

import config

import pybrawl
from pybrawl.rest import ApiException


class TestCardsApi(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        self.api = pybrawl.CardsApi(pybrawl.ApiClient(config.getConfiguration()))
        pass

    def tearDown(self):
        pass

    def test_cards(self):
        try:
            # Get list of available cards
            cardList = self.api.get_cards()
            #print(cardList)
            assert type(cardList.items) == list
            for card in cardList.items:
                if card.id == '26000000':
                    assert card.name == 'Knight'
                    assert card.max_level == 13
        except ApiException as e:
            print("Exception when calling CardsApi->get_cards: %s\n" % e)
            assert False

if __name__ == '__main__':
    unittest.main()
