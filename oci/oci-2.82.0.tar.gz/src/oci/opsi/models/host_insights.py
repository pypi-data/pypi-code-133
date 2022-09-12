# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInsights(object):
    """
    Logical grouping used for Operations Insights host related operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostInsights object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_insights:
            The value to assign to the host_insights property of this HostInsights.
        :type host_insights: object

        """
        self.swagger_types = {
            'host_insights': 'object'
        }

        self.attribute_map = {
            'host_insights': 'hostInsights'
        }

        self._host_insights = None

    @property
    def host_insights(self):
        """
        Gets the host_insights of this HostInsights.
        Host Insights Object.


        :return: The host_insights of this HostInsights.
        :rtype: object
        """
        return self._host_insights

    @host_insights.setter
    def host_insights(self, host_insights):
        """
        Sets the host_insights of this HostInsights.
        Host Insights Object.


        :param host_insights: The host_insights of this HostInsights.
        :type: object
        """
        self._host_insights = host_insights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
