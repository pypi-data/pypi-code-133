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


class PatchIcxCategory(object):
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
        'description': 'str',
        'rules': 'list[PatchIcxCategoryRulesArray]',
        'rules_filters': 'list[PatchIcxCategoryFiltersArray]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'rules': 'rules',
        'rules_filters': 'rules.filters'
    }

    def __init__(self, name=None, description=None, rules=None, rules_filters=None, local_vars_configuration=None):  # noqa: E501
        """PatchIcxCategory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._rules = None
        self._rules_filters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules
        if rules_filters is not None:
            self.rules_filters = rules_filters

    @property
    def name(self):
        """Gets the name of this PatchIcxCategory.  # noqa: E501


        :return: The name of this PatchIcxCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchIcxCategory.


        :param name: The name of this PatchIcxCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PatchIcxCategory.  # noqa: E501


        :return: The description of this PatchIcxCategory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchIcxCategory.


        :param description: The description of this PatchIcxCategory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this PatchIcxCategory.  # noqa: E501


        :return: The rules of this PatchIcxCategory.  # noqa: E501
        :rtype: list[PatchIcxCategoryRulesArray]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PatchIcxCategory.


        :param rules: The rules of this PatchIcxCategory.  # noqa: E501
        :type: list[PatchIcxCategoryRulesArray]
        """

        self._rules = rules

    @property
    def rules_filters(self):
        """Gets the rules_filters of this PatchIcxCategory.  # noqa: E501


        :return: The rules_filters of this PatchIcxCategory.  # noqa: E501
        :rtype: list[PatchIcxCategoryFiltersArray]
        """
        return self._rules_filters

    @rules_filters.setter
    def rules_filters(self, rules_filters):
        """Sets the rules_filters of this PatchIcxCategory.


        :param rules_filters: The rules_filters of this PatchIcxCategory.  # noqa: E501
        :type: list[PatchIcxCategoryFiltersArray]
        """

        self._rules_filters = rules_filters

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
        if not isinstance(other, PatchIcxCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchIcxCategory):
            return True

        return self.to_dict() != other.to_dict()
