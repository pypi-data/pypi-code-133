# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatisticsTimeSeries(object):
    """
    SQL performance statistics per database
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatisticsTimeSeries object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SqlStatisticsTimeSeries.
        :type name: str

        :param values:
            The value to assign to the values property of this SqlStatisticsTimeSeries.
        :type values: list[float]

        """
        self.swagger_types = {
            'name': 'str',
            'values': 'list[float]'
        }

        self.attribute_map = {
            'name': 'name',
            'values': 'values'
        }

        self._name = None
        self._values = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlStatisticsTimeSeries.
        SQL performance statistic name


        :return: The name of this SqlStatisticsTimeSeries.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlStatisticsTimeSeries.
        SQL performance statistic name


        :param name: The name of this SqlStatisticsTimeSeries.
        :type: str
        """
        self._name = name

    @property
    def values(self):
        """
        **[Required]** Gets the values of this SqlStatisticsTimeSeries.
        SQL performance statistic value


        :return: The values of this SqlStatisticsTimeSeries.
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this SqlStatisticsTimeSeries.
        SQL performance statistic value


        :param values: The values of this SqlStatisticsTimeSeries.
        :type: list[float]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
