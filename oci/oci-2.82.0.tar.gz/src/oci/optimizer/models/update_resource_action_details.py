# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResourceActionDetails(object):
    """
    The request object for updating the resource action details.
    """

    #: A constant which can be used with the status property of a UpdateResourceActionDetails.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a UpdateResourceActionDetails.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    #: A constant which can be used with the status property of a UpdateResourceActionDetails.
    #: This constant has a value of "POSTPONED"
    STATUS_POSTPONED = "POSTPONED"

    #: A constant which can be used with the status property of a UpdateResourceActionDetails.
    #: This constant has a value of "IMPLEMENTED"
    STATUS_IMPLEMENTED = "IMPLEMENTED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResourceActionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateResourceActionDetails.
            Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"
        :type status: str

        :param time_status_end:
            The value to assign to the time_status_end property of this UpdateResourceActionDetails.
        :type time_status_end: datetime

        """
        self.swagger_types = {
            'status': 'str',
            'time_status_end': 'datetime'
        }

        self.attribute_map = {
            'status': 'status',
            'time_status_end': 'timeStatusEnd'
        }

        self._status = None
        self._time_status_end = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateResourceActionDetails.
        The status of the resource action.

        Allowed values for this property are: "PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"


        :return: The status of this UpdateResourceActionDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateResourceActionDetails.
        The status of the resource action.


        :param status: The status of this UpdateResourceActionDetails.
        :type: str
        """
        allowed_values = ["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def time_status_end(self):
        """
        Gets the time_status_end of this UpdateResourceActionDetails.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :return: The time_status_end of this UpdateResourceActionDetails.
        :rtype: datetime
        """
        return self._time_status_end

    @time_status_end.setter
    def time_status_end(self, time_status_end):
        """
        Sets the time_status_end of this UpdateResourceActionDetails.
        The date and time the current status will change. The format is defined by RFC3339.

        For example, \"The current `postponed` status of the resource action will end and change to `pending` on this
        date and time.\"


        :param time_status_end: The time_status_end of this UpdateResourceActionDetails.
        :type: datetime
        """
        self._time_status_end = time_status_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
