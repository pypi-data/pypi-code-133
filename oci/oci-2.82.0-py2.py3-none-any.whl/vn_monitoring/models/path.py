# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Path(object):
    """
    Defines the configuration of the traffic path in `PathAnalysisResult`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Path object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param forward_route:
            The value to assign to the forward_route property of this Path.
        :type forward_route: oci.vn_monitoring.models.TrafficRoute

        :param return_route:
            The value to assign to the return_route property of this Path.
        :type return_route: oci.vn_monitoring.models.TrafficRoute

        :param topology:
            The value to assign to the topology property of this Path.
        :type topology: oci.vn_monitoring.models.PathTopology

        """
        self.swagger_types = {
            'forward_route': 'TrafficRoute',
            'return_route': 'TrafficRoute',
            'topology': 'PathTopology'
        }

        self.attribute_map = {
            'forward_route': 'forwardRoute',
            'return_route': 'returnRoute',
            'topology': 'topology'
        }

        self._forward_route = None
        self._return_route = None
        self._topology = None

    @property
    def forward_route(self):
        """
        **[Required]** Gets the forward_route of this Path.

        :return: The forward_route of this Path.
        :rtype: oci.vn_monitoring.models.TrafficRoute
        """
        return self._forward_route

    @forward_route.setter
    def forward_route(self, forward_route):
        """
        Sets the forward_route of this Path.

        :param forward_route: The forward_route of this Path.
        :type: oci.vn_monitoring.models.TrafficRoute
        """
        self._forward_route = forward_route

    @property
    def return_route(self):
        """
        Gets the return_route of this Path.

        :return: The return_route of this Path.
        :rtype: oci.vn_monitoring.models.TrafficRoute
        """
        return self._return_route

    @return_route.setter
    def return_route(self, return_route):
        """
        Sets the return_route of this Path.

        :param return_route: The return_route of this Path.
        :type: oci.vn_monitoring.models.TrafficRoute
        """
        self._return_route = return_route

    @property
    def topology(self):
        """
        **[Required]** Gets the topology of this Path.

        :return: The topology of this Path.
        :rtype: oci.vn_monitoring.models.PathTopology
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """
        Sets the topology of this Path.

        :param topology: The topology of this Path.
        :type: oci.vn_monitoring.models.PathTopology
        """
        self._topology = topology

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
