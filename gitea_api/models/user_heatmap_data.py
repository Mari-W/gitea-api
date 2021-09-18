# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserHeatmapData(object):
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
        'contributions': 'int',
        'timestamp': 'TimeStamp'
    }

    attribute_map = {
        'contributions': 'contributions',
        'timestamp': 'timestamp'
    }

    def __init__(self, contributions=None, timestamp=None):  # noqa: E501
        """UserHeatmapData - a model defined in Swagger"""  # noqa: E501
        self._contributions = None
        self._timestamp = None
        self.discriminator = None
        if contributions is not None:
            self.contributions = contributions
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def contributions(self):
        """Gets the contributions of this UserHeatmapData.  # noqa: E501


        :return: The contributions of this UserHeatmapData.  # noqa: E501
        :rtype: int
        """
        return self._contributions

    @contributions.setter
    def contributions(self, contributions):
        """Sets the contributions of this UserHeatmapData.


        :param contributions: The contributions of this UserHeatmapData.  # noqa: E501
        :type: int
        """

        self._contributions = contributions

    @property
    def timestamp(self):
        """Gets the timestamp of this UserHeatmapData.  # noqa: E501


        :return: The timestamp of this UserHeatmapData.  # noqa: E501
        :rtype: TimeStamp
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UserHeatmapData.


        :param timestamp: The timestamp of this UserHeatmapData.  # noqa: E501
        :type: TimeStamp
        """

        self._timestamp = timestamp

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
        if issubclass(UserHeatmapData, dict):
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
        if not isinstance(other, UserHeatmapData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
