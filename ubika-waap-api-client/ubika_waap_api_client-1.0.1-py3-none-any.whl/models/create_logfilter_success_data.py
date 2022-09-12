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


class CreateLogfilterSuccessData(object):
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
        'read_only': 'bool',
        'used_by': 'list[CreateLogfilterUsedBySuccessArray]',
        't_update': 'float'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'description': 'description',
        'read_only': 'readOnly',
        'used_by': 'usedBy',
        't_update': 'tUpdate'
    }

    def __init__(self, uid=None, name=None, description=None, read_only=None, used_by=None, t_update=None, local_vars_configuration=None):  # noqa: E501
        """CreateLogfilterSuccessData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._description = None
        self._read_only = None
        self._used_by = None
        self._t_update = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if read_only is not None:
            self.read_only = read_only
        if used_by is not None:
            self.used_by = used_by
        if t_update is not None:
            self.t_update = t_update

    @property
    def uid(self):
        """Gets the uid of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The uid of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CreateLogfilterSuccessData.


        :param uid: The uid of this CreateLogfilterSuccessData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The name of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLogfilterSuccessData.


        :param name: The name of this CreateLogfilterSuccessData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The description of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLogfilterSuccessData.


        :param description: The description of this CreateLogfilterSuccessData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def read_only(self):
        """Gets the read_only of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The read_only of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this CreateLogfilterSuccessData.


        :param read_only: The read_only of this CreateLogfilterSuccessData.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def used_by(self):
        """Gets the used_by of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The used_by of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: list[CreateLogfilterUsedBySuccessArray]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this CreateLogfilterSuccessData.


        :param used_by: The used_by of this CreateLogfilterSuccessData.  # noqa: E501
        :type: list[CreateLogfilterUsedBySuccessArray]
        """

        self._used_by = used_by

    @property
    def t_update(self):
        """Gets the t_update of this CreateLogfilterSuccessData.  # noqa: E501


        :return: The t_update of this CreateLogfilterSuccessData.  # noqa: E501
        :rtype: float
        """
        return self._t_update

    @t_update.setter
    def t_update(self, t_update):
        """Sets the t_update of this CreateLogfilterSuccessData.


        :param t_update: The t_update of this CreateLogfilterSuccessData.  # noqa: E501
        :type: float
        """

        self._t_update = t_update

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
        if not isinstance(other, CreateLogfilterSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLogfilterSuccessData):
            return True

        return self.to_dict() != other.to_dict()
