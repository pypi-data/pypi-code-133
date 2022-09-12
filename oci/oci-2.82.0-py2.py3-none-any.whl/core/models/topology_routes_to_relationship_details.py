# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyRoutesToRelationshipDetails(object):
    """
    Defines route rule details for a `routesTo` relationship.
    """

    #: A constant which can be used with the route_type property of a TopologyRoutesToRelationshipDetails.
    #: This constant has a value of "STATIC"
    ROUTE_TYPE_STATIC = "STATIC"

    #: A constant which can be used with the route_type property of a TopologyRoutesToRelationshipDetails.
    #: This constant has a value of "DYNAMIC"
    ROUTE_TYPE_DYNAMIC = "DYNAMIC"

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyRoutesToRelationshipDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_type:
            The value to assign to the destination_type property of this TopologyRoutesToRelationshipDetails.
        :type destination_type: str

        :param destination:
            The value to assign to the destination property of this TopologyRoutesToRelationshipDetails.
        :type destination: str

        :param route_table_id:
            The value to assign to the route_table_id property of this TopologyRoutesToRelationshipDetails.
        :type route_table_id: str

        :param route_type:
            The value to assign to the route_type property of this TopologyRoutesToRelationshipDetails.
            Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type route_type: str

        """
        self.swagger_types = {
            'destination_type': 'str',
            'destination': 'str',
            'route_table_id': 'str',
            'route_type': 'str'
        }

        self.attribute_map = {
            'destination_type': 'destinationType',
            'destination': 'destination',
            'route_table_id': 'routeTableId',
            'route_type': 'routeType'
        }

        self._destination_type = None
        self._destination = None
        self._route_table_id = None
        self._route_type = None

    @property
    def destination_type(self):
        """
        **[Required]** Gets the destination_type of this TopologyRoutesToRelationshipDetails.
        The destinationType can be set to one of two values:

        * Use `CIDR_BLOCK` if the rule's `destination` is an IP address range in CIDR notation.

        * Use `SERVICE_CIDR_BLOCK` if the rule's `destination` is the `cidrBlock` value for a :class:`Service`.


        :return: The destination_type of this TopologyRoutesToRelationshipDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this TopologyRoutesToRelationshipDetails.
        The destinationType can be set to one of two values:

        * Use `CIDR_BLOCK` if the rule's `destination` is an IP address range in CIDR notation.

        * Use `SERVICE_CIDR_BLOCK` if the rule's `destination` is the `cidrBlock` value for a :class:`Service`.


        :param destination_type: The destination_type of this TopologyRoutesToRelationshipDetails.
        :type: str
        """
        self._destination_type = destination_type

    @property
    def destination(self):
        """
        **[Required]** Gets the destination of this TopologyRoutesToRelationshipDetails.
        An IP address range in CIDR notation or the `cidrBlock` value for a :class:`Service`.


        :return: The destination of this TopologyRoutesToRelationshipDetails.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this TopologyRoutesToRelationshipDetails.
        An IP address range in CIDR notation or the `cidrBlock` value for a :class:`Service`.


        :param destination: The destination of this TopologyRoutesToRelationshipDetails.
        :type: str
        """
        self._destination = destination

    @property
    def route_table_id(self):
        """
        **[Required]** Gets the route_table_id of this TopologyRoutesToRelationshipDetails.
        The `OCID`__ of the routing table that contains the route rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The route_table_id of this TopologyRoutesToRelationshipDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this TopologyRoutesToRelationshipDetails.
        The `OCID`__ of the routing table that contains the route rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param route_table_id: The route_table_id of this TopologyRoutesToRelationshipDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def route_type(self):
        """
        Gets the route_type of this TopologyRoutesToRelationshipDetails.
        A route rule can be `STATIC` if manually added to the route table or `DYNAMIC` if imported from another route table.

        Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The route_type of this TopologyRoutesToRelationshipDetails.
        :rtype: str
        """
        return self._route_type

    @route_type.setter
    def route_type(self, route_type):
        """
        Sets the route_type of this TopologyRoutesToRelationshipDetails.
        A route rule can be `STATIC` if manually added to the route table or `DYNAMIC` if imported from another route table.


        :param route_type: The route_type of this TopologyRoutesToRelationshipDetails.
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC"]
        if not value_allowed_none_or_none_sentinel(route_type, allowed_values):
            route_type = 'UNKNOWN_ENUM_VALUE'
        self._route_type = route_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
