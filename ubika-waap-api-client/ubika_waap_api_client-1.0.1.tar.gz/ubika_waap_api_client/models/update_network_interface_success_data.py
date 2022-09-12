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


class UpdateNetworkInterfaceSuccessData(object):
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
        'device': 'CreateApplianceSysctlProfile',
        'appliance': 'CreateApplianceSysctlProfile',
        'uid': 'str',
        'name': 'str',
        'ip': 'str',
        'netmask': 'str',
        'active': 'str',
        'used_by': 'list[UpdateNetworkInterfaceUsedBySuccessArray]',
        't_update': 'float'
    }

    attribute_map = {
        'device': 'device',
        'appliance': 'appliance',
        'uid': 'uid',
        'name': 'name',
        'ip': 'ip',
        'netmask': 'netmask',
        'active': 'active',
        'used_by': 'usedBy',
        't_update': 'tUpdate'
    }

    def __init__(self, device=None, appliance=None, uid=None, name=None, ip=None, netmask=None, active=None, used_by=None, t_update=None, local_vars_configuration=None):  # noqa: E501
        """UpdateNetworkInterfaceSuccessData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device = None
        self._appliance = None
        self._uid = None
        self._name = None
        self._ip = None
        self._netmask = None
        self._active = None
        self._used_by = None
        self._t_update = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if appliance is not None:
            self.appliance = appliance
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if netmask is not None:
            self.netmask = netmask
        if active is not None:
            self.active = active
        if used_by is not None:
            self.used_by = used_by
        if t_update is not None:
            self.t_update = t_update

    @property
    def device(self):
        """Gets the device of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The device of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this UpdateNetworkInterfaceSuccessData.


        :param device: The device of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._device = device

    @property
    def appliance(self):
        """Gets the appliance of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The appliance of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this UpdateNetworkInterfaceSuccessData.


        :param appliance: The appliance of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._appliance = appliance

    @property
    def uid(self):
        """Gets the uid of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The uid of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UpdateNetworkInterfaceSuccessData.


        :param uid: The uid of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The name of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkInterfaceSuccessData.


        :param name: The name of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The ip of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this UpdateNetworkInterfaceSuccessData.


        :param ip: The ip of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def netmask(self):
        """Gets the netmask of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The netmask of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this UpdateNetworkInterfaceSuccessData.


        :param netmask: The netmask of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def active(self):
        """Gets the active of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The active of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UpdateNetworkInterfaceSuccessData.


        :param active: The active of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def used_by(self):
        """Gets the used_by of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The used_by of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: list[UpdateNetworkInterfaceUsedBySuccessArray]
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        """Sets the used_by of this UpdateNetworkInterfaceSuccessData.


        :param used_by: The used_by of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :type: list[UpdateNetworkInterfaceUsedBySuccessArray]
        """

        self._used_by = used_by

    @property
    def t_update(self):
        """Gets the t_update of this UpdateNetworkInterfaceSuccessData.  # noqa: E501


        :return: The t_update of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
        :rtype: float
        """
        return self._t_update

    @t_update.setter
    def t_update(self, t_update):
        """Sets the t_update of this UpdateNetworkInterfaceSuccessData.


        :param t_update: The t_update of this UpdateNetworkInterfaceSuccessData.  # noqa: E501
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
        if not isinstance(other, UpdateNetworkInterfaceSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateNetworkInterfaceSuccessData):
            return True

        return self.to_dict() != other.to_dict()
