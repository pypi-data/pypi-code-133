# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionTaskSummary(object):
    """
    Summary of the Transcription Task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionTaskSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TranscriptionTaskSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TranscriptionTaskSummary.
        :type display_name: str

        :param percent_complete:
            The value to assign to the percent_complete property of this TranscriptionTaskSummary.
        :type percent_complete: int

        :param file_size_in_bytes:
            The value to assign to the file_size_in_bytes property of this TranscriptionTaskSummary.
        :type file_size_in_bytes: int

        :param file_duration_in_seconds:
            The value to assign to the file_duration_in_seconds property of this TranscriptionTaskSummary.
        :type file_duration_in_seconds: int

        :param processing_duration_in_seconds:
            The value to assign to the processing_duration_in_seconds property of this TranscriptionTaskSummary.
        :type processing_duration_in_seconds: int

        :param time_started:
            The value to assign to the time_started property of this TranscriptionTaskSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this TranscriptionTaskSummary.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TranscriptionTaskSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TranscriptionTaskSummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'percent_complete': 'int',
            'file_size_in_bytes': 'int',
            'file_duration_in_seconds': 'int',
            'processing_duration_in_seconds': 'int',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'percent_complete': 'percentComplete',
            'file_size_in_bytes': 'fileSizeInBytes',
            'file_duration_in_seconds': 'fileDurationInSeconds',
            'processing_duration_in_seconds': 'processingDurationInSeconds',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._display_name = None
        self._percent_complete = None
        self._file_size_in_bytes = None
        self._file_duration_in_seconds = None
        self._processing_duration_in_seconds = None
        self._time_started = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TranscriptionTaskSummary.
        The `OCID`__ of the task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this TranscriptionTaskSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TranscriptionTaskSummary.
        The `OCID`__ of the task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this TranscriptionTaskSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TranscriptionTaskSummary.
        A user-friendly display name for the task.


        :return: The display_name of this TranscriptionTaskSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TranscriptionTaskSummary.
        A user-friendly display name for the task.


        :param display_name: The display_name of this TranscriptionTaskSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this TranscriptionTaskSummary.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :return: The percent_complete of this TranscriptionTaskSummary.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this TranscriptionTaskSummary.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :param percent_complete: The percent_complete of this TranscriptionTaskSummary.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def file_size_in_bytes(self):
        """
        Gets the file_size_in_bytes of this TranscriptionTaskSummary.
        Size of input file in Bytes.


        :return: The file_size_in_bytes of this TranscriptionTaskSummary.
        :rtype: int
        """
        return self._file_size_in_bytes

    @file_size_in_bytes.setter
    def file_size_in_bytes(self, file_size_in_bytes):
        """
        Sets the file_size_in_bytes of this TranscriptionTaskSummary.
        Size of input file in Bytes.


        :param file_size_in_bytes: The file_size_in_bytes of this TranscriptionTaskSummary.
        :type: int
        """
        self._file_size_in_bytes = file_size_in_bytes

    @property
    def file_duration_in_seconds(self):
        """
        Gets the file_duration_in_seconds of this TranscriptionTaskSummary.
        Duration of input file in Seconds.


        :return: The file_duration_in_seconds of this TranscriptionTaskSummary.
        :rtype: int
        """
        return self._file_duration_in_seconds

    @file_duration_in_seconds.setter
    def file_duration_in_seconds(self, file_duration_in_seconds):
        """
        Sets the file_duration_in_seconds of this TranscriptionTaskSummary.
        Duration of input file in Seconds.


        :param file_duration_in_seconds: The file_duration_in_seconds of this TranscriptionTaskSummary.
        :type: int
        """
        self._file_duration_in_seconds = file_duration_in_seconds

    @property
    def processing_duration_in_seconds(self):
        """
        Gets the processing_duration_in_seconds of this TranscriptionTaskSummary.
        Task proccessing duration, which excludes waiting time in the system.


        :return: The processing_duration_in_seconds of this TranscriptionTaskSummary.
        :rtype: int
        """
        return self._processing_duration_in_seconds

    @processing_duration_in_seconds.setter
    def processing_duration_in_seconds(self, processing_duration_in_seconds):
        """
        Sets the processing_duration_in_seconds of this TranscriptionTaskSummary.
        Task proccessing duration, which excludes waiting time in the system.


        :param processing_duration_in_seconds: The processing_duration_in_seconds of this TranscriptionTaskSummary.
        :type: int
        """
        self._processing_duration_in_seconds = processing_duration_in_seconds

    @property
    def time_started(self):
        """
        Gets the time_started of this TranscriptionTaskSummary.
        Task started time


        :return: The time_started of this TranscriptionTaskSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this TranscriptionTaskSummary.
        Task started time


        :param time_started: The time_started of this TranscriptionTaskSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this TranscriptionTaskSummary.
        Job finished time


        :return: The time_finished of this TranscriptionTaskSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this TranscriptionTaskSummary.
        Job finished time


        :param time_finished: The time_finished of this TranscriptionTaskSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TranscriptionTaskSummary.
        The current state of the Speech Job.


        :return: The lifecycle_state of this TranscriptionTaskSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TranscriptionTaskSummary.
        The current state of the Speech Job.


        :param lifecycle_state: The lifecycle_state of this TranscriptionTaskSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TranscriptionTaskSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TranscriptionTaskSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TranscriptionTaskSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TranscriptionTaskSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
