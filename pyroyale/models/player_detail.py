# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from pyroyale.models.arena import Arena  # noqa: F401,E501
from pyroyale.models.clan_base import ClanBase  # noqa: F401,E501
from pyroyale.models.player_base import PlayerBase  # noqa: F401,E501
from pyroyale.models.player_detail_achievements import PlayerDetailAchievements  # noqa: F401,E501
from pyroyale.models.player_detail_cards import PlayerDetailCards  # noqa: F401,E501
from pyroyale.models.player_detail_current_favourite_card import PlayerDetailCurrentFavouriteCard  # noqa: F401,E501
from pyroyale.models.player_detail_league_statistics import PlayerDetailLeagueStatistics  # noqa: F401,E501


class PlayerDetail(PlayerBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'best_trophies': 'int',
        'wins': 'int',
        'losses': 'int',
        'battle_count': 'int',
        'three_crown_wins': 'int',
        'challenge_cards_won': 'int',
        'challenge_max_wins': 'int',
        'tournament_cards_won': 'int',
        'tournament_battle_count': 'int',
        'role': 'str',
        'donations': 'int',
        'donations_received': 'int',
        'total_donations': 'int',
        'war_day_wins': 'int',
        'clan_cards_collected': 'int',
        'clan': 'ClanBase',
        'arena': 'Arena',
        'league_statistics': 'PlayerDetailLeagueStatistics',
        'achievements': 'list[PlayerDetailAchievements]',
        'cards': 'list[PlayerDetailCards]',
        'current_favourite_card': 'PlayerDetailCurrentFavouriteCard'
    }

    attribute_map = {
        'best_trophies': 'bestTrophies',
        'wins': 'wins',
        'losses': 'losses',
        'battle_count': 'battleCount',
        'three_crown_wins': 'threeCrownWins',
        'challenge_cards_won': 'challengeCardsWon',
        'challenge_max_wins': 'challengeMaxWins',
        'tournament_cards_won': 'tournamentCardsWon',
        'tournament_battle_count': 'tournamentBattleCount',
        'role': 'role',
        'donations': 'donations',
        'donations_received': 'donationsReceived',
        'total_donations': 'totalDonations',
        'war_day_wins': 'warDayWins',
        'clan_cards_collected': 'clanCardsCollected',
        'clan': 'clan',
        'arena': 'arena',
        'league_statistics': 'leagueStatistics',
        'achievements': 'achievements',
        'cards': 'cards',
        'current_favourite_card': 'currentFavouriteCard'
    }

    def __init__(self, best_trophies=None, wins=None, losses=None, battle_count=None, three_crown_wins=None, challenge_cards_won=None, challenge_max_wins=None, tournament_cards_won=None, tournament_battle_count=None, role=None, donations=None, donations_received=None, total_donations=None, war_day_wins=None, clan_cards_collected=None, clan=None, arena=None, league_statistics=None, achievements=None, cards=None, current_favourite_card=None):  # noqa: E501
        """PlayerDetail - a model defined in Swagger"""  # noqa: E501
        self._best_trophies = None
        self._wins = None
        self._losses = None
        self._battle_count = None
        self._three_crown_wins = None
        self._challenge_cards_won = None
        self._challenge_max_wins = None
        self._tournament_cards_won = None
        self._tournament_battle_count = None
        self._role = None
        self._donations = None
        self._donations_received = None
        self._total_donations = None
        self._war_day_wins = None
        self._clan_cards_collected = None
        self._clan = None
        self._arena = None
        self._league_statistics = None
        self._achievements = None
        self._cards = None
        self._current_favourite_card = None
        self.discriminator = None
        if best_trophies is not None:
            self.best_trophies = best_trophies
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if battle_count is not None:
            self.battle_count = battle_count
        if three_crown_wins is not None:
            self.three_crown_wins = three_crown_wins
        if challenge_cards_won is not None:
            self.challenge_cards_won = challenge_cards_won
        if challenge_max_wins is not None:
            self.challenge_max_wins = challenge_max_wins
        if tournament_cards_won is not None:
            self.tournament_cards_won = tournament_cards_won
        if tournament_battle_count is not None:
            self.tournament_battle_count = tournament_battle_count
        if role is not None:
            self.role = role
        if donations is not None:
            self.donations = donations
        if donations_received is not None:
            self.donations_received = donations_received
        if total_donations is not None:
            self.total_donations = total_donations
        if war_day_wins is not None:
            self.war_day_wins = war_day_wins
        if clan_cards_collected is not None:
            self.clan_cards_collected = clan_cards_collected
        if clan is not None:
            self.clan = clan
        if arena is not None:
            self.arena = arena
        if league_statistics is not None:
            self.league_statistics = league_statistics
        if achievements is not None:
            self.achievements = achievements
        if cards is not None:
            self.cards = cards
        if current_favourite_card is not None:
            self.current_favourite_card = current_favourite_card

    @property
    def best_trophies(self):
        """Gets the best_trophies of this PlayerDetail.  # noqa: E501


        :return: The best_trophies of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._best_trophies

    @best_trophies.setter
    def best_trophies(self, best_trophies):
        """Sets the best_trophies of this PlayerDetail.


        :param best_trophies: The best_trophies of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._best_trophies = best_trophies

    @property
    def wins(self):
        """Gets the wins of this PlayerDetail.  # noqa: E501


        :return: The wins of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this PlayerDetail.


        :param wins: The wins of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this PlayerDetail.  # noqa: E501


        :return: The losses of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this PlayerDetail.


        :param losses: The losses of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def battle_count(self):
        """Gets the battle_count of this PlayerDetail.  # noqa: E501


        :return: The battle_count of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._battle_count

    @battle_count.setter
    def battle_count(self, battle_count):
        """Sets the battle_count of this PlayerDetail.


        :param battle_count: The battle_count of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._battle_count = battle_count

    @property
    def three_crown_wins(self):
        """Gets the three_crown_wins of this PlayerDetail.  # noqa: E501


        :return: The three_crown_wins of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._three_crown_wins

    @three_crown_wins.setter
    def three_crown_wins(self, three_crown_wins):
        """Sets the three_crown_wins of this PlayerDetail.


        :param three_crown_wins: The three_crown_wins of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._three_crown_wins = three_crown_wins

    @property
    def challenge_cards_won(self):
        """Gets the challenge_cards_won of this PlayerDetail.  # noqa: E501


        :return: The challenge_cards_won of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._challenge_cards_won

    @challenge_cards_won.setter
    def challenge_cards_won(self, challenge_cards_won):
        """Sets the challenge_cards_won of this PlayerDetail.


        :param challenge_cards_won: The challenge_cards_won of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._challenge_cards_won = challenge_cards_won

    @property
    def challenge_max_wins(self):
        """Gets the challenge_max_wins of this PlayerDetail.  # noqa: E501


        :return: The challenge_max_wins of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._challenge_max_wins

    @challenge_max_wins.setter
    def challenge_max_wins(self, challenge_max_wins):
        """Sets the challenge_max_wins of this PlayerDetail.


        :param challenge_max_wins: The challenge_max_wins of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._challenge_max_wins = challenge_max_wins

    @property
    def tournament_cards_won(self):
        """Gets the tournament_cards_won of this PlayerDetail.  # noqa: E501


        :return: The tournament_cards_won of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._tournament_cards_won

    @tournament_cards_won.setter
    def tournament_cards_won(self, tournament_cards_won):
        """Sets the tournament_cards_won of this PlayerDetail.


        :param tournament_cards_won: The tournament_cards_won of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._tournament_cards_won = tournament_cards_won

    @property
    def tournament_battle_count(self):
        """Gets the tournament_battle_count of this PlayerDetail.  # noqa: E501


        :return: The tournament_battle_count of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._tournament_battle_count

    @tournament_battle_count.setter
    def tournament_battle_count(self, tournament_battle_count):
        """Sets the tournament_battle_count of this PlayerDetail.


        :param tournament_battle_count: The tournament_battle_count of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._tournament_battle_count = tournament_battle_count

    @property
    def role(self):
        """Gets the role of this PlayerDetail.  # noqa: E501


        :return: The role of this PlayerDetail.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PlayerDetail.


        :param role: The role of this PlayerDetail.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def donations(self):
        """Gets the donations of this PlayerDetail.  # noqa: E501


        :return: The donations of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._donations

    @donations.setter
    def donations(self, donations):
        """Sets the donations of this PlayerDetail.


        :param donations: The donations of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._donations = donations

    @property
    def donations_received(self):
        """Gets the donations_received of this PlayerDetail.  # noqa: E501


        :return: The donations_received of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._donations_received

    @donations_received.setter
    def donations_received(self, donations_received):
        """Sets the donations_received of this PlayerDetail.


        :param donations_received: The donations_received of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._donations_received = donations_received

    @property
    def total_donations(self):
        """Gets the total_donations of this PlayerDetail.  # noqa: E501


        :return: The total_donations of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._total_donations

    @total_donations.setter
    def total_donations(self, total_donations):
        """Sets the total_donations of this PlayerDetail.


        :param total_donations: The total_donations of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._total_donations = total_donations

    @property
    def war_day_wins(self):
        """Gets the war_day_wins of this PlayerDetail.  # noqa: E501


        :return: The war_day_wins of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._war_day_wins

    @war_day_wins.setter
    def war_day_wins(self, war_day_wins):
        """Sets the war_day_wins of this PlayerDetail.


        :param war_day_wins: The war_day_wins of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._war_day_wins = war_day_wins

    @property
    def clan_cards_collected(self):
        """Gets the clan_cards_collected of this PlayerDetail.  # noqa: E501


        :return: The clan_cards_collected of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._clan_cards_collected

    @clan_cards_collected.setter
    def clan_cards_collected(self, clan_cards_collected):
        """Sets the clan_cards_collected of this PlayerDetail.


        :param clan_cards_collected: The clan_cards_collected of this PlayerDetail.  # noqa: E501
        :type: int
        """

        self._clan_cards_collected = clan_cards_collected

    @property
    def clan(self):
        """Gets the clan of this PlayerDetail.  # noqa: E501


        :return: The clan of this PlayerDetail.  # noqa: E501
        :rtype: ClanBase
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this PlayerDetail.


        :param clan: The clan of this PlayerDetail.  # noqa: E501
        :type: ClanBase
        """

        self._clan = clan

    @property
    def arena(self):
        """Gets the arena of this PlayerDetail.  # noqa: E501


        :return: The arena of this PlayerDetail.  # noqa: E501
        :rtype: Arena
        """
        return self._arena

    @arena.setter
    def arena(self, arena):
        """Sets the arena of this PlayerDetail.


        :param arena: The arena of this PlayerDetail.  # noqa: E501
        :type: Arena
        """

        self._arena = arena

    @property
    def league_statistics(self):
        """Gets the league_statistics of this PlayerDetail.  # noqa: E501


        :return: The league_statistics of this PlayerDetail.  # noqa: E501
        :rtype: PlayerDetailLeagueStatistics
        """
        return self._league_statistics

    @league_statistics.setter
    def league_statistics(self, league_statistics):
        """Sets the league_statistics of this PlayerDetail.


        :param league_statistics: The league_statistics of this PlayerDetail.  # noqa: E501
        :type: PlayerDetailLeagueStatistics
        """

        self._league_statistics = league_statistics

    @property
    def achievements(self):
        """Gets the achievements of this PlayerDetail.  # noqa: E501


        :return: The achievements of this PlayerDetail.  # noqa: E501
        :rtype: list[PlayerDetailAchievements]
        """
        return self._achievements

    @achievements.setter
    def achievements(self, achievements):
        """Sets the achievements of this PlayerDetail.


        :param achievements: The achievements of this PlayerDetail.  # noqa: E501
        :type: list[PlayerDetailAchievements]
        """

        self._achievements = achievements

    @property
    def cards(self):
        """Gets the cards of this PlayerDetail.  # noqa: E501


        :return: The cards of this PlayerDetail.  # noqa: E501
        :rtype: list[PlayerDetailCards]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this PlayerDetail.


        :param cards: The cards of this PlayerDetail.  # noqa: E501
        :type: list[PlayerDetailCards]
        """

        self._cards = cards

    @property
    def current_favourite_card(self):
        """Gets the current_favourite_card of this PlayerDetail.  # noqa: E501


        :return: The current_favourite_card of this PlayerDetail.  # noqa: E501
        :rtype: PlayerDetailCurrentFavouriteCard
        """
        return self._current_favourite_card

    @current_favourite_card.setter
    def current_favourite_card(self, current_favourite_card):
        """Sets the current_favourite_card of this PlayerDetail.


        :param current_favourite_card: The current_favourite_card of this PlayerDetail.  # noqa: E501
        :type: PlayerDetailCurrentFavouriteCard
        """

        self._current_favourite_card = current_favourite_card

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlayerDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
