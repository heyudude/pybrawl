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
from pyroyale.models.clan_member import ClanMember  # noqa: F401,E501
from pyroyale.models.location import Location  # noqa: F401,E501
from pyroyale.models.search_result_clan import SearchResultClan  # noqa: F401,E501


class Clan(SearchResultClan):
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
        'description': 'str',
        'clan_chest_status': 'str',
        'clan_chest_points': 'int',
        'member_list': 'list[ClanMember]'
    }

    attribute_map = {
        'description': 'description',
        'clan_chest_status': 'clanChestStatus',
        'clan_chest_points': 'clanChestPoints',
        'member_list': 'memberList'
    }

    def __init__(self, description=None, clan_chest_status=None, clan_chest_points=None, member_list=None):  # noqa: E501
        """Clan - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._clan_chest_status = None
        self._clan_chest_points = None
        self._member_list = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if clan_chest_status is not None:
            self.clan_chest_status = clan_chest_status
        if clan_chest_points is not None:
            self.clan_chest_points = clan_chest_points
        if member_list is not None:
            self.member_list = member_list

    @property
    def description(self):
        """Gets the description of this Clan.  # noqa: E501


        :return: The description of this Clan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Clan.


        :param description: The description of this Clan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def clan_chest_status(self):
        """Gets the clan_chest_status of this Clan.  # noqa: E501


        :return: The clan_chest_status of this Clan.  # noqa: E501
        :rtype: str
        """
        return self._clan_chest_status

    @clan_chest_status.setter
    def clan_chest_status(self, clan_chest_status):
        """Sets the clan_chest_status of this Clan.


        :param clan_chest_status: The clan_chest_status of this Clan.  # noqa: E501
        :type: str
        """

        self._clan_chest_status = clan_chest_status

    @property
    def clan_chest_points(self):
        """Gets the clan_chest_points of this Clan.  # noqa: E501


        :return: The clan_chest_points of this Clan.  # noqa: E501
        :rtype: int
        """
        return self._clan_chest_points

    @clan_chest_points.setter
    def clan_chest_points(self, clan_chest_points):
        """Sets the clan_chest_points of this Clan.


        :param clan_chest_points: The clan_chest_points of this Clan.  # noqa: E501
        :type: int
        """

        self._clan_chest_points = clan_chest_points

    @property
    def member_list(self):
        """Gets the member_list of this Clan.  # noqa: E501


        :return: The member_list of this Clan.  # noqa: E501
        :rtype: list[ClanMember]
        """
        return self._member_list

    @member_list.setter
    def member_list(self, member_list):
        """Sets the member_list of this Clan.


        :param member_list: The member_list of this Clan.  # noqa: E501
        :type: list[ClanMember]
        """

        self._member_list = member_list

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
        if issubclass(Clan, dict):
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
        if not isinstance(other, Clan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
