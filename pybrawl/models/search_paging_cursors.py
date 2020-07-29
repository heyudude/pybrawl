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


class SearchPagingCursors(object):
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
        'after': 'str',
        'before': 'str'
    }

    attribute_map = {
        'after': 'after',
        'before': 'before'
    }

    def __init__(self, after=None, before=None, local_vars_configuration=None):  # noqa: E501
        """SearchPagingCursors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._after = None
        self._before = None
        self.discriminator = None

        if after is not None:
            self.after = after
        if before is not None:
            self.before = before

    @property
    def after(self):
        """Gets the after of this SearchPagingCursors.  # noqa: E501


        :return: The after of this SearchPagingCursors.  # noqa: E501
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this SearchPagingCursors.


        :param after: The after of this SearchPagingCursors.  # noqa: E501
        :type after: str
        """

        self._after = after

    @property
    def before(self):
        """Gets the before of this SearchPagingCursors.  # noqa: E501


        :return: The before of this SearchPagingCursors.  # noqa: E501
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this SearchPagingCursors.


        :param before: The before of this SearchPagingCursors.  # noqa: E501
        :type before: str
        """

        self._before = before

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
        if not isinstance(other, SearchPagingCursors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchPagingCursors):
            return True

        return self.to_dict() != other.to_dict()
