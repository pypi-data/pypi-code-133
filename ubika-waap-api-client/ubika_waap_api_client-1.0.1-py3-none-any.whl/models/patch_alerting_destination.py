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


class PatchAlertingDestination(object):
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
        'smtp_config': 'CreateAlertingDestinationsSMTPConfig',
        'syslog_config': 'CreateAlertingDestinationsSyslogConfig',
        'snmp_config': 'CreateAlertingDestinationsSNMPConfig'
    }

    attribute_map = {
        'name': 'name',
        'smtp_config': 'SMTPConfig',
        'syslog_config': 'syslogConfig',
        'snmp_config': 'SNMPConfig'
    }

    def __init__(self, name=None, smtp_config=None, syslog_config=None, snmp_config=None, local_vars_configuration=None):  # noqa: E501
        """PatchAlertingDestination - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._smtp_config = None
        self._syslog_config = None
        self._snmp_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if smtp_config is not None:
            self.smtp_config = smtp_config
        if syslog_config is not None:
            self.syslog_config = syslog_config
        if snmp_config is not None:
            self.snmp_config = snmp_config

    @property
    def name(self):
        """Gets the name of this PatchAlertingDestination.  # noqa: E501


        :return: The name of this PatchAlertingDestination.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchAlertingDestination.


        :param name: The name of this PatchAlertingDestination.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def smtp_config(self):
        """Gets the smtp_config of this PatchAlertingDestination.  # noqa: E501


        :return: The smtp_config of this PatchAlertingDestination.  # noqa: E501
        :rtype: CreateAlertingDestinationsSMTPConfig
        """
        return self._smtp_config

    @smtp_config.setter
    def smtp_config(self, smtp_config):
        """Sets the smtp_config of this PatchAlertingDestination.


        :param smtp_config: The smtp_config of this PatchAlertingDestination.  # noqa: E501
        :type: CreateAlertingDestinationsSMTPConfig
        """

        self._smtp_config = smtp_config

    @property
    def syslog_config(self):
        """Gets the syslog_config of this PatchAlertingDestination.  # noqa: E501


        :return: The syslog_config of this PatchAlertingDestination.  # noqa: E501
        :rtype: CreateAlertingDestinationsSyslogConfig
        """
        return self._syslog_config

    @syslog_config.setter
    def syslog_config(self, syslog_config):
        """Sets the syslog_config of this PatchAlertingDestination.


        :param syslog_config: The syslog_config of this PatchAlertingDestination.  # noqa: E501
        :type: CreateAlertingDestinationsSyslogConfig
        """

        self._syslog_config = syslog_config

    @property
    def snmp_config(self):
        """Gets the snmp_config of this PatchAlertingDestination.  # noqa: E501


        :return: The snmp_config of this PatchAlertingDestination.  # noqa: E501
        :rtype: CreateAlertingDestinationsSNMPConfig
        """
        return self._snmp_config

    @snmp_config.setter
    def snmp_config(self, snmp_config):
        """Sets the snmp_config of this PatchAlertingDestination.


        :param snmp_config: The snmp_config of this PatchAlertingDestination.  # noqa: E501
        :type: CreateAlertingDestinationsSNMPConfig
        """

        self._snmp_config = snmp_config

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
        if not isinstance(other, PatchAlertingDestination):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchAlertingDestination):
            return True

        return self.to_dict() != other.to_dict()
