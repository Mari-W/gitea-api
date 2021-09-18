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

class GenerateRepoOption(object):
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
        'avatar': 'bool',
        'description': 'str',
        'git_content': 'bool',
        'git_hooks': 'bool',
        'labels': 'bool',
        'name': 'str',
        'owner': 'str',
        'private': 'bool',
        'topics': 'bool',
        'webhooks': 'bool'
    }

    attribute_map = {
        'avatar': 'avatar',
        'description': 'description',
        'git_content': 'git_content',
        'git_hooks': 'git_hooks',
        'labels': 'labels',
        'name': 'name',
        'owner': 'owner',
        'private': 'private',
        'topics': 'topics',
        'webhooks': 'webhooks'
    }

    def __init__(self, avatar=None, description=None, git_content=None, git_hooks=None, labels=None, name=None, owner=None, private=None, topics=None, webhooks=None):  # noqa: E501
        """GenerateRepoOption - a model defined in Swagger"""  # noqa: E501
        self._avatar = None
        self._description = None
        self._git_content = None
        self._git_hooks = None
        self._labels = None
        self._name = None
        self._owner = None
        self._private = None
        self._topics = None
        self._webhooks = None
        self.discriminator = None
        if avatar is not None:
            self.avatar = avatar
        if description is not None:
            self.description = description
        if git_content is not None:
            self.git_content = git_content
        if git_hooks is not None:
            self.git_hooks = git_hooks
        if labels is not None:
            self.labels = labels
        self.name = name
        self.owner = owner
        if private is not None:
            self.private = private
        if topics is not None:
            self.topics = topics
        if webhooks is not None:
            self.webhooks = webhooks

    @property
    def avatar(self):
        """Gets the avatar of this GenerateRepoOption.  # noqa: E501

        include avatar of the template repo  # noqa: E501

        :return: The avatar of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this GenerateRepoOption.

        include avatar of the template repo  # noqa: E501

        :param avatar: The avatar of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._avatar = avatar

    @property
    def description(self):
        """Gets the description of this GenerateRepoOption.  # noqa: E501

        Description of the repository to create  # noqa: E501

        :return: The description of this GenerateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GenerateRepoOption.

        Description of the repository to create  # noqa: E501

        :param description: The description of this GenerateRepoOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def git_content(self):
        """Gets the git_content of this GenerateRepoOption.  # noqa: E501

        include git content of default branch in template repo  # noqa: E501

        :return: The git_content of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._git_content

    @git_content.setter
    def git_content(self, git_content):
        """Sets the git_content of this GenerateRepoOption.

        include git content of default branch in template repo  # noqa: E501

        :param git_content: The git_content of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._git_content = git_content

    @property
    def git_hooks(self):
        """Gets the git_hooks of this GenerateRepoOption.  # noqa: E501

        include git hooks in template repo  # noqa: E501

        :return: The git_hooks of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._git_hooks

    @git_hooks.setter
    def git_hooks(self, git_hooks):
        """Sets the git_hooks of this GenerateRepoOption.

        include git hooks in template repo  # noqa: E501

        :param git_hooks: The git_hooks of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._git_hooks = git_hooks

    @property
    def labels(self):
        """Gets the labels of this GenerateRepoOption.  # noqa: E501

        include labels in template repo  # noqa: E501

        :return: The labels of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GenerateRepoOption.

        include labels in template repo  # noqa: E501

        :param labels: The labels of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this GenerateRepoOption.  # noqa: E501

        Name of the repository to create  # noqa: E501

        :return: The name of this GenerateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GenerateRepoOption.

        Name of the repository to create  # noqa: E501

        :param name: The name of this GenerateRepoOption.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this GenerateRepoOption.  # noqa: E501

        The organization or person who will own the new repository  # noqa: E501

        :return: The owner of this GenerateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GenerateRepoOption.

        The organization or person who will own the new repository  # noqa: E501

        :param owner: The owner of this GenerateRepoOption.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def private(self):
        """Gets the private of this GenerateRepoOption.  # noqa: E501

        Whether the repository is private  # noqa: E501

        :return: The private of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this GenerateRepoOption.

        Whether the repository is private  # noqa: E501

        :param private: The private of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def topics(self):
        """Gets the topics of this GenerateRepoOption.  # noqa: E501

        include topics in template repo  # noqa: E501

        :return: The topics of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this GenerateRepoOption.

        include topics in template repo  # noqa: E501

        :param topics: The topics of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._topics = topics

    @property
    def webhooks(self):
        """Gets the webhooks of this GenerateRepoOption.  # noqa: E501

        include webhooks in template repo  # noqa: E501

        :return: The webhooks of this GenerateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this GenerateRepoOption.

        include webhooks in template repo  # noqa: E501

        :param webhooks: The webhooks of this GenerateRepoOption.  # noqa: E501
        :type: bool
        """

        self._webhooks = webhooks

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
        if issubclass(GenerateRepoOption, dict):
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
        if not isinstance(other, GenerateRepoOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
