# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResolverSummary(object):
    """
    An OCI DNS resolver. If the resolver has an attached VCN, the VCN will attempt to answer queries based on the
    attached views in priority order. If the query does not match any of the attached views, the query will be
    evaluated against the default view. If the default view does not match, the rules will be evaluated in
    priority order. If no rules match the query, answers come from Internet DNS. A resolver may have a maximum of 10
    resolver endpoints.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ResolverSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new ResolverSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ResolverSummary.
        :type compartment_id: str

        :param attached_vcn_id:
            The value to assign to the attached_vcn_id property of this ResolverSummary.
        :type attached_vcn_id: str

        :param display_name:
            The value to assign to the display_name property of this ResolverSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResolverSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResolverSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param id:
            The value to assign to the id property of this ResolverSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this ResolverSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ResolverSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ResolverSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param _self:
            The value to assign to the _self property of this ResolverSummary.
        :type _self: str

        :param default_view_id:
            The value to assign to the default_view_id property of this ResolverSummary.
        :type default_view_id: str

        :param is_protected:
            The value to assign to the is_protected property of this ResolverSummary.
        :type is_protected: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'attached_vcn_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            '_self': 'str',
            'default_view_id': 'str',
            'is_protected': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'attached_vcn_id': 'attachedVcnId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'id': 'id',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            '_self': 'self',
            'default_view_id': 'defaultViewId',
            'is_protected': 'isProtected'
        }

        self._compartment_id = None
        self._attached_vcn_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self.__self = None
        self._default_view_id = None
        self._is_protected = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResolverSummary.
        The OCID of the owning compartment.


        :return: The compartment_id of this ResolverSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResolverSummary.
        The OCID of the owning compartment.


        :param compartment_id: The compartment_id of this ResolverSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def attached_vcn_id(self):
        """
        Gets the attached_vcn_id of this ResolverSummary.
        The OCID of the attached VCN.


        :return: The attached_vcn_id of this ResolverSummary.
        :rtype: str
        """
        return self._attached_vcn_id

    @attached_vcn_id.setter
    def attached_vcn_id(self, attached_vcn_id):
        """
        Sets the attached_vcn_id of this ResolverSummary.
        The OCID of the attached VCN.


        :param attached_vcn_id: The attached_vcn_id of this ResolverSummary.
        :type: str
        """
        self._attached_vcn_id = attached_vcn_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ResolverSummary.
        The display name of the resolver.


        :return: The display_name of this ResolverSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResolverSummary.
        The display name of the resolver.


        :param display_name: The display_name of this ResolverSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ResolverSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ResolverSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResolverSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ResolverSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ResolverSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ResolverSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResolverSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ResolverSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResolverSummary.
        The OCID of the resolver.


        :return: The id of this ResolverSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResolverSummary.
        The OCID of the resolver.


        :param id: The id of this ResolverSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ResolverSummary.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this ResolverSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResolverSummary.
        The date and time the resource was created in \"YYYY-MM-ddThh:mm:ssZ\" format
        with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this ResolverSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ResolverSummary.
        The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\"
        format with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_updated of this ResolverSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ResolverSummary.
        The date and time the resource was last updated in \"YYYY-MM-ddThh:mm:ssZ\"
        format with a Z offset, as defined by RFC 3339.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_updated: The time_updated of this ResolverSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ResolverSummary.
        The current state of the resource.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ResolverSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ResolverSummary.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this ResolverSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def _self(self):
        """
        **[Required]** Gets the _self of this ResolverSummary.
        The canonical absolute URL of the resource.


        :return: The _self of this ResolverSummary.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this ResolverSummary.
        The canonical absolute URL of the resource.


        :param _self: The _self of this ResolverSummary.
        :type: str
        """
        self.__self = _self

    @property
    def default_view_id(self):
        """
        Gets the default_view_id of this ResolverSummary.
        The OCID of the default view.


        :return: The default_view_id of this ResolverSummary.
        :rtype: str
        """
        return self._default_view_id

    @default_view_id.setter
    def default_view_id(self, default_view_id):
        """
        Sets the default_view_id of this ResolverSummary.
        The OCID of the default view.


        :param default_view_id: The default_view_id of this ResolverSummary.
        :type: str
        """
        self._default_view_id = default_view_id

    @property
    def is_protected(self):
        """
        **[Required]** Gets the is_protected of this ResolverSummary.
        A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.


        :return: The is_protected of this ResolverSummary.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """
        Sets the is_protected of this ResolverSummary.
        A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.


        :param is_protected: The is_protected of this ResolverSummary.
        :type: bool
        """
        self._is_protected = is_protected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
