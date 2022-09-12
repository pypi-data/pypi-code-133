# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrafficNode(object):
    """
    Defines the configuration of the OCI entity that represents a traffic node in `PathAnalysisResult`.
    """

    #: A constant which can be used with the type property of a TrafficNode.
    #: This constant has a value of "VISIBLE"
    TYPE_VISIBLE = "VISIBLE"

    #: A constant which can be used with the type property of a TrafficNode.
    #: This constant has a value of "ACCESS_DENIED"
    TYPE_ACCESS_DENIED = "ACCESS_DENIED"

    def __init__(self, **kwargs):
        """
        Initializes a new TrafficNode object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.VisibleTrafficNode`
        * :class:`~oci.vn_monitoring.models.AccessDeniedTrafficNode`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TrafficNode.
            Allowed values for this property are: "VISIBLE", "ACCESS_DENIED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param egress_traffic:
            The value to assign to the egress_traffic property of this TrafficNode.
        :type egress_traffic: oci.vn_monitoring.models.EgressTrafficSpec

        :param next_hop_routing_action:
            The value to assign to the next_hop_routing_action property of this TrafficNode.
        :type next_hop_routing_action: oci.vn_monitoring.models.RoutingAction

        :param egress_security_action:
            The value to assign to the egress_security_action property of this TrafficNode.
        :type egress_security_action: oci.vn_monitoring.models.SecurityAction

        :param ingress_security_action:
            The value to assign to the ingress_security_action property of this TrafficNode.
        :type ingress_security_action: oci.vn_monitoring.models.SecurityAction

        """
        self.swagger_types = {
            'type': 'str',
            'egress_traffic': 'EgressTrafficSpec',
            'next_hop_routing_action': 'RoutingAction',
            'egress_security_action': 'SecurityAction',
            'ingress_security_action': 'SecurityAction'
        }

        self.attribute_map = {
            'type': 'type',
            'egress_traffic': 'egressTraffic',
            'next_hop_routing_action': 'nextHopRoutingAction',
            'egress_security_action': 'egressSecurityAction',
            'ingress_security_action': 'ingressSecurityAction'
        }

        self._type = None
        self._egress_traffic = None
        self._next_hop_routing_action = None
        self._egress_security_action = None
        self._ingress_security_action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VISIBLE':
            return 'VisibleTrafficNode'

        if type == 'ACCESS_DENIED':
            return 'AccessDeniedTrafficNode'
        else:
            return 'TrafficNode'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TrafficNode.
        Type of the `TrafficNode`.

        Allowed values for this property are: "VISIBLE", "ACCESS_DENIED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TrafficNode.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TrafficNode.
        Type of the `TrafficNode`.


        :param type: The type of this TrafficNode.
        :type: str
        """
        allowed_values = ["VISIBLE", "ACCESS_DENIED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def egress_traffic(self):
        """
        Gets the egress_traffic of this TrafficNode.

        :return: The egress_traffic of this TrafficNode.
        :rtype: oci.vn_monitoring.models.EgressTrafficSpec
        """
        return self._egress_traffic

    @egress_traffic.setter
    def egress_traffic(self, egress_traffic):
        """
        Sets the egress_traffic of this TrafficNode.

        :param egress_traffic: The egress_traffic of this TrafficNode.
        :type: oci.vn_monitoring.models.EgressTrafficSpec
        """
        self._egress_traffic = egress_traffic

    @property
    def next_hop_routing_action(self):
        """
        Gets the next_hop_routing_action of this TrafficNode.

        :return: The next_hop_routing_action of this TrafficNode.
        :rtype: oci.vn_monitoring.models.RoutingAction
        """
        return self._next_hop_routing_action

    @next_hop_routing_action.setter
    def next_hop_routing_action(self, next_hop_routing_action):
        """
        Sets the next_hop_routing_action of this TrafficNode.

        :param next_hop_routing_action: The next_hop_routing_action of this TrafficNode.
        :type: oci.vn_monitoring.models.RoutingAction
        """
        self._next_hop_routing_action = next_hop_routing_action

    @property
    def egress_security_action(self):
        """
        Gets the egress_security_action of this TrafficNode.

        :return: The egress_security_action of this TrafficNode.
        :rtype: oci.vn_monitoring.models.SecurityAction
        """
        return self._egress_security_action

    @egress_security_action.setter
    def egress_security_action(self, egress_security_action):
        """
        Sets the egress_security_action of this TrafficNode.

        :param egress_security_action: The egress_security_action of this TrafficNode.
        :type: oci.vn_monitoring.models.SecurityAction
        """
        self._egress_security_action = egress_security_action

    @property
    def ingress_security_action(self):
        """
        Gets the ingress_security_action of this TrafficNode.

        :return: The ingress_security_action of this TrafficNode.
        :rtype: oci.vn_monitoring.models.SecurityAction
        """
        return self._ingress_security_action

    @ingress_security_action.setter
    def ingress_security_action(self, ingress_security_action):
        """
        Sets the ingress_security_action of this TrafficNode.

        :param ingress_security_action: The ingress_security_action of this TrafficNode.
        :type: oci.vn_monitoring.models.SecurityAction
        """
        self._ingress_security_action = ingress_security_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
