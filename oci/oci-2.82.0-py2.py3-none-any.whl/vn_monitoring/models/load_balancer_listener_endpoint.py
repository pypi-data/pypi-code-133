# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .endpoint import Endpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerListenerEndpoint(Endpoint):
    """
    Defines the details required for a LOAD_BALANCER_LISTENER-type `Endpoint`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerListenerEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.LoadBalancerListenerEndpoint.type` attribute
        of this class is ``LOAD_BALANCER_LISTENER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LoadBalancerListenerEndpoint.
            Allowed values for this property are: "IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN"
        :type type: str

        :param listener_id:
            The value to assign to the listener_id property of this LoadBalancerListenerEndpoint.
        :type listener_id: str

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this LoadBalancerListenerEndpoint.
        :type load_balancer_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'listener_id': 'str',
            'load_balancer_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'listener_id': 'listenerId',
            'load_balancer_id': 'loadBalancerId'
        }

        self._type = None
        self._listener_id = None
        self._load_balancer_id = None
        self._type = 'LOAD_BALANCER_LISTENER'

    @property
    def listener_id(self):
        """
        **[Required]** Gets the listener_id of this LoadBalancerListenerEndpoint.
        The `OCID`__ of the load balancer listener.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The listener_id of this LoadBalancerListenerEndpoint.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """
        Sets the listener_id of this LoadBalancerListenerEndpoint.
        The `OCID`__ of the load balancer listener.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param listener_id: The listener_id of this LoadBalancerListenerEndpoint.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this LoadBalancerListenerEndpoint.
        The `OCID`__ of the listener's load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this LoadBalancerListenerEndpoint.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this LoadBalancerListenerEndpoint.
        The `OCID`__ of the listener's load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this LoadBalancerListenerEndpoint.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
