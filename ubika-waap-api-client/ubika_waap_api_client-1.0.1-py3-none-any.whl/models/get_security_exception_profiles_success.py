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


class GetSecurityExceptionProfilesSuccess(object):
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
        'data': 'list[GetSecurityExceptionProfilesDataSuccessArray]',
        'data_rules': 'list[GetSecurityExceptionProfilesRulesSuccessArray]',
        'data_rules_conditions': 'list[GetSecurityExceptionProfilesConditionsSuccessArray]',
        'data_rules_matching_parts': 'list[GetSecurityExceptionProfilesMatchingPartsSuccessArray]'
    }

    attribute_map = {
        'data': 'data',
        'data_rules': 'data.rules',
        'data_rules_conditions': 'data.rules.conditions',
        'data_rules_matching_parts': 'data.rules.matchingParts'
    }

    def __init__(self, data=None, data_rules=None, data_rules_conditions=None, data_rules_matching_parts=None, local_vars_configuration=None):  # noqa: E501
        """GetSecurityExceptionProfilesSuccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._data_rules = None
        self._data_rules_conditions = None
        self._data_rules_matching_parts = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if data_rules is not None:
            self.data_rules = data_rules
        if data_rules_conditions is not None:
            self.data_rules_conditions = data_rules_conditions
        if data_rules_matching_parts is not None:
            self.data_rules_matching_parts = data_rules_matching_parts

    @property
    def data(self):
        """Gets the data of this GetSecurityExceptionProfilesSuccess.  # noqa: E501


        :return: The data of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :rtype: list[GetSecurityExceptionProfilesDataSuccessArray]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetSecurityExceptionProfilesSuccess.


        :param data: The data of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :type: list[GetSecurityExceptionProfilesDataSuccessArray]
        """

        self._data = data

    @property
    def data_rules(self):
        """Gets the data_rules of this GetSecurityExceptionProfilesSuccess.  # noqa: E501


        :return: The data_rules of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :rtype: list[GetSecurityExceptionProfilesRulesSuccessArray]
        """
        return self._data_rules

    @data_rules.setter
    def data_rules(self, data_rules):
        """Sets the data_rules of this GetSecurityExceptionProfilesSuccess.


        :param data_rules: The data_rules of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :type: list[GetSecurityExceptionProfilesRulesSuccessArray]
        """

        self._data_rules = data_rules

    @property
    def data_rules_conditions(self):
        """Gets the data_rules_conditions of this GetSecurityExceptionProfilesSuccess.  # noqa: E501


        :return: The data_rules_conditions of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :rtype: list[GetSecurityExceptionProfilesConditionsSuccessArray]
        """
        return self._data_rules_conditions

    @data_rules_conditions.setter
    def data_rules_conditions(self, data_rules_conditions):
        """Sets the data_rules_conditions of this GetSecurityExceptionProfilesSuccess.


        :param data_rules_conditions: The data_rules_conditions of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :type: list[GetSecurityExceptionProfilesConditionsSuccessArray]
        """

        self._data_rules_conditions = data_rules_conditions

    @property
    def data_rules_matching_parts(self):
        """Gets the data_rules_matching_parts of this GetSecurityExceptionProfilesSuccess.  # noqa: E501


        :return: The data_rules_matching_parts of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :rtype: list[GetSecurityExceptionProfilesMatchingPartsSuccessArray]
        """
        return self._data_rules_matching_parts

    @data_rules_matching_parts.setter
    def data_rules_matching_parts(self, data_rules_matching_parts):
        """Sets the data_rules_matching_parts of this GetSecurityExceptionProfilesSuccess.


        :param data_rules_matching_parts: The data_rules_matching_parts of this GetSecurityExceptionProfilesSuccess.  # noqa: E501
        :type: list[GetSecurityExceptionProfilesMatchingPartsSuccessArray]
        """

        self._data_rules_matching_parts = data_rules_matching_parts

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
        if not isinstance(other, GetSecurityExceptionProfilesSuccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSecurityExceptionProfilesSuccess):
            return True

        return self.to_dict() != other.to_dict()
