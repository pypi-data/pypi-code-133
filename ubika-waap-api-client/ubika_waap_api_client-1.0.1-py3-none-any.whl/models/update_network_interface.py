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


class UpdateNetworkInterface(object):
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
        'device': 'UpdateNetworkInterfaceDevice',
        'ip': 'str',
        'netmask': 'str',
        'active': 'str'
    }

    attribute_map = {
        'device': 'device',
        'ip': 'ip',
        'netmask': 'netmask',
        'active': 'active'
    }

    def __init__(self, device=None, ip=None, netmask=None, active=None, local_vars_configuration=None):  # noqa: E501
        """UpdateNetworkInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device = None
        self._ip = None
        self._netmask = None
        self._active = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if ip is not None:
            self.ip = ip
        if netmask is not None:
            self.netmask = netmask
        if active is not None:
            self.active = active

    @property
    def device(self):
        """Gets the device of this UpdateNetworkInterface.  # noqa: E501


        :return: The device of this UpdateNetworkInterface.  # noqa: E501
        :rtype: UpdateNetworkInterfaceDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this UpdateNetworkInterface.


        :param device: The device of this UpdateNetworkInterface.  # noqa: E501
        :type: UpdateNetworkInterfaceDevice
        """

        self._device = device

    @property
    def ip(self):
        """Gets the ip of this UpdateNetworkInterface.  # noqa: E501


        :return: The ip of this UpdateNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this UpdateNetworkInterface.


        :param ip: The ip of this UpdateNetworkInterface.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def netmask(self):
        """Gets the netmask of this UpdateNetworkInterface.  # noqa: E501


        :return: The netmask of this UpdateNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this UpdateNetworkInterface.


        :param netmask: The netmask of this UpdateNetworkInterface.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def active(self):
        """Gets the active of this UpdateNetworkInterface.  # noqa: E501


        :return: The active of this UpdateNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UpdateNetworkInterface.


        :param active: The active of this UpdateNetworkInterface.  # noqa: E501
        :type: str
        """

        self._active = active

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
        if not isinstance(other, UpdateNetworkInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateNetworkInterface):
            return True

        return self.to_dict() != other.to_dict()
