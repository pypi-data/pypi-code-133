# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicIp(object):
    """
    A *public IP* is a conceptual term that refers to a public IP address and related properties.
    The `publicIp` object is the API representation of a public IP.

    There are two types of public IPs:
    1. Ephemeral
    2. Reserved

    For more information and comparison of the two types,
    see `Public IP Addresses`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm
    """

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "ASSIGNING"
    LIFECYCLE_STATE_ASSIGNING = "ASSIGNING"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "ASSIGNED"
    LIFECYCLE_STATE_ASSIGNED = "ASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "UNASSIGNING"
    LIFECYCLE_STATE_UNASSIGNING = "UNASSIGNING"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "UNASSIGNED"
    LIFECYCLE_STATE_UNASSIGNED = "UNASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a PublicIp.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifetime property of a PublicIp.
    #: This constant has a value of "EPHEMERAL"
    LIFETIME_EPHEMERAL = "EPHEMERAL"

    #: A constant which can be used with the lifetime property of a PublicIp.
    #: This constant has a value of "RESERVED"
    LIFETIME_RESERVED = "RESERVED"

    #: A constant which can be used with the scope property of a PublicIp.
    #: This constant has a value of "REGION"
    SCOPE_REGION = "REGION"

    #: A constant which can be used with the scope property of a PublicIp.
    #: This constant has a value of "AVAILABILITY_DOMAIN"
    SCOPE_AVAILABILITY_DOMAIN = "AVAILABILITY_DOMAIN"

    def __init__(self, **kwargs):
        """
        Initializes a new PublicIp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this PublicIp.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PublicIp.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this PublicIp.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this PublicIp.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PublicIp.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this PublicIp.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this PublicIp.
        :type ip_address: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PublicIp.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param lifetime:
            The value to assign to the lifetime property of this PublicIp.
            Allowed values for this property are: "EPHEMERAL", "RESERVED"
        :type lifetime: str

        :param private_ip_id:
            The value to assign to the private_ip_id property of this PublicIp.
        :type private_ip_id: str

        :param scope:
            The value to assign to the scope property of this PublicIp.
            Allowed values for this property are: "REGION", "AVAILABILITY_DOMAIN"
        :type scope: str

        :param time_created:
            The value to assign to the time_created property of this PublicIp.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ip_address': 'str',
            'lifecycle_state': 'str',
            'lifetime': 'str',
            'private_ip_id': 'str',
            'scope': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ip_address': 'ipAddress',
            'lifecycle_state': 'lifecycleState',
            'lifetime': 'lifetime',
            'private_ip_id': 'privateIpId',
            'scope': 'scope',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._ip_address = None
        self._lifecycle_state = None
        self._lifetime = None
        self._private_ip_id = None
        self._scope = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this PublicIp.
        The public IP's availability domain. This property is set only for ephemeral public IPs
        (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value
        is the availability domain of the assigned private IP.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this PublicIp.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this PublicIp.
        The public IP's availability domain. This property is set only for ephemeral public IPs
        (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value
        is the availability domain of the assigned private IP.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this PublicIp.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this PublicIp.
        The `OCID`__ of the compartment containing the public IP. For an ephemeral public IP, this is
        the same compartment as the private IP's. For a reserved public IP that is currently assigned,
        this can be a different compartment than the assigned private IP's.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PublicIp.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PublicIp.
        The `OCID`__ of the compartment containing the public IP. For an ephemeral public IP, this is
        the same compartment as the private IP's. For a reserved public IP that is currently assigned,
        this can be a different compartment than the assigned private IP's.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PublicIp.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PublicIp.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PublicIp.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PublicIp.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PublicIp.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this PublicIp.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this PublicIp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PublicIp.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this PublicIp.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PublicIp.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PublicIp.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PublicIp.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PublicIp.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        Gets the id of this PublicIp.
        The public IP's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this PublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublicIp.
        The public IP's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this PublicIp.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this PublicIp.
        The public IP address of the `publicIp` object.

        Example: `203.0.113.2`


        :return: The ip_address of this PublicIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this PublicIp.
        The public IP address of the `publicIp` object.

        Example: `203.0.113.2`


        :param ip_address: The ip_address of this PublicIp.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PublicIp.
        The public IP's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this PublicIp.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PublicIp.
        The public IP's current state.


        :param lifecycle_state: The lifecycle_state of this PublicIp.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ASSIGNING", "ASSIGNED", "UNASSIGNING", "UNASSIGNED", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def lifetime(self):
        """
        Gets the lifetime of this PublicIp.
        Defines when the public IP is deleted and released back to Oracle's public IP pool.

        * `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned private IP. The
        ephemeral public IP is automatically deleted when its private IP is deleted, when
        the VNIC is terminated, or when the instance is terminated. An ephemeral
        public IP must always be assigned to a private IP.

        * `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
        whenever you like. It does not need to be assigned to a private IP at all times.

        For more information and comparison of the two types,
        see `Public IP Addresses`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm

        Allowed values for this property are: "EPHEMERAL", "RESERVED"


        :return: The lifetime of this PublicIp.
        :rtype: str
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """
        Sets the lifetime of this PublicIp.
        Defines when the public IP is deleted and released back to Oracle's public IP pool.

        * `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned private IP. The
        ephemeral public IP is automatically deleted when its private IP is deleted, when
        the VNIC is terminated, or when the instance is terminated. An ephemeral
        public IP must always be assigned to a private IP.

        * `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
        whenever you like. It does not need to be assigned to a private IP at all times.

        For more information and comparison of the two types,
        see `Public IP Addresses`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm


        :param lifetime: The lifetime of this PublicIp.
        :type: str
        """
        allowed_values = ["EPHEMERAL", "RESERVED"]
        if not value_allowed_none_or_none_sentinel(lifetime, allowed_values):
            raise ValueError(
                "Invalid value for `lifetime`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifetime = lifetime

    @property
    def private_ip_id(self):
        """
        Gets the private_ip_id of this PublicIp.
        The `OCID`__ of the private IP that the public IP is currently assigned to, or in the
        process of being assigned to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The private_ip_id of this PublicIp.
        :rtype: str
        """
        return self._private_ip_id

    @private_ip_id.setter
    def private_ip_id(self, private_ip_id):
        """
        Sets the private_ip_id of this PublicIp.
        The `OCID`__ of the private IP that the public IP is currently assigned to, or in the
        process of being assigned to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param private_ip_id: The private_ip_id of this PublicIp.
        :type: str
        """
        self._private_ip_id = private_ip_id

    @property
    def scope(self):
        """
        Gets the scope of this PublicIp.
        Whether the public IP is regional or specific to a particular availability domain.

        * `REGION`: The public IP exists within a region and can be assigned to a private IP
        in any availability domain in the region. Reserved public IPs have `scope` = `REGION`.

        * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the private IP
        it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
        Ephemeral public IPs have `scope` = `AVAILABILITY_DOMAIN`.

        Allowed values for this property are: "REGION", "AVAILABILITY_DOMAIN"


        :return: The scope of this PublicIp.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this PublicIp.
        Whether the public IP is regional or specific to a particular availability domain.

        * `REGION`: The public IP exists within a region and can be assigned to a private IP
        in any availability domain in the region. Reserved public IPs have `scope` = `REGION`.

        * `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the private IP
        it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
        Ephemeral public IPs have `scope` = `AVAILABILITY_DOMAIN`.


        :param scope: The scope of this PublicIp.
        :type: str
        """
        allowed_values = ["REGION", "AVAILABILITY_DOMAIN"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                "Invalid value for `scope`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scope = scope

    @property
    def time_created(self):
        """
        Gets the time_created of this PublicIp.
        The date and time the public IP was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PublicIp.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PublicIp.
        The date and time the public IP was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PublicIp.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
