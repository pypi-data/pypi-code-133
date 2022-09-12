# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .date_range import DateRange
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicDateRange(DateRange):
    """
    The saved dynamic date range (Required when staticDateRange is missing).
    """

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "LAST_7_DAYS"
    DYNAMIC_DATE_RANGE_TYPE_LAST_7_DAYS = "LAST_7_DAYS"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "LAST_CALENDAR_WEEK"
    DYNAMIC_DATE_RANGE_TYPE_LAST_CALENDAR_WEEK = "LAST_CALENDAR_WEEK"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "LAST_CALENDAR_MONTH"
    DYNAMIC_DATE_RANGE_TYPE_LAST_CALENDAR_MONTH = "LAST_CALENDAR_MONTH"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "LAST_30_DAYS"
    DYNAMIC_DATE_RANGE_TYPE_LAST_30_DAYS = "LAST_30_DAYS"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "MONTH_TO_DATE"
    DYNAMIC_DATE_RANGE_TYPE_MONTH_TO_DATE = "MONTH_TO_DATE"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "LAST_YEAR"
    DYNAMIC_DATE_RANGE_TYPE_LAST_YEAR = "LAST_YEAR"

    #: A constant which can be used with the dynamic_date_range_type property of a DynamicDateRange.
    #: This constant has a value of "YEAR_TODATE"
    DYNAMIC_DATE_RANGE_TYPE_YEAR_TODATE = "YEAR_TODATE"

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicDateRange object with values from keyword arguments. The default value of the :py:attr:`~oci.usage_api.models.DynamicDateRange.date_range_type` attribute
        of this class is ``DYNAMIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param date_range_type:
            The value to assign to the date_range_type property of this DynamicDateRange.
            Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type date_range_type: str

        :param dynamic_date_range_type:
            The value to assign to the dynamic_date_range_type property of this DynamicDateRange.
            Allowed values for this property are: "LAST_7_DAYS", "LAST_CALENDAR_WEEK", "LAST_CALENDAR_MONTH", "LAST_30_DAYS", "MONTH_TO_DATE", "LAST_YEAR", "YEAR_TODATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dynamic_date_range_type: str

        """
        self.swagger_types = {
            'date_range_type': 'str',
            'dynamic_date_range_type': 'str'
        }

        self.attribute_map = {
            'date_range_type': 'dateRangeType',
            'dynamic_date_range_type': 'dynamicDateRangeType'
        }

        self._date_range_type = None
        self._dynamic_date_range_type = None
        self._date_range_type = 'DYNAMIC'

    @property
    def dynamic_date_range_type(self):
        """
        **[Required]** Gets the dynamic_date_range_type of this DynamicDateRange.
        Allowed values for this property are: "LAST_7_DAYS", "LAST_CALENDAR_WEEK", "LAST_CALENDAR_MONTH", "LAST_30_DAYS", "MONTH_TO_DATE", "LAST_YEAR", "YEAR_TODATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dynamic_date_range_type of this DynamicDateRange.
        :rtype: str
        """
        return self._dynamic_date_range_type

    @dynamic_date_range_type.setter
    def dynamic_date_range_type(self, dynamic_date_range_type):
        """
        Sets the dynamic_date_range_type of this DynamicDateRange.

        :param dynamic_date_range_type: The dynamic_date_range_type of this DynamicDateRange.
        :type: str
        """
        allowed_values = ["LAST_7_DAYS", "LAST_CALENDAR_WEEK", "LAST_CALENDAR_MONTH", "LAST_30_DAYS", "MONTH_TO_DATE", "LAST_YEAR", "YEAR_TODATE"]
        if not value_allowed_none_or_none_sentinel(dynamic_date_range_type, allowed_values):
            dynamic_date_range_type = 'UNKNOWN_ENUM_VALUE'
        self._dynamic_date_range_type = dynamic_date_range_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
