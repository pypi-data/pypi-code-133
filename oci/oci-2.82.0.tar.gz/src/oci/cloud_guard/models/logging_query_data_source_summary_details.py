# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_summary_details import DataSourceSummaryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingQueryDataSourceSummaryDetails(DataSourceSummaryDetails):
    """
    The information about new Logging Query of type DataSourceSummary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingQueryDataSourceSummaryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.LoggingQueryDataSourceSummaryDetails.data_source_feed_provider` attribute
        of this class is ``LOGGINGQUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this LoggingQueryDataSourceSummaryDetails.
            Allowed values for this property are: "LOGGINGQUERY"
        :type data_source_feed_provider: str

        :param regions:
            The value to assign to the regions property of this LoggingQueryDataSourceSummaryDetails.
        :type regions: list[str]

        :param data_source_detector_mapping_info:
            The value to assign to the data_source_detector_mapping_info property of this LoggingQueryDataSourceSummaryDetails.
        :type data_source_detector_mapping_info: list[oci.cloud_guard.models.DataSourceMappingInfo]

        :param region_status_detail:
            The value to assign to the region_status_detail property of this LoggingQueryDataSourceSummaryDetails.
        :type region_status_detail: list[oci.cloud_guard.models.RegionStatusDetail]

        """
        self.swagger_types = {
            'data_source_feed_provider': 'str',
            'regions': 'list[str]',
            'data_source_detector_mapping_info': 'list[DataSourceMappingInfo]',
            'region_status_detail': 'list[RegionStatusDetail]'
        }

        self.attribute_map = {
            'data_source_feed_provider': 'dataSourceFeedProvider',
            'regions': 'regions',
            'data_source_detector_mapping_info': 'dataSourceDetectorMappingInfo',
            'region_status_detail': 'regionStatusDetail'
        }

        self._data_source_feed_provider = None
        self._regions = None
        self._data_source_detector_mapping_info = None
        self._region_status_detail = None
        self._data_source_feed_provider = 'LOGGINGQUERY'

    @property
    def regions(self):
        """
        Gets the regions of this LoggingQueryDataSourceSummaryDetails.
        DataSource customer specified regions


        :return: The regions of this LoggingQueryDataSourceSummaryDetails.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this LoggingQueryDataSourceSummaryDetails.
        DataSource customer specified regions


        :param regions: The regions of this LoggingQueryDataSourceSummaryDetails.
        :type: list[str]
        """
        self._regions = regions

    @property
    def data_source_detector_mapping_info(self):
        """
        Gets the data_source_detector_mapping_info of this LoggingQueryDataSourceSummaryDetails.
        DataSource mapping with detectorRecipe and detectorRule


        :return: The data_source_detector_mapping_info of this LoggingQueryDataSourceSummaryDetails.
        :rtype: list[oci.cloud_guard.models.DataSourceMappingInfo]
        """
        return self._data_source_detector_mapping_info

    @data_source_detector_mapping_info.setter
    def data_source_detector_mapping_info(self, data_source_detector_mapping_info):
        """
        Sets the data_source_detector_mapping_info of this LoggingQueryDataSourceSummaryDetails.
        DataSource mapping with detectorRecipe and detectorRule


        :param data_source_detector_mapping_info: The data_source_detector_mapping_info of this LoggingQueryDataSourceSummaryDetails.
        :type: list[oci.cloud_guard.models.DataSourceMappingInfo]
        """
        self._data_source_detector_mapping_info = data_source_detector_mapping_info

    @property
    def region_status_detail(self):
        """
        Gets the region_status_detail of this LoggingQueryDataSourceSummaryDetails.
        DataSource query metadata replication region and status.


        :return: The region_status_detail of this LoggingQueryDataSourceSummaryDetails.
        :rtype: list[oci.cloud_guard.models.RegionStatusDetail]
        """
        return self._region_status_detail

    @region_status_detail.setter
    def region_status_detail(self, region_status_detail):
        """
        Sets the region_status_detail of this LoggingQueryDataSourceSummaryDetails.
        DataSource query metadata replication region and status.


        :param region_status_detail: The region_status_detail of this LoggingQueryDataSourceSummaryDetails.
        :type: list[oci.cloud_guard.models.RegionStatusDetail]
        """
        self._region_status_detail = region_status_detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
