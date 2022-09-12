# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VantagePointNode(object):
    """
    Vantage Point Node
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VantagePointNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VantagePointNode.
        :type id: str

        :param name:
            The value to assign to the name property of this VantagePointNode.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this VantagePointNode.
        :type display_name: str

        :param geo_info:
            The value to assign to the geo_info property of this VantagePointNode.
        :type geo_info: str

        :param outgoing_links:
            The value to assign to the outgoing_links property of this VantagePointNode.
        :type outgoing_links: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'geo_info': 'str',
            'outgoing_links': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'geo_info': 'geoInfo',
            'outgoing_links': 'outgoingLinks'
        }

        self._id = None
        self._name = None
        self._display_name = None
        self._geo_info = None
        self._outgoing_links = None

    @property
    def id(self):
        """
        Gets the id of this VantagePointNode.
        id of Vantage Point node


        :return: The id of this VantagePointNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VantagePointNode.
        id of Vantage Point node


        :param id: The id of this VantagePointNode.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this VantagePointNode.
        name of Vantage Point node


        :return: The name of this VantagePointNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VantagePointNode.
        name of Vantage Point node


        :param name: The name of this VantagePointNode.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this VantagePointNode.
        display name of Vantage Point node


        :return: The display_name of this VantagePointNode.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VantagePointNode.
        display name of Vantage Point node


        :param display_name: The display_name of this VantagePointNode.
        :type: str
        """
        self._display_name = display_name

    @property
    def geo_info(self):
        """
        Gets the geo_info of this VantagePointNode.
        geo info


        :return: The geo_info of this VantagePointNode.
        :rtype: str
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """
        Sets the geo_info of this VantagePointNode.
        geo info


        :param geo_info: The geo_info of this VantagePointNode.
        :type: str
        """
        self._geo_info = geo_info

    @property
    def outgoing_links(self):
        """
        Gets the outgoing_links of this VantagePointNode.
        links outgoing from this Vantage Point node


        :return: The outgoing_links of this VantagePointNode.
        :rtype: list[str]
        """
        return self._outgoing_links

    @outgoing_links.setter
    def outgoing_links(self, outgoing_links):
        """
        Sets the outgoing_links of this VantagePointNode.
        links outgoing from this Vantage Point node


        :param outgoing_links: The outgoing_links of this VantagePointNode.
        :type: list[str]
        """
        self._outgoing_links = outgoing_links

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
