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


class Event(object):
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
        'id': 'int',
        'mode': 'str',
        'map': 'str',
        'battle': 'list[Battle]'
    }

    attribute_map = {
        'id': 'id',
        'mode': 'mode',
        'map': 'map',
        'battle': 'battle'
    }

    def __init__(self, id=None, mode=None, map=None, battle=None, local_vars_configuration=None):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._mode = None
        self._map = None
        self._battle = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mode is not None:
            self.mode = mode
        if map is not None:
            self.map = map
        if battle is not None:
            self.battle = battle

    @property
    def id(self):
        """Gets the id of this Event.  # noqa: E501


        :return: The id of this Event.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mode(self):
        """Gets the mode of this Event.  # noqa: E501


        :return: The mode of this Event.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Event.


        :param mode: The mode of this Event.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def map(self):
        """Gets the map of this Event.  # noqa: E501


        :return: The map of this Event.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this Event.


        :param map: The map of this Event.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def battle(self):
        """Gets the battle of this Event.  # noqa: E501


        :return: The battle of this Event.  # noqa: E501
        :rtype: list[Battle]
        """
        return self._battle

    @battle.setter
    def battle(self, battle):
        """Sets the battle of this Event.


        :param battle: The battle of this Event.  # noqa: E501
        :type: list[Battle]
        """

        self._battle = battle

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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
