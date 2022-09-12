# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpensearchClusterBackupSummary(object):
    """
    The summary of information about an OpenSearch cluster backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpensearchClusterBackupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpensearchClusterBackupSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OpensearchClusterBackupSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpensearchClusterBackupSummary.
        :type compartment_id: str

        :param backup_type:
            The value to assign to the backup_type property of this OpensearchClusterBackupSummary.
        :type backup_type: str

        :param source_cluster_id:
            The value to assign to the source_cluster_id property of this OpensearchClusterBackupSummary.
        :type source_cluster_id: str

        :param time_created:
            The value to assign to the time_created property of this OpensearchClusterBackupSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpensearchClusterBackupSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpensearchClusterBackupSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OpensearchClusterBackupSummary.
        :type lifecycle_details: str

        :param time_expired:
            The value to assign to the time_expired property of this OpensearchClusterBackupSummary.
        :type time_expired: datetime

        :param backup_size:
            The value to assign to the backup_size property of this OpensearchClusterBackupSummary.
        :type backup_size: float

        :param source_cluster_display_name:
            The value to assign to the source_cluster_display_name property of this OpensearchClusterBackupSummary.
        :type source_cluster_display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpensearchClusterBackupSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpensearchClusterBackupSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpensearchClusterBackupSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'backup_type': 'str',
            'source_cluster_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_expired': 'datetime',
            'backup_size': 'float',
            'source_cluster_display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'backup_type': 'backupType',
            'source_cluster_id': 'sourceClusterId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_expired': 'timeExpired',
            'backup_size': 'backupSize',
            'source_cluster_display_name': 'sourceClusterDisplayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._backup_type = None
        self._source_cluster_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_expired = None
        self._backup_size = None
        self._source_cluster_display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OpensearchClusterBackupSummary.
        The OCID of the cluster backup.


        :return: The id of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpensearchClusterBackupSummary.
        The OCID of the cluster backup.


        :param id: The id of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this OpensearchClusterBackupSummary.
        The name of the cluster backup. Avoid entering confidential information.


        :return: The display_name of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpensearchClusterBackupSummary.
        The name of the cluster backup. Avoid entering confidential information.


        :param display_name: The display_name of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OpensearchClusterBackupSummary.
        The OCID of the compartment where the cluster backup is located.


        :return: The compartment_id of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpensearchClusterBackupSummary.
        The OCID of the compartment where the cluster backup is located.


        :param compartment_id: The compartment_id of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this OpensearchClusterBackupSummary.
        Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.


        :return: The backup_type of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this OpensearchClusterBackupSummary.
        Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.


        :param backup_type: The backup_type of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._backup_type = backup_type

    @property
    def source_cluster_id(self):
        """
        **[Required]** Gets the source_cluster_id of this OpensearchClusterBackupSummary.
        The OCID of the source OpenSearch cluster for the cluster backup.


        :return: The source_cluster_id of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._source_cluster_id

    @source_cluster_id.setter
    def source_cluster_id(self, source_cluster_id):
        """
        Sets the source_cluster_id of this OpensearchClusterBackupSummary.
        The OCID of the source OpenSearch cluster for the cluster backup.


        :param source_cluster_id: The source_cluster_id of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._source_cluster_id = source_cluster_id

    @property
    def time_created(self):
        """
        Gets the time_created of this OpensearchClusterBackupSummary.
        The date and time the cluster backup was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OpensearchClusterBackupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpensearchClusterBackupSummary.
        The date and time the cluster backup was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OpensearchClusterBackupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpensearchClusterBackupSummary.
        The date and time the cluster backup was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this OpensearchClusterBackupSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpensearchClusterBackupSummary.
        The date and time the cluster backup was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this OpensearchClusterBackupSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OpensearchClusterBackupSummary.
        The current state of the cluster backup.


        :return: The lifecycle_state of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpensearchClusterBackupSummary.
        The current state of the cluster backup.


        :param lifecycle_state: The lifecycle_state of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OpensearchClusterBackupSummary.
        Additional information about the current lifecycle state of the cluster backup.


        :return: The lifecycle_details of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OpensearchClusterBackupSummary.
        Additional information about the current lifecycle state of the cluster backup.


        :param lifecycle_details: The lifecycle_details of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_expired(self):
        """
        Gets the time_expired of this OpensearchClusterBackupSummary.
        The date and time the cluster backup expires. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_expired of this OpensearchClusterBackupSummary.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this OpensearchClusterBackupSummary.
        The date and time the cluster backup expires. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_expired: The time_expired of this OpensearchClusterBackupSummary.
        :type: datetime
        """
        self._time_expired = time_expired

    @property
    def backup_size(self):
        """
        Gets the backup_size of this OpensearchClusterBackupSummary.
        The size in GB of the cluster backup.


        :return: The backup_size of this OpensearchClusterBackupSummary.
        :rtype: float
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """
        Sets the backup_size of this OpensearchClusterBackupSummary.
        The size in GB of the cluster backup.


        :param backup_size: The backup_size of this OpensearchClusterBackupSummary.
        :type: float
        """
        self._backup_size = backup_size

    @property
    def source_cluster_display_name(self):
        """
        Gets the source_cluster_display_name of this OpensearchClusterBackupSummary.
        The name of the source OpenSearch cluster for the cluster backup.


        :return: The source_cluster_display_name of this OpensearchClusterBackupSummary.
        :rtype: str
        """
        return self._source_cluster_display_name

    @source_cluster_display_name.setter
    def source_cluster_display_name(self, source_cluster_display_name):
        """
        Sets the source_cluster_display_name of this OpensearchClusterBackupSummary.
        The name of the source OpenSearch cluster for the cluster backup.


        :param source_cluster_display_name: The source_cluster_display_name of this OpensearchClusterBackupSummary.
        :type: str
        """
        self._source_cluster_display_name = source_cluster_display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpensearchClusterBackupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpensearchClusterBackupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpensearchClusterBackupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpensearchClusterBackupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpensearchClusterBackupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpensearchClusterBackupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpensearchClusterBackupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpensearchClusterBackupSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpensearchClusterBackupSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpensearchClusterBackupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpensearchClusterBackupSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpensearchClusterBackupSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
