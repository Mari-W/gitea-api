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

class AccessToken(object):
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
        'id': 'int',
        'name': 'str',
        'sha1': 'str',
        'token_last_eight': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'sha1': 'sha1',
        'token_last_eight': 'token_last_eight'
    }

    def __init__(self, id=None, name=None, sha1=None, token_last_eight=None):  # noqa: E501
        """AccessToken - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._sha1 = None
        self._token_last_eight = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sha1 is not None:
            self.sha1 = sha1
        if token_last_eight is not None:
            self.token_last_eight = token_last_eight

    @property
    def id(self):
        """Gets the id of this AccessToken.  # noqa: E501


        :return: The id of this AccessToken.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessToken.


        :param id: The id of this AccessToken.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AccessToken.  # noqa: E501


        :return: The name of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessToken.


        :param name: The name of this AccessToken.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sha1(self):
        """Gets the sha1 of this AccessToken.  # noqa: E501


        :return: The sha1 of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this AccessToken.


        :param sha1: The sha1 of this AccessToken.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def token_last_eight(self):
        """Gets the token_last_eight of this AccessToken.  # noqa: E501


        :return: The token_last_eight of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token_last_eight

    @token_last_eight.setter
    def token_last_eight(self, token_last_eight):
        """Sets the token_last_eight of this AccessToken.


        :param token_last_eight: The token_last_eight of this AccessToken.  # noqa: E501
        :type: str
        """

        self._token_last_eight = token_last_eight

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
        if issubclass(AccessToken, dict):
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
        if not isinstance(other, AccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other