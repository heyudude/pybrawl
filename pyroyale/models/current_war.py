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
from pyroyale.models.current_war_clan import CurrentWarClan  # noqa: F401,E501
from pyroyale.models.war_clan import WarClan  # noqa: F401,E501
from pyroyale.models.war_participant import WarParticipant  # noqa: F401,E501


class CurrentWar(object):
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
        'state': 'str',
        'war_end_time': 'str',
        'clan': 'CurrentWarClan',
        'participants': 'list[WarParticipant]',
        'clans': 'list[WarClan]'
    }

    attribute_map = {
        'state': 'state',
        'war_end_time': 'warEndTime',
        'clan': 'clan',
        'participants': 'participants',
        'clans': 'clans'
    }

    def __init__(self, state=None, war_end_time=None, clan=None, participants=None, clans=None):  # noqa: E501
        """CurrentWar - a model defined in Swagger"""  # noqa: E501
        self._state = None
        self._war_end_time = None
        self._clan = None
        self._participants = None
        self._clans = None
        self.discriminator = None
        if state is not None:
            self.state = state
        if war_end_time is not None:
            self.war_end_time = war_end_time
        if clan is not None:
            self.clan = clan
        if participants is not None:
            self.participants = participants
        if clans is not None:
            self.clans = clans

    @property
    def state(self):
        """Gets the state of this CurrentWar.  # noqa: E501


        :return: The state of this CurrentWar.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CurrentWar.


        :param state: The state of this CurrentWar.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def war_end_time(self):
        """Gets the war_end_time of this CurrentWar.  # noqa: E501


        :return: The war_end_time of this CurrentWar.  # noqa: E501
        :rtype: str
        """
        return self._war_end_time

    @war_end_time.setter
    def war_end_time(self, war_end_time):
        """Sets the war_end_time of this CurrentWar.


        :param war_end_time: The war_end_time of this CurrentWar.  # noqa: E501
        :type: str
        """

        self._war_end_time = war_end_time

    @property
    def clan(self):
        """Gets the clan of this CurrentWar.  # noqa: E501


        :return: The clan of this CurrentWar.  # noqa: E501
        :rtype: CurrentWarClan
        """
        return self._clan

    @clan.setter
    def clan(self, clan):
        """Sets the clan of this CurrentWar.


        :param clan: The clan of this CurrentWar.  # noqa: E501
        :type: CurrentWarClan
        """

        self._clan = clan

    @property
    def participants(self):
        """Gets the participants of this CurrentWar.  # noqa: E501


        :return: The participants of this CurrentWar.  # noqa: E501
        :rtype: list[WarParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this CurrentWar.


        :param participants: The participants of this CurrentWar.  # noqa: E501
        :type: list[WarParticipant]
        """

        self._participants = participants

    @property
    def clans(self):
        """Gets the clans of this CurrentWar.  # noqa: E501


        :return: The clans of this CurrentWar.  # noqa: E501
        :rtype: list[WarClan]
        """
        return self._clans

    @clans.setter
    def clans(self, clans):
        """Sets the clans of this CurrentWar.


        :param clans: The clans of this CurrentWar.  # noqa: E501
        :type: list[WarClan]
        """

        self._clans = clans

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
        if issubclass(CurrentWar, dict):
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
        if not isinstance(other, CurrentWar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
