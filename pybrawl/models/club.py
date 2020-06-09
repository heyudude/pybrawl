# coding: utf-8

"""
    Brawl Stars API

    Unofficial Swagger definition for the official Brawl Stars API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pybrawl.configuration import Configuration


class Club(object):
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
        'badge_id': 'int',
        'type': 'str',
        'club_score': 'int',
        'required_trophies': 'int',
        'members': 'int',
        'location': 'Location',
        'description': 'str',
        'club_chest_status': 'str',
        'club_chest_points': 'int',
        'member_list': 'list[ClubMember]'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'badge_id': 'badgeId',
        'type': 'type',
        'club_score': 'clubScore',
        'required_trophies': 'requiredTrophies',
        'members': 'members',
        'location': 'location',
        'description': 'description',
        'club_chest_status': 'clubChestStatus',
        'club_chest_points': 'clubChestPoints',
        'member_list': 'memberList'
    }

    def __init__(self, tag=None, name=None, badge_id=None, type=None, club_score=None, required_trophies=None, members=None, location=None, description=None, club_chest_status=None, club_chest_points=None, member_list=None, local_vars_configuration=None):  # noqa: E501
        """Club - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._name = None
        self._badge_id = None
        self._type = None
        self._club_score = None
        self._required_trophies = None
        self._members = None
        self._location = None
        self._description = None
        self._club_chest_status = None
        self._club_chest_points = None
        self._member_list = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if badge_id is not None:
            self.badge_id = badge_id
        if type is not None:
            self.type = type
        if club_score is not None:
            self.club_score = club_score
        if required_trophies is not None:
            self.required_trophies = required_trophies
        if members is not None:
            self.members = members
        if location is not None:
            self.location = location
        if description is not None:
            self.description = description
        if club_chest_status is not None:
            self.club_chest_status = club_chest_status
        if club_chest_points is not None:
            self.club_chest_points = club_chest_points
        if member_list is not None:
            self.member_list = member_list

    @property
    def tag(self):
        """Gets the tag of this Club.  # noqa: E501


        :return: The tag of this Club.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Club.


        :param tag: The tag of this Club.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this Club.  # noqa: E501


        :return: The name of this Club.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Club.


        :param name: The name of this Club.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def badge_id(self):
        """Gets the badge_id of this Club.  # noqa: E501


        :return: The badge_id of this Club.  # noqa: E501
        :rtype: int
        """
        return self._badge_id

    @badge_id.setter
    def badge_id(self, badge_id):
        """Sets the badge_id of this Club.


        :param badge_id: The badge_id of this Club.  # noqa: E501
        :type: int
        """

        self._badge_id = badge_id

    @property
    def type(self):
        """Gets the type of this Club.  # noqa: E501


        :return: The type of this Club.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Club.


        :param type: The type of this Club.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def club_score(self):
        """Gets the club_score of this Club.  # noqa: E501


        :return: The club_score of this Club.  # noqa: E501
        :rtype: int
        """
        return self._club_score

    @club_score.setter
    def club_score(self, club_score):
        """Sets the club_score of this Club.


        :param club_score: The club_score of this Club.  # noqa: E501
        :type: int
        """

        self._club_score = club_score

    @property
    def required_trophies(self):
        """Gets the required_trophies of this Club.  # noqa: E501


        :return: The required_trophies of this Club.  # noqa: E501
        :rtype: int
        """
        return self._required_trophies

    @required_trophies.setter
    def required_trophies(self, required_trophies):
        """Sets the required_trophies of this Club.


        :param required_trophies: The required_trophies of this Club.  # noqa: E501
        :type: int
        """

        self._required_trophies = required_trophies

    @property
    def members(self):
        """Gets the members of this Club.  # noqa: E501


        :return: The members of this Club.  # noqa: E501
        :rtype: int
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Club.


        :param members: The members of this Club.  # noqa: E501
        :type: int
        """

        self._members = members

    @property
    def location(self):
        """Gets the location of this Club.  # noqa: E501


        :return: The location of this Club.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Club.


        :param location: The location of this Club.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def description(self):
        """Gets the description of this Club.  # noqa: E501


        :return: The description of this Club.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Club.


        :param description: The description of this Club.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def club_chest_status(self):
        """Gets the club_chest_status of this Club.  # noqa: E501


        :return: The club_chest_status of this Club.  # noqa: E501
        :rtype: str
        """
        return self._club_chest_status

    @club_chest_status.setter
    def club_chest_status(self, club_chest_status):
        """Sets the club_chest_status of this Club.


        :param club_chest_status: The club_chest_status of this Club.  # noqa: E501
        :type: str
        """

        self._club_chest_status = club_chest_status

    @property
    def club_chest_points(self):
        """Gets the club_chest_points of this Club.  # noqa: E501


        :return: The club_chest_points of this Club.  # noqa: E501
        :rtype: int
        """
        return self._club_chest_points

    @club_chest_points.setter
    def club_chest_points(self, club_chest_points):
        """Sets the club_chest_points of this Club.


        :param club_chest_points: The club_chest_points of this Club.  # noqa: E501
        :type: int
        """

        self._club_chest_points = club_chest_points

    @property
    def member_list(self):
        """Gets the member_list of this Club.  # noqa: E501


        :return: The member_list of this Club.  # noqa: E501
        :rtype: list[ClubMember]
        """
        return self._member_list

    @member_list.setter
    def member_list(self, member_list):
        """Sets the member_list of this Club.


        :param member_list: The member_list of this Club.  # noqa: E501
        :type: list[ClubMember]
        """

        self._member_list = member_list

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
        if not isinstance(other, Club):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Club):
            return True

        return self.to_dict() != other.to_dict()
