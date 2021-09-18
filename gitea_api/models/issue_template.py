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

class IssueTemplate(object):
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
        'about': 'str',
        'content': 'str',
        'file_name': 'str',
        'labels': 'list[str]',
        'name': 'str',
        'title': 'str'
    }

    attribute_map = {
        'about': 'about',
        'content': 'content',
        'file_name': 'file_name',
        'labels': 'labels',
        'name': 'name',
        'title': 'title'
    }

    def __init__(self, about=None, content=None, file_name=None, labels=None, name=None, title=None):  # noqa: E501
        """IssueTemplate - a model defined in Swagger"""  # noqa: E501
        self._about = None
        self._content = None
        self._file_name = None
        self._labels = None
        self._name = None
        self._title = None
        self.discriminator = None
        if about is not None:
            self.about = about
        if content is not None:
            self.content = content
        if file_name is not None:
            self.file_name = file_name
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title

    @property
    def about(self):
        """Gets the about of this IssueTemplate.  # noqa: E501


        :return: The about of this IssueTemplate.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this IssueTemplate.


        :param about: The about of this IssueTemplate.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def content(self):
        """Gets the content of this IssueTemplate.  # noqa: E501


        :return: The content of this IssueTemplate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this IssueTemplate.


        :param content: The content of this IssueTemplate.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def file_name(self):
        """Gets the file_name of this IssueTemplate.  # noqa: E501


        :return: The file_name of this IssueTemplate.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this IssueTemplate.


        :param file_name: The file_name of this IssueTemplate.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def labels(self):
        """Gets the labels of this IssueTemplate.  # noqa: E501


        :return: The labels of this IssueTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IssueTemplate.


        :param labels: The labels of this IssueTemplate.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this IssueTemplate.  # noqa: E501


        :return: The name of this IssueTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IssueTemplate.


        :param name: The name of this IssueTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this IssueTemplate.  # noqa: E501


        :return: The title of this IssueTemplate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IssueTemplate.


        :param title: The title of this IssueTemplate.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(IssueTemplate, dict):
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
        if not isinstance(other, IssueTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
