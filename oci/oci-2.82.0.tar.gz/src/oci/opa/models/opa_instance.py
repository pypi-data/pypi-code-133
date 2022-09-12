# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpaInstance(object):
    """
    Description of OpaInstance.
    """

    #: A constant which can be used with the consumption_model property of a OpaInstance.
    #: This constant has a value of "UCM"
    CONSUMPTION_MODEL_UCM = "UCM"

    #: A constant which can be used with the consumption_model property of a OpaInstance.
    #: This constant has a value of "GOV"
    CONSUMPTION_MODEL_GOV = "GOV"

    #: A constant which can be used with the consumption_model property of a OpaInstance.
    #: This constant has a value of "SAAS"
    CONSUMPTION_MODEL_SAAS = "SAAS"

    #: A constant which can be used with the shape_name property of a OpaInstance.
    #: This constant has a value of "DEVELOPMENT"
    SHAPE_NAME_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the shape_name property of a OpaInstance.
    #: This constant has a value of "PRODUCTION"
    SHAPE_NAME_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the metering_type property of a OpaInstance.
    #: This constant has a value of "EXECUTION_PACK"
    METERING_TYPE_EXECUTION_PACK = "EXECUTION_PACK"

    #: A constant which can be used with the metering_type property of a OpaInstance.
    #: This constant has a value of "USERS"
    METERING_TYPE_USERS = "USERS"

    #: A constant which can be used with the metering_type property of a OpaInstance.
    #: This constant has a value of "EMPLOYEE"
    METERING_TYPE_EMPLOYEE = "EMPLOYEE"

    #: A constant which can be used with the metering_type property of a OpaInstance.
    #: This constant has a value of "NAMED_USER"
    METERING_TYPE_NAMED_USER = "NAMED_USER"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OpaInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OpaInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpaInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OpaInstance.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OpaInstance.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpaInstance.
        :type compartment_id: str

        :param instance_url:
            The value to assign to the instance_url property of this OpaInstance.
        :type instance_url: str

        :param consumption_model:
            The value to assign to the consumption_model property of this OpaInstance.
            Allowed values for this property are: "UCM", "GOV", "SAAS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type consumption_model: str

        :param shape_name:
            The value to assign to the shape_name property of this OpaInstance.
            Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape_name: str

        :param metering_type:
            The value to assign to the metering_type property of this OpaInstance.
            Allowed values for this property are: "EXECUTION_PACK", "USERS", "EMPLOYEE", "NAMED_USER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metering_type: str

        :param time_created:
            The value to assign to the time_created property of this OpaInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpaInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpaInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param identity_app_guid:
            The value to assign to the identity_app_guid property of this OpaInstance.
        :type identity_app_guid: str

        :param identity_app_display_name:
            The value to assign to the identity_app_display_name property of this OpaInstance.
        :type identity_app_display_name: str

        :param identity_domain_url:
            The value to assign to the identity_domain_url property of this OpaInstance.
        :type identity_domain_url: str

        :param identity_app_opc_service_instance_guid:
            The value to assign to the identity_app_opc_service_instance_guid property of this OpaInstance.
        :type identity_app_opc_service_instance_guid: str

        :param is_breakglass_enabled:
            The value to assign to the is_breakglass_enabled property of this OpaInstance.
        :type is_breakglass_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpaInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpaInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpaInstance.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'instance_url': 'str',
            'consumption_model': 'str',
            'shape_name': 'str',
            'metering_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'identity_app_guid': 'str',
            'identity_app_display_name': 'str',
            'identity_domain_url': 'str',
            'identity_app_opc_service_instance_guid': 'str',
            'is_breakglass_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'instance_url': 'instanceUrl',
            'consumption_model': 'consumptionModel',
            'shape_name': 'shapeName',
            'metering_type': 'meteringType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'identity_app_guid': 'identityAppGuid',
            'identity_app_display_name': 'identityAppDisplayName',
            'identity_domain_url': 'identityDomainUrl',
            'identity_app_opc_service_instance_guid': 'identityAppOpcServiceInstanceGuid',
            'is_breakglass_enabled': 'isBreakglassEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._instance_url = None
        self._consumption_model = None
        self._shape_name = None
        self._metering_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._identity_app_guid = None
        self._identity_app_display_name = None
        self._identity_domain_url = None
        self._identity_app_opc_service_instance_guid = None
        self._is_breakglass_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OpaInstance.
        Unique identifier that is immutable on creation


        :return: The id of this OpaInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpaInstance.
        Unique identifier that is immutable on creation


        :param id: The id of this OpaInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OpaInstance.
        OpaInstance Identifier, can be renamed


        :return: The display_name of this OpaInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpaInstance.
        OpaInstance Identifier, can be renamed


        :param display_name: The display_name of this OpaInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OpaInstance.
        Description of the Process Automation instance.


        :return: The description of this OpaInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OpaInstance.
        Description of the Process Automation instance.


        :param description: The description of this OpaInstance.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OpaInstance.
        Compartment Identifier


        :return: The compartment_id of this OpaInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpaInstance.
        Compartment Identifier


        :param compartment_id: The compartment_id of this OpaInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def instance_url(self):
        """
        Gets the instance_url of this OpaInstance.
        OPA Instance URL


        :return: The instance_url of this OpaInstance.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """
        Sets the instance_url of this OpaInstance.
        OPA Instance URL


        :param instance_url: The instance_url of this OpaInstance.
        :type: str
        """
        self._instance_url = instance_url

    @property
    def consumption_model(self):
        """
        Gets the consumption_model of this OpaInstance.
        The entitlement used for billing purposes

        Allowed values for this property are: "UCM", "GOV", "SAAS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The consumption_model of this OpaInstance.
        :rtype: str
        """
        return self._consumption_model

    @consumption_model.setter
    def consumption_model(self, consumption_model):
        """
        Sets the consumption_model of this OpaInstance.
        The entitlement used for billing purposes


        :param consumption_model: The consumption_model of this OpaInstance.
        :type: str
        """
        allowed_values = ["UCM", "GOV", "SAAS"]
        if not value_allowed_none_or_none_sentinel(consumption_model, allowed_values):
            consumption_model = 'UNKNOWN_ENUM_VALUE'
        self._consumption_model = consumption_model

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this OpaInstance.
        Shape of the instance.

        Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape_name of this OpaInstance.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this OpaInstance.
        Shape of the instance.


        :param shape_name: The shape_name of this OpaInstance.
        :type: str
        """
        allowed_values = ["DEVELOPMENT", "PRODUCTION"]
        if not value_allowed_none_or_none_sentinel(shape_name, allowed_values):
            shape_name = 'UNKNOWN_ENUM_VALUE'
        self._shape_name = shape_name

    @property
    def metering_type(self):
        """
        Gets the metering_type of this OpaInstance.
        MeteringType Identifier

        Allowed values for this property are: "EXECUTION_PACK", "USERS", "EMPLOYEE", "NAMED_USER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metering_type of this OpaInstance.
        :rtype: str
        """
        return self._metering_type

    @metering_type.setter
    def metering_type(self, metering_type):
        """
        Sets the metering_type of this OpaInstance.
        MeteringType Identifier


        :param metering_type: The metering_type of this OpaInstance.
        :type: str
        """
        allowed_values = ["EXECUTION_PACK", "USERS", "EMPLOYEE", "NAMED_USER"]
        if not value_allowed_none_or_none_sentinel(metering_type, allowed_values):
            metering_type = 'UNKNOWN_ENUM_VALUE'
        self._metering_type = metering_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OpaInstance.
        The time when OpaInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this OpaInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpaInstance.
        The time when OpaInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OpaInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpaInstance.
        The time the OpaInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OpaInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpaInstance.
        The time the OpaInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OpaInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OpaInstance.
        The current state of the OpaInstance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OpaInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpaInstance.
        The current state of the OpaInstance.


        :param lifecycle_state: The lifecycle_state of this OpaInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def identity_app_guid(self):
        """
        Gets the identity_app_guid of this OpaInstance.
        This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.


        :return: The identity_app_guid of this OpaInstance.
        :rtype: str
        """
        return self._identity_app_guid

    @identity_app_guid.setter
    def identity_app_guid(self, identity_app_guid):
        """
        Sets the identity_app_guid of this OpaInstance.
        This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.


        :param identity_app_guid: The identity_app_guid of this OpaInstance.
        :type: str
        """
        self._identity_app_guid = identity_app_guid

    @property
    def identity_app_display_name(self):
        """
        Gets the identity_app_display_name of this OpaInstance.
        This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :return: The identity_app_display_name of this OpaInstance.
        :rtype: str
        """
        return self._identity_app_display_name

    @identity_app_display_name.setter
    def identity_app_display_name(self, identity_app_display_name):
        """
        Sets the identity_app_display_name of this OpaInstance.
        This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :param identity_app_display_name: The identity_app_display_name of this OpaInstance.
        :type: str
        """
        self._identity_app_display_name = identity_app_display_name

    @property
    def identity_domain_url(self):
        """
        Gets the identity_domain_url of this OpaInstance.
        This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :return: The identity_domain_url of this OpaInstance.
        :rtype: str
        """
        return self._identity_domain_url

    @identity_domain_url.setter
    def identity_domain_url(self, identity_domain_url):
        """
        Sets the identity_domain_url of this OpaInstance.
        This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :param identity_domain_url: The identity_domain_url of this OpaInstance.
        :type: str
        """
        self._identity_domain_url = identity_domain_url

    @property
    def identity_app_opc_service_instance_guid(self):
        """
        Gets the identity_app_opc_service_instance_guid of this OpaInstance.
        This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :return: The identity_app_opc_service_instance_guid of this OpaInstance.
        :rtype: str
        """
        return self._identity_app_opc_service_instance_guid

    @identity_app_opc_service_instance_guid.setter
    def identity_app_opc_service_instance_guid(self, identity_app_opc_service_instance_guid):
        """
        Sets the identity_app_opc_service_instance_guid of this OpaInstance.
        This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.


        :param identity_app_opc_service_instance_guid: The identity_app_opc_service_instance_guid of this OpaInstance.
        :type: str
        """
        self._identity_app_opc_service_instance_guid = identity_app_opc_service_instance_guid

    @property
    def is_breakglass_enabled(self):
        """
        Gets the is_breakglass_enabled of this OpaInstance.
        indicates if breakGlass is enabled for the opa instance.


        :return: The is_breakglass_enabled of this OpaInstance.
        :rtype: bool
        """
        return self._is_breakglass_enabled

    @is_breakglass_enabled.setter
    def is_breakglass_enabled(self, is_breakglass_enabled):
        """
        Sets the is_breakglass_enabled of this OpaInstance.
        indicates if breakGlass is enabled for the opa instance.


        :param is_breakglass_enabled: The is_breakglass_enabled of this OpaInstance.
        :type: bool
        """
        self._is_breakglass_enabled = is_breakglass_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpaInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpaInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpaInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpaInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpaInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpaInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpaInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpaInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpaInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpaInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpaInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpaInstance.
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
