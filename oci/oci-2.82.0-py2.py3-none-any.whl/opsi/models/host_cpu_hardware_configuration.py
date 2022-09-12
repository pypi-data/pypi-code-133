# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostCpuHardwareConfiguration(HostConfigurationMetricGroup):
    """
    CPU Hardware Configuration metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostCpuHardwareConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostCpuHardwareConfiguration.metric_name` attribute
        of this class is ``HOST_CPU_HARDWARE_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostCpuHardwareConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostCpuHardwareConfiguration.
        :type time_collected: datetime

        :param total_sockets:
            The value to assign to the total_sockets property of this HostCpuHardwareConfiguration.
        :type total_sockets: int

        :param vendor_name:
            The value to assign to the vendor_name property of this HostCpuHardwareConfiguration.
        :type vendor_name: str

        :param frequency_in_mhz:
            The value to assign to the frequency_in_mhz property of this HostCpuHardwareConfiguration.
        :type frequency_in_mhz: float

        :param cache_in_mb:
            The value to assign to the cache_in_mb property of this HostCpuHardwareConfiguration.
        :type cache_in_mb: float

        :param cpu_implementation:
            The value to assign to the cpu_implementation property of this HostCpuHardwareConfiguration.
        :type cpu_implementation: str

        :param model:
            The value to assign to the model property of this HostCpuHardwareConfiguration.
        :type model: str

        :param cpu_family:
            The value to assign to the cpu_family property of this HostCpuHardwareConfiguration.
        :type cpu_family: str

        :param cores_per_socket:
            The value to assign to the cores_per_socket property of this HostCpuHardwareConfiguration.
        :type cores_per_socket: int

        :param threads_per_socket:
            The value to assign to the threads_per_socket property of this HostCpuHardwareConfiguration.
        :type threads_per_socket: int

        :param hyper_threading_enabled:
            The value to assign to the hyper_threading_enabled property of this HostCpuHardwareConfiguration.
        :type hyper_threading_enabled: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'total_sockets': 'int',
            'vendor_name': 'str',
            'frequency_in_mhz': 'float',
            'cache_in_mb': 'float',
            'cpu_implementation': 'str',
            'model': 'str',
            'cpu_family': 'str',
            'cores_per_socket': 'int',
            'threads_per_socket': 'int',
            'hyper_threading_enabled': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'total_sockets': 'totalSockets',
            'vendor_name': 'vendorName',
            'frequency_in_mhz': 'frequencyInMhz',
            'cache_in_mb': 'cacheInMB',
            'cpu_implementation': 'cpuImplementation',
            'model': 'model',
            'cpu_family': 'cpuFamily',
            'cores_per_socket': 'coresPerSocket',
            'threads_per_socket': 'threadsPerSocket',
            'hyper_threading_enabled': 'hyperThreadingEnabled'
        }

        self._metric_name = None
        self._time_collected = None
        self._total_sockets = None
        self._vendor_name = None
        self._frequency_in_mhz = None
        self._cache_in_mb = None
        self._cpu_implementation = None
        self._model = None
        self._cpu_family = None
        self._cores_per_socket = None
        self._threads_per_socket = None
        self._hyper_threading_enabled = None
        self._metric_name = 'HOST_CPU_HARDWARE_CONFIGURATION'

    @property
    def total_sockets(self):
        """
        Gets the total_sockets of this HostCpuHardwareConfiguration.
        Total number of CPU Sockets


        :return: The total_sockets of this HostCpuHardwareConfiguration.
        :rtype: int
        """
        return self._total_sockets

    @total_sockets.setter
    def total_sockets(self, total_sockets):
        """
        Sets the total_sockets of this HostCpuHardwareConfiguration.
        Total number of CPU Sockets


        :param total_sockets: The total_sockets of this HostCpuHardwareConfiguration.
        :type: int
        """
        self._total_sockets = total_sockets

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this HostCpuHardwareConfiguration.
        Name of the CPU vendor


        :return: The vendor_name of this HostCpuHardwareConfiguration.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this HostCpuHardwareConfiguration.
        Name of the CPU vendor


        :param vendor_name: The vendor_name of this HostCpuHardwareConfiguration.
        :type: str
        """
        self._vendor_name = vendor_name

    @property
    def frequency_in_mhz(self):
        """
        Gets the frequency_in_mhz of this HostCpuHardwareConfiguration.
        Clock frequency of the processor in megahertz


        :return: The frequency_in_mhz of this HostCpuHardwareConfiguration.
        :rtype: float
        """
        return self._frequency_in_mhz

    @frequency_in_mhz.setter
    def frequency_in_mhz(self, frequency_in_mhz):
        """
        Sets the frequency_in_mhz of this HostCpuHardwareConfiguration.
        Clock frequency of the processor in megahertz


        :param frequency_in_mhz: The frequency_in_mhz of this HostCpuHardwareConfiguration.
        :type: float
        """
        self._frequency_in_mhz = frequency_in_mhz

    @property
    def cache_in_mb(self):
        """
        Gets the cache_in_mb of this HostCpuHardwareConfiguration.
        Size of cache memory in megabytes


        :return: The cache_in_mb of this HostCpuHardwareConfiguration.
        :rtype: float
        """
        return self._cache_in_mb

    @cache_in_mb.setter
    def cache_in_mb(self, cache_in_mb):
        """
        Sets the cache_in_mb of this HostCpuHardwareConfiguration.
        Size of cache memory in megabytes


        :param cache_in_mb: The cache_in_mb of this HostCpuHardwareConfiguration.
        :type: float
        """
        self._cache_in_mb = cache_in_mb

    @property
    def cpu_implementation(self):
        """
        Gets the cpu_implementation of this HostCpuHardwareConfiguration.
        Model name of processor


        :return: The cpu_implementation of this HostCpuHardwareConfiguration.
        :rtype: str
        """
        return self._cpu_implementation

    @cpu_implementation.setter
    def cpu_implementation(self, cpu_implementation):
        """
        Sets the cpu_implementation of this HostCpuHardwareConfiguration.
        Model name of processor


        :param cpu_implementation: The cpu_implementation of this HostCpuHardwareConfiguration.
        :type: str
        """
        self._cpu_implementation = cpu_implementation

    @property
    def model(self):
        """
        Gets the model of this HostCpuHardwareConfiguration.
        CPU model


        :return: The model of this HostCpuHardwareConfiguration.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this HostCpuHardwareConfiguration.
        CPU model


        :param model: The model of this HostCpuHardwareConfiguration.
        :type: str
        """
        self._model = model

    @property
    def cpu_family(self):
        """
        Gets the cpu_family of this HostCpuHardwareConfiguration.
        Type of processor in the system


        :return: The cpu_family of this HostCpuHardwareConfiguration.
        :rtype: str
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """
        Sets the cpu_family of this HostCpuHardwareConfiguration.
        Type of processor in the system


        :param cpu_family: The cpu_family of this HostCpuHardwareConfiguration.
        :type: str
        """
        self._cpu_family = cpu_family

    @property
    def cores_per_socket(self):
        """
        Gets the cores_per_socket of this HostCpuHardwareConfiguration.
        Number of cores per socket


        :return: The cores_per_socket of this HostCpuHardwareConfiguration.
        :rtype: int
        """
        return self._cores_per_socket

    @cores_per_socket.setter
    def cores_per_socket(self, cores_per_socket):
        """
        Sets the cores_per_socket of this HostCpuHardwareConfiguration.
        Number of cores per socket


        :param cores_per_socket: The cores_per_socket of this HostCpuHardwareConfiguration.
        :type: int
        """
        self._cores_per_socket = cores_per_socket

    @property
    def threads_per_socket(self):
        """
        Gets the threads_per_socket of this HostCpuHardwareConfiguration.
        Number of threads per socket


        :return: The threads_per_socket of this HostCpuHardwareConfiguration.
        :rtype: int
        """
        return self._threads_per_socket

    @threads_per_socket.setter
    def threads_per_socket(self, threads_per_socket):
        """
        Sets the threads_per_socket of this HostCpuHardwareConfiguration.
        Number of threads per socket


        :param threads_per_socket: The threads_per_socket of this HostCpuHardwareConfiguration.
        :type: int
        """
        self._threads_per_socket = threads_per_socket

    @property
    def hyper_threading_enabled(self):
        """
        Gets the hyper_threading_enabled of this HostCpuHardwareConfiguration.
        Indicates if hyper-threading is enabled or not


        :return: The hyper_threading_enabled of this HostCpuHardwareConfiguration.
        :rtype: str
        """
        return self._hyper_threading_enabled

    @hyper_threading_enabled.setter
    def hyper_threading_enabled(self, hyper_threading_enabled):
        """
        Sets the hyper_threading_enabled of this HostCpuHardwareConfiguration.
        Indicates if hyper-threading is enabled or not


        :param hyper_threading_enabled: The hyper_threading_enabled of this HostCpuHardwareConfiguration.
        :type: str
        """
        self._hyper_threading_enabled = hyper_threading_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
