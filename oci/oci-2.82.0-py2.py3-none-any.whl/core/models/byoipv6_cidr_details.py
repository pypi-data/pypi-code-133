# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Byoipv6CidrDetails(object):
    """
    The list of one or more BYOIPv6 CIDR blocks for the VCN that meets the following criteria:
    - The CIDR must from a BYOIPv6 range.
    - The IPv6 CIDR blocks must be valid.
    - Multiple CIDR blocks must not overlap each other or the on-premises network CIDR block.
    - The number of CIDR blocks must not exceed the limit of IPv6 CIDR blocks allowed to a VCN.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Byoipv6CidrDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param byoipv6_range_id:
            The value to assign to the byoipv6_range_id property of this Byoipv6CidrDetails.
        :type byoipv6_range_id: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this Byoipv6CidrDetails.
        :type ipv6_cidr_block: str

        """
        self.swagger_types = {
            'byoipv6_range_id': 'str',
            'ipv6_cidr_block': 'str'
        }

        self.attribute_map = {
            'byoipv6_range_id': 'byoipv6RangeId',
            'ipv6_cidr_block': 'ipv6CidrBlock'
        }

        self._byoipv6_range_id = None
        self._ipv6_cidr_block = None

    @property
    def byoipv6_range_id(self):
        """
        **[Required]** Gets the byoipv6_range_id of this Byoipv6CidrDetails.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The byoipv6_range_id of this Byoipv6CidrDetails.
        :rtype: str
        """
        return self._byoipv6_range_id

    @byoipv6_range_id.setter
    def byoipv6_range_id(self, byoipv6_range_id):
        """
        Sets the byoipv6_range_id of this Byoipv6CidrDetails.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param byoipv6_range_id: The byoipv6_range_id of this Byoipv6CidrDetails.
        :type: str
        """
        self._byoipv6_range_id = byoipv6_range_id

    @property
    def ipv6_cidr_block(self):
        """
        **[Required]** Gets the ipv6_cidr_block of this Byoipv6CidrDetails.
        An IPv6 CIDR block required to create a VCN with a BYOIP prefix. It could be the whole CIDR block identified in `byoipv6RangeId`, or a subrange.
        Example: `2001:0db8:0123::/48`


        :return: The ipv6_cidr_block of this Byoipv6CidrDetails.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this Byoipv6CidrDetails.
        An IPv6 CIDR block required to create a VCN with a BYOIP prefix. It could be the whole CIDR block identified in `byoipv6RangeId`, or a subrange.
        Example: `2001:0db8:0123::/48`


        :param ipv6_cidr_block: The ipv6_cidr_block of this Byoipv6CidrDetails.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
