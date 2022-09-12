# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .continuous_query_start_policy import ContinuousQueryStartPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbsoluteTimeStartPolicy(ContinuousQueryStartPolicy):
    """
    Policy that defines the exact start time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AbsoluteTimeStartPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.AbsoluteTimeStartPolicy.start_policy_type` attribute
        of this class is ``ABSOLUTE_TIME_START_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_policy_type:
            The value to assign to the start_policy_type property of this AbsoluteTimeStartPolicy.
            Allowed values for this property are: "NO_DELAY_START_POLICY", "ABSOLUTE_TIME_START_POLICY"
        :type start_policy_type: str

        :param query_start_time:
            The value to assign to the query_start_time property of this AbsoluteTimeStartPolicy.
        :type query_start_time: datetime

        """
        self.swagger_types = {
            'start_policy_type': 'str',
            'query_start_time': 'datetime'
        }

        self.attribute_map = {
            'start_policy_type': 'startPolicyType',
            'query_start_time': 'queryStartTime'
        }

        self._start_policy_type = None
        self._query_start_time = None
        self._start_policy_type = 'ABSOLUTE_TIME_START_POLICY'

    @property
    def query_start_time(self):
        """
        Gets the query_start_time of this AbsoluteTimeStartPolicy.
        Time when the query can start, if not specified it can start immediately.


        :return: The query_start_time of this AbsoluteTimeStartPolicy.
        :rtype: datetime
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        """
        Sets the query_start_time of this AbsoluteTimeStartPolicy.
        Time when the query can start, if not specified it can start immediately.


        :param query_start_time: The query_start_time of this AbsoluteTimeStartPolicy.
        :type: datetime
        """
        self._query_start_time = query_start_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
