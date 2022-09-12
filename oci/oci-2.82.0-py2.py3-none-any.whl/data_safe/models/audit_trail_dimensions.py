# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditTrailDimensions(object):
    """
    Details of aggregation dimensions used for summarizing audit trails.
    """

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailDimensions.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditTrailDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param location:
            The value to assign to the location property of this AuditTrailDimensions.
        :type location: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AuditTrailDimensions.
            Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this AuditTrailDimensions.
        :type status: str

        :param target_id:
            The value to assign to the target_id property of this AuditTrailDimensions.
        :type target_id: str

        """
        self.swagger_types = {
            'location': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'target_id': 'str'
        }

        self.attribute_map = {
            'location': 'location',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'target_id': 'targetId'
        }

        self._location = None
        self._lifecycle_state = None
        self._status = None
        self._target_id = None

    @property
    def location(self):
        """
        Gets the location of this AuditTrailDimensions.
        The location represents the source of audit records that provides documentary evidence of the sequence of activities in the target database.


        :return: The location of this AuditTrailDimensions.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this AuditTrailDimensions.
        The location represents the source of audit records that provides documentary evidence of the sequence of activities in the target database.


        :param location: The location of this AuditTrailDimensions.
        :type: str
        """
        self._location = location

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AuditTrailDimensions.
        The current state of the audit trail.

        Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AuditTrailDimensions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AuditTrailDimensions.
        The current state of the audit trail.


        :param lifecycle_state: The lifecycle_state of this AuditTrailDimensions.
        :type: str
        """
        allowed_values = ["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        Gets the status of this AuditTrailDimensions.
        The current sub-state of the audit trail..


        :return: The status of this AuditTrailDimensions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AuditTrailDimensions.
        The current sub-state of the audit trail..


        :param status: The status of this AuditTrailDimensions.
        :type: str
        """
        self._status = status

    @property
    def target_id(self):
        """
        Gets the target_id of this AuditTrailDimensions.
        The OCID of the Data Safe target for which the audit trail is created.


        :return: The target_id of this AuditTrailDimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditTrailDimensions.
        The OCID of the Data Safe target for which the audit trail is created.


        :param target_id: The target_id of this AuditTrailDimensions.
        :type: str
        """
        self._target_id = target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
