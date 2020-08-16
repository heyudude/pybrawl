# coding: utf-8

"""
    Brawl_Stars_API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/heyudude/brawlstars-swagger
"""


import pprint
import re  # noqa: F401

import six

from pybrawl.configuration import Configuration


class RankingClubList(object):
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
        'trophies': 'int',
        'rank': 'int',
        'membercount': 'int',
        'paging': 'SearchPaging'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'trophies': 'trophies',
        'rank': 'rank',
        'membercount': 'membercount',
        'paging': 'paging'
    }

    def __init__(self, tag=None, name=None, trophies=None, rank=None, membercount=None, paging=None, local_vars_configuration=None):  # noqa: E501
        """RankingClubList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._name = None
        self._trophies = None
        self._rank = None
        self._membercount = None
        self._paging = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if trophies is not None:
            self.trophies = trophies
        if rank is not None:
            self.rank = rank
        if membercount is not None:
            self.membercount = membercount
        if paging is not None:
            self.paging = paging

    @property
    def tag(self):
        """Gets the tag of this RankingClubList.  # noqa: E501


        :return: The tag of this RankingClubList.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this RankingClubList.


        :param tag: The tag of this RankingClubList.  # noqa: E501
        :type tag: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this RankingClubList.  # noqa: E501


        :return: The name of this RankingClubList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RankingClubList.


        :param name: The name of this RankingClubList.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def trophies(self):
        """Gets the trophies of this RankingClubList.  # noqa: E501


        :return: The trophies of this RankingClubList.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this RankingClubList.


        :param trophies: The trophies of this RankingClubList.  # noqa: E501
        :type trophies: int
        """

        self._trophies = trophies

    @property
    def rank(self):
        """Gets the rank of this RankingClubList.  # noqa: E501


        :return: The rank of this RankingClubList.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this RankingClubList.


        :param rank: The rank of this RankingClubList.  # noqa: E501
        :type rank: int
        """

        self._rank = rank

    @property
    def membercount(self):
        """Gets the membercount of this RankingClubList.  # noqa: E501


        :return: The membercount of this RankingClubList.  # noqa: E501
        :rtype: int
        """
        return self._membercount

    @membercount.setter
    def membercount(self, membercount):
        """Sets the membercount of this RankingClubList.


        :param membercount: The membercount of this RankingClubList.  # noqa: E501
        :type membercount: int
        """

        self._membercount = membercount

    @property
    def paging(self):
        """Gets the paging of this RankingClubList.  # noqa: E501


        :return: The paging of this RankingClubList.  # noqa: E501
        :rtype: SearchPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this RankingClubList.


        :param paging: The paging of this RankingClubList.  # noqa: E501
        :type paging: SearchPaging
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
        if not isinstance(other, RankingClubList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RankingClubList):
            return True

        return self.to_dict() != other.to_dict()
