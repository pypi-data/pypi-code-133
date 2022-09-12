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


class PatchAccesslogprofileSuccessData(object):
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
        'type': 'str',
        'format': 'str',
        'used_by': 'list[PatchAccesslogprofileUsedBySuccessArray]',
        't_update': 'float',
        't_create': 'float'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'type': 'type',
        'format': 'format',
        'used_by': 'usedBy',
        't_update': 'tUpdate',
        't_create': 'tCreate'
    }

    def __init__(self, uid=None, name=None, type=None, format=None, used_by=None, t_update=None, t_create=None, local_vars_configuration=None):  # noqa: E501
        """PatchAccesslogprofileSuccessData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._type = None
        self._format = None
        self._used_by = None
        self._t_update = None
        self._t_create = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if used_by is not None:
            self.used_by = used_by
        if t_update is not None:
            self.t_update = t_update
        if t_create is not None:
            self.t_create = t_create

    @property
    def uid(self):
        """Gets the uid of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The uid of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PatchAccesslogprofileSuccessData.


        :param uid: The uid of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The name of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchAccesslogprofileSuccessData.


        :param name: The name of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The type of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatchAccesslogprofileSuccessData.


        :param type: The type of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """Gets the format of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The format of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PatchAccesslogprofileSuccessData.


        :param format: The format of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def used_by(self):
        """Gets the used_by of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The used_by of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: list[PatchAccesslogprofileUsedBySuccessArray]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this PatchAccesslogprofileSuccessData.


        :param used_by: The used_by of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: list[PatchAccesslogprofileUsedBySuccessArray]
        """

        self._used_by = used_by

    @property
    def t_update(self):
        """Gets the t_update of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The t_update of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: float
        """
        return self._t_update

    @t_update.setter
    def t_update(self, t_update):
        """Sets the t_update of this PatchAccesslogprofileSuccessData.


        :param t_update: The t_update of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: float
        """

        self._t_update = t_update

    @property
    def t_create(self):
        """Gets the t_create of this PatchAccesslogprofileSuccessData.  # noqa: E501


        :return: The t_create of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :rtype: float
        """
        return self._t_create

    @t_create.setter
    def t_create(self, t_create):
        """Sets the t_create of this PatchAccesslogprofileSuccessData.


        :param t_create: The t_create of this PatchAccesslogprofileSuccessData.  # noqa: E501
        :type: float
        """

        self._t_create = t_create

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
        if not isinstance(other, PatchAccesslogprofileSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchAccesslogprofileSuccessData):
            return True

        return self.to_dict() != other.to_dict()
