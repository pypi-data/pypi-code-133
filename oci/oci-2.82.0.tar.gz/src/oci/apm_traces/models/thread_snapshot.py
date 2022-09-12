# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ThreadSnapshot(object):
    """
    Thread snapshot.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ThreadSnapshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_stamp:
            The value to assign to the time_stamp property of this ThreadSnapshot.
        :type time_stamp: datetime

        :param thread_snapshot_details:
            The value to assign to the thread_snapshot_details property of this ThreadSnapshot.
        :type thread_snapshot_details: list[oci.apm_traces.models.SnapshotDetail]

        :param stack_trace:
            The value to assign to the stack_trace property of this ThreadSnapshot.
        :type stack_trace: list[oci.apm_traces.models.StackTraceElement]

        """
        self.swagger_types = {
            'time_stamp': 'datetime',
            'thread_snapshot_details': 'list[SnapshotDetail]',
            'stack_trace': 'list[StackTraceElement]'
        }

        self.attribute_map = {
            'time_stamp': 'timeStamp',
            'thread_snapshot_details': 'threadSnapshotDetails',
            'stack_trace': 'stackTrace'
        }

        self._time_stamp = None
        self._thread_snapshot_details = None
        self._stack_trace = None

    @property
    def time_stamp(self):
        """
        Gets the time_stamp of this ThreadSnapshot.
        Snapshot time.


        :return: The time_stamp of this ThreadSnapshot.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """
        Sets the time_stamp of this ThreadSnapshot.
        Snapshot time.


        :param time_stamp: The time_stamp of this ThreadSnapshot.
        :type: datetime
        """
        self._time_stamp = time_stamp

    @property
    def thread_snapshot_details(self):
        """
        Gets the thread_snapshot_details of this ThreadSnapshot.
        Snapshot details.


        :return: The thread_snapshot_details of this ThreadSnapshot.
        :rtype: list[oci.apm_traces.models.SnapshotDetail]
        """
        return self._thread_snapshot_details

    @thread_snapshot_details.setter
    def thread_snapshot_details(self, thread_snapshot_details):
        """
        Sets the thread_snapshot_details of this ThreadSnapshot.
        Snapshot details.


        :param thread_snapshot_details: The thread_snapshot_details of this ThreadSnapshot.
        :type: list[oci.apm_traces.models.SnapshotDetail]
        """
        self._thread_snapshot_details = thread_snapshot_details

    @property
    def stack_trace(self):
        """
        Gets the stack_trace of this ThreadSnapshot.
        Stack trace.


        :return: The stack_trace of this ThreadSnapshot.
        :rtype: list[oci.apm_traces.models.StackTraceElement]
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """
        Sets the stack_trace of this ThreadSnapshot.
        Stack trace.


        :param stack_trace: The stack_trace of this ThreadSnapshot.
        :type: list[oci.apm_traces.models.StackTraceElement]
        """
        self._stack_trace = stack_trace

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
