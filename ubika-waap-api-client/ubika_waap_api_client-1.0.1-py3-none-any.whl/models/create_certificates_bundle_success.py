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


class CreateCertificatesBundleSuccess(object):
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
        'data': 'CreateCertificatesBundleSuccessData',
        'data_ca': 'list[CreateCertificatesBundleCaSuccessArray]',
        'data_ca_ocsp': 'list[CreateCertificatesBundleCaOCSPSuccessArray]',
        'data_crl': 'list[CreateCertificatesBundleCrlSuccessArray]'
    }

    attribute_map = {
        'data': 'data',
        'data_ca': 'data.ca',
        'data_ca_ocsp': 'data.caOCSP',
        'data_crl': 'data.crl'
    }

    def __init__(self, data=None, data_ca=None, data_ca_ocsp=None, data_crl=None, local_vars_configuration=None):  # noqa: E501
        """CreateCertificatesBundleSuccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._data_ca = None
        self._data_ca_ocsp = None
        self._data_crl = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if data_ca is not None:
            self.data_ca = data_ca
        if data_ca_ocsp is not None:
            self.data_ca_ocsp = data_ca_ocsp
        if data_crl is not None:
            self.data_crl = data_crl

    @property
    def data(self):
        """Gets the data of this CreateCertificatesBundleSuccess.  # noqa: E501


        :return: The data of this CreateCertificatesBundleSuccess.  # noqa: E501
        :rtype: CreateCertificatesBundleSuccessData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateCertificatesBundleSuccess.


        :param data: The data of this CreateCertificatesBundleSuccess.  # noqa: E501
        :type: CreateCertificatesBundleSuccessData
        """

        self._data = data

    @property
    def data_ca(self):
        """Gets the data_ca of this CreateCertificatesBundleSuccess.  # noqa: E501


        :return: The data_ca of this CreateCertificatesBundleSuccess.  # noqa: E501
        :rtype: list[CreateCertificatesBundleCaSuccessArray]
        """
        return self._data_ca

    @data_ca.setter
    def data_ca(self, data_ca):
        """Sets the data_ca of this CreateCertificatesBundleSuccess.


        :param data_ca: The data_ca of this CreateCertificatesBundleSuccess.  # noqa: E501
        :type: list[CreateCertificatesBundleCaSuccessArray]
        """

        self._data_ca = data_ca

    @property
    def data_ca_ocsp(self):
        """Gets the data_ca_ocsp of this CreateCertificatesBundleSuccess.  # noqa: E501


        :return: The data_ca_ocsp of this CreateCertificatesBundleSuccess.  # noqa: E501
        :rtype: list[CreateCertificatesBundleCaOCSPSuccessArray]
        """
        return self._data_ca_ocsp

    @data_ca_ocsp.setter
    def data_ca_ocsp(self, data_ca_ocsp):
        """Sets the data_ca_ocsp of this CreateCertificatesBundleSuccess.


        :param data_ca_ocsp: The data_ca_ocsp of this CreateCertificatesBundleSuccess.  # noqa: E501
        :type: list[CreateCertificatesBundleCaOCSPSuccessArray]
        """

        self._data_ca_ocsp = data_ca_ocsp

    @property
    def data_crl(self):
        """Gets the data_crl of this CreateCertificatesBundleSuccess.  # noqa: E501


        :return: The data_crl of this CreateCertificatesBundleSuccess.  # noqa: E501
        :rtype: list[CreateCertificatesBundleCrlSuccessArray]
        """
        return self._data_crl

    @data_crl.setter
    def data_crl(self, data_crl):
        """Sets the data_crl of this CreateCertificatesBundleSuccess.


        :param data_crl: The data_crl of this CreateCertificatesBundleSuccess.  # noqa: E501
        :type: list[CreateCertificatesBundleCrlSuccessArray]
        """

        self._data_crl = data_crl

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
        if not isinstance(other, CreateCertificatesBundleSuccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCertificatesBundleSuccess):
            return True

        return self.to_dict() != other.to_dict()
