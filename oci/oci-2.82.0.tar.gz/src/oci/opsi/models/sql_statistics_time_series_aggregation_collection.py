# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatisticsTimeSeriesAggregationCollection(object):
    """
    SQL performance statistics over the selected time window.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatisticsTimeSeriesAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type sql_identifier: str

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type time_interval_end: datetime

        :param item_duration_in_ms:
            The value to assign to the item_duration_in_ms property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type item_duration_in_ms: int

        :param end_timestamps:
            The value to assign to the end_timestamps property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type end_timestamps: list[datetime]

        :param items:
            The value to assign to the items property of this SqlStatisticsTimeSeriesAggregationCollection.
        :type items: list[oci.opsi.models.SqlStatisticsTimeSeriesAggregation]

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'item_duration_in_ms': 'int',
            'end_timestamps': 'list[datetime]',
            'items': 'list[SqlStatisticsTimeSeriesAggregation]'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'item_duration_in_ms': 'itemDurationInMs',
            'end_timestamps': 'endTimestamps',
            'items': 'items'
        }

        self._sql_identifier = None
        self._time_interval_start = None
        self._time_interval_end = None
        self._item_duration_in_ms = None
        self._end_timestamps = None
        self._items = None

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlStatisticsTimeSeriesAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlStatisticsTimeSeriesAggregationCollection.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SqlStatisticsTimeSeriesAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SqlStatisticsTimeSeriesAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SqlStatisticsTimeSeriesAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SqlStatisticsTimeSeriesAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def item_duration_in_ms(self):
        """
        **[Required]** Gets the item_duration_in_ms of this SqlStatisticsTimeSeriesAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :return: The item_duration_in_ms of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: int
        """
        return self._item_duration_in_ms

    @item_duration_in_ms.setter
    def item_duration_in_ms(self, item_duration_in_ms):
        """
        Sets the item_duration_in_ms of this SqlStatisticsTimeSeriesAggregationCollection.
        Time duration in milliseconds between data points (one hour or one day).


        :param item_duration_in_ms: The item_duration_in_ms of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: int
        """
        self._item_duration_in_ms = item_duration_in_ms

    @property
    def end_timestamps(self):
        """
        Gets the end_timestamps of this SqlStatisticsTimeSeriesAggregationCollection.
        Array comprising of all the sampling period end timestamps in RFC 3339 format.


        :return: The end_timestamps of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: list[datetime]
        """
        return self._end_timestamps

    @end_timestamps.setter
    def end_timestamps(self, end_timestamps):
        """
        Sets the end_timestamps of this SqlStatisticsTimeSeriesAggregationCollection.
        Array comprising of all the sampling period end timestamps in RFC 3339 format.


        :param end_timestamps: The end_timestamps of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: list[datetime]
        """
        self._end_timestamps = end_timestamps

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SqlStatisticsTimeSeriesAggregationCollection.
        Array of SQL performance statistics across databases.


        :return: The items of this SqlStatisticsTimeSeriesAggregationCollection.
        :rtype: list[oci.opsi.models.SqlStatisticsTimeSeriesAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SqlStatisticsTimeSeriesAggregationCollection.
        Array of SQL performance statistics across databases.


        :param items: The items of this SqlStatisticsTimeSeriesAggregationCollection.
        :type: list[oci.opsi.models.SqlStatisticsTimeSeriesAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
