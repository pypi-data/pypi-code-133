# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    A summary of the status of a work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.fusion_apps.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        Possible operation types.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        Possible operation types.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        Possible operation status.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        Possible operation status.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The id of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The id of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The ocid of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The ocid of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.fusion_apps.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.fusion_apps.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequestSummary.
        Percentage of the request completed.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        Percentage of the request completed.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequestSummary.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        The date and time the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        The date and time the request was started, as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        The date and time the request was started, as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        The date and time the object was finished, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        The date and time the object was finished, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
