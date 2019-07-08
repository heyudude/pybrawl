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
from pyroyale.models.location import Location  # noqa: F401,E501


class ClanRankingListItems(object):
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
        'name': 'str',
        'rank': 'int',
        'previous_rank': 'int',
        'location': 'Location',
        'clan_score': 'int',
        'badge_id': 'int',
        'members': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'rank': 'rank',
        'previous_rank': 'previousRank',
        'location': 'location',
        'clan_score': 'clanScore',
        'badge_id': 'badgeId',
        'members': 'members'
    }

    def __init__(self, tag=None, name=None, rank=None, previous_rank=None, location=None, clan_score=None, badge_id=None, members=None):  # noqa: E501
        """ClanRankingListItems - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._name = None
        self._rank = None
        self._previous_rank = None
        self._location = None
        self._clan_score = None
        self._badge_id = None
        self._members = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if rank is not None:
            self.rank = rank
        if previous_rank is not None:
            self.previous_rank = previous_rank
        if location is not None:
            self.location = location
        if clan_score is not None:
            self.clan_score = clan_score
        if badge_id is not None:
            self.badge_id = badge_id
        if members is not None:
            self.members = members

    @property
    def tag(self):
        """Gets the tag of this ClanRankingListItems.  # noqa: E501


        :return: The tag of this ClanRankingListItems.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ClanRankingListItems.


        :param tag: The tag of this ClanRankingListItems.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this ClanRankingListItems.  # noqa: E501


        :return: The name of this ClanRankingListItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClanRankingListItems.


        :param name: The name of this ClanRankingListItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rank(self):
        """Gets the rank of this ClanRankingListItems.  # noqa: E501


        :return: The rank of this ClanRankingListItems.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this ClanRankingListItems.


        :param rank: The rank of this ClanRankingListItems.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def previous_rank(self):
        """Gets the previous_rank of this ClanRankingListItems.  # noqa: E501


        :return: The previous_rank of this ClanRankingListItems.  # noqa: E501
        :rtype: int
        """
        return self._previous_rank

    @previous_rank.setter
    def previous_rank(self, previous_rank):
        """Sets the previous_rank of this ClanRankingListItems.


        :param previous_rank: The previous_rank of this ClanRankingListItems.  # noqa: E501
        :type: int
        """

        self._previous_rank = previous_rank

    @property
    def location(self):
        """Gets the location of this ClanRankingListItems.  # noqa: E501


        :return: The location of this ClanRankingListItems.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClanRankingListItems.


        :param location: The location of this ClanRankingListItems.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def clan_score(self):
        """Gets the clan_score of this ClanRankingListItems.  # noqa: E501


        :return: The clan_score of this ClanRankingListItems.  # noqa: E501
        :rtype: int
        """
        return self._clan_score

    @clan_score.setter
    def clan_score(self, clan_score):
        """Sets the clan_score of this ClanRankingListItems.


        :param clan_score: The clan_score of this ClanRankingListItems.  # noqa: E501
        :type: int
        """

        self._clan_score = clan_score

    @property
    def badge_id(self):
        """Gets the badge_id of this ClanRankingListItems.  # noqa: E501


        :return: The badge_id of this ClanRankingListItems.  # noqa: E501
        :rtype: int
        """
        return self._badge_id

    @badge_id.setter
    def badge_id(self, badge_id):
        """Sets the badge_id of this ClanRankingListItems.


        :param badge_id: The badge_id of this ClanRankingListItems.  # noqa: E501
        :type: int
        """

        self._badge_id = badge_id

    @property
    def members(self):
        """Gets the members of this ClanRankingListItems.  # noqa: E501


        :return: The members of this ClanRankingListItems.  # noqa: E501
        :rtype: int
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ClanRankingListItems.


        :param members: The members of this ClanRankingListItems.  # noqa: E501
        :type: int
        """

        self._members = members

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
        if issubclass(ClanRankingListItems, dict):
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
        if not isinstance(other, ClanRankingListItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
