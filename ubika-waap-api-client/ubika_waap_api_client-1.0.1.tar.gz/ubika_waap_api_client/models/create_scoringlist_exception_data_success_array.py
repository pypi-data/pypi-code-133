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


class CreateScoringlistExceptionDataSuccessArray(object):
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
        'rule_uid': 'str',
        'description': 'str',
        'type': 'str',
        'path': 'str',
        'case_sensitive': 'bool',
        'negative': 'bool'
    }

    attribute_map = {
        'uid': 'uid',
        'rule_uid': 'ruleUid',
        'description': 'description',
        'type': 'type',
        'path': 'path',
        'case_sensitive': 'caseSensitive',
        'negative': 'negative'
    }

    def __init__(self, uid=None, rule_uid=None, description=None, type=None, path=None, case_sensitive=None, negative=None, local_vars_configuration=None):  # noqa: E501
        """CreateScoringlistExceptionDataSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._rule_uid = None
        self._description = None
        self._type = None
        self._path = None
        self._case_sensitive = None
        self._negative = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if rule_uid is not None:
            self.rule_uid = rule_uid
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if negative is not None:
            self.negative = negative

    @property
    def uid(self):
        """Gets the uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CreateScoringlistExceptionDataSuccessArray.


        :param uid: The uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def rule_uid(self):
        """Gets the rule_uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The rule_uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._rule_uid

    @rule_uid.setter
    def rule_uid(self, rule_uid):
        """Sets the rule_uid of this CreateScoringlistExceptionDataSuccessArray.


        :param rule_uid: The rule_uid of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._rule_uid = rule_uid

    @property
    def description(self):
        """Gets the description of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The description of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateScoringlistExceptionDataSuccessArray.


        :param description: The description of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The type of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateScoringlistExceptionDataSuccessArray.


        :param type: The type of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def path(self):
        """Gets the path of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The path of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreateScoringlistExceptionDataSuccessArray.


        :param path: The path of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The case_sensitive of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this CreateScoringlistExceptionDataSuccessArray.


        :param case_sensitive: The case_sensitive of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def negative(self):
        """Gets the negative of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501


        :return: The negative of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this CreateScoringlistExceptionDataSuccessArray.


        :param negative: The negative of this CreateScoringlistExceptionDataSuccessArray.  # noqa: E501
        :type: bool
        """

        self._negative = negative

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
        if not isinstance(other, CreateScoringlistExceptionDataSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateScoringlistExceptionDataSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
