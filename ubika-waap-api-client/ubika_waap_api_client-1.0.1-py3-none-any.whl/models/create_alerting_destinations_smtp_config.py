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


class CreateAlertingDestinationsSMTPConfig(object):
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
        'ip': 'str',
        'port': 'int',
        'login': 'str',
        '_pass': 'str',
        'mail_from': 'str',
        'mail_to': 'str',
        'mail_crypt_protocol': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'login': 'login',
        '_pass': 'pass',
        'mail_from': 'mailFrom',
        'mail_to': 'mailTo',
        'mail_crypt_protocol': 'mailCryptProtocol'
    }

    def __init__(self, ip=None, port=None, login=None, _pass=None, mail_from=None, mail_to=None, mail_crypt_protocol=None, local_vars_configuration=None):  # noqa: E501
        """CreateAlertingDestinationsSMTPConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._port = None
        self._login = None
        self.__pass = None
        self._mail_from = None
        self._mail_to = None
        self._mail_crypt_protocol = None
        self.discriminator = None

        self.ip = ip
        self.port = port
        if login is not None:
            self.login = login
        if _pass is not None:
            self._pass = _pass
        self.mail_from = mail_from
        self.mail_to = mail_to
        self.mail_crypt_protocol = mail_crypt_protocol

    @property
    def ip(self):
        """Gets the ip of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The ip of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CreateAlertingDestinationsSMTPConfig.


        :param ip: The ip of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The port of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateAlertingDestinationsSMTPConfig.


        :param port: The port of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def login(self):
        """Gets the login of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The login of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this CreateAlertingDestinationsSMTPConfig.


        :param login: The login of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def _pass(self):
        """Gets the _pass of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The _pass of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this CreateAlertingDestinationsSMTPConfig.


        :param _pass: The _pass of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """

        self.__pass = _pass

    @property
    def mail_from(self):
        """Gets the mail_from of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The mail_from of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self._mail_from

    @mail_from.setter
    def mail_from(self, mail_from):
        """Sets the mail_from of this CreateAlertingDestinationsSMTPConfig.


        :param mail_from: The mail_from of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mail_from is None:  # noqa: E501
            raise ValueError("Invalid value for `mail_from`, must not be `None`")  # noqa: E501

        self._mail_from = mail_from

    @property
    def mail_to(self):
        """Gets the mail_to of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The mail_to of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self._mail_to

    @mail_to.setter
    def mail_to(self, mail_to):
        """Sets the mail_to of this CreateAlertingDestinationsSMTPConfig.


        :param mail_to: The mail_to of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mail_to is None:  # noqa: E501
            raise ValueError("Invalid value for `mail_to`, must not be `None`")  # noqa: E501

        self._mail_to = mail_to

    @property
    def mail_crypt_protocol(self):
        """Gets the mail_crypt_protocol of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501


        :return: The mail_crypt_protocol of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :rtype: str
        """
        return self._mail_crypt_protocol

    @mail_crypt_protocol.setter
    def mail_crypt_protocol(self, mail_crypt_protocol):
        """Sets the mail_crypt_protocol of this CreateAlertingDestinationsSMTPConfig.


        :param mail_crypt_protocol: The mail_crypt_protocol of this CreateAlertingDestinationsSMTPConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mail_crypt_protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `mail_crypt_protocol`, must not be `None`")  # noqa: E501

        self._mail_crypt_protocol = mail_crypt_protocol

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
        if not isinstance(other, CreateAlertingDestinationsSMTPConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAlertingDestinationsSMTPConfig):
            return True

        return self.to_dict() != other.to_dict()
