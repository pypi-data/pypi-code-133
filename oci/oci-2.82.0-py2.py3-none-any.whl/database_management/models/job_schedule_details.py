# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobScheduleDetails(object):
    """
    The details of the job schedule.
    """

    #: A constant which can be used with the interval_type property of a JobScheduleDetails.
    #: This constant has a value of "DAILY"
    INTERVAL_TYPE_DAILY = "DAILY"

    #: A constant which can be used with the interval_type property of a JobScheduleDetails.
    #: This constant has a value of "HOURLY"
    INTERVAL_TYPE_HOURLY = "HOURLY"

    #: A constant which can be used with the interval_type property of a JobScheduleDetails.
    #: This constant has a value of "WEEKLY"
    INTERVAL_TYPE_WEEKLY = "WEEKLY"

    #: A constant which can be used with the interval_type property of a JobScheduleDetails.
    #: This constant has a value of "MONTHLY"
    INTERVAL_TYPE_MONTHLY = "MONTHLY"

    #: A constant which can be used with the interval_type property of a JobScheduleDetails.
    #: This constant has a value of "NEVER"
    INTERVAL_TYPE_NEVER = "NEVER"

    def __init__(self, **kwargs):
        """
        Initializes a new JobScheduleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_time:
            The value to assign to the start_time property of this JobScheduleDetails.
        :type start_time: str

        :param end_time:
            The value to assign to the end_time property of this JobScheduleDetails.
        :type end_time: str

        :param interval_type:
            The value to assign to the interval_type property of this JobScheduleDetails.
            Allowed values for this property are: "DAILY", "HOURLY", "WEEKLY", "MONTHLY", "NEVER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type interval_type: str

        :param interval_value:
            The value to assign to the interval_value property of this JobScheduleDetails.
        :type interval_value: str

        """
        self.swagger_types = {
            'start_time': 'str',
            'end_time': 'str',
            'interval_type': 'str',
            'interval_value': 'str'
        }

        self.attribute_map = {
            'start_time': 'startTime',
            'end_time': 'endTime',
            'interval_type': 'intervalType',
            'interval_value': 'intervalValue'
        }

        self._start_time = None
        self._end_time = None
        self._interval_type = None
        self._interval_value = None

    @property
    def start_time(self):
        """
        Gets the start_time of this JobScheduleDetails.
        The start time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The start_time of this JobScheduleDetails.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this JobScheduleDetails.
        The start time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param start_time: The start_time of this JobScheduleDetails.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this JobScheduleDetails.
        The end time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The end_time of this JobScheduleDetails.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this JobScheduleDetails.
        The end time of the scheduled job in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param end_time: The end_time of this JobScheduleDetails.
        :type: str
        """
        self._end_time = end_time

    @property
    def interval_type(self):
        """
        Gets the interval_type of this JobScheduleDetails.
        The interval type for a recurring scheduled job. For a non-recurring (one time) job, NEVER must be specified as the interval type.

        Allowed values for this property are: "DAILY", "HOURLY", "WEEKLY", "MONTHLY", "NEVER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The interval_type of this JobScheduleDetails.
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        """
        Sets the interval_type of this JobScheduleDetails.
        The interval type for a recurring scheduled job. For a non-recurring (one time) job, NEVER must be specified as the interval type.


        :param interval_type: The interval_type of this JobScheduleDetails.
        :type: str
        """
        allowed_values = ["DAILY", "HOURLY", "WEEKLY", "MONTHLY", "NEVER"]
        if not value_allowed_none_or_none_sentinel(interval_type, allowed_values):
            interval_type = 'UNKNOWN_ENUM_VALUE'
        self._interval_type = interval_type

    @property
    def interval_value(self):
        """
        Gets the interval_value of this JobScheduleDetails.
        The value for the interval period for a recurring scheduled job.


        :return: The interval_value of this JobScheduleDetails.
        :rtype: str
        """
        return self._interval_value

    @interval_value.setter
    def interval_value(self, interval_value):
        """
        Sets the interval_value of this JobScheduleDetails.
        The value for the interval period for a recurring scheduled job.


        :param interval_value: The interval_value of this JobScheduleDetails.
        :type: str
        """
        self._interval_value = interval_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
