# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsOperationTask(object):
    """
    The details of the Optimizer Statistics Collection task.
    """

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "TABLE"
    TARGET_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "GLOBAL_TABLE"
    TARGET_TYPE_GLOBAL_TABLE = "GLOBAL_TABLE"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "COORDINATOR_TABLE"
    TARGET_TYPE_COORDINATOR_TABLE = "COORDINATOR_TABLE"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "TABLE_PARTITION"
    TARGET_TYPE_TABLE_PARTITION = "TABLE_PARTITION"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "TABLE_SUBPARTITION"
    TARGET_TYPE_TABLE_SUBPARTITION = "TABLE_SUBPARTITION"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "INDEX"
    TARGET_TYPE_INDEX = "INDEX"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "INDEX_PARTITION"
    TARGET_TYPE_INDEX_PARTITION = "INDEX_PARTITION"

    #: A constant which can be used with the target_type property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "INDEX_SUBPARTITION"
    TARGET_TYPE_INDEX_SUBPARTITION = "INDEX_SUBPARTITION"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "SKIPPED"
    STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a OptimizerStatisticsOperationTask.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsOperationTask object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target:
            The value to assign to the target property of this OptimizerStatisticsOperationTask.
        :type target: str

        :param target_type:
            The value to assign to the target_type property of this OptimizerStatisticsOperationTask.
            Allowed values for this property are: "TABLE", "GLOBAL_TABLE", "COORDINATOR_TABLE", "TABLE_PARTITION", "TABLE_SUBPARTITION", "INDEX", "INDEX_PARTITION", "INDEX_SUBPARTITION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_type: str

        :param time_start:
            The value to assign to the time_start property of this OptimizerStatisticsOperationTask.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this OptimizerStatisticsOperationTask.
        :type time_end: datetime

        :param status:
            The value to assign to the status property of this OptimizerStatisticsOperationTask.
            Allowed values for this property are: "PENDING", "IN_PROGRESS", "SKIPPED", "TIMED_OUT", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'target': 'str',
            'target_type': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'status': 'str'
        }

        self.attribute_map = {
            'target': 'target',
            'target_type': 'targetType',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'status': 'status'
        }

        self._target = None
        self._target_type = None
        self._time_start = None
        self._time_end = None
        self._status = None

    @property
    def target(self):
        """
        **[Required]** Gets the target of this OptimizerStatisticsOperationTask.
        The name of the target object for which statistics are gathered.


        :return: The target of this OptimizerStatisticsOperationTask.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this OptimizerStatisticsOperationTask.
        The name of the target object for which statistics are gathered.


        :param target: The target of this OptimizerStatisticsOperationTask.
        :type: str
        """
        self._target = target

    @property
    def target_type(self):
        """
        **[Required]** Gets the target_type of this OptimizerStatisticsOperationTask.
        The type of target object.

        Allowed values for this property are: "TABLE", "GLOBAL_TABLE", "COORDINATOR_TABLE", "TABLE_PARTITION", "TABLE_SUBPARTITION", "INDEX", "INDEX_PARTITION", "INDEX_SUBPARTITION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_type of this OptimizerStatisticsOperationTask.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this OptimizerStatisticsOperationTask.
        The type of target object.


        :param target_type: The target_type of this OptimizerStatisticsOperationTask.
        :type: str
        """
        allowed_values = ["TABLE", "GLOBAL_TABLE", "COORDINATOR_TABLE", "TABLE_PARTITION", "TABLE_SUBPARTITION", "INDEX", "INDEX_PARTITION", "INDEX_SUBPARTITION"]
        if not value_allowed_none_or_none_sentinel(target_type, allowed_values):
            target_type = 'UNKNOWN_ENUM_VALUE'
        self._target_type = target_type

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this OptimizerStatisticsOperationTask.
        The start time of the Optimizer Statistics Collection task.


        :return: The time_start of this OptimizerStatisticsOperationTask.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this OptimizerStatisticsOperationTask.
        The start time of the Optimizer Statistics Collection task.


        :param time_start: The time_start of this OptimizerStatisticsOperationTask.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        **[Required]** Gets the time_end of this OptimizerStatisticsOperationTask.
        The end time of the Optimizer Statistics Collection task.


        :return: The time_end of this OptimizerStatisticsOperationTask.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this OptimizerStatisticsOperationTask.
        The end time of the Optimizer Statistics Collection task.


        :param time_end: The time_end of this OptimizerStatisticsOperationTask.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def status(self):
        """
        **[Required]** Gets the status of this OptimizerStatisticsOperationTask.
        The status of the Optimizer Statistics Collection task.

        Allowed values for this property are: "PENDING", "IN_PROGRESS", "SKIPPED", "TIMED_OUT", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this OptimizerStatisticsOperationTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OptimizerStatisticsOperationTask.
        The status of the Optimizer Statistics Collection task.


        :param status: The status of this OptimizerStatisticsOperationTask.
        :type: str
        """
        allowed_values = ["PENDING", "IN_PROGRESS", "SKIPPED", "TIMED_OUT", "COMPLETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
