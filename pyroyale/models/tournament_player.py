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


class TournamentPlayer(object):
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
        'score': 'int',
        'rank': 'int',
        'clan': 'ClanBase'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'score': 'score',
        'rank': 'rank',
        'clan': 'clan'
    }

    def __init__(self, tag=None, name=None, score=None, rank=None, clan=None):  # noqa: E501
        """TournamentPlayer - a model defined in OpenAPI"""  # noqa: E501

        self._tag = None
        self._name = None
        self._score = None
        self._rank = None
        self._clan = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if score is not None:
            self.score = score
        if rank is not None:
            self.rank = rank
        if clan is not None:
            self.clan = clan

    @property
    def tag(self):
        """Gets the tag of this TournamentPlayer.  # noqa: E501


        :return: The tag of this TournamentPlayer.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TournamentPlayer.


        :param tag: The tag of this TournamentPlayer.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this TournamentPlayer.  # noqa: E501


        :return: The name of this TournamentPlayer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TournamentPlayer.


        :param name: The name of this TournamentPlayer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def score(self):
        """Gets the score of this TournamentPlayer.  # noqa: E501


        :return: The score of this TournamentPlayer.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TournamentPlayer.


        :param score: The score of this TournamentPlayer.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def rank(self):
        """Gets the rank of this TournamentPlayer.  # noqa: E501


        :return: The rank of this TournamentPlayer.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this TournamentPlayer.


        :param rank: The rank of this TournamentPlayer.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def clan(self):
        """Gets the clan of this TournamentPlayer.  # noqa: E501


        :return: The clan of this TournamentPlayer.  # noqa: E501
        :rtype: ClanBase
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this TournamentPlayer.


        :param clan: The clan of this TournamentPlayer.  # noqa: E501
        :type: ClanBase
        """

        self._clan = clan

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
        if not isinstance(other, TournamentPlayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
