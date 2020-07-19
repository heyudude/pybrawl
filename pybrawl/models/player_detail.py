# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/heyudude/brawlstars-swagger
"""


import pprint
import re  # noqa: F401

import six

from pybrawl.configuration import Configuration


class PlayerDetail(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'tag': 'str',
        'name': 'str',
        'name_color': 'list[object]',
        'icon': 'str',
        'trophies': 'int',
        'highest_trophies': 'int',
        'highest_power_play_points': 'int',
        'exp_level': 'int',
        'exp_points': 'int',
        'is_qualified_from_championship_challenge': 'bool',
        '_3vs3_victories': 'int',
        'solo_victories': 'int',
        'duo_victories': 'int',
        'best_robo_rumble_time': 'int',
        'best_time_as_big_brawler': 'int',
        'club': 'ClubBase',
        'brawlers': 'list[Brawler]'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'name_color': 'nameColor',
        'icon': 'icon',
        'trophies': 'trophies',
        'highest_trophies': 'highestTrophies',
        'highest_power_play_points': 'highestPowerPlayPoints',
        'exp_level': 'expLevel',
        'exp_points': 'expPoints',
        'is_qualified_from_championship_challenge': 'isQualifiedFromChampionshipChallenge',
        '_3vs3_victories': '3vs3Victories',
        'solo_victories': 'soloVictories',
        'duo_victories': 'duoVictories',
        'best_robo_rumble_time': 'bestRoboRumbleTime',
        'best_time_as_big_brawler': 'bestTimeAsBigBrawler',
        'club': 'club',
        'brawlers': 'brawlers'
    }

    def __init__(self, tag=None, name=None, name_color=None, icon=None, trophies=None, highest_trophies=None, highest_power_play_points=None, exp_level=None, exp_points=None, is_qualified_from_championship_challenge=None, _3vs3_victories=None, solo_victories=None, duo_victories=None, best_robo_rumble_time=None, best_time_as_big_brawler=None, club=None, brawlers=None, local_vars_configuration=None):  # noqa: E501
        """PlayerDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._name = None
        self._name_color = None
        self._icon = None
        self._trophies = None
        self._highest_trophies = None
        self._highest_power_play_points = None
        self._exp_level = None
        self._exp_points = None
        self._is_qualified_from_championship_challenge = None
        self.__3vs3_victories = None
        self._solo_victories = None
        self._duo_victories = None
        self._best_robo_rumble_time = None
        self._best_time_as_big_brawler = None
        self._club = None
        self._brawlers = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if name_color is not None:
            self.name_color = name_color
        if icon is not None:
            self.icon = icon
        if trophies is not None:
            self.trophies = trophies
        if highest_trophies is not None:
            self.highest_trophies = highest_trophies
        if highest_power_play_points is not None:
            self.highest_power_play_points = highest_power_play_points
        if exp_level is not None:
            self.exp_level = exp_level
        if exp_points is not None:
            self.exp_points = exp_points
        if is_qualified_from_championship_challenge is not None:
            self.is_qualified_from_championship_challenge = is_qualified_from_championship_challenge
        if _3vs3_victories is not None:
            self._3vs3_victories = _3vs3_victories
        if solo_victories is not None:
            self.solo_victories = solo_victories
        if duo_victories is not None:
            self.duo_victories = duo_victories
        if best_robo_rumble_time is not None:
            self.best_robo_rumble_time = best_robo_rumble_time
        if best_time_as_big_brawler is not None:
            self.best_time_as_big_brawler = best_time_as_big_brawler
        if club is not None:
            self.club = club
        if brawlers is not None:
            self.brawlers = brawlers

    @property
    def tag(self):
        """Gets the tag of this PlayerDetail.  # noqa: E501


        :return: The tag of this PlayerDetail.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerDetail.


        :param tag: The tag of this PlayerDetail.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this PlayerDetail.  # noqa: E501


        :return: The name of this PlayerDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerDetail.


        :param name: The name of this PlayerDetail.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def name_color(self):
        """Gets the name_color of this PlayerDetail.  # noqa: E501


        :return: The name_color of this PlayerDetail.  # noqa: E501
        :rtype: list[object]
        """
        return self._name_color

    @name_color.setter
    def name_color(self, name_color):
        """Sets the name_color of this PlayerDetail.


        :param name_color: The name_color of this PlayerDetail.  # noqa: E501
        :type name_color: list[object]
        """

        self._name_color = name_color

    @property
    def icon(self):
        """Gets the icon of this PlayerDetail.  # noqa: E501


        :return: The icon of this PlayerDetail.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PlayerDetail.


        :param icon: The icon of this PlayerDetail.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def trophies(self):
        """Gets the trophies of this PlayerDetail.  # noqa: E501


        :return: The trophies of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this PlayerDetail.


        :param trophies: The trophies of this PlayerDetail.  # noqa: E501
        :type trophies: int
        """

        self._trophies = trophies

    @property
    def highest_trophies(self):
        """Gets the highest_trophies of this PlayerDetail.  # noqa: E501


        :return: The highest_trophies of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._highest_trophies

    @highest_trophies.setter
    def highest_trophies(self, highest_trophies):
        """Sets the highest_trophies of this PlayerDetail.


        :param highest_trophies: The highest_trophies of this PlayerDetail.  # noqa: E501
        :type highest_trophies: int
        """

        self._highest_trophies = highest_trophies

    @property
    def highest_power_play_points(self):
        """Gets the highest_power_play_points of this PlayerDetail.  # noqa: E501


        :return: The highest_power_play_points of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._highest_power_play_points

    @highest_power_play_points.setter
    def highest_power_play_points(self, highest_power_play_points):
        """Sets the highest_power_play_points of this PlayerDetail.


        :param highest_power_play_points: The highest_power_play_points of this PlayerDetail.  # noqa: E501
        :type highest_power_play_points: int
        """

        self._highest_power_play_points = highest_power_play_points

    @property
    def exp_level(self):
        """Gets the exp_level of this PlayerDetail.  # noqa: E501


        :return: The exp_level of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._exp_level

    @exp_level.setter
    def exp_level(self, exp_level):
        """Sets the exp_level of this PlayerDetail.


        :param exp_level: The exp_level of this PlayerDetail.  # noqa: E501
        :type exp_level: int
        """

        self._exp_level = exp_level

    @property
    def exp_points(self):
        """Gets the exp_points of this PlayerDetail.  # noqa: E501


        :return: The exp_points of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._exp_points

    @exp_points.setter
    def exp_points(self, exp_points):
        """Sets the exp_points of this PlayerDetail.


        :param exp_points: The exp_points of this PlayerDetail.  # noqa: E501
        :type exp_points: int
        """

        self._exp_points = exp_points

    @property
    def is_qualified_from_championship_challenge(self):
        """Gets the is_qualified_from_championship_challenge of this PlayerDetail.  # noqa: E501


        :return: The is_qualified_from_championship_challenge of this PlayerDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_qualified_from_championship_challenge

    @is_qualified_from_championship_challenge.setter
    def is_qualified_from_championship_challenge(self, is_qualified_from_championship_challenge):
        """Sets the is_qualified_from_championship_challenge of this PlayerDetail.


        :param is_qualified_from_championship_challenge: The is_qualified_from_championship_challenge of this PlayerDetail.  # noqa: E501
        :type is_qualified_from_championship_challenge: bool
        """

        self._is_qualified_from_championship_challenge = is_qualified_from_championship_challenge

    @property
    def _3vs3_victories(self):
        """Gets the _3vs3_victories of this PlayerDetail.  # noqa: E501


        :return: The _3vs3_victories of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self.__3vs3_victories

    @_3vs3_victories.setter
    def _3vs3_victories(self, _3vs3_victories):
        """Sets the _3vs3_victories of this PlayerDetail.


        :param _3vs3_victories: The _3vs3_victories of this PlayerDetail.  # noqa: E501
        :type _3vs3_victories: int
        """

        self.__3vs3_victories = _3vs3_victories

    @property
    def solo_victories(self):
        """Gets the solo_victories of this PlayerDetail.  # noqa: E501


        :return: The solo_victories of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._solo_victories

    @solo_victories.setter
    def solo_victories(self, solo_victories):
        """Sets the solo_victories of this PlayerDetail.


        :param solo_victories: The solo_victories of this PlayerDetail.  # noqa: E501
        :type solo_victories: int
        """

        self._solo_victories = solo_victories

    @property
    def duo_victories(self):
        """Gets the duo_victories of this PlayerDetail.  # noqa: E501


        :return: The duo_victories of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._duo_victories

    @duo_victories.setter
    def duo_victories(self, duo_victories):
        """Sets the duo_victories of this PlayerDetail.


        :param duo_victories: The duo_victories of this PlayerDetail.  # noqa: E501
        :type duo_victories: int
        """

        self._duo_victories = duo_victories

    @property
    def best_robo_rumble_time(self):
        """Gets the best_robo_rumble_time of this PlayerDetail.  # noqa: E501


        :return: The best_robo_rumble_time of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._best_robo_rumble_time

    @best_robo_rumble_time.setter
    def best_robo_rumble_time(self, best_robo_rumble_time):
        """Sets the best_robo_rumble_time of this PlayerDetail.


        :param best_robo_rumble_time: The best_robo_rumble_time of this PlayerDetail.  # noqa: E501
        :type best_robo_rumble_time: int
        """

        self._best_robo_rumble_time = best_robo_rumble_time

    @property
    def best_time_as_big_brawler(self):
        """Gets the best_time_as_big_brawler of this PlayerDetail.  # noqa: E501


        :return: The best_time_as_big_brawler of this PlayerDetail.  # noqa: E501
        :rtype: int
        """
        return self._best_time_as_big_brawler

    @best_time_as_big_brawler.setter
    def best_time_as_big_brawler(self, best_time_as_big_brawler):
        """Sets the best_time_as_big_brawler of this PlayerDetail.


        :param best_time_as_big_brawler: The best_time_as_big_brawler of this PlayerDetail.  # noqa: E501
        :type best_time_as_big_brawler: int
        """

        self._best_time_as_big_brawler = best_time_as_big_brawler

    @property
    def club(self):
        """Gets the club of this PlayerDetail.  # noqa: E501


        :return: The club of this PlayerDetail.  # noqa: E501
        :rtype: ClubBase
        """
        return self._club

    @club.setter
    def club(self, club):
        """Sets the club of this PlayerDetail.


        :param club: The club of this PlayerDetail.  # noqa: E501
        :type club: ClubBase
        """

        self._club = club

    @property
    def brawlers(self):
        """Gets the brawlers of this PlayerDetail.  # noqa: E501


        :return: The brawlers of this PlayerDetail.  # noqa: E501
        :rtype: list[Brawler]
        """
        return self._brawlers

    @brawlers.setter
    def brawlers(self, brawlers):
        """Sets the brawlers of this PlayerDetail.


        :param brawlers: The brawlers of this PlayerDetail.  # noqa: E501
        :type brawlers: list[Brawler]
        """

        self._brawlers = brawlers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerDetail):
            return True

        return self.to_dict() != other.to_dict()
