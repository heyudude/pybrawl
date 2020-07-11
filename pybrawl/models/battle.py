# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pybrawl.configuration import Configuration


class Battle(object):
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
        'mode': 'str',
        'type': 'str',
        'result': 'str',
        'duration': 'int',
        'trophy_change': 'int',
        'star_player': 'list[StarPlayer]',
        'teams': 'list[Teams]'
    }

    attribute_map = {
        'mode': 'mode',
        'type': 'type',
        'result': 'result',
        'duration': 'duration',
        'trophy_change': 'trophyChange',
        'star_player': 'starPlayer',
        'teams': 'teams'
    }

    def __init__(self, mode=None, type=None, result=None, duration=None, trophy_change=None, star_player=None, teams=None, local_vars_configuration=None):  # noqa: E501
        """Battle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mode = None
        self._type = None
        self._result = None
        self._duration = None
        self._trophy_change = None
        self._star_player = None
        self._teams = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if type is not None:
            self.type = type
        if result is not None:
            self.result = result
        if duration is not None:
            self.duration = duration
        if trophy_change is not None:
            self.trophy_change = trophy_change
        if star_player is not None:
            self.star_player = star_player
        if teams is not None:
            self.teams = teams

    @property
    def mode(self):
        """Gets the mode of this Battle.  # noqa: E501


        :return: The mode of this Battle.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Battle.


        :param mode: The mode of this Battle.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def type(self):
        """Gets the type of this Battle.  # noqa: E501


        :return: The type of this Battle.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Battle.


        :param type: The type of this Battle.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def result(self):
        """Gets the result of this Battle.  # noqa: E501


        :return: The result of this Battle.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Battle.


        :param result: The result of this Battle.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def duration(self):
        """Gets the duration of this Battle.  # noqa: E501


        :return: The duration of this Battle.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Battle.


        :param duration: The duration of this Battle.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def trophy_change(self):
        """Gets the trophy_change of this Battle.  # noqa: E501


        :return: The trophy_change of this Battle.  # noqa: E501
        :rtype: int
        """
        return self._trophy_change

    @trophy_change.setter
    def trophy_change(self, trophy_change):
        """Sets the trophy_change of this Battle.


        :param trophy_change: The trophy_change of this Battle.  # noqa: E501
        :type: int
        """

        self._trophy_change = trophy_change

    @property
    def star_player(self):
        """Gets the star_player of this Battle.  # noqa: E501


        :return: The star_player of this Battle.  # noqa: E501
        :rtype: list[StarPlayer]
        """
        return self._star_player

    @star_player.setter
    def star_player(self, star_player):
        """Sets the star_player of this Battle.


        :param star_player: The star_player of this Battle.  # noqa: E501
        :type: list[StarPlayer]
        """

        self._star_player = star_player

    @property
    def teams(self):
        """Gets the teams of this Battle.  # noqa: E501


        :return: The teams of this Battle.  # noqa: E501
        :rtype: list[Teams]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Battle.


        :param teams: The teams of this Battle.  # noqa: E501
        :type: list[Teams]
        """

        self._teams = teams

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
        if not isinstance(other, Battle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Battle):
            return True

        return self.to_dict() != other.to_dict()
