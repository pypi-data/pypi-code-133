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


class GetCACertificatesDataSuccessArray(object):
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
        'ca': 'list[GetCACertificatesCaSuccessArray]'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'ca': 'ca'
    }

    def __init__(self, uid=None, name=None, ca=None, local_vars_configuration=None):  # noqa: E501
        """GetCACertificatesDataSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._ca = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if ca is not None:
            self.ca = ca

    @property
    def uid(self):
        """Gets the uid of this GetCACertificatesDataSuccessArray.  # noqa: E501


        :return: The uid of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GetCACertificatesDataSuccessArray.


        :param uid: The uid of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this GetCACertificatesDataSuccessArray.  # noqa: E501


        :return: The name of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCACertificatesDataSuccessArray.


        :param name: The name of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ca(self):
        """Gets the ca of this GetCACertificatesDataSuccessArray.  # noqa: E501


        :return: The ca of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :rtype: list[GetCACertificatesCaSuccessArray]
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this GetCACertificatesDataSuccessArray.


        :param ca: The ca of this GetCACertificatesDataSuccessArray.  # noqa: E501
        :type: list[GetCACertificatesCaSuccessArray]
        """

        self._ca = ca

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
        if not isinstance(other, GetCACertificatesDataSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCACertificatesDataSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
