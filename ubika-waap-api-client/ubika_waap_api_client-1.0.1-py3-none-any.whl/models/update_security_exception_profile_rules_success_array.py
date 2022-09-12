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


class UpdateSecurityExceptionProfileRulesSuccessArray(object):
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
        'uid': 'str',
        'name': 'str',
        'enabled': 'bool',
        'description': 'str',
        'conditions': 'list[UpdateSecurityExceptionProfileConditionsSuccessArray]',
        'matching_parts': 'list[UpdateSecurityExceptionProfileMatchingPartsSuccessArray]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'enabled': 'enabled',
        'description': 'description',
        'conditions': 'conditions',
        'matching_parts': 'matchingParts'
    }

    def __init__(self, uid=None, name=None, enabled=None, description=None, conditions=None, matching_parts=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSecurityExceptionProfileRulesSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._enabled = None
        self._description = None
        self._conditions = None
        self._matching_parts = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if description is not None:
            self.description = description
        if conditions is not None:
            self.conditions = conditions
        if matching_parts is not None:
            self.matching_parts = matching_parts

    @property
    def uid(self):
        """Gets the uid of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The uid of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param uid: The uid of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The name of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param name: The name of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The enabled of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param enabled: The enabled of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def description(self):
        """Gets the description of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The description of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param description: The description of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def conditions(self):
        """Gets the conditions of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The conditions of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: list[UpdateSecurityExceptionProfileConditionsSuccessArray]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param conditions: The conditions of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: list[UpdateSecurityExceptionProfileConditionsSuccessArray]
        """

        self._conditions = conditions

    @property
    def matching_parts(self):
        """Gets the matching_parts of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501


        :return: The matching_parts of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :rtype: list[UpdateSecurityExceptionProfileMatchingPartsSuccessArray]
        """
        return self._matching_parts

    @matching_parts.setter
    def matching_parts(self, matching_parts):
        """Sets the matching_parts of this UpdateSecurityExceptionProfileRulesSuccessArray.


        :param matching_parts: The matching_parts of this UpdateSecurityExceptionProfileRulesSuccessArray.  # noqa: E501
        :type: list[UpdateSecurityExceptionProfileMatchingPartsSuccessArray]
        """

        self._matching_parts = matching_parts

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
        if not isinstance(other, UpdateSecurityExceptionProfileRulesSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSecurityExceptionProfileRulesSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
