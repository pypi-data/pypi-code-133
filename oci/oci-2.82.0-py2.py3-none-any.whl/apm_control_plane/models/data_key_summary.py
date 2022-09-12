# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataKeySummary(object):
    """
    Summary of Data Key.
    """

    #: A constant which can be used with the type property of a DataKeySummary.
    #: This constant has a value of "PRIVATE"
    TYPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the type property of a DataKeySummary.
    #: This constant has a value of "PUBLIC"
    TYPE_PUBLIC = "PUBLIC"

    def __init__(self, **kwargs):
        """
        Initializes a new DataKeySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this DataKeySummary.
        :type value: str

        :param name:
            The value to assign to the name property of this DataKeySummary.
        :type name: str

        :param type:
            The value to assign to the type property of this DataKeySummary.
            Allowed values for this property are: "PRIVATE", "PUBLIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'value': 'str',
            'name': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'name': 'name',
            'type': 'type'
        }

        self._value = None
        self._name = None
        self._type = None

    @property
    def value(self):
        """
        Gets the value of this DataKeySummary.
        Value of the Data Key.


        :return: The value of this DataKeySummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DataKeySummary.
        Value of the Data Key.


        :param value: The value of this DataKeySummary.
        :type: str
        """
        self._value = value

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataKeySummary.
        Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.


        :return: The name of this DataKeySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataKeySummary.
        Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.


        :param name: The name of this DataKeySummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DataKeySummary.
        Type of the Data Key.

        Allowed values for this property are: "PRIVATE", "PUBLIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DataKeySummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataKeySummary.
        Type of the Data Key.


        :param type: The type of this DataKeySummary.
        :type: str
        """
        allowed_values = ["PRIVATE", "PUBLIC"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
