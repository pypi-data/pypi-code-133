# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CollectedAuditVolumeSummary(object):
    """
    The volume data point for audit data collected by datasafe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CollectedAuditVolumeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_profile_id:
            The value to assign to the audit_profile_id property of this CollectedAuditVolumeSummary.
        :type audit_profile_id: str

        :param month_in_consideration:
            The value to assign to the month_in_consideration property of this CollectedAuditVolumeSummary.
        :type month_in_consideration: datetime

        :param online_volume:
            The value to assign to the online_volume property of this CollectedAuditVolumeSummary.
        :type online_volume: int

        :param archived_volume:
            The value to assign to the archived_volume property of this CollectedAuditVolumeSummary.
        :type archived_volume: int

        """
        self.swagger_types = {
            'audit_profile_id': 'str',
            'month_in_consideration': 'datetime',
            'online_volume': 'int',
            'archived_volume': 'int'
        }

        self.attribute_map = {
            'audit_profile_id': 'auditProfileId',
            'month_in_consideration': 'monthInConsideration',
            'online_volume': 'onlineVolume',
            'archived_volume': 'archivedVolume'
        }

        self._audit_profile_id = None
        self._month_in_consideration = None
        self._online_volume = None
        self._archived_volume = None

    @property
    def audit_profile_id(self):
        """
        **[Required]** Gets the audit_profile_id of this CollectedAuditVolumeSummary.
        The OCID of the audit profile resource.


        :return: The audit_profile_id of this CollectedAuditVolumeSummary.
        :rtype: str
        """
        return self._audit_profile_id

    @audit_profile_id.setter
    def audit_profile_id(self, audit_profile_id):
        """
        Sets the audit_profile_id of this CollectedAuditVolumeSummary.
        The OCID of the audit profile resource.


        :param audit_profile_id: The audit_profile_id of this CollectedAuditVolumeSummary.
        :type: str
        """
        self._audit_profile_id = audit_profile_id

    @property
    def month_in_consideration(self):
        """
        **[Required]** Gets the month_in_consideration of this CollectedAuditVolumeSummary.
        Represents the month under consideration in which the aggregated audit data volume collected by Data Safe is displayed.
        This field will be the UTC start of the day of the first day of the month for which the aggregate count corresponds to, in the format defined by RFC3339..
        For instance, the value of 01-01-2021T00:00:00Z represents Jan 2021.


        :return: The month_in_consideration of this CollectedAuditVolumeSummary.
        :rtype: datetime
        """
        return self._month_in_consideration

    @month_in_consideration.setter
    def month_in_consideration(self, month_in_consideration):
        """
        Sets the month_in_consideration of this CollectedAuditVolumeSummary.
        Represents the month under consideration in which the aggregated audit data volume collected by Data Safe is displayed.
        This field will be the UTC start of the day of the first day of the month for which the aggregate count corresponds to, in the format defined by RFC3339..
        For instance, the value of 01-01-2021T00:00:00Z represents Jan 2021.


        :param month_in_consideration: The month_in_consideration of this CollectedAuditVolumeSummary.
        :type: datetime
        """
        self._month_in_consideration = month_in_consideration

    @property
    def online_volume(self):
        """
        **[Required]** Gets the online_volume of this CollectedAuditVolumeSummary.
        The audit data volume collected by Data Safe and is available online in repository.


        :return: The online_volume of this CollectedAuditVolumeSummary.
        :rtype: int
        """
        return self._online_volume

    @online_volume.setter
    def online_volume(self, online_volume):
        """
        Sets the online_volume of this CollectedAuditVolumeSummary.
        The audit data volume collected by Data Safe and is available online in repository.


        :param online_volume: The online_volume of this CollectedAuditVolumeSummary.
        :type: int
        """
        self._online_volume = online_volume

    @property
    def archived_volume(self):
        """
        **[Required]** Gets the archived_volume of this CollectedAuditVolumeSummary.
        The audit data volume collected by Data Safe and is available in archive storage.


        :return: The archived_volume of this CollectedAuditVolumeSummary.
        :rtype: int
        """
        return self._archived_volume

    @archived_volume.setter
    def archived_volume(self, archived_volume):
        """
        Sets the archived_volume of this CollectedAuditVolumeSummary.
        The audit data volume collected by Data Safe and is available in archive storage.


        :param archived_volume: The archived_volume of this CollectedAuditVolumeSummary.
        :type: int
        """
        self._archived_volume = archived_volume

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
