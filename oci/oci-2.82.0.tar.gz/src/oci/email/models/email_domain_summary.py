# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmailDomainSummary(object):
    """
    The properties that define a email domain.
    A Email Domain contains configuration used to assert responsibility for emails sent from that domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmailDomainSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this EmailDomainSummary.
        :type name: str

        :param id:
            The value to assign to the id property of this EmailDomainSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmailDomainSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmailDomainSummary.
        :type lifecycle_state: str

        :param active_dkim_id:
            The value to assign to the active_dkim_id property of this EmailDomainSummary.
        :type active_dkim_id: str

        :param description:
            The value to assign to the description property of this EmailDomainSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this EmailDomainSummary.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmailDomainSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmailDomainSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmailDomainSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'active_dkim_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'active_dkim_id': 'activeDkimId',
            'description': 'description',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._name = None
        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._active_dkim_id = None
        self._description = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this EmailDomainSummary.
        The name of the email domain in the Internet Domain Name System (DNS).

        Example: `example.net`


        :return: The name of this EmailDomainSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailDomainSummary.
        The name of the email domain in the Internet Domain Name System (DNS).

        Example: `example.net`


        :param name: The name of this EmailDomainSummary.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EmailDomainSummary.
        The `OCID`__ of the email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this EmailDomainSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmailDomainSummary.
        The `OCID`__ of the email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this EmailDomainSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this EmailDomainSummary.
        The `OCID`__ of the compartment that contains this email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EmailDomainSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EmailDomainSummary.
        The `OCID`__ of the compartment that contains this email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EmailDomainSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EmailDomainSummary.
        The current state of the email domain.


        :return: The lifecycle_state of this EmailDomainSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EmailDomainSummary.
        The current state of the email domain.


        :param lifecycle_state: The lifecycle_state of this EmailDomainSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def active_dkim_id(self):
        """
        Gets the active_dkim_id of this EmailDomainSummary.
        The `OCID`__ of the DKIM key
        that is adding the DKIM signature for this email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The active_dkim_id of this EmailDomainSummary.
        :rtype: str
        """
        return self._active_dkim_id

    @active_dkim_id.setter
    def active_dkim_id(self, active_dkim_id):
        """
        Sets the active_dkim_id of this EmailDomainSummary.
        The `OCID`__ of the DKIM key
        that is adding the DKIM signature for this email domain.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param active_dkim_id: The active_dkim_id of this EmailDomainSummary.
        :type: str
        """
        self._active_dkim_id = active_dkim_id

    @property
    def description(self):
        """
        Gets the description of this EmailDomainSummary.
        The description of a email domain.


        :return: The description of this EmailDomainSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EmailDomainSummary.
        The description of a email domain.


        :param description: The description of this EmailDomainSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this EmailDomainSummary.
        The time the email domain was created, expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        Example: `2021-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EmailDomainSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EmailDomainSummary.
        The time the email domain was created, expressed in `RFC 3339`__
        timestamp format, \"YYYY-MM-ddThh:mmZ\".

        Example: `2021-02-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EmailDomainSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this EmailDomainSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this EmailDomainSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EmailDomainSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this EmailDomainSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this EmailDomainSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this EmailDomainSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EmailDomainSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this EmailDomainSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EmailDomainSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EmailDomainSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EmailDomainSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EmailDomainSummary.
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
