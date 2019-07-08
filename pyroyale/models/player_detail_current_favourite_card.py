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
from pyroyale.models.player_detail_icon_urls import PlayerDetailIconUrls  # noqa: F401,E501


class PlayerDetailCurrentFavouriteCard(object):
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
        'id': 'int',
        'max_level': 'int',
        'icon_urls': 'PlayerDetailIconUrls'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'max_level': 'maxLevel',
        'icon_urls': 'iconUrls'
    }

    def __init__(self, name=None, id=None, max_level=None, icon_urls=None):  # noqa: E501
        """PlayerDetailCurrentFavouriteCard - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._max_level = None
        self._icon_urls = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if max_level is not None:
            self.max_level = max_level
        if icon_urls is not None:
            self.icon_urls = icon_urls

    @property
    def name(self):
        """Gets the name of this PlayerDetailCurrentFavouriteCard.  # noqa: E501


        :return: The name of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerDetailCurrentFavouriteCard.


        :param name: The name of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this PlayerDetailCurrentFavouriteCard.  # noqa: E501


        :return: The id of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayerDetailCurrentFavouriteCard.


        :param id: The id of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_level(self):
        """Gets the max_level of this PlayerDetailCurrentFavouriteCard.  # noqa: E501


        :return: The max_level of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this PlayerDetailCurrentFavouriteCard.


        :param max_level: The max_level of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def icon_urls(self):
        """Gets the icon_urls of this PlayerDetailCurrentFavouriteCard.  # noqa: E501


        :return: The icon_urls of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :rtype: PlayerDetailIconUrls
        """
        return self._icon_urls

    @icon_urls.setter
    def icon_urls(self, icon_urls):
        """Sets the icon_urls of this PlayerDetailCurrentFavouriteCard.


        :param icon_urls: The icon_urls of this PlayerDetailCurrentFavouriteCard.  # noqa: E501
        :type: PlayerDetailIconUrls
        """

        self._icon_urls = icon_urls

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
        if issubclass(PlayerDetailCurrentFavouriteCard, dict):
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
        if not isinstance(other, PlayerDetailCurrentFavouriteCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
