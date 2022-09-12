# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParameterValue(object):
    """
    User defined value for a parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParameterValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param simple_value:
            The value to assign to the simple_value property of this ParameterValue.
        :type simple_value: object

        :param root_object_value:
            The value to assign to the root_object_value property of this ParameterValue.
        :type root_object_value: object

        """
        self.swagger_types = {
            'simple_value': 'object',
            'root_object_value': 'object'
        }

        self.attribute_map = {
            'simple_value': 'simpleValue',
            'root_object_value': 'rootObjectValue'
        }

        self._simple_value = None
        self._root_object_value = None

    @property
    def simple_value(self):
        """
        Gets the simple_value of this ParameterValue.
        A simple value for the parameter.


        :return: The simple_value of this ParameterValue.
        :rtype: object
        """
        return self._simple_value

    @simple_value.setter
    def simple_value(self, simple_value):
        """
        Sets the simple_value of this ParameterValue.
        A simple value for the parameter.


        :param simple_value: The simple_value of this ParameterValue.
        :type: object
        """
        self._simple_value = simple_value

    @property
    def root_object_value(self):
        """
        Gets the root_object_value of this ParameterValue.
        This can be any object such as a file entity, a schema, or a table.


        :return: The root_object_value of this ParameterValue.
        :rtype: object
        """
        return self._root_object_value

    @root_object_value.setter
    def root_object_value(self, root_object_value):
        """
        Sets the root_object_value of this ParameterValue.
        This can be any object such as a file entity, a schema, or a table.


        :param root_object_value: The root_object_value of this ParameterValue.
        :type: object
        """
        self._root_object_value = root_object_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
