# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionJobSummary(object):
    """
    Summary of the Transcription Job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TranscriptionJobSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TranscriptionJobSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TranscriptionJobSummary.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this TranscriptionJobSummary.
        :type created_by: str

        :param percent_complete:
            The value to assign to the percent_complete property of this TranscriptionJobSummary.
        :type percent_complete: int

        :param time_accepted:
            The value to assign to the time_accepted property of this TranscriptionJobSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this TranscriptionJobSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this TranscriptionJobSummary.
        :type time_finished: datetime

        :param total_tasks:
            The value to assign to the total_tasks property of this TranscriptionJobSummary.
        :type total_tasks: int

        :param outstanding_tasks:
            The value to assign to the outstanding_tasks property of this TranscriptionJobSummary.
        :type outstanding_tasks: int

        :param successful_tasks:
            The value to assign to the successful_tasks property of this TranscriptionJobSummary.
        :type successful_tasks: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TranscriptionJobSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TranscriptionJobSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TranscriptionJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TranscriptionJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TranscriptionJobSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'created_by': 'str',
            'percent_complete': 'int',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'total_tasks': 'int',
            'outstanding_tasks': 'int',
            'successful_tasks': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'total_tasks': 'totalTasks',
            'outstanding_tasks': 'outstandingTasks',
            'successful_tasks': 'successfulTasks',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._created_by = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._total_tasks = None
        self._outstanding_tasks = None
        self._successful_tasks = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TranscriptionJobSummary.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TranscriptionJobSummary.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this TranscriptionJobSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TranscriptionJobSummary.
        A user-friendly display name for the job.


        :return: The display_name of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TranscriptionJobSummary.
        A user-friendly display name for the job.


        :param display_name: The display_name of this TranscriptionJobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TranscriptionJobSummary.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TranscriptionJobSummary.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this TranscriptionJobSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        Gets the created_by of this TranscriptionJobSummary.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this TranscriptionJobSummary.
        The `OCID`__ of the user who created the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this TranscriptionJobSummary.
        :type: str
        """
        self._created_by = created_by

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this TranscriptionJobSummary.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :return: The percent_complete of this TranscriptionJobSummary.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this TranscriptionJobSummary.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :param percent_complete: The percent_complete of this TranscriptionJobSummary.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this TranscriptionJobSummary.
        Job accepted time.


        :return: The time_accepted of this TranscriptionJobSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this TranscriptionJobSummary.
        Job accepted time.


        :param time_accepted: The time_accepted of this TranscriptionJobSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this TranscriptionJobSummary.
        Job started time.


        :return: The time_started of this TranscriptionJobSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this TranscriptionJobSummary.
        Job started time.


        :param time_started: The time_started of this TranscriptionJobSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this TranscriptionJobSummary.
        Job finished time.


        :return: The time_finished of this TranscriptionJobSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this TranscriptionJobSummary.
        Job finished time.


        :param time_finished: The time_finished of this TranscriptionJobSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def total_tasks(self):
        """
        Gets the total_tasks of this TranscriptionJobSummary.
        Total number of tasks in a job.


        :return: The total_tasks of this TranscriptionJobSummary.
        :rtype: int
        """
        return self._total_tasks

    @total_tasks.setter
    def total_tasks(self, total_tasks):
        """
        Sets the total_tasks of this TranscriptionJobSummary.
        Total number of tasks in a job.


        :param total_tasks: The total_tasks of this TranscriptionJobSummary.
        :type: int
        """
        self._total_tasks = total_tasks

    @property
    def outstanding_tasks(self):
        """
        Gets the outstanding_tasks of this TranscriptionJobSummary.
        Total outstanding tasks in a job.


        :return: The outstanding_tasks of this TranscriptionJobSummary.
        :rtype: int
        """
        return self._outstanding_tasks

    @outstanding_tasks.setter
    def outstanding_tasks(self, outstanding_tasks):
        """
        Sets the outstanding_tasks of this TranscriptionJobSummary.
        Total outstanding tasks in a job.


        :param outstanding_tasks: The outstanding_tasks of this TranscriptionJobSummary.
        :type: int
        """
        self._outstanding_tasks = outstanding_tasks

    @property
    def successful_tasks(self):
        """
        Gets the successful_tasks of this TranscriptionJobSummary.
        Total successful tasks in a job.


        :return: The successful_tasks of this TranscriptionJobSummary.
        :rtype: int
        """
        return self._successful_tasks

    @successful_tasks.setter
    def successful_tasks(self, successful_tasks):
        """
        Sets the successful_tasks of this TranscriptionJobSummary.
        Total successful tasks in a job.


        :param successful_tasks: The successful_tasks of this TranscriptionJobSummary.
        :type: int
        """
        self._successful_tasks = successful_tasks

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TranscriptionJobSummary.
        The current state of the Speech Job.


        :return: The lifecycle_state of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TranscriptionJobSummary.
        The current state of the Speech Job.


        :param lifecycle_state: The lifecycle_state of this TranscriptionJobSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TranscriptionJobSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TranscriptionJobSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TranscriptionJobSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TranscriptionJobSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TranscriptionJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this TranscriptionJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TranscriptionJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this TranscriptionJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TranscriptionJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this TranscriptionJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TranscriptionJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this TranscriptionJobSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TranscriptionJobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this TranscriptionJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TranscriptionJobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this TranscriptionJobSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
