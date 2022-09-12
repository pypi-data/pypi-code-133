# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostNetworkConfiguration(HostConfigurationMetricGroup):
    """
    Network Configuration metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostNetworkConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostNetworkConfiguration.metric_name` attribute
        of this class is ``HOST_NETWORK_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostNetworkConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostNetworkConfiguration.
        :type time_collected: datetime

        :param interface_name:
            The value to assign to the interface_name property of this HostNetworkConfiguration.
        :type interface_name: str

        :param ip_address:
            The value to assign to the ip_address property of this HostNetworkConfiguration.
        :type ip_address: str

        :param mac_address:
            The value to assign to the mac_address property of this HostNetworkConfiguration.
        :type mac_address: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'interface_name': 'str',
            'ip_address': 'str',
            'mac_address': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'interface_name': 'interfaceName',
            'ip_address': 'ipAddress',
            'mac_address': 'macAddress'
        }

        self._metric_name = None
        self._time_collected = None
        self._interface_name = None
        self._ip_address = None
        self._mac_address = None
        self._metric_name = 'HOST_NETWORK_CONFIGURATION'

    @property
    def interface_name(self):
        """
        **[Required]** Gets the interface_name of this HostNetworkConfiguration.
        Name of the network interface


        :return: The interface_name of this HostNetworkConfiguration.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this HostNetworkConfiguration.
        Name of the network interface


        :param interface_name: The interface_name of this HostNetworkConfiguration.
        :type: str
        """
        self._interface_name = interface_name

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this HostNetworkConfiguration.
        IP address (IPv4 or IPv6) of the network interface


        :return: The ip_address of this HostNetworkConfiguration.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this HostNetworkConfiguration.
        IP address (IPv4 or IPv6) of the network interface


        :param ip_address: The ip_address of this HostNetworkConfiguration.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def mac_address(self):
        """
        Gets the mac_address of this HostNetworkConfiguration.
        MAC address of the network interface. MAC address is a 12-digit hexadecimal number separated by colons or dashes or dots. Following formats are accepted: MM:MM:MM:SS:SS:SS, MM-MM-MM-SS-SS-SS, MM.MM.MM.SS.SS.SS, MMM:MMM:SSS:SSS, MMM-MMM-SSS-SSS, MMM.MMM.SSS.SSS, MMMM:MMSS:SSSS, MMMM-MMSS-SSSS, MMMM.MMSS.SSSS


        :return: The mac_address of this HostNetworkConfiguration.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this HostNetworkConfiguration.
        MAC address of the network interface. MAC address is a 12-digit hexadecimal number separated by colons or dashes or dots. Following formats are accepted: MM:MM:MM:SS:SS:SS, MM-MM-MM-SS-SS-SS, MM.MM.MM.SS.SS.SS, MMM:MMM:SSS:SSS, MMM-MMM-SSS-SSS, MMM.MMM.SSS.SSS, MMMM:MMSS:SSSS, MMMM-MMSS-SSSS, MMMM.MMSS.SSSS


        :param mac_address: The mac_address of this HostNetworkConfiguration.
        :type: str
        """
        self._mac_address = mac_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
