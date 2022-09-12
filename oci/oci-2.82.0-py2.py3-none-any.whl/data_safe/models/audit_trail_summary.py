# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditTrailSummary(object):
    """
    Summary of an audit trail.
    """

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "STARTING"
    STATUS_STARTING = "STARTING"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "COLLECTING"
    STATUS_COLLECTING = "COLLECTING"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "RECOVERING"
    STATUS_RECOVERING = "RECOVERING"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "IDLE"
    STATUS_IDLE = "IDLE"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "STOPPING"
    STATUS_STOPPING = "STOPPING"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "STOPPED"
    STATUS_STOPPED = "STOPPED"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "RESUMING"
    STATUS_RESUMING = "RESUMING"

    #: A constant which can be used with the status property of a AuditTrailSummary.
    #: This constant has a value of "RETRYING"
    STATUS_RETRYING = "RETRYING"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AuditTrailSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditTrailSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AuditTrailSummary.
        :type id: str

        :param audit_profile_id:
            The value to assign to the audit_profile_id property of this AuditTrailSummary.
        :type audit_profile_id: str

        :param display_name:
            The value to assign to the display_name property of this AuditTrailSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this AuditTrailSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AuditTrailSummary.
        :type time_updated: datetime

        :param status:
            The value to assign to the status property of this AuditTrailSummary.
            Allowed values for this property are: "STARTING", "COLLECTING", "RECOVERING", "IDLE", "STOPPING", "STOPPED", "RESUMING", "RETRYING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param description:
            The value to assign to the description property of this AuditTrailSummary.
        :type description: str

        :param trail_location:
            The value to assign to the trail_location property of this AuditTrailSummary.
        :type trail_location: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AuditTrailSummary.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this AuditTrailSummary.
        :type target_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AuditTrailSummary.
            Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AuditTrailSummary.
        :type lifecycle_details: str

        :param is_auto_purge_enabled:
            The value to assign to the is_auto_purge_enabled property of this AuditTrailSummary.
        :type is_auto_purge_enabled: bool

        :param audit_collection_start_time:
            The value to assign to the audit_collection_start_time property of this AuditTrailSummary.
        :type audit_collection_start_time: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AuditTrailSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AuditTrailSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'audit_profile_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'status': 'str',
            'description': 'str',
            'trail_location': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_auto_purge_enabled': 'bool',
            'audit_collection_start_time': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'audit_profile_id': 'auditProfileId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'status': 'status',
            'description': 'description',
            'trail_location': 'trailLocation',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_auto_purge_enabled': 'isAutoPurgeEnabled',
            'audit_collection_start_time': 'auditCollectionStartTime',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._audit_profile_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._status = None
        self._description = None
        self._trail_location = None
        self._compartment_id = None
        self._target_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_auto_purge_enabled = None
        self._audit_collection_start_time = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AuditTrailSummary.
        The OCID of the audit trail.


        :return: The id of this AuditTrailSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuditTrailSummary.
        The OCID of the audit trail.


        :param id: The id of this AuditTrailSummary.
        :type: str
        """
        self._id = id

    @property
    def audit_profile_id(self):
        """
        **[Required]** Gets the audit_profile_id of this AuditTrailSummary.
        The OCID of the  parent audit.


        :return: The audit_profile_id of this AuditTrailSummary.
        :rtype: str
        """
        return self._audit_profile_id

    @audit_profile_id.setter
    def audit_profile_id(self, audit_profile_id):
        """
        Sets the audit_profile_id of this AuditTrailSummary.
        The OCID of the  parent audit.


        :param audit_profile_id: The audit_profile_id of this AuditTrailSummary.
        :type: str
        """
        self._audit_profile_id = audit_profile_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AuditTrailSummary.
        The display name of the audit trail.


        :return: The display_name of this AuditTrailSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AuditTrailSummary.
        The display name of the audit trail.


        :param display_name: The display_name of this AuditTrailSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AuditTrailSummary.
        The date and time the audit trail was created, in the format defined by RFC3339.


        :return: The time_created of this AuditTrailSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AuditTrailSummary.
        The date and time the audit trail was created, in the format defined by RFC3339.


        :param time_created: The time_created of this AuditTrailSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AuditTrailSummary.
        The date and time the audit trail was updated, in the format defined by RFC3339.


        :return: The time_updated of this AuditTrailSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AuditTrailSummary.
        The date and time the audit trail was updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this AuditTrailSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def status(self):
        """
        **[Required]** Gets the status of this AuditTrailSummary.
        The current sub-state of the audit trail.

        Allowed values for this property are: "STARTING", "COLLECTING", "RECOVERING", "IDLE", "STOPPING", "STOPPED", "RESUMING", "RETRYING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AuditTrailSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AuditTrailSummary.
        The current sub-state of the audit trail.


        :param status: The status of this AuditTrailSummary.
        :type: str
        """
        allowed_values = ["STARTING", "COLLECTING", "RECOVERING", "IDLE", "STOPPING", "STOPPED", "RESUMING", "RETRYING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def description(self):
        """
        Gets the description of this AuditTrailSummary.
        The description of audit trail.


        :return: The description of this AuditTrailSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AuditTrailSummary.
        The description of audit trail.


        :param description: The description of this AuditTrailSummary.
        :type: str
        """
        self._description = description

    @property
    def trail_location(self):
        """
        Gets the trail_location of this AuditTrailSummary.
        An audit trail location represents the source of audit records that provides documentary evidence of the sequence of activities in the target database.


        :return: The trail_location of this AuditTrailSummary.
        :rtype: str
        """
        return self._trail_location

    @trail_location.setter
    def trail_location(self, trail_location):
        """
        Sets the trail_location of this AuditTrailSummary.
        An audit trail location represents the source of audit records that provides documentary evidence of the sequence of activities in the target database.


        :param trail_location: The trail_location of this AuditTrailSummary.
        :type: str
        """
        self._trail_location = trail_location

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AuditTrailSummary.
        The OCID of the compartment that contains the audit.


        :return: The compartment_id of this AuditTrailSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AuditTrailSummary.
        The OCID of the compartment that contains the audit.


        :param compartment_id: The compartment_id of this AuditTrailSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this AuditTrailSummary.
        The OCID of the Data Safe target for which the audit trail is created.


        :return: The target_id of this AuditTrailSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditTrailSummary.
        The OCID of the Data Safe target for which the audit trail is created.


        :param target_id: The target_id of this AuditTrailSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AuditTrailSummary.
        The current state of the audit trail.

        Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AuditTrailSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AuditTrailSummary.
        The current state of the audit trail.


        :param lifecycle_state: The lifecycle_state of this AuditTrailSummary.
        :type: str
        """
        allowed_values = ["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AuditTrailSummary.
        Details about the current state of the audit trail in Data Safe.


        :return: The lifecycle_details of this AuditTrailSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AuditTrailSummary.
        Details about the current state of the audit trail in Data Safe.


        :param lifecycle_details: The lifecycle_details of this AuditTrailSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_auto_purge_enabled(self):
        """
        Gets the is_auto_purge_enabled of this AuditTrailSummary.
        Indicates if auto purge is enabled on the target database, which helps delete audit data in the
        target database every seven days so that the database's audit trail does not become too large.


        :return: The is_auto_purge_enabled of this AuditTrailSummary.
        :rtype: bool
        """
        return self._is_auto_purge_enabled

    @is_auto_purge_enabled.setter
    def is_auto_purge_enabled(self, is_auto_purge_enabled):
        """
        Sets the is_auto_purge_enabled of this AuditTrailSummary.
        Indicates if auto purge is enabled on the target database, which helps delete audit data in the
        target database every seven days so that the database's audit trail does not become too large.


        :param is_auto_purge_enabled: The is_auto_purge_enabled of this AuditTrailSummary.
        :type: bool
        """
        self._is_auto_purge_enabled = is_auto_purge_enabled

    @property
    def audit_collection_start_time(self):
        """
        Gets the audit_collection_start_time of this AuditTrailSummary.
        The date from which the audit trail must start collecting data, in the format defined by RFC3339.


        :return: The audit_collection_start_time of this AuditTrailSummary.
        :rtype: datetime
        """
        return self._audit_collection_start_time

    @audit_collection_start_time.setter
    def audit_collection_start_time(self, audit_collection_start_time):
        """
        Sets the audit_collection_start_time of this AuditTrailSummary.
        The date from which the audit trail must start collecting data, in the format defined by RFC3339.


        :param audit_collection_start_time: The audit_collection_start_time of this AuditTrailSummary.
        :type: datetime
        """
        self._audit_collection_start_time = audit_collection_start_time

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AuditTrailSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AuditTrailSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AuditTrailSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AuditTrailSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AuditTrailSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AuditTrailSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AuditTrailSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AuditTrailSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
