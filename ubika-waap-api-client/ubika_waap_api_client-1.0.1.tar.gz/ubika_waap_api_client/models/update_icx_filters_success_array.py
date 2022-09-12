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


class UpdateIcxFiltersSuccessArray(object):
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
        'key': 'str',
        'value': 'str',
        'key_type': 'str',
        'value_type': 'str',
        'key_condition': 'str',
        'value_condition': 'str'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'value': 'value',
        'key_type': 'keyType',
        'value_type': 'valueType',
        'key_condition': 'keyCondition',
        'value_condition': 'valueCondition'
    }

    def __init__(self, name=None, key=None, value=None, key_type=None, value_type=None, key_condition=None, value_condition=None, local_vars_configuration=None):  # noqa: E501
        """UpdateIcxFiltersSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._key = None
        self._value = None
        self._key_type = None
        self._value_type = None
        self._key_condition = None
        self._value_condition = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if key_type is not None:
            self.key_type = key_type
        if value_type is not None:
            self.value_type = value_type
        if key_condition is not None:
            self.key_condition = key_condition
        if value_condition is not None:
            self.value_condition = value_condition

    @property
    def name(self):
        """Gets the name of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The name of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateIcxFiltersSuccessArray.


        :param name: The name of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The key of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateIcxFiltersSuccessArray.


        :param key: The key of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The value of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateIcxFiltersSuccessArray.


        :param value: The value of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def key_type(self):
        """Gets the key_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The key_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this UpdateIcxFiltersSuccessArray.


        :param key_type: The key_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def value_type(self):
        """Gets the value_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The value_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this UpdateIcxFiltersSuccessArray.


        :param value_type: The value_type of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def key_condition(self):
        """Gets the key_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The key_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._key_condition

    @key_condition.setter
    def key_condition(self, key_condition):
        """Sets the key_condition of this UpdateIcxFiltersSuccessArray.


        :param key_condition: The key_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._key_condition = key_condition

    @property
    def value_condition(self):
        """Gets the value_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501


        :return: The value_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._value_condition

    @value_condition.setter
    def value_condition(self, value_condition):
        """Sets the value_condition of this UpdateIcxFiltersSuccessArray.


        :param value_condition: The value_condition of this UpdateIcxFiltersSuccessArray.  # noqa: E501
        :type: str
        """

        self._value_condition = value_condition

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
        if not isinstance(other, UpdateIcxFiltersSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateIcxFiltersSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
