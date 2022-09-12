# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotebookSessionSummary(object):
    """
    Summary information for a notebook session.
    """

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a NotebookSessionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new NotebookSessionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NotebookSessionSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this NotebookSessionSummary.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this NotebookSessionSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this NotebookSessionSummary.
        :type project_id: str

        :param created_by:
            The value to assign to the created_by property of this NotebookSessionSummary.
        :type created_by: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NotebookSessionSummary.
        :type compartment_id: str

        :param notebook_session_configuration_details:
            The value to assign to the notebook_session_configuration_details property of this NotebookSessionSummary.
        :type notebook_session_configuration_details: oci.data_science.models.NotebookSessionConfigurationDetails

        :param notebook_session_config_details:
            The value to assign to the notebook_session_config_details property of this NotebookSessionSummary.
        :type notebook_session_config_details: oci.data_science.models.NotebookSessionConfigDetails

        :param notebook_session_url:
            The value to assign to the notebook_session_url property of this NotebookSessionSummary.
        :type notebook_session_url: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NotebookSessionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this NotebookSessionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this NotebookSessionSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'project_id': 'str',
            'created_by': 'str',
            'compartment_id': 'str',
            'notebook_session_configuration_details': 'NotebookSessionConfigurationDetails',
            'notebook_session_config_details': 'NotebookSessionConfigDetails',
            'notebook_session_url': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'created_by': 'createdBy',
            'compartment_id': 'compartmentId',
            'notebook_session_configuration_details': 'notebookSessionConfigurationDetails',
            'notebook_session_config_details': 'notebookSessionConfigDetails',
            'notebook_session_url': 'notebookSessionUrl',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._time_created = None
        self._display_name = None
        self._project_id = None
        self._created_by = None
        self._compartment_id = None
        self._notebook_session_configuration_details = None
        self._notebook_session_config_details = None
        self._notebook_session_url = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NotebookSessionSummary.
        The `OCID`__ of the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this NotebookSessionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NotebookSessionSummary.
        The `OCID`__ of the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this NotebookSessionSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this NotebookSessionSummary.
        The date and time the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this NotebookSessionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NotebookSessionSummary.
        The date and time the resource was created in the timestamp format defined by `RFC3339`__.
        Example: 2019-08-25T21:10:29.41Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this NotebookSessionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NotebookSessionSummary.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My NotebookSession`


        :return: The display_name of this NotebookSessionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NotebookSessionSummary.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My NotebookSession`


        :param display_name: The display_name of this NotebookSessionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this NotebookSessionSummary.
        The `OCID`__ of the project associated with the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this NotebookSessionSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this NotebookSessionSummary.
        The `OCID`__ of the project associated with the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this NotebookSessionSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this NotebookSessionSummary.
        The `OCID`__ of the user who created the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this NotebookSessionSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this NotebookSessionSummary.
        The `OCID`__ of the user who created the notebook session.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this NotebookSessionSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this NotebookSessionSummary.
        The `OCID`__ of the notebook session's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this NotebookSessionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NotebookSessionSummary.
        The `OCID`__ of the notebook session's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this NotebookSessionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def notebook_session_configuration_details(self):
        """
        Gets the notebook_session_configuration_details of this NotebookSessionSummary.

        :return: The notebook_session_configuration_details of this NotebookSessionSummary.
        :rtype: oci.data_science.models.NotebookSessionConfigurationDetails
        """
        return self._notebook_session_configuration_details

    @notebook_session_configuration_details.setter
    def notebook_session_configuration_details(self, notebook_session_configuration_details):
        """
        Sets the notebook_session_configuration_details of this NotebookSessionSummary.

        :param notebook_session_configuration_details: The notebook_session_configuration_details of this NotebookSessionSummary.
        :type: oci.data_science.models.NotebookSessionConfigurationDetails
        """
        self._notebook_session_configuration_details = notebook_session_configuration_details

    @property
    def notebook_session_config_details(self):
        """
        Gets the notebook_session_config_details of this NotebookSessionSummary.

        :return: The notebook_session_config_details of this NotebookSessionSummary.
        :rtype: oci.data_science.models.NotebookSessionConfigDetails
        """
        return self._notebook_session_config_details

    @notebook_session_config_details.setter
    def notebook_session_config_details(self, notebook_session_config_details):
        """
        Sets the notebook_session_config_details of this NotebookSessionSummary.

        :param notebook_session_config_details: The notebook_session_config_details of this NotebookSessionSummary.
        :type: oci.data_science.models.NotebookSessionConfigDetails
        """
        self._notebook_session_config_details = notebook_session_config_details

    @property
    def notebook_session_url(self):
        """
        Gets the notebook_session_url of this NotebookSessionSummary.
        The URL to interact with the notebook session.


        :return: The notebook_session_url of this NotebookSessionSummary.
        :rtype: str
        """
        return self._notebook_session_url

    @notebook_session_url.setter
    def notebook_session_url(self, notebook_session_url):
        """
        Sets the notebook_session_url of this NotebookSessionSummary.
        The URL to interact with the notebook session.


        :param notebook_session_url: The notebook_session_url of this NotebookSessionSummary.
        :type: str
        """
        self._notebook_session_url = notebook_session_url

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this NotebookSessionSummary.
        The state of the notebook session.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this NotebookSessionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NotebookSessionSummary.
        The state of the notebook session.


        :param lifecycle_state: The lifecycle_state of this NotebookSessionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this NotebookSessionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this NotebookSessionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this NotebookSessionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this NotebookSessionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this NotebookSessionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this NotebookSessionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this NotebookSessionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this NotebookSessionSummary.
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
