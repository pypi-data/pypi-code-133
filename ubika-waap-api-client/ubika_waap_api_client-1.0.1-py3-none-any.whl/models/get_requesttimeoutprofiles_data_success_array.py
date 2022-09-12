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


class GetRequesttimeoutprofilesDataSuccessArray(object):
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
        'header_timeout': 'str',
        'body_timeout': 'str',
        'header_rate': 'int',
        'body_rate': 'int',
        't_update': 'float',
        't_create': 'float'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'header_timeout': 'headerTimeout',
        'body_timeout': 'bodyTimeout',
        'header_rate': 'headerRate',
        'body_rate': 'bodyRate',
        't_update': 'tUpdate',
        't_create': 'tCreate'
    }

    def __init__(self, uid=None, name=None, header_timeout=None, body_timeout=None, header_rate=None, body_rate=None, t_update=None, t_create=None, local_vars_configuration=None):  # noqa: E501
        """GetRequesttimeoutprofilesDataSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._header_timeout = None
        self._body_timeout = None
        self._header_rate = None
        self._body_rate = None
        self._t_update = None
        self._t_create = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if header_timeout is not None:
            self.header_timeout = header_timeout
        if body_timeout is not None:
            self.body_timeout = body_timeout
        if header_rate is not None:
            self.header_rate = header_rate
        if body_rate is not None:
            self.body_rate = body_rate
        if t_update is not None:
            self.t_update = t_update
        if t_create is not None:
            self.t_create = t_create

    @property
    def uid(self):
        """Gets the uid of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The uid of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetRequesttimeoutprofilesDataSuccessArray.


        :param uid: The uid of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The name of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetRequesttimeoutprofilesDataSuccessArray.


        :param name: The name of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def header_timeout(self):
        """Gets the header_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The header_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._header_timeout

    @header_timeout.setter
    def header_timeout(self, header_timeout):
        """Sets the header_timeout of this GetRequesttimeoutprofilesDataSuccessArray.


        :param header_timeout: The header_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._header_timeout = header_timeout

    @property
    def body_timeout(self):
        """Gets the body_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The body_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._body_timeout

    @body_timeout.setter
    def body_timeout(self, body_timeout):
        """Sets the body_timeout of this GetRequesttimeoutprofilesDataSuccessArray.


        :param body_timeout: The body_timeout of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._body_timeout = body_timeout

    @property
    def header_rate(self):
        """Gets the header_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The header_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: int
        """
        return self._header_rate

    @header_rate.setter
    def header_rate(self, header_rate):
        """Sets the header_rate of this GetRequesttimeoutprofilesDataSuccessArray.


        :param header_rate: The header_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: int
        """

        self._header_rate = header_rate

    @property
    def body_rate(self):
        """Gets the body_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The body_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: int
        """
        return self._body_rate

    @body_rate.setter
    def body_rate(self, body_rate):
        """Sets the body_rate of this GetRequesttimeoutprofilesDataSuccessArray.


        :param body_rate: The body_rate of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: int
        """

        self._body_rate = body_rate

    @property
    def t_update(self):
        """Gets the t_update of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The t_update of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: float
        """
        return self._t_update

    @t_update.setter
    def t_update(self, t_update):
        """Sets the t_update of this GetRequesttimeoutprofilesDataSuccessArray.


        :param t_update: The t_update of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :type: float
        """

        self._t_update = t_update

    @property
    def t_create(self):
        """Gets the t_create of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501


        :return: The t_create of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
        :rtype: float
        """
        return self._t_create

    @t_create.setter
    def t_create(self, t_create):
        """Sets the t_create of this GetRequesttimeoutprofilesDataSuccessArray.


        :param t_create: The t_create of this GetRequesttimeoutprofilesDataSuccessArray.  # noqa: E501
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
        if not isinstance(other, GetRequesttimeoutprofilesDataSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetRequesttimeoutprofilesDataSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
