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


class CreateSecondaryTunnelSuccessData(object):
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
        'active': 'str',
        'reverse_proxy': 'CreateApplianceSysctlProfile',
        'parent_tunnel': 'CreateApplianceSysctlProfile',
        'in_network_interface': 'CreateApplianceSysctlProfile',
        't_update': 'float'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'active': 'active',
        'reverse_proxy': 'reverseProxy',
        'parent_tunnel': 'parentTunnel',
        'in_network_interface': 'inNetworkInterface',
        't_update': 'tUpdate'
    }

    def __init__(self, uid=None, name=None, active=None, reverse_proxy=None, parent_tunnel=None, in_network_interface=None, t_update=None, local_vars_configuration=None):  # noqa: E501
        """CreateSecondaryTunnelSuccessData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._active = None
        self._reverse_proxy = None
        self._parent_tunnel = None
        self._in_network_interface = None
        self._t_update = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if reverse_proxy is not None:
            self.reverse_proxy = reverse_proxy
        if parent_tunnel is not None:
            self.parent_tunnel = parent_tunnel
        if in_network_interface is not None:
            self.in_network_interface = in_network_interface
        if t_update is not None:
            self.t_update = t_update

    @property
    def uid(self):
        """Gets the uid of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The uid of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this CreateSecondaryTunnelSuccessData.


        :param uid: The uid of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The name of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecondaryTunnelSuccessData.


        :param name: The name of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The active of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this CreateSecondaryTunnelSuccessData.


        :param active: The active of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def reverse_proxy(self):
        """Gets the reverse_proxy of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The reverse_proxy of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._reverse_proxy

    @reverse_proxy.setter
    def reverse_proxy(self, reverse_proxy):
        """Sets the reverse_proxy of this CreateSecondaryTunnelSuccessData.


        :param reverse_proxy: The reverse_proxy of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._reverse_proxy = reverse_proxy

    @property
    def parent_tunnel(self):
        """Gets the parent_tunnel of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The parent_tunnel of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._parent_tunnel

    @parent_tunnel.setter
    def parent_tunnel(self, parent_tunnel):
        """Sets the parent_tunnel of this CreateSecondaryTunnelSuccessData.


        :param parent_tunnel: The parent_tunnel of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._parent_tunnel = parent_tunnel

    @property
    def in_network_interface(self):
        """Gets the in_network_interface of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The in_network_interface of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._in_network_interface

    @in_network_interface.setter
    def in_network_interface(self, in_network_interface):
        """Sets the in_network_interface of this CreateSecondaryTunnelSuccessData.


        :param in_network_interface: The in_network_interface of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._in_network_interface = in_network_interface

    @property
    def t_update(self):
        """Gets the t_update of this CreateSecondaryTunnelSuccessData.  # noqa: E501


        :return: The t_update of this CreateSecondaryTunnelSuccessData.  # noqa: E501
        :rtype: float
        """
        return self._t_update

    @t_update.setter
    def t_update(self, t_update):
        """Sets the t_update of this CreateSecondaryTunnelSuccessData.


        :param t_update: The t_update of this CreateSecondaryTunnelSuccessData.  # noqa: E501
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
        if not isinstance(other, CreateSecondaryTunnelSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSecondaryTunnelSuccessData):
            return True

        return self.to_dict() != other.to_dict()
