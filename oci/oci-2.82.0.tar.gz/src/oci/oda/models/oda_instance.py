# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaInstance(object):
    """
    Description of `OdaServiceInstance` object.
    """

    #: A constant which can be used with the shape_name property of a OdaInstance.
    #: This constant has a value of "DEVELOPMENT"
    SHAPE_NAME_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the shape_name property of a OdaInstance.
    #: This constant has a value of "PRODUCTION"
    SHAPE_NAME_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_SUB_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "STARTING"
    LIFECYCLE_SUB_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_SUB_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "CHANGING_COMPARTMENT"
    LIFECYCLE_SUB_STATE_CHANGING_COMPARTMENT = "CHANGING_COMPARTMENT"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "ACTIVATING_CUSTOMER_ENCRYPTION_KEY"
    LIFECYCLE_SUB_STATE_ACTIVATING_CUSTOMER_ENCRYPTION_KEY = "ACTIVATING_CUSTOMER_ENCRYPTION_KEY"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "UPDATING_CUSTOMER_ENCRYPTION_KEY"
    LIFECYCLE_SUB_STATE_UPDATING_CUSTOMER_ENCRYPTION_KEY = "UPDATING_CUSTOMER_ENCRYPTION_KEY"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "DEACTIVATING_CUSTOMER_ENCRYPTION_KEY"
    LIFECYCLE_SUB_STATE_DEACTIVATING_CUSTOMER_ENCRYPTION_KEY = "DEACTIVATING_CUSTOMER_ENCRYPTION_KEY"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_SUB_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "DELETE_PENDING"
    LIFECYCLE_SUB_STATE_DELETE_PENDING = "DELETE_PENDING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "RECOVERING"
    LIFECYCLE_SUB_STATE_RECOVERING = "RECOVERING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_SUB_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "PURGING"
    LIFECYCLE_SUB_STATE_PURGING = "PURGING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "QUEUED"
    LIFECYCLE_SUB_STATE_QUEUED = "QUEUED"

    def __init__(self, **kwargs):
        """
        Initializes a new OdaInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OdaInstance.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OdaInstance.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OdaInstance.
        :type compartment_id: str

        :param shape_name:
            The value to assign to the shape_name property of this OdaInstance.
            Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape_name: str

        :param web_app_url:
            The value to assign to the web_app_url property of this OdaInstance.
        :type web_app_url: str

        :param connector_url:
            The value to assign to the connector_url property of this OdaInstance.
        :type connector_url: str

        :param time_created:
            The value to assign to the time_created property of this OdaInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OdaInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this OdaInstance.
            Allowed values for this property are: "CREATING", "STARTING", "STOPPING", "CHANGING_COMPARTMENT", "ACTIVATING_CUSTOMER_ENCRYPTION_KEY", "UPDATING_CUSTOMER_ENCRYPTION_KEY", "DEACTIVATING_CUSTOMER_ENCRYPTION_KEY", "DELETING", "DELETE_PENDING", "RECOVERING", "UPDATING", "PURGING", "QUEUED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_sub_state: str

        :param state_message:
            The value to assign to the state_message property of this OdaInstance.
        :type state_message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OdaInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OdaInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param is_role_based_access:
            The value to assign to the is_role_based_access property of this OdaInstance.
        :type is_role_based_access: bool

        :param identity_domain:
            The value to assign to the identity_domain property of this OdaInstance.
        :type identity_domain: str

        :param identity_app_guid:
            The value to assign to the identity_app_guid property of this OdaInstance.
        :type identity_app_guid: str

        :param identity_app_console_url:
            The value to assign to the identity_app_console_url property of this OdaInstance.
        :type identity_app_console_url: str

        :param imported_package_names:
            The value to assign to the imported_package_names property of this OdaInstance.
        :type imported_package_names: list[str]

        :param imported_package_ids:
            The value to assign to the imported_package_ids property of this OdaInstance.
        :type imported_package_ids: list[str]

        :param attachment_types:
            The value to assign to the attachment_types property of this OdaInstance.
        :type attachment_types: list[str]

        :param attachment_ids:
            The value to assign to the attachment_ids property of this OdaInstance.
        :type attachment_ids: list[str]

        :param restricted_operations:
            The value to assign to the restricted_operations property of this OdaInstance.
        :type restricted_operations: list[oci.oda.models.RestrictedOperation]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'shape_name': 'str',
            'web_app_url': 'str',
            'connector_url': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'state_message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_role_based_access': 'bool',
            'identity_domain': 'str',
            'identity_app_guid': 'str',
            'identity_app_console_url': 'str',
            'imported_package_names': 'list[str]',
            'imported_package_ids': 'list[str]',
            'attachment_types': 'list[str]',
            'attachment_ids': 'list[str]',
            'restricted_operations': 'list[RestrictedOperation]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'shape_name': 'shapeName',
            'web_app_url': 'webAppUrl',
            'connector_url': 'connectorUrl',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'state_message': 'stateMessage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_role_based_access': 'isRoleBasedAccess',
            'identity_domain': 'identityDomain',
            'identity_app_guid': 'identityAppGuid',
            'identity_app_console_url': 'identityAppConsoleUrl',
            'imported_package_names': 'importedPackageNames',
            'imported_package_ids': 'importedPackageIds',
            'attachment_types': 'attachmentTypes',
            'attachment_ids': 'attachmentIds',
            'restricted_operations': 'restrictedOperations'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._shape_name = None
        self._web_app_url = None
        self._connector_url = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._state_message = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_role_based_access = None
        self._identity_domain = None
        self._identity_app_guid = None
        self._identity_app_console_url = None
        self._imported_package_names = None
        self._imported_package_ids = None
        self._attachment_types = None
        self._attachment_ids = None
        self._restricted_operations = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaInstance.
        Unique immutable identifier that was assigned when the instance was created.


        :return: The id of this OdaInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaInstance.
        Unique immutable identifier that was assigned when the instance was created.


        :param id: The id of this OdaInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this OdaInstance.
        User-defined name for the Digital Assistant instance. Avoid entering confidential information.
        You can change this value.


        :return: The display_name of this OdaInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OdaInstance.
        User-defined name for the Digital Assistant instance. Avoid entering confidential information.
        You can change this value.


        :param display_name: The display_name of this OdaInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OdaInstance.
        Description of the Digital Assistant instance.


        :return: The description of this OdaInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OdaInstance.
        Description of the Digital Assistant instance.


        :param description: The description of this OdaInstance.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OdaInstance.
        Identifier of the compartment that the instance belongs to.


        :return: The compartment_id of this OdaInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OdaInstance.
        Identifier of the compartment that the instance belongs to.


        :param compartment_id: The compartment_id of this OdaInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this OdaInstance.
        Shape or size of the instance.

        Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape_name of this OdaInstance.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this OdaInstance.
        Shape or size of the instance.


        :param shape_name: The shape_name of this OdaInstance.
        :type: str
        """
        allowed_values = ["DEVELOPMENT", "PRODUCTION"]
        if not value_allowed_none_or_none_sentinel(shape_name, allowed_values):
            shape_name = 'UNKNOWN_ENUM_VALUE'
        self._shape_name = shape_name

    @property
    def web_app_url(self):
        """
        Gets the web_app_url of this OdaInstance.
        URL for the Digital Assistant web application that's associated with the instance.


        :return: The web_app_url of this OdaInstance.
        :rtype: str
        """
        return self._web_app_url

    @web_app_url.setter
    def web_app_url(self, web_app_url):
        """
        Sets the web_app_url of this OdaInstance.
        URL for the Digital Assistant web application that's associated with the instance.


        :param web_app_url: The web_app_url of this OdaInstance.
        :type: str
        """
        self._web_app_url = web_app_url

    @property
    def connector_url(self):
        """
        Gets the connector_url of this OdaInstance.
        URL for the connector's endpoint.


        :return: The connector_url of this OdaInstance.
        :rtype: str
        """
        return self._connector_url

    @connector_url.setter
    def connector_url(self, connector_url):
        """
        Sets the connector_url of this OdaInstance.
        URL for the connector's endpoint.


        :param connector_url: The connector_url of this OdaInstance.
        :type: str
        """
        self._connector_url = connector_url

    @property
    def time_created(self):
        """
        Gets the time_created of this OdaInstance.
        When the Digital Assistant instance was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OdaInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaInstance.
        When the Digital Assistant instance was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OdaInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OdaInstance.
        When the Digital Assistance instance was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this OdaInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OdaInstance.
        When the Digital Assistance instance was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this OdaInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OdaInstance.
        The current state of the Digital Assistant instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OdaInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaInstance.
        The current state of the Digital Assistant instance.


        :param lifecycle_state: The lifecycle_state of this OdaInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_sub_state(self):
        """
        Gets the lifecycle_sub_state of this OdaInstance.
        The current sub-state of the Digital Assistant instance.

        Allowed values for this property are: "CREATING", "STARTING", "STOPPING", "CHANGING_COMPARTMENT", "ACTIVATING_CUSTOMER_ENCRYPTION_KEY", "UPDATING_CUSTOMER_ENCRYPTION_KEY", "DEACTIVATING_CUSTOMER_ENCRYPTION_KEY", "DELETING", "DELETE_PENDING", "RECOVERING", "UPDATING", "PURGING", "QUEUED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_sub_state of this OdaInstance.
        :rtype: str
        """
        return self._lifecycle_sub_state

    @lifecycle_sub_state.setter
    def lifecycle_sub_state(self, lifecycle_sub_state):
        """
        Sets the lifecycle_sub_state of this OdaInstance.
        The current sub-state of the Digital Assistant instance.


        :param lifecycle_sub_state: The lifecycle_sub_state of this OdaInstance.
        :type: str
        """
        allowed_values = ["CREATING", "STARTING", "STOPPING", "CHANGING_COMPARTMENT", "ACTIVATING_CUSTOMER_ENCRYPTION_KEY", "UPDATING_CUSTOMER_ENCRYPTION_KEY", "DEACTIVATING_CUSTOMER_ENCRYPTION_KEY", "DELETING", "DELETE_PENDING", "RECOVERING", "UPDATING", "PURGING", "QUEUED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_sub_state, allowed_values):
            lifecycle_sub_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_sub_state = lifecycle_sub_state

    @property
    def state_message(self):
        """
        Gets the state_message of this OdaInstance.
        A message that describes the current state in more detail.
        For example, actionable information about an instance that's in the `FAILED` state.


        :return: The state_message of this OdaInstance.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this OdaInstance.
        A message that describes the current state in more detail.
        For example, actionable information about an instance that's in the `FAILED` state.


        :param state_message: The state_message of this OdaInstance.
        :type: str
        """
        self._state_message = state_message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OdaInstance.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OdaInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OdaInstance.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OdaInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OdaInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OdaInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OdaInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OdaInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_role_based_access(self):
        """
        Gets the is_role_based_access of this OdaInstance.
        Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization via IAM policies (false)


        :return: The is_role_based_access of this OdaInstance.
        :rtype: bool
        """
        return self._is_role_based_access

    @is_role_based_access.setter
    def is_role_based_access(self, is_role_based_access):
        """
        Sets the is_role_based_access of this OdaInstance.
        Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization via IAM policies (false)


        :param is_role_based_access: The is_role_based_access of this OdaInstance.
        :type: bool
        """
        self._is_role_based_access = is_role_based_access

    @property
    def identity_domain(self):
        """
        Gets the identity_domain of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation. Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and user roll mappings they like to grant access to users within the identity domain.


        :return: The identity_domain of this OdaInstance.
        :rtype: str
        """
        return self._identity_domain

    @identity_domain.setter
    def identity_domain(self, identity_domain):
        """
        Sets the identity_domain of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation. Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and user roll mappings they like to grant access to users within the identity domain.


        :param identity_domain: The identity_domain of this OdaInstance.
        :type: str
        """
        self._identity_domain = identity_domain

    @property
    def identity_app_guid(self):
        """
        Gets the identity_app_guid of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the GUID of the Identity Application instance Digital Assistant has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this Digital Assistant instance for users within the identity domain.


        :return: The identity_app_guid of this OdaInstance.
        :rtype: str
        """
        return self._identity_app_guid

    @identity_app_guid.setter
    def identity_app_guid(self, identity_app_guid):
        """
        Sets the identity_app_guid of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the GUID of the Identity Application instance Digital Assistant has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this Digital Assistant instance for users within the identity domain.


        :param identity_app_guid: The identity_app_guid of this OdaInstance.
        :type: str
        """
        self._identity_app_guid = identity_app_guid

    @property
    def identity_app_console_url(self):
        """
        Gets the identity_app_console_url of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the URL for the administration console used to manage the Identity Application instance Digital Assistant has created inside the user-specified identity domain.


        :return: The identity_app_console_url of this OdaInstance.
        :rtype: str
        """
        return self._identity_app_console_url

    @identity_app_console_url.setter
    def identity_app_console_url(self, identity_app_console_url):
        """
        Sets the identity_app_console_url of this OdaInstance.
        If isRoleBasedAccess is set to true, this property specifies the URL for the administration console used to manage the Identity Application instance Digital Assistant has created inside the user-specified identity domain.


        :param identity_app_console_url: The identity_app_console_url of this OdaInstance.
        :type: str
        """
        self._identity_app_console_url = identity_app_console_url

    @property
    def imported_package_names(self):
        """
        Gets the imported_package_names of this OdaInstance.
        A list of package names imported into this instance (if any). Use importedPackageIds field to get the details of the imported packages.


        :return: The imported_package_names of this OdaInstance.
        :rtype: list[str]
        """
        return self._imported_package_names

    @imported_package_names.setter
    def imported_package_names(self, imported_package_names):
        """
        Sets the imported_package_names of this OdaInstance.
        A list of package names imported into this instance (if any). Use importedPackageIds field to get the details of the imported packages.


        :param imported_package_names: The imported_package_names of this OdaInstance.
        :type: list[str]
        """
        self._imported_package_names = imported_package_names

    @property
    def imported_package_ids(self):
        """
        Gets the imported_package_ids of this OdaInstance.
        A list of package ids imported into this instance (if any). Use GetImportedPackage to get the details of the imported packages.


        :return: The imported_package_ids of this OdaInstance.
        :rtype: list[str]
        """
        return self._imported_package_ids

    @imported_package_ids.setter
    def imported_package_ids(self, imported_package_ids):
        """
        Sets the imported_package_ids of this OdaInstance.
        A list of package ids imported into this instance (if any). Use GetImportedPackage to get the details of the imported packages.


        :param imported_package_ids: The imported_package_ids of this OdaInstance.
        :type: list[str]
        """
        self._imported_package_ids = imported_package_ids

    @property
    def attachment_types(self):
        """
        Gets the attachment_types of this OdaInstance.
        A list of attachment types for this instance (if any). Use attachmentIds to get the details of the attachments.


        :return: The attachment_types of this OdaInstance.
        :rtype: list[str]
        """
        return self._attachment_types

    @attachment_types.setter
    def attachment_types(self, attachment_types):
        """
        Sets the attachment_types of this OdaInstance.
        A list of attachment types for this instance (if any). Use attachmentIds to get the details of the attachments.


        :param attachment_types: The attachment_types of this OdaInstance.
        :type: list[str]
        """
        self._attachment_types = attachment_types

    @property
    def attachment_ids(self):
        """
        Gets the attachment_ids of this OdaInstance.
        A list of attachment identifiers for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.


        :return: The attachment_ids of this OdaInstance.
        :rtype: list[str]
        """
        return self._attachment_ids

    @attachment_ids.setter
    def attachment_ids(self, attachment_ids):
        """
        Sets the attachment_ids of this OdaInstance.
        A list of attachment identifiers for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.


        :param attachment_ids: The attachment_ids of this OdaInstance.
        :type: list[str]
        """
        self._attachment_ids = attachment_ids

    @property
    def restricted_operations(self):
        """
        Gets the restricted_operations of this OdaInstance.
        A list of restricted operations (across all attachments) for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.


        :return: The restricted_operations of this OdaInstance.
        :rtype: list[oci.oda.models.RestrictedOperation]
        """
        return self._restricted_operations

    @restricted_operations.setter
    def restricted_operations(self, restricted_operations):
        """
        Sets the restricted_operations of this OdaInstance.
        A list of restricted operations (across all attachments) for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.


        :param restricted_operations: The restricted_operations of this OdaInstance.
        :type: list[oci.oda.models.RestrictedOperation]
        """
        self._restricted_operations = restricted_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
