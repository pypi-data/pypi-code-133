# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Whitelist(object):
    """
    An array of IP addresses that bypass the Web Application Firewall. Supports both single IP addresses or subnet masks (CIDR notation).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Whitelist object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Whitelist.
        :type name: str

        :param addresses:
            The value to assign to the addresses property of this Whitelist.
        :type addresses: list[str]

        :param address_lists:
            The value to assign to the address_lists property of this Whitelist.
        :type address_lists: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'addresses': 'list[str]',
            'address_lists': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'addresses': 'addresses',
            'address_lists': 'addressLists'
        }

        self._name = None
        self._addresses = None
        self._address_lists = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Whitelist.
        The unique name of the whitelist.


        :return: The name of this Whitelist.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Whitelist.
        The unique name of the whitelist.


        :param name: The name of this Whitelist.
        :type: str
        """
        self._name = name

    @property
    def addresses(self):
        """
        Gets the addresses of this Whitelist.
        A set of IP addresses or CIDR notations to include in the whitelist.


        :return: The addresses of this Whitelist.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this Whitelist.
        A set of IP addresses or CIDR notations to include in the whitelist.


        :param addresses: The addresses of this Whitelist.
        :type: list[str]
        """
        self._addresses = addresses

    @property
    def address_lists(self):
        """
        Gets the address_lists of this Whitelist.
        A list of `OCID`__ of IP address lists to include in the whitelist.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The address_lists of this Whitelist.
        :rtype: list[str]
        """
        return self._address_lists

    @address_lists.setter
    def address_lists(self, address_lists):
        """
        Sets the address_lists of this Whitelist.
        A list of `OCID`__ of IP address lists to include in the whitelist.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param address_lists: The address_lists of this Whitelist.
        :type: list[str]
        """
        self._address_lists = address_lists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
