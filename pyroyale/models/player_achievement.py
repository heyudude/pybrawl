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


class PlayerAchievement(object):
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
        'name': 'str',
        'stars': 'int',
        'value': 'int',
        'target': 'int',
        'info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'stars': 'stars',
        'value': 'value',
        'target': 'target',
        'info': 'info'
    }

    def __init__(self, name=None, stars=None, value=None, target=None, info=None):  # noqa: E501
        """PlayerAchievement - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._stars = None
        self._value = None
        self._target = None
        self._info = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if stars is not None:
            self.stars = stars
        if value is not None:
            self.value = value
        if target is not None:
            self.target = target
        if info is not None:
            self.info = info

    @property
    def name(self):
        """Gets the name of this PlayerAchievement.  # noqa: E501


        :return: The name of this PlayerAchievement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerAchievement.


        :param name: The name of this PlayerAchievement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def stars(self):
        """Gets the stars of this PlayerAchievement.  # noqa: E501


        :return: The stars of this PlayerAchievement.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this PlayerAchievement.


        :param stars: The stars of this PlayerAchievement.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def value(self):
        """Gets the value of this PlayerAchievement.  # noqa: E501


        :return: The value of this PlayerAchievement.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PlayerAchievement.


        :param value: The value of this PlayerAchievement.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def target(self):
        """Gets the target of this PlayerAchievement.  # noqa: E501


        :return: The target of this PlayerAchievement.  # noqa: E501
        :rtype: int
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this PlayerAchievement.


        :param target: The target of this PlayerAchievement.  # noqa: E501
        :type: int
        """

        self._target = target

    @property
    def info(self):
        """Gets the info of this PlayerAchievement.  # noqa: E501


        :return: The info of this PlayerAchievement.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this PlayerAchievement.


        :param info: The info of this PlayerAchievement.  # noqa: E501
        :type: str
        """

        self._info = info

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
        if issubclass(PlayerAchievement, dict):
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
        if not isinstance(other, PlayerAchievement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other