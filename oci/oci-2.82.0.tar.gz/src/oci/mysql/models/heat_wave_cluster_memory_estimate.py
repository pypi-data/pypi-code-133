# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveClusterMemoryEstimate(object):
    """
    HeatWave cluster memory estimate
    that can be used to determine a suitable HeatWave cluster size. For each MySQL user table the estimated memory
    footprint when the table is loaded to the HeatWave cluster memory is returned.
    """

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a HeatWaveClusterMemoryEstimate.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveClusterMemoryEstimate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this HeatWaveClusterMemoryEstimate.
        :type db_system_id: str

        :param status:
            The value to assign to the status property of this HeatWaveClusterMemoryEstimate.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this HeatWaveClusterMemoryEstimate.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HeatWaveClusterMemoryEstimate.
        :type time_updated: datetime

        :param table_schemas:
            The value to assign to the table_schemas property of this HeatWaveClusterMemoryEstimate.
        :type table_schemas: list[oci.mysql.models.HeatWaveClusterSchemaMemoryEstimate]

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'table_schemas': 'list[HeatWaveClusterSchemaMemoryEstimate]'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'table_schemas': 'tableSchemas'
        }

        self._db_system_id = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._table_schemas = None

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this HeatWaveClusterMemoryEstimate.
        The OCID of the DB System the HeatWave cluster memory estimate is associated with.


        :return: The db_system_id of this HeatWaveClusterMemoryEstimate.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this HeatWaveClusterMemoryEstimate.
        The OCID of the DB System the HeatWave cluster memory estimate is associated with.


        :param db_system_id: The db_system_id of this HeatWaveClusterMemoryEstimate.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this HeatWaveClusterMemoryEstimate.
        Current status of the Work Request generating the HeatWave cluster memory estimate.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this HeatWaveClusterMemoryEstimate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HeatWaveClusterMemoryEstimate.
        Current status of the Work Request generating the HeatWave cluster memory estimate.


        :param status: The status of this HeatWaveClusterMemoryEstimate.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this HeatWaveClusterMemoryEstimate.
        The date and time that the Work Request to generate the HeatWave cluster memory estimate was issued, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc333


        :return: The time_created of this HeatWaveClusterMemoryEstimate.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HeatWaveClusterMemoryEstimate.
        The date and time that the Work Request to generate the HeatWave cluster memory estimate was issued, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc333


        :param time_created: The time_created of this HeatWaveClusterMemoryEstimate.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this HeatWaveClusterMemoryEstimate.
        The date and time that the HeatWave cluster memory estimate was generated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc333


        :return: The time_updated of this HeatWaveClusterMemoryEstimate.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HeatWaveClusterMemoryEstimate.
        The date and time that the HeatWave cluster memory estimate was generated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc333


        :param time_updated: The time_updated of this HeatWaveClusterMemoryEstimate.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def table_schemas(self):
        """
        **[Required]** Gets the table_schemas of this HeatWaveClusterMemoryEstimate.
        Collection of schemas with estimated memory footprints for MySQL user tables of each schema
        when loaded to HeatWave cluster memory.


        :return: The table_schemas of this HeatWaveClusterMemoryEstimate.
        :rtype: list[oci.mysql.models.HeatWaveClusterSchemaMemoryEstimate]
        """
        return self._table_schemas

    @table_schemas.setter
    def table_schemas(self, table_schemas):
        """
        Sets the table_schemas of this HeatWaveClusterMemoryEstimate.
        Collection of schemas with estimated memory footprints for MySQL user tables of each schema
        when loaded to HeatWave cluster memory.


        :param table_schemas: The table_schemas of this HeatWaveClusterMemoryEstimate.
        :type: list[oci.mysql.models.HeatWaveClusterSchemaMemoryEstimate]
        """
        self._table_schemas = table_schemas

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
