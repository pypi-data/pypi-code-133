# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContextVariable(object):
    """
    ContextVariable model.
    """

    #: A constant which can be used with the type property of a ContextVariable.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a ContextVariable.
    #: This constant has a value of "NUMBER"
    TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the type property of a ContextVariable.
    #: This constant has a value of "ENTITY"
    TYPE_ENTITY = "ENTITY"

    #: A constant which can be used with the type property of a ContextVariable.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the type property of a ContextVariable.
    #: This constant has a value of "LIST"
    TYPE_LIST = "LIST"

    def __init__(self, **kwargs):
        """
        Initializes a new ContextVariable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ContextVariable.
        :type name: str

        :param value:
            The value to assign to the value property of this ContextVariable.
        :type value: str

        :param type:
            The value to assign to the type property of this ContextVariable.
            Allowed values for this property are: "STRING", "NUMBER", "ENTITY", "BOOLEAN", "LIST"
        :type type: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'type': 'type'
        }

        self._name = None
        self._value = None
        self._type = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ContextVariable.
        The name of the variable.


        :return: The name of this ContextVariable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContextVariable.
        The name of the variable.


        :param name: The name of this ContextVariable.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ContextVariable.
        The value of the variable.


        :return: The value of this ContextVariable.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ContextVariable.
        The value of the variable.


        :param value: The value of this ContextVariable.
        :type: str
        """
        self._value = value

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ContextVariable.
        The type of the variable.

        Allowed values for this property are: "STRING", "NUMBER", "ENTITY", "BOOLEAN", "LIST"


        :return: The type of this ContextVariable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ContextVariable.
        The type of the variable.


        :param type: The type of this ContextVariable.
        :type: str
        """
        allowed_values = ["STRING", "NUMBER", "ENTITY", "BOOLEAN", "LIST"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
