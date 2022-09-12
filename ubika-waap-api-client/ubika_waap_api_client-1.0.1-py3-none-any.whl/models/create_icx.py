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


class CreateIcx(object):
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
        'template': 'CreateApplianceSysctlProfile',
        'categories': 'list[CreateIcxCategoriesArray]',
        'categories_rules': 'list[CreateIcxRulesArray]',
        'categories_rules_filters': 'list[CreateIcxFiltersArray]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'template': 'template',
        'categories': 'categories',
        'categories_rules': 'categories.rules',
        'categories_rules_filters': 'categories.rules.filters'
    }

    def __init__(self, name=None, description=None, template=None, categories=None, categories_rules=None, categories_rules_filters=None, local_vars_configuration=None):  # noqa: E501
        """CreateIcx - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._template = None
        self._categories = None
        self._categories_rules = None
        self._categories_rules_filters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if template is not None:
            self.template = template
        if categories is not None:
            self.categories = categories
        if categories_rules is not None:
            self.categories_rules = categories_rules
        if categories_rules_filters is not None:
            self.categories_rules_filters = categories_rules_filters

    @property
    def name(self):
        """Gets the name of this CreateIcx.  # noqa: E501


        :return: The name of this CreateIcx.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIcx.


        :param name: The name of this CreateIcx.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateIcx.  # noqa: E501


        :return: The description of this CreateIcx.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIcx.


        :param description: The description of this CreateIcx.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def template(self):
        """Gets the template of this CreateIcx.  # noqa: E501


        :return: The template of this CreateIcx.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateIcx.


        :param template: The template of this CreateIcx.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._template = template

    @property
    def categories(self):
        """Gets the categories of this CreateIcx.  # noqa: E501


        :return: The categories of this CreateIcx.  # noqa: E501
        :rtype: list[CreateIcxCategoriesArray]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CreateIcx.


        :param categories: The categories of this CreateIcx.  # noqa: E501
        :type: list[CreateIcxCategoriesArray]
        """

        self._categories = categories

    @property
    def categories_rules(self):
        """Gets the categories_rules of this CreateIcx.  # noqa: E501


        :return: The categories_rules of this CreateIcx.  # noqa: E501
        :rtype: list[CreateIcxRulesArray]
        """
        return self._categories_rules

    @categories_rules.setter
    def categories_rules(self, categories_rules):
        """Sets the categories_rules of this CreateIcx.


        :param categories_rules: The categories_rules of this CreateIcx.  # noqa: E501
        :type: list[CreateIcxRulesArray]
        """

        self._categories_rules = categories_rules

    @property
    def categories_rules_filters(self):
        """Gets the categories_rules_filters of this CreateIcx.  # noqa: E501


        :return: The categories_rules_filters of this CreateIcx.  # noqa: E501
        :rtype: list[CreateIcxFiltersArray]
        """
        return self._categories_rules_filters

    @categories_rules_filters.setter
    def categories_rules_filters(self, categories_rules_filters):
        """Sets the categories_rules_filters of this CreateIcx.


        :param categories_rules_filters: The categories_rules_filters of this CreateIcx.  # noqa: E501
        :type: list[CreateIcxFiltersArray]
        """

        self._categories_rules_filters = categories_rules_filters

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
        if not isinstance(other, CreateIcx):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateIcx):
            return True

        return self.to_dict() != other.to_dict()
