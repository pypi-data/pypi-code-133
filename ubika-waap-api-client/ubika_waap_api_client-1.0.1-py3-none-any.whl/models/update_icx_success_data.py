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


class UpdateIcxSuccessData(object):
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
        'description': 'str',
        'editable': 'bool',
        'legacy_resolve': 'bool',
        'categories': 'list[UpdateIcxCategoriesSuccessArray]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'description': 'description',
        'editable': 'editable',
        'legacy_resolve': 'legacyResolve',
        'categories': 'categories'
    }

    def __init__(self, uid=None, name=None, description=None, editable=None, legacy_resolve=None, categories=None, local_vars_configuration=None):  # noqa: E501
        """UpdateIcxSuccessData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._description = None
        self._editable = None
        self._legacy_resolve = None
        self._categories = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if editable is not None:
            self.editable = editable
        if legacy_resolve is not None:
            self.legacy_resolve = legacy_resolve
        if categories is not None:
            self.categories = categories

    @property
    def uid(self):
        """Gets the uid of this UpdateIcxSuccessData.  # noqa: E501


        :return: The uid of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UpdateIcxSuccessData.


        :param uid: The uid of this UpdateIcxSuccessData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this UpdateIcxSuccessData.  # noqa: E501


        :return: The name of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateIcxSuccessData.


        :param name: The name of this UpdateIcxSuccessData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateIcxSuccessData.  # noqa: E501


        :return: The description of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateIcxSuccessData.


        :param description: The description of this UpdateIcxSuccessData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def editable(self):
        """Gets the editable of this UpdateIcxSuccessData.  # noqa: E501


        :return: The editable of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this UpdateIcxSuccessData.


        :param editable: The editable of this UpdateIcxSuccessData.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def legacy_resolve(self):
        """Gets the legacy_resolve of this UpdateIcxSuccessData.  # noqa: E501


        :return: The legacy_resolve of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: bool
        """
        return self._legacy_resolve

    @legacy_resolve.setter
    def legacy_resolve(self, legacy_resolve):
        """Sets the legacy_resolve of this UpdateIcxSuccessData.


        :param legacy_resolve: The legacy_resolve of this UpdateIcxSuccessData.  # noqa: E501
        :type: bool
        """

        self._legacy_resolve = legacy_resolve

    @property
    def categories(self):
        """Gets the categories of this UpdateIcxSuccessData.  # noqa: E501


        :return: The categories of this UpdateIcxSuccessData.  # noqa: E501
        :rtype: list[UpdateIcxCategoriesSuccessArray]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this UpdateIcxSuccessData.


        :param categories: The categories of this UpdateIcxSuccessData.  # noqa: E501
        :type: list[UpdateIcxCategoriesSuccessArray]
        """

        self._categories = categories

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
        if not isinstance(other, UpdateIcxSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateIcxSuccessData):
            return True

        return self.to_dict() != other.to_dict()
