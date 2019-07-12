# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from pyroyale.models.game_mode import GameMode  # noqa: F401,E501


class Tournament(object):
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
        'tag': 'str',
        'type': 'str',
        'status': 'str',
        'level_cap': 'int',
        'first_place_card_prize': 'int',
        'creator_tag': 'str',
        'name': 'str',
        'description': 'str',
        'capacity': 'int',
        'max_capacity': 'int',
        'preparation_duration': 'int',
        'duration': 'int',
        'created_time': 'str',
        'game_mode': 'GameMode'
    }

    attribute_map = {
        'tag': 'tag',
        'type': 'type',
        'status': 'status',
        'level_cap': 'levelCap',
        'first_place_card_prize': 'firstPlaceCardPrize',
        'creator_tag': 'creatorTag',
        'name': 'name',
        'description': 'description',
        'capacity': 'capacity',
        'max_capacity': 'maxCapacity',
        'preparation_duration': 'preparationDuration',
        'duration': 'duration',
        'created_time': 'createdTime',
        'game_mode': 'gameMode'
    }

    def __init__(self, tag=None, type=None, status=None, level_cap=None, first_place_card_prize=None, creator_tag=None, name=None, description=None, capacity=None, max_capacity=None, preparation_duration=None, duration=None, created_time=None, game_mode=None):  # noqa: E501
        """Tournament - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._type = None
        self._status = None
        self._level_cap = None
        self._first_place_card_prize = None
        self._creator_tag = None
        self._name = None
        self._description = None
        self._capacity = None
        self._max_capacity = None
        self._preparation_duration = None
        self._duration = None
        self._created_time = None
        self._game_mode = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if level_cap is not None:
            self.level_cap = level_cap
        if first_place_card_prize is not None:
            self.first_place_card_prize = first_place_card_prize
        if creator_tag is not None:
            self.creator_tag = creator_tag
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if capacity is not None:
            self.capacity = capacity
        if max_capacity is not None:
            self.max_capacity = max_capacity
        if preparation_duration is not None:
            self.preparation_duration = preparation_duration
        if duration is not None:
            self.duration = duration
        if created_time is not None:
            self.created_time = created_time
        if game_mode is not None:
            self.game_mode = game_mode

    @property
    def tag(self):
        """Gets the tag of this Tournament.  # noqa: E501


        :return: The tag of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Tournament.


        :param tag: The tag of this Tournament.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this Tournament.  # noqa: E501


        :return: The type of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Tournament.


        :param type: The type of this Tournament.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this Tournament.  # noqa: E501


        :return: The status of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Tournament.


        :param status: The status of this Tournament.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def level_cap(self):
        """Gets the level_cap of this Tournament.  # noqa: E501


        :return: The level_cap of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._level_cap

    @level_cap.setter
    def level_cap(self, level_cap):
        """Sets the level_cap of this Tournament.


        :param level_cap: The level_cap of this Tournament.  # noqa: E501
        :type: int
        """

        self._level_cap = level_cap

    @property
    def first_place_card_prize(self):
        """Gets the first_place_card_prize of this Tournament.  # noqa: E501


        :return: The first_place_card_prize of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._first_place_card_prize

    @first_place_card_prize.setter
    def first_place_card_prize(self, first_place_card_prize):
        """Sets the first_place_card_prize of this Tournament.


        :param first_place_card_prize: The first_place_card_prize of this Tournament.  # noqa: E501
        :type: int
        """

        self._first_place_card_prize = first_place_card_prize

    @property
    def creator_tag(self):
        """Gets the creator_tag of this Tournament.  # noqa: E501


        :return: The creator_tag of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._creator_tag

    @creator_tag.setter
    def creator_tag(self, creator_tag):
        """Sets the creator_tag of this Tournament.


        :param creator_tag: The creator_tag of this Tournament.  # noqa: E501
        :type: str
        """

        self._creator_tag = creator_tag

    @property
    def name(self):
        """Gets the name of this Tournament.  # noqa: E501


        :return: The name of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tournament.


        :param name: The name of this Tournament.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Tournament.  # noqa: E501


        :return: The description of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tournament.


        :param description: The description of this Tournament.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def capacity(self):
        """Gets the capacity of this Tournament.  # noqa: E501


        :return: The capacity of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Tournament.


        :param capacity: The capacity of this Tournament.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def max_capacity(self):
        """Gets the max_capacity of this Tournament.  # noqa: E501


        :return: The max_capacity of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this Tournament.


        :param max_capacity: The max_capacity of this Tournament.  # noqa: E501
        :type: int
        """

        self._max_capacity = max_capacity

    @property
    def preparation_duration(self):
        """Gets the preparation_duration of this Tournament.  # noqa: E501


        :return: The preparation_duration of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._preparation_duration

    @preparation_duration.setter
    def preparation_duration(self, preparation_duration):
        """Sets the preparation_duration of this Tournament.


        :param preparation_duration: The preparation_duration of this Tournament.  # noqa: E501
        :type: int
        """

        self._preparation_duration = preparation_duration

    @property
    def duration(self):
        """Gets the duration of this Tournament.  # noqa: E501


        :return: The duration of this Tournament.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Tournament.


        :param duration: The duration of this Tournament.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def created_time(self):
        """Gets the created_time of this Tournament.  # noqa: E501


        :return: The created_time of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Tournament.


        :param created_time: The created_time of this Tournament.  # noqa: E501
        :type: str
        """

        self._created_time = created_time

    @property
    def game_mode(self):
        """Gets the game_mode of this Tournament.  # noqa: E501


        :return: The game_mode of this Tournament.  # noqa: E501
        :rtype: GameMode
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """Sets the game_mode of this Tournament.


        :param game_mode: The game_mode of this Tournament.  # noqa: E501
        :type: GameMode
        """

        self._game_mode = game_mode

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
        if issubclass(Tournament, dict):
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
        if not isinstance(other, Tournament):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
