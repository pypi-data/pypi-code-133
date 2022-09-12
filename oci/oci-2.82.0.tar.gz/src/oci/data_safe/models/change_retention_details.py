# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeRetentionDetails(object):
    """
    Details for the audit retention months to be modified.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeRetentionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param online_months:
            The value to assign to the online_months property of this ChangeRetentionDetails.
        :type online_months: int

        :param offline_months:
            The value to assign to the offline_months property of this ChangeRetentionDetails.
        :type offline_months: int

        :param is_override_global_retention_setting:
            The value to assign to the is_override_global_retention_setting property of this ChangeRetentionDetails.
        :type is_override_global_retention_setting: bool

        """
        self.swagger_types = {
            'online_months': 'int',
            'offline_months': 'int',
            'is_override_global_retention_setting': 'bool'
        }

        self.attribute_map = {
            'online_months': 'onlineMonths',
            'offline_months': 'offlineMonths',
            'is_override_global_retention_setting': 'isOverrideGlobalRetentionSetting'
        }

        self._online_months = None
        self._offline_months = None
        self._is_override_global_retention_setting = None

    @property
    def online_months(self):
        """
        Gets the online_months of this ChangeRetentionDetails.
        Indicates the number of months the audit records will be stored online in Oracle Data Safe audit repository for
        immediate reporting and analysis. Minimum: 1; Maximum:12 months


        :return: The online_months of this ChangeRetentionDetails.
        :rtype: int
        """
        return self._online_months

    @online_months.setter
    def online_months(self, online_months):
        """
        Sets the online_months of this ChangeRetentionDetails.
        Indicates the number of months the audit records will be stored online in Oracle Data Safe audit repository for
        immediate reporting and analysis. Minimum: 1; Maximum:12 months


        :param online_months: The online_months of this ChangeRetentionDetails.
        :type: int
        """
        self._online_months = online_months

    @property
    def offline_months(self):
        """
        Gets the offline_months of this ChangeRetentionDetails.
        Indicates the number of months the audit records will be stored offline in the Data Safe audit archive.
        Minimum: 0; Maximum: 72 months.
        If you have a requirement to store the audit data even longer in archive, please contact the Oracle Support.


        :return: The offline_months of this ChangeRetentionDetails.
        :rtype: int
        """
        return self._offline_months

    @offline_months.setter
    def offline_months(self, offline_months):
        """
        Sets the offline_months of this ChangeRetentionDetails.
        Indicates the number of months the audit records will be stored offline in the Data Safe audit archive.
        Minimum: 0; Maximum: 72 months.
        If you have a requirement to store the audit data even longer in archive, please contact the Oracle Support.


        :param offline_months: The offline_months of this ChangeRetentionDetails.
        :type: int
        """
        self._offline_months = offline_months

    @property
    def is_override_global_retention_setting(self):
        """
        Gets the is_override_global_retention_setting of this ChangeRetentionDetails.
        Indicates whether audit retention settings like online and offline months is set at the
        target level overriding the global audit retention settings.


        :return: The is_override_global_retention_setting of this ChangeRetentionDetails.
        :rtype: bool
        """
        return self._is_override_global_retention_setting

    @is_override_global_retention_setting.setter
    def is_override_global_retention_setting(self, is_override_global_retention_setting):
        """
        Sets the is_override_global_retention_setting of this ChangeRetentionDetails.
        Indicates whether audit retention settings like online and offline months is set at the
        target level overriding the global audit retention settings.


        :param is_override_global_retention_setting: The is_override_global_retention_setting of this ChangeRetentionDetails.
        :type: bool
        """
        self._is_override_global_retention_setting = is_override_global_retention_setting

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
