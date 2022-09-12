# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsCollectionOperation(object):
    """
    The summary of the Optimizer Statistics Collection tasks, which includes details of the Managed Database and the execution.
    """

    #: A constant which can be used with the status property of a OptimizerStatisticsCollectionOperation.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a OptimizerStatisticsCollectionOperation.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a OptimizerStatisticsCollectionOperation.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a OptimizerStatisticsCollectionOperation.
    #: This constant has a value of "TIMED_OUT"
    STATUS_TIMED_OUT = "TIMED_OUT"

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsCollectionOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database:
            The value to assign to the database property of this OptimizerStatisticsCollectionOperation.
        :type database: oci.database_management.models.OptimizerDatabase

        :param tasks:
            The value to assign to the tasks property of this OptimizerStatisticsCollectionOperation.
        :type tasks: list[oci.database_management.models.OptimizerStatisticsOperationTask]

        :param id:
            The value to assign to the id property of this OptimizerStatisticsCollectionOperation.
        :type id: int

        :param operation_name:
            The value to assign to the operation_name property of this OptimizerStatisticsCollectionOperation.
        :type operation_name: str

        :param target:
            The value to assign to the target property of this OptimizerStatisticsCollectionOperation.
        :type target: str

        :param job_name:
            The value to assign to the job_name property of this OptimizerStatisticsCollectionOperation.
        :type job_name: str

        :param status:
            The value to assign to the status property of this OptimizerStatisticsCollectionOperation.
            Allowed values for this property are: "IN_PROGRESS", "COMPLETED", "FAILED", "TIMED_OUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param start_time:
            The value to assign to the start_time property of this OptimizerStatisticsCollectionOperation.
        :type start_time: str

        :param end_time:
            The value to assign to the end_time property of this OptimizerStatisticsCollectionOperation.
        :type end_time: str

        :param duration_in_seconds:
            The value to assign to the duration_in_seconds property of this OptimizerStatisticsCollectionOperation.
        :type duration_in_seconds: float

        :param completed_count:
            The value to assign to the completed_count property of this OptimizerStatisticsCollectionOperation.
        :type completed_count: int

        :param in_progress_count:
            The value to assign to the in_progress_count property of this OptimizerStatisticsCollectionOperation.
        :type in_progress_count: int

        :param failed_count:
            The value to assign to the failed_count property of this OptimizerStatisticsCollectionOperation.
        :type failed_count: int

        :param timed_out_count:
            The value to assign to the timed_out_count property of this OptimizerStatisticsCollectionOperation.
        :type timed_out_count: int

        :param total_objects_count:
            The value to assign to the total_objects_count property of this OptimizerStatisticsCollectionOperation.
        :type total_objects_count: int

        """
        self.swagger_types = {
            'database': 'OptimizerDatabase',
            'tasks': 'list[OptimizerStatisticsOperationTask]',
            'id': 'int',
            'operation_name': 'str',
            'target': 'str',
            'job_name': 'str',
            'status': 'str',
            'start_time': 'str',
            'end_time': 'str',
            'duration_in_seconds': 'float',
            'completed_count': 'int',
            'in_progress_count': 'int',
            'failed_count': 'int',
            'timed_out_count': 'int',
            'total_objects_count': 'int'
        }

        self.attribute_map = {
            'database': 'database',
            'tasks': 'tasks',
            'id': 'id',
            'operation_name': 'operationName',
            'target': 'target',
            'job_name': 'jobName',
            'status': 'status',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'duration_in_seconds': 'durationInSeconds',
            'completed_count': 'completedCount',
            'in_progress_count': 'inProgressCount',
            'failed_count': 'failedCount',
            'timed_out_count': 'timedOutCount',
            'total_objects_count': 'totalObjectsCount'
        }

        self._database = None
        self._tasks = None
        self._id = None
        self._operation_name = None
        self._target = None
        self._job_name = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._duration_in_seconds = None
        self._completed_count = None
        self._in_progress_count = None
        self._failed_count = None
        self._timed_out_count = None
        self._total_objects_count = None

    @property
    def database(self):
        """
        Gets the database of this OptimizerStatisticsCollectionOperation.

        :return: The database of this OptimizerStatisticsCollectionOperation.
        :rtype: oci.database_management.models.OptimizerDatabase
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this OptimizerStatisticsCollectionOperation.

        :param database: The database of this OptimizerStatisticsCollectionOperation.
        :type: oci.database_management.models.OptimizerDatabase
        """
        self._database = database

    @property
    def tasks(self):
        """
        Gets the tasks of this OptimizerStatisticsCollectionOperation.
        An array of Optimizer Statistics Collection task details.


        :return: The tasks of this OptimizerStatisticsCollectionOperation.
        :rtype: list[oci.database_management.models.OptimizerStatisticsOperationTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """
        Sets the tasks of this OptimizerStatisticsCollectionOperation.
        An array of Optimizer Statistics Collection task details.


        :param tasks: The tasks of this OptimizerStatisticsCollectionOperation.
        :type: list[oci.database_management.models.OptimizerStatisticsOperationTask]
        """
        self._tasks = tasks

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OptimizerStatisticsCollectionOperation.
        The ID of the operation.


        :return: The id of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OptimizerStatisticsCollectionOperation.
        The ID of the operation.


        :param id: The id of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._id = id

    @property
    def operation_name(self):
        """
        **[Required]** Gets the operation_name of this OptimizerStatisticsCollectionOperation.
        The name of the operation.


        :return: The operation_name of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """
        Sets the operation_name of this OptimizerStatisticsCollectionOperation.
        The name of the operation.


        :param operation_name: The operation_name of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        self._operation_name = operation_name

    @property
    def target(self):
        """
        **[Required]** Gets the target of this OptimizerStatisticsCollectionOperation.
        The target object type such as Table, Index, and Partition.


        :return: The target of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this OptimizerStatisticsCollectionOperation.
        The target object type such as Table, Index, and Partition.


        :param target: The target of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        self._target = target

    @property
    def job_name(self):
        """
        **[Required]** Gets the job_name of this OptimizerStatisticsCollectionOperation.
        The name of the job.


        :return: The job_name of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this OptimizerStatisticsCollectionOperation.
        The name of the job.


        :param job_name: The job_name of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        self._job_name = job_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this OptimizerStatisticsCollectionOperation.
        The status of the operation such as Completed, and Failed.

        Allowed values for this property are: "IN_PROGRESS", "COMPLETED", "FAILED", "TIMED_OUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OptimizerStatisticsCollectionOperation.
        The status of the operation such as Completed, and Failed.


        :param status: The status of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED", "FAILED", "TIMED_OUT"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def start_time(self):
        """
        **[Required]** Gets the start_time of this OptimizerStatisticsCollectionOperation.
        The start time of the operation.


        :return: The start_time of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this OptimizerStatisticsCollectionOperation.
        The start time of the operation.


        :param start_time: The start_time of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        **[Required]** Gets the end_time of this OptimizerStatisticsCollectionOperation.
        The end time of the operation.


        :return: The end_time of this OptimizerStatisticsCollectionOperation.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this OptimizerStatisticsCollectionOperation.
        The end time of the operation.


        :param end_time: The end_time of this OptimizerStatisticsCollectionOperation.
        :type: str
        """
        self._end_time = end_time

    @property
    def duration_in_seconds(self):
        """
        **[Required]** Gets the duration_in_seconds of this OptimizerStatisticsCollectionOperation.
        The time it takes to complete the operation (in seconds).


        :return: The duration_in_seconds of this OptimizerStatisticsCollectionOperation.
        :rtype: float
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        """
        Sets the duration_in_seconds of this OptimizerStatisticsCollectionOperation.
        The time it takes to complete the operation (in seconds).


        :param duration_in_seconds: The duration_in_seconds of this OptimizerStatisticsCollectionOperation.
        :type: float
        """
        self._duration_in_seconds = duration_in_seconds

    @property
    def completed_count(self):
        """
        Gets the completed_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection is completed.


        :return: The completed_count of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """
        Sets the completed_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection is completed.


        :param completed_count: The completed_count of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._completed_count = completed_count

    @property
    def in_progress_count(self):
        """
        Gets the in_progress_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection is in progress.


        :return: The in_progress_count of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._in_progress_count

    @in_progress_count.setter
    def in_progress_count(self, in_progress_count):
        """
        Sets the in_progress_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection is in progress.


        :param in_progress_count: The in_progress_count of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._in_progress_count = in_progress_count

    @property
    def failed_count(self):
        """
        Gets the failed_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection failed.


        :return: The failed_count of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """
        Sets the failed_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection failed.


        :param failed_count: The failed_count of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._failed_count = failed_count

    @property
    def timed_out_count(self):
        """
        Gets the timed_out_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection timed out.


        :return: The timed_out_count of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._timed_out_count

    @timed_out_count.setter
    def timed_out_count(self, timed_out_count):
        """
        Sets the timed_out_count of this OptimizerStatisticsCollectionOperation.
        The number of objects for which statistics collection timed out.


        :param timed_out_count: The timed_out_count of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._timed_out_count = timed_out_count

    @property
    def total_objects_count(self):
        """
        Gets the total_objects_count of this OptimizerStatisticsCollectionOperation.
        The total number of objects for which statistics is collected. This number is the sum of all the objects
        with various statuses: completed, inProgress, failed, and timedOut.


        :return: The total_objects_count of this OptimizerStatisticsCollectionOperation.
        :rtype: int
        """
        return self._total_objects_count

    @total_objects_count.setter
    def total_objects_count(self, total_objects_count):
        """
        Sets the total_objects_count of this OptimizerStatisticsCollectionOperation.
        The total number of objects for which statistics is collected. This number is the sum of all the objects
        with various statuses: completed, inProgress, failed, and timedOut.


        :param total_objects_count: The total_objects_count of this OptimizerStatisticsCollectionOperation.
        :type: int
        """
        self._total_objects_count = total_objects_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
