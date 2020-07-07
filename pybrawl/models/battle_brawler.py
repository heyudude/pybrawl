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


class BattleBrawler(object):
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
        'id': 'str',
        'name': 'str',
        'power': 'int',
        'trophies': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'power': 'power',
        'trophies': 'trophies'
    }

    def __init__(self, id=None, name=None, power=None, trophies=None, local_vars_configuration=None):  # noqa: E501
        """BattleBrawler - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._power = None
        self._trophies = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if power is not None:
            self.power = power
        if trophies is not None:
            self.trophies = trophies

    @property
    def id(self):
        """Gets the id of this BattleBrawler.  # noqa: E501


        :return: The id of this BattleBrawler.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BattleBrawler.


        :param id: The id of this BattleBrawler.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BattleBrawler.  # noqa: E501


        :return: The name of this BattleBrawler.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BattleBrawler.


        :param name: The name of this BattleBrawler.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def power(self):
        """Gets the power of this BattleBrawler.  # noqa: E501


        :return: The power of this BattleBrawler.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this BattleBrawler.


        :param power: The power of this BattleBrawler.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def trophies(self):
        """Gets the trophies of this BattleBrawler.  # noqa: E501


        :return: The trophies of this BattleBrawler.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this BattleBrawler.


        :param trophies: The trophies of this BattleBrawler.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

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
        if not isinstance(other, BattleBrawler):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BattleBrawler):
            return True

        return self.to_dict() != other.to_dict()
