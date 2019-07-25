# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class LocationList(object):
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
        'items': 'list[Location]',
        'paging': 'SearchPaging'
    }

    attribute_map = {
        'items': 'items',
        'paging': 'paging'
    }

    def __init__(self, items=None, paging=None):  # noqa: E501
        """LocationList - a model defined in OpenAPI"""  # noqa: E501

        self._items = None
        self._paging = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if paging is not None:
            self.paging = paging

    @property
    def items(self):
        """Gets the items of this LocationList.  # noqa: E501


        :return: The items of this LocationList.  # noqa: E501
        :rtype: list[Location]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this LocationList.


        :param items: The items of this LocationList.  # noqa: E501
        :type: list[Location]
        """

        self._items = items

    @property
    def paging(self):
        """Gets the paging of this LocationList.  # noqa: E501


        :return: The paging of this LocationList.  # noqa: E501
        :rtype: SearchPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this LocationList.


        :param paging: The paging of this LocationList.  # noqa: E501
        :type: SearchPaging
        """

        self._paging = paging

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
        if not isinstance(other, LocationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
