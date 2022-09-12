# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FlexComponentSummary(object):
    """
    The Flex Components for a DB system. The Flex Component determines resources to allocate to the DB system -  CPU cores, memory and storage for Flex shapes.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
    If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FlexComponentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FlexComponentSummary.
        :type name: str

        :param minimum_core_count:
            The value to assign to the minimum_core_count property of this FlexComponentSummary.
        :type minimum_core_count: int

        :param available_core_count:
            The value to assign to the available_core_count property of this FlexComponentSummary.
        :type available_core_count: int

        :param available_db_storage_in_gbs:
            The value to assign to the available_db_storage_in_gbs property of this FlexComponentSummary.
        :type available_db_storage_in_gbs: int

        """
        self.swagger_types = {
            'name': 'str',
            'minimum_core_count': 'int',
            'available_core_count': 'int',
            'available_db_storage_in_gbs': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'minimum_core_count': 'minimumCoreCount',
            'available_core_count': 'availableCoreCount',
            'available_db_storage_in_gbs': 'availableDbStorageInGBs'
        }

        self._name = None
        self._minimum_core_count = None
        self._available_core_count = None
        self._available_db_storage_in_gbs = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this FlexComponentSummary.
        The name of the Flex Component used for the DB system.


        :return: The name of this FlexComponentSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FlexComponentSummary.
        The name of the Flex Component used for the DB system.


        :param name: The name of this FlexComponentSummary.
        :type: str
        """
        self._name = name

    @property
    def minimum_core_count(self):
        """
        Gets the minimum_core_count of this FlexComponentSummary.
        The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.


        :return: The minimum_core_count of this FlexComponentSummary.
        :rtype: int
        """
        return self._minimum_core_count

    @minimum_core_count.setter
    def minimum_core_count(self, minimum_core_count):
        """
        Sets the minimum_core_count of this FlexComponentSummary.
        The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.


        :param minimum_core_count: The minimum_core_count of this FlexComponentSummary.
        :type: int
        """
        self._minimum_core_count = minimum_core_count

    @property
    def available_core_count(self):
        """
        Gets the available_core_count of this FlexComponentSummary.
        The maximum number of CPU cores that can ben enabled on the DB Server for this Flex Component.


        :return: The available_core_count of this FlexComponentSummary.
        :rtype: int
        """
        return self._available_core_count

    @available_core_count.setter
    def available_core_count(self, available_core_count):
        """
        Sets the available_core_count of this FlexComponentSummary.
        The maximum number of CPU cores that can ben enabled on the DB Server for this Flex Component.


        :param available_core_count: The available_core_count of this FlexComponentSummary.
        :type: int
        """
        self._available_core_count = available_core_count

    @property
    def available_db_storage_in_gbs(self):
        """
        Gets the available_db_storage_in_gbs of this FlexComponentSummary.
        The maximum  storage that can be enabled on the Storage Server for this Flex Component.


        :return: The available_db_storage_in_gbs of this FlexComponentSummary.
        :rtype: int
        """
        return self._available_db_storage_in_gbs

    @available_db_storage_in_gbs.setter
    def available_db_storage_in_gbs(self, available_db_storage_in_gbs):
        """
        Sets the available_db_storage_in_gbs of this FlexComponentSummary.
        The maximum  storage that can be enabled on the Storage Server for this Flex Component.


        :param available_db_storage_in_gbs: The available_db_storage_in_gbs of this FlexComponentSummary.
        :type: int
        """
        self._available_db_storage_in_gbs = available_db_storage_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
