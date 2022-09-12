# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiskPerformanceDetails(object):
    """
    Representation of disk performance detail parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiskPerformanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disk_iops:
            The value to assign to the disk_iops property of this DiskPerformanceDetails.
        :type disk_iops: float

        :param disk_throughput_in_mbps:
            The value to assign to the disk_throughput_in_mbps property of this DiskPerformanceDetails.
        :type disk_throughput_in_mbps: float

        """
        self.swagger_types = {
            'disk_iops': 'float',
            'disk_throughput_in_mbps': 'float'
        }

        self.attribute_map = {
            'disk_iops': 'diskIops',
            'disk_throughput_in_mbps': 'diskThroughputInMbps'
        }

        self._disk_iops = None
        self._disk_throughput_in_mbps = None

    @property
    def disk_iops(self):
        """
        **[Required]** Gets the disk_iops of this DiskPerformanceDetails.
        Disk IOPS in thousands.


        :return: The disk_iops of this DiskPerformanceDetails.
        :rtype: float
        """
        return self._disk_iops

    @disk_iops.setter
    def disk_iops(self, disk_iops):
        """
        Sets the disk_iops of this DiskPerformanceDetails.
        Disk IOPS in thousands.


        :param disk_iops: The disk_iops of this DiskPerformanceDetails.
        :type: float
        """
        self._disk_iops = disk_iops

    @property
    def disk_throughput_in_mbps(self):
        """
        **[Required]** Gets the disk_throughput_in_mbps of this DiskPerformanceDetails.
        Disk Throughput in Mbps.


        :return: The disk_throughput_in_mbps of this DiskPerformanceDetails.
        :rtype: float
        """
        return self._disk_throughput_in_mbps

    @disk_throughput_in_mbps.setter
    def disk_throughput_in_mbps(self, disk_throughput_in_mbps):
        """
        Sets the disk_throughput_in_mbps of this DiskPerformanceDetails.
        Disk Throughput in Mbps.


        :param disk_throughput_in_mbps: The disk_throughput_in_mbps of this DiskPerformanceDetails.
        :type: float
        """
        self._disk_throughput_in_mbps = disk_throughput_in_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
