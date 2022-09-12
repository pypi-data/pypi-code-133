# coding: utf-8

"""
    UBIKA WAAP Gateway and Cloud API

    The UBIKA's WAAP management API provides a REST/JSON programming interface. It allows automation and scripting of WAAP administration tasks, such as management of reverse proxies and tunnels. The API documentation is shipped with the product itself. Once the product installed, you can access the documentation on the following URL https://ManagementWAAP:3001/api/v1/doc/  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ubika_waap_api_client.configuration import Configuration


class CreateIcxRulesArray(object):
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
        'name': 'str',
        'uid': 'str',
        'match': 'str',
        'action': 'str',
        'scope': 'str',
        'enable': 'bool',
        'description': 'str',
        'filters': 'list[CreateIcxFiltersArray]'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'match': 'match',
        'action': 'action',
        'scope': 'scope',
        'enable': 'enable',
        'description': 'description',
        'filters': 'filters'
    }

    def __init__(self, name=None, uid=None, match=None, action=None, scope=None, enable=None, description=None, filters=None, local_vars_configuration=None):  # noqa: E501
        """CreateIcxRulesArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._uid = None
        self._match = None
        self._action = None
        self._scope = None
        self._enable = None
        self._description = None
        self._filters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if match is not None:
            self.match = match
        if action is not None:
            self.action = action
        if scope is not None:
            self.scope = scope
        if enable is not None:
            self.enable = enable
        if description is not None:
            self.description = description
        if filters is not None:
            self.filters = filters

    @property
    def name(self):
        """Gets the name of this CreateIcxRulesArray.  # noqa: E501


        :return: The name of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIcxRulesArray.


        :param name: The name of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this CreateIcxRulesArray.  # noqa: E501


        :return: The uid of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CreateIcxRulesArray.


        :param uid: The uid of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def match(self):
        """Gets the match of this CreateIcxRulesArray.  # noqa: E501


        :return: The match of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this CreateIcxRulesArray.


        :param match: The match of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def action(self):
        """Gets the action of this CreateIcxRulesArray.  # noqa: E501


        :return: The action of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateIcxRulesArray.


        :param action: The action of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def scope(self):
        """Gets the scope of this CreateIcxRulesArray.  # noqa: E501


        :return: The scope of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateIcxRulesArray.


        :param scope: The scope of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def enable(self):
        """Gets the enable of this CreateIcxRulesArray.  # noqa: E501


        :return: The enable of this CreateIcxRulesArray.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateIcxRulesArray.


        :param enable: The enable of this CreateIcxRulesArray.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def description(self):
        """Gets the description of this CreateIcxRulesArray.  # noqa: E501


        :return: The description of this CreateIcxRulesArray.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIcxRulesArray.


        :param description: The description of this CreateIcxRulesArray.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def filters(self):
        """Gets the filters of this CreateIcxRulesArray.  # noqa: E501


        :return: The filters of this CreateIcxRulesArray.  # noqa: E501
        :rtype: list[CreateIcxFiltersArray]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this CreateIcxRulesArray.


        :param filters: The filters of this CreateIcxRulesArray.  # noqa: E501
        :type: list[CreateIcxFiltersArray]
        """

        self._filters = filters

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
        if not isinstance(other, CreateIcxRulesArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateIcxRulesArray):
            return True

        return self.to_dict() != other.to_dict()
