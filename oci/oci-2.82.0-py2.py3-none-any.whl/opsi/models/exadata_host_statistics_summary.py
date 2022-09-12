# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .exadata_insight_resource_statistics_aggregation import ExadataInsightResourceStatisticsAggregation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataHostStatisticsSummary(ExadataInsightResourceStatisticsAggregation):
    """
    Host details and statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataHostStatisticsSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.ExadataHostStatisticsSummary.exadata_resource_type` attribute
        of this class is ``HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_resource_type:
            The value to assign to the exadata_resource_type property of this ExadataHostStatisticsSummary.
            Allowed values for this property are: "DATABASE", "HOST", "STORAGE_SERVER", "DISKGROUP"
        :type exadata_resource_type: str

        :param resource_details:
            The value to assign to the resource_details property of this ExadataHostStatisticsSummary.
        :type resource_details: oci.opsi.models.HostDetails

        :param current_statistics:
            The value to assign to the current_statistics property of this ExadataHostStatisticsSummary.
        :type current_statistics: oci.opsi.models.ExadataInsightResourceStatistics

        """
        self.swagger_types = {
            'exadata_resource_type': 'str',
            'resource_details': 'HostDetails',
            'current_statistics': 'ExadataInsightResourceStatistics'
        }

        self.attribute_map = {
            'exadata_resource_type': 'exadataResourceType',
            'resource_details': 'resourceDetails',
            'current_statistics': 'currentStatistics'
        }

        self._exadata_resource_type = None
        self._resource_details = None
        self._current_statistics = None
        self._exadata_resource_type = 'HOST'

    @property
    def resource_details(self):
        """
        **[Required]** Gets the resource_details of this ExadataHostStatisticsSummary.

        :return: The resource_details of this ExadataHostStatisticsSummary.
        :rtype: oci.opsi.models.HostDetails
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        """
        Sets the resource_details of this ExadataHostStatisticsSummary.

        :param resource_details: The resource_details of this ExadataHostStatisticsSummary.
        :type: oci.opsi.models.HostDetails
        """
        self._resource_details = resource_details

    @property
    def current_statistics(self):
        """
        **[Required]** Gets the current_statistics of this ExadataHostStatisticsSummary.

        :return: The current_statistics of this ExadataHostStatisticsSummary.
        :rtype: oci.opsi.models.ExadataInsightResourceStatistics
        """
        return self._current_statistics

    @current_statistics.setter
    def current_statistics(self, current_statistics):
        """
        Sets the current_statistics of this ExadataHostStatisticsSummary.

        :param current_statistics: The current_statistics of this ExadataHostStatisticsSummary.
        :type: oci.opsi.models.ExadataInsightResourceStatistics
        """
        self._current_statistics = current_statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
