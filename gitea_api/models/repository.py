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

class Repository(object):
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
        'allow_merge_commits': 'bool',
        'allow_rebase': 'bool',
        'allow_rebase_explicit': 'bool',
        'allow_squash_merge': 'bool',
        'archived': 'bool',
        'avatar_url': 'str',
        'clone_url': 'str',
        'created_at': 'datetime',
        'default_branch': 'str',
        'default_merge_style': 'str',
        'description': 'str',
        'empty': 'bool',
        'external_tracker': 'ExternalTracker',
        'external_wiki': 'ExternalWiki',
        'fork': 'bool',
        'forks_count': 'int',
        'full_name': 'str',
        'has_issues': 'bool',
        'has_projects': 'bool',
        'has_pull_requests': 'bool',
        'has_wiki': 'bool',
        'html_url': 'str',
        'id': 'int',
        'ignore_whitespace_conflicts': 'bool',
        'internal': 'bool',
        'internal_tracker': 'InternalTracker',
        'mirror': 'bool',
        'mirror_interval': 'str',
        'name': 'str',
        'open_issues_count': 'int',
        'open_pr_counter': 'int',
        'original_url': 'str',
        'owner': 'User',
        'parent': 'Repository',
        'permissions': 'Permission',
        'private': 'bool',
        'release_counter': 'int',
        'size': 'int',
        'ssh_url': 'str',
        'stars_count': 'int',
        'template': 'bool',
        'updated_at': 'datetime',
        'watchers_count': 'int',
        'website': 'str'
    }

    attribute_map = {
        'allow_merge_commits': 'allow_merge_commits',
        'allow_rebase': 'allow_rebase',
        'allow_rebase_explicit': 'allow_rebase_explicit',
        'allow_squash_merge': 'allow_squash_merge',
        'archived': 'archived',
        'avatar_url': 'avatar_url',
        'clone_url': 'clone_url',
        'created_at': 'created_at',
        'default_branch': 'default_branch',
        'default_merge_style': 'default_merge_style',
        'description': 'description',
        'empty': 'empty',
        'external_tracker': 'external_tracker',
        'external_wiki': 'external_wiki',
        'fork': 'fork',
        'forks_count': 'forks_count',
        'full_name': 'full_name',
        'has_issues': 'has_issues',
        'has_projects': 'has_projects',
        'has_pull_requests': 'has_pull_requests',
        'has_wiki': 'has_wiki',
        'html_url': 'html_url',
        'id': 'id',
        'ignore_whitespace_conflicts': 'ignore_whitespace_conflicts',
        'internal': 'internal',
        'internal_tracker': 'internal_tracker',
        'mirror': 'mirror',
        'mirror_interval': 'mirror_interval',
        'name': 'name',
        'open_issues_count': 'open_issues_count',
        'open_pr_counter': 'open_pr_counter',
        'original_url': 'original_url',
        'owner': 'owner',
        'parent': 'parent',
        'permissions': 'permissions',
        'private': 'private',
        'release_counter': 'release_counter',
        'size': 'size',
        'ssh_url': 'ssh_url',
        'stars_count': 'stars_count',
        'template': 'template',
        'updated_at': 'updated_at',
        'watchers_count': 'watchers_count',
        'website': 'website'
    }

    def __init__(self, allow_merge_commits=None, allow_rebase=None, allow_rebase_explicit=None, allow_squash_merge=None, archived=None, avatar_url=None, clone_url=None, created_at=None, default_branch=None, default_merge_style=None, description=None, empty=None, external_tracker=None, external_wiki=None, fork=None, forks_count=None, full_name=None, has_issues=None, has_projects=None, has_pull_requests=None, has_wiki=None, html_url=None, id=None, ignore_whitespace_conflicts=None, internal=None, internal_tracker=None, mirror=None, mirror_interval=None, name=None, open_issues_count=None, open_pr_counter=None, original_url=None, owner=None, parent=None, permissions=None, private=None, release_counter=None, size=None, ssh_url=None, stars_count=None, template=None, updated_at=None, watchers_count=None, website=None):  # noqa: E501
        """Repository - a model defined in Swagger"""  # noqa: E501
        self._allow_merge_commits = None
        self._allow_rebase = None
        self._allow_rebase_explicit = None
        self._allow_squash_merge = None
        self._archived = None
        self._avatar_url = None
        self._clone_url = None
        self._created_at = None
        self._default_branch = None
        self._default_merge_style = None
        self._description = None
        self._empty = None
        self._external_tracker = None
        self._external_wiki = None
        self._fork = None
        self._forks_count = None
        self._full_name = None
        self._has_issues = None
        self._has_projects = None
        self._has_pull_requests = None
        self._has_wiki = None
        self._html_url = None
        self._id = None
        self._ignore_whitespace_conflicts = None
        self._internal = None
        self._internal_tracker = None
        self._mirror = None
        self._mirror_interval = None
        self._name = None
        self._open_issues_count = None
        self._open_pr_counter = None
        self._original_url = None
        self._owner = None
        self._parent = None
        self._permissions = None
        self._private = None
        self._release_counter = None
        self._size = None
        self._ssh_url = None
        self._stars_count = None
        self._template = None
        self._updated_at = None
        self._watchers_count = None
        self._website = None
        self.discriminator = None
        if allow_merge_commits is not None:
            self.allow_merge_commits = allow_merge_commits
        if allow_rebase is not None:
            self.allow_rebase = allow_rebase
        if allow_rebase_explicit is not None:
            self.allow_rebase_explicit = allow_rebase_explicit
        if allow_squash_merge is not None:
            self.allow_squash_merge = allow_squash_merge
        if archived is not None:
            self.archived = archived
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if clone_url is not None:
            self.clone_url = clone_url
        if created_at is not None:
            self.created_at = created_at
        if default_branch is not None:
            self.default_branch = default_branch
        if default_merge_style is not None:
            self.default_merge_style = default_merge_style
        if description is not None:
            self.description = description
        if empty is not None:
            self.empty = empty
        if external_tracker is not None:
            self.external_tracker = external_tracker
        if external_wiki is not None:
            self.external_wiki = external_wiki
        if fork is not None:
            self.fork = fork
        if forks_count is not None:
            self.forks_count = forks_count
        if full_name is not None:
            self.full_name = full_name
        if has_issues is not None:
            self.has_issues = has_issues
        if has_projects is not None:
            self.has_projects = has_projects
        if has_pull_requests is not None:
            self.has_pull_requests = has_pull_requests
        if has_wiki is not None:
            self.has_wiki = has_wiki
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if ignore_whitespace_conflicts is not None:
            self.ignore_whitespace_conflicts = ignore_whitespace_conflicts
        if internal is not None:
            self.internal = internal
        if internal_tracker is not None:
            self.internal_tracker = internal_tracker
        if mirror is not None:
            self.mirror = mirror
        if mirror_interval is not None:
            self.mirror_interval = mirror_interval
        if name is not None:
            self.name = name
        if open_issues_count is not None:
            self.open_issues_count = open_issues_count
        if open_pr_counter is not None:
            self.open_pr_counter = open_pr_counter
        if original_url is not None:
            self.original_url = original_url
        if owner is not None:
            self.owner = owner
        if parent is not None:
            self.parent = parent
        if permissions is not None:
            self.permissions = permissions
        if private is not None:
            self.private = private
        if release_counter is not None:
            self.release_counter = release_counter
        if size is not None:
            self.size = size
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if stars_count is not None:
            self.stars_count = stars_count
        if template is not None:
            self.template = template
        if updated_at is not None:
            self.updated_at = updated_at
        if watchers_count is not None:
            self.watchers_count = watchers_count
        if website is not None:
            self.website = website

    @property
    def allow_merge_commits(self):
        """Gets the allow_merge_commits of this Repository.  # noqa: E501


        :return: The allow_merge_commits of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._allow_merge_commits

    @allow_merge_commits.setter
    def allow_merge_commits(self, allow_merge_commits):
        """Sets the allow_merge_commits of this Repository.


        :param allow_merge_commits: The allow_merge_commits of this Repository.  # noqa: E501
        :type: bool
        """

        self._allow_merge_commits = allow_merge_commits

    @property
    def allow_rebase(self):
        """Gets the allow_rebase of this Repository.  # noqa: E501


        :return: The allow_rebase of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._allow_rebase

    @allow_rebase.setter
    def allow_rebase(self, allow_rebase):
        """Sets the allow_rebase of this Repository.


        :param allow_rebase: The allow_rebase of this Repository.  # noqa: E501
        :type: bool
        """

        self._allow_rebase = allow_rebase

    @property
    def allow_rebase_explicit(self):
        """Gets the allow_rebase_explicit of this Repository.  # noqa: E501


        :return: The allow_rebase_explicit of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._allow_rebase_explicit

    @allow_rebase_explicit.setter
    def allow_rebase_explicit(self, allow_rebase_explicit):
        """Sets the allow_rebase_explicit of this Repository.


        :param allow_rebase_explicit: The allow_rebase_explicit of this Repository.  # noqa: E501
        :type: bool
        """

        self._allow_rebase_explicit = allow_rebase_explicit

    @property
    def allow_squash_merge(self):
        """Gets the allow_squash_merge of this Repository.  # noqa: E501


        :return: The allow_squash_merge of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._allow_squash_merge

    @allow_squash_merge.setter
    def allow_squash_merge(self, allow_squash_merge):
        """Sets the allow_squash_merge of this Repository.


        :param allow_squash_merge: The allow_squash_merge of this Repository.  # noqa: E501
        :type: bool
        """

        self._allow_squash_merge = allow_squash_merge

    @property
    def archived(self):
        """Gets the archived of this Repository.  # noqa: E501


        :return: The archived of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Repository.


        :param archived: The archived of this Repository.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Repository.  # noqa: E501


        :return: The avatar_url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Repository.


        :param avatar_url: The avatar_url of this Repository.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def clone_url(self):
        """Gets the clone_url of this Repository.  # noqa: E501


        :return: The clone_url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._clone_url

    @clone_url.setter
    def clone_url(self, clone_url):
        """Sets the clone_url of this Repository.


        :param clone_url: The clone_url of this Repository.  # noqa: E501
        :type: str
        """

        self._clone_url = clone_url

    @property
    def created_at(self):
        """Gets the created_at of this Repository.  # noqa: E501


        :return: The created_at of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Repository.


        :param created_at: The created_at of this Repository.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def default_branch(self):
        """Gets the default_branch of this Repository.  # noqa: E501


        :return: The default_branch of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this Repository.


        :param default_branch: The default_branch of this Repository.  # noqa: E501
        :type: str
        """

        self._default_branch = default_branch

    @property
    def default_merge_style(self):
        """Gets the default_merge_style of this Repository.  # noqa: E501


        :return: The default_merge_style of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._default_merge_style

    @default_merge_style.setter
    def default_merge_style(self, default_merge_style):
        """Sets the default_merge_style of this Repository.


        :param default_merge_style: The default_merge_style of this Repository.  # noqa: E501
        :type: str
        """

        self._default_merge_style = default_merge_style

    @property
    def description(self):
        """Gets the description of this Repository.  # noqa: E501


        :return: The description of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Repository.


        :param description: The description of this Repository.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def empty(self):
        """Gets the empty of this Repository.  # noqa: E501


        :return: The empty of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this Repository.


        :param empty: The empty of this Repository.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def external_tracker(self):
        """Gets the external_tracker of this Repository.  # noqa: E501


        :return: The external_tracker of this Repository.  # noqa: E501
        :rtype: ExternalTracker
        """
        return self._external_tracker

    @external_tracker.setter
    def external_tracker(self, external_tracker):
        """Sets the external_tracker of this Repository.


        :param external_tracker: The external_tracker of this Repository.  # noqa: E501
        :type: ExternalTracker
        """

        self._external_tracker = external_tracker

    @property
    def external_wiki(self):
        """Gets the external_wiki of this Repository.  # noqa: E501


        :return: The external_wiki of this Repository.  # noqa: E501
        :rtype: ExternalWiki
        """
        return self._external_wiki

    @external_wiki.setter
    def external_wiki(self, external_wiki):
        """Sets the external_wiki of this Repository.


        :param external_wiki: The external_wiki of this Repository.  # noqa: E501
        :type: ExternalWiki
        """

        self._external_wiki = external_wiki

    @property
    def fork(self):
        """Gets the fork of this Repository.  # noqa: E501


        :return: The fork of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._fork

    @fork.setter
    def fork(self, fork):
        """Sets the fork of this Repository.


        :param fork: The fork of this Repository.  # noqa: E501
        :type: bool
        """

        self._fork = fork

    @property
    def forks_count(self):
        """Gets the forks_count of this Repository.  # noqa: E501


        :return: The forks_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._forks_count

    @forks_count.setter
    def forks_count(self, forks_count):
        """Sets the forks_count of this Repository.


        :param forks_count: The forks_count of this Repository.  # noqa: E501
        :type: int
        """

        self._forks_count = forks_count

    @property
    def full_name(self):
        """Gets the full_name of this Repository.  # noqa: E501


        :return: The full_name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Repository.


        :param full_name: The full_name of this Repository.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def has_issues(self):
        """Gets the has_issues of this Repository.  # noqa: E501


        :return: The has_issues of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._has_issues

    @has_issues.setter
    def has_issues(self, has_issues):
        """Sets the has_issues of this Repository.


        :param has_issues: The has_issues of this Repository.  # noqa: E501
        :type: bool
        """

        self._has_issues = has_issues

    @property
    def has_projects(self):
        """Gets the has_projects of this Repository.  # noqa: E501


        :return: The has_projects of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._has_projects

    @has_projects.setter
    def has_projects(self, has_projects):
        """Sets the has_projects of this Repository.


        :param has_projects: The has_projects of this Repository.  # noqa: E501
        :type: bool
        """

        self._has_projects = has_projects

    @property
    def has_pull_requests(self):
        """Gets the has_pull_requests of this Repository.  # noqa: E501


        :return: The has_pull_requests of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._has_pull_requests

    @has_pull_requests.setter
    def has_pull_requests(self, has_pull_requests):
        """Sets the has_pull_requests of this Repository.


        :param has_pull_requests: The has_pull_requests of this Repository.  # noqa: E501
        :type: bool
        """

        self._has_pull_requests = has_pull_requests

    @property
    def has_wiki(self):
        """Gets the has_wiki of this Repository.  # noqa: E501


        :return: The has_wiki of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._has_wiki

    @has_wiki.setter
    def has_wiki(self, has_wiki):
        """Sets the has_wiki of this Repository.


        :param has_wiki: The has_wiki of this Repository.  # noqa: E501
        :type: bool
        """

        self._has_wiki = has_wiki

    @property
    def html_url(self):
        """Gets the html_url of this Repository.  # noqa: E501


        :return: The html_url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this Repository.


        :param html_url: The html_url of this Repository.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this Repository.  # noqa: E501


        :return: The id of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Repository.


        :param id: The id of this Repository.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ignore_whitespace_conflicts(self):
        """Gets the ignore_whitespace_conflicts of this Repository.  # noqa: E501


        :return: The ignore_whitespace_conflicts of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_whitespace_conflicts

    @ignore_whitespace_conflicts.setter
    def ignore_whitespace_conflicts(self, ignore_whitespace_conflicts):
        """Sets the ignore_whitespace_conflicts of this Repository.


        :param ignore_whitespace_conflicts: The ignore_whitespace_conflicts of this Repository.  # noqa: E501
        :type: bool
        """

        self._ignore_whitespace_conflicts = ignore_whitespace_conflicts

    @property
    def internal(self):
        """Gets the internal of this Repository.  # noqa: E501


        :return: The internal of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this Repository.


        :param internal: The internal of this Repository.  # noqa: E501
        :type: bool
        """

        self._internal = internal

    @property
    def internal_tracker(self):
        """Gets the internal_tracker of this Repository.  # noqa: E501


        :return: The internal_tracker of this Repository.  # noqa: E501
        :rtype: InternalTracker
        """
        return self._internal_tracker

    @internal_tracker.setter
    def internal_tracker(self, internal_tracker):
        """Sets the internal_tracker of this Repository.


        :param internal_tracker: The internal_tracker of this Repository.  # noqa: E501
        :type: InternalTracker
        """

        self._internal_tracker = internal_tracker

    @property
    def mirror(self):
        """Gets the mirror of this Repository.  # noqa: E501


        :return: The mirror of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this Repository.


        :param mirror: The mirror of this Repository.  # noqa: E501
        :type: bool
        """

        self._mirror = mirror

    @property
    def mirror_interval(self):
        """Gets the mirror_interval of this Repository.  # noqa: E501


        :return: The mirror_interval of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._mirror_interval

    @mirror_interval.setter
    def mirror_interval(self, mirror_interval):
        """Sets the mirror_interval of this Repository.


        :param mirror_interval: The mirror_interval of this Repository.  # noqa: E501
        :type: str
        """

        self._mirror_interval = mirror_interval

    @property
    def name(self):
        """Gets the name of this Repository.  # noqa: E501


        :return: The name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Repository.


        :param name: The name of this Repository.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def open_issues_count(self):
        """Gets the open_issues_count of this Repository.  # noqa: E501


        :return: The open_issues_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._open_issues_count

    @open_issues_count.setter
    def open_issues_count(self, open_issues_count):
        """Sets the open_issues_count of this Repository.


        :param open_issues_count: The open_issues_count of this Repository.  # noqa: E501
        :type: int
        """

        self._open_issues_count = open_issues_count

    @property
    def open_pr_counter(self):
        """Gets the open_pr_counter of this Repository.  # noqa: E501


        :return: The open_pr_counter of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._open_pr_counter

    @open_pr_counter.setter
    def open_pr_counter(self, open_pr_counter):
        """Sets the open_pr_counter of this Repository.


        :param open_pr_counter: The open_pr_counter of this Repository.  # noqa: E501
        :type: int
        """

        self._open_pr_counter = open_pr_counter

    @property
    def original_url(self):
        """Gets the original_url of this Repository.  # noqa: E501


        :return: The original_url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._original_url

    @original_url.setter
    def original_url(self, original_url):
        """Sets the original_url of this Repository.


        :param original_url: The original_url of this Repository.  # noqa: E501
        :type: str
        """

        self._original_url = original_url

    @property
    def owner(self):
        """Gets the owner of this Repository.  # noqa: E501


        :return: The owner of this Repository.  # noqa: E501
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Repository.


        :param owner: The owner of this Repository.  # noqa: E501
        :type: User
        """

        self._owner = owner

    @property
    def parent(self):
        """Gets the parent of this Repository.  # noqa: E501


        :return: The parent of this Repository.  # noqa: E501
        :rtype: Repository
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Repository.


        :param parent: The parent of this Repository.  # noqa: E501
        :type: Repository
        """

        self._parent = parent

    @property
    def permissions(self):
        """Gets the permissions of this Repository.  # noqa: E501


        :return: The permissions of this Repository.  # noqa: E501
        :rtype: Permission
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Repository.


        :param permissions: The permissions of this Repository.  # noqa: E501
        :type: Permission
        """

        self._permissions = permissions

    @property
    def private(self):
        """Gets the private of this Repository.  # noqa: E501


        :return: The private of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Repository.


        :param private: The private of this Repository.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def release_counter(self):
        """Gets the release_counter of this Repository.  # noqa: E501


        :return: The release_counter of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._release_counter

    @release_counter.setter
    def release_counter(self, release_counter):
        """Sets the release_counter of this Repository.


        :param release_counter: The release_counter of this Repository.  # noqa: E501
        :type: int
        """

        self._release_counter = release_counter

    @property
    def size(self):
        """Gets the size of this Repository.  # noqa: E501


        :return: The size of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Repository.


        :param size: The size of this Repository.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def ssh_url(self):
        """Gets the ssh_url of this Repository.  # noqa: E501


        :return: The ssh_url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this Repository.


        :param ssh_url: The ssh_url of this Repository.  # noqa: E501
        :type: str
        """

        self._ssh_url = ssh_url

    @property
    def stars_count(self):
        """Gets the stars_count of this Repository.  # noqa: E501


        :return: The stars_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._stars_count

    @stars_count.setter
    def stars_count(self, stars_count):
        """Sets the stars_count of this Repository.


        :param stars_count: The stars_count of this Repository.  # noqa: E501
        :type: int
        """

        self._stars_count = stars_count

    @property
    def template(self):
        """Gets the template of this Repository.  # noqa: E501


        :return: The template of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Repository.


        :param template: The template of this Repository.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def updated_at(self):
        """Gets the updated_at of this Repository.  # noqa: E501


        :return: The updated_at of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Repository.


        :param updated_at: The updated_at of this Repository.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def watchers_count(self):
        """Gets the watchers_count of this Repository.  # noqa: E501


        :return: The watchers_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._watchers_count

    @watchers_count.setter
    def watchers_count(self, watchers_count):
        """Sets the watchers_count of this Repository.


        :param watchers_count: The watchers_count of this Repository.  # noqa: E501
        :type: int
        """

        self._watchers_count = watchers_count

    @property
    def website(self):
        """Gets the website of this Repository.  # noqa: E501


        :return: The website of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Repository.


        :param website: The website of this Repository.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(Repository, dict):
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
        if not isinstance(other, Repository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
