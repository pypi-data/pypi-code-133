# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReservedIP(object):
    """
    An object representing a reserved IP address to be attached or that is already attached to a network load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReservedIP object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ReservedIP.
        :type id: str

        """
        self.swagger_types = {
            'id': 'str'
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = None

    @property
    def id(self):
        """
        Gets the id of this ReservedIP.
        OCID of the reserved public IP address created with the virtual cloud network.

        Reserved public IP addresses are IP addresses that are registered using the virtual cloud network API.

        Create a reserved public IP address. When you create the network load balancer, enter the OCID of the reserved public IP address in the
        reservedIp field to attach the IP address to the network load balancer. This task configures the network load balancer to listen to traffic on this IP address.

        Reserved public IP addresses are not deleted when the network load balancer is deleted. The IP addresses become unattached from the network load balancer.

        Example: \"ocid1.publicip.oc1.phx.unique_ID\"


        :return: The id of this ReservedIP.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReservedIP.
        OCID of the reserved public IP address created with the virtual cloud network.

        Reserved public IP addresses are IP addresses that are registered using the virtual cloud network API.

        Create a reserved public IP address. When you create the network load balancer, enter the OCID of the reserved public IP address in the
        reservedIp field to attach the IP address to the network load balancer. This task configures the network load balancer to listen to traffic on this IP address.

        Reserved public IP addresses are not deleted when the network load balancer is deleted. The IP addresses become unattached from the network load balancer.

        Example: \"ocid1.publicip.oc1.phx.unique_ID\"


        :param id: The id of this ReservedIP.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
