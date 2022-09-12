# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateDatabaseToolsConnectionResult(object):
    """
    Connection validation result.
    """

    #: A constant which can be used with the type property of a ValidateDatabaseToolsConnectionResult.
    #: This constant has a value of "ORACLE_DATABASE"
    TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    #: A constant which can be used with the type property of a ValidateDatabaseToolsConnectionResult.
    #: This constant has a value of "MYSQL"
    TYPE_MYSQL = "MYSQL"

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateDatabaseToolsConnectionResult object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_tools.models.ValidateDatabaseToolsConnectionOracleDatabaseResult`
        * :class:`~oci.database_tools.models.ValidateDatabaseToolsConnectionMySqlResult`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ValidateDatabaseToolsConnectionResult.
            Allowed values for this property are: "ORACLE_DATABASE", "MYSQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param code:
            The value to assign to the code property of this ValidateDatabaseToolsConnectionResult.
        :type code: str

        :param message:
            The value to assign to the message property of this ValidateDatabaseToolsConnectionResult.
        :type message: str

        :param cause:
            The value to assign to the cause property of this ValidateDatabaseToolsConnectionResult.
        :type cause: str

        :param action:
            The value to assign to the action property of this ValidateDatabaseToolsConnectionResult.
        :type action: str

        """
        self.swagger_types = {
            'type': 'str',
            'code': 'str',
            'message': 'str',
            'cause': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'code': 'code',
            'message': 'message',
            'cause': 'cause',
            'action': 'action'
        }

        self._type = None
        self._code = None
        self._message = None
        self._cause = None
        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ORACLE_DATABASE':
            return 'ValidateDatabaseToolsConnectionOracleDatabaseResult'

        if type == 'MYSQL':
            return 'ValidateDatabaseToolsConnectionMySqlResult'
        else:
            return 'ValidateDatabaseToolsConnectionResult'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ValidateDatabaseToolsConnectionResult.
        The Database Tools connection type.

        Allowed values for this property are: "ORACLE_DATABASE", "MYSQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ValidateDatabaseToolsConnectionResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ValidateDatabaseToolsConnectionResult.
        The Database Tools connection type.


        :param type: The type of this ValidateDatabaseToolsConnectionResult.
        :type: str
        """
        allowed_values = ["ORACLE_DATABASE", "MYSQL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def code(self):
        """
        **[Required]** Gets the code of this ValidateDatabaseToolsConnectionResult.
        A short code that defines the result of the validation, meant for programmatic parsing. The value OK indicates that the validation was successful.


        :return: The code of this ValidateDatabaseToolsConnectionResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ValidateDatabaseToolsConnectionResult.
        A short code that defines the result of the validation, meant for programmatic parsing. The value OK indicates that the validation was successful.


        :param code: The code of this ValidateDatabaseToolsConnectionResult.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that describes the result of the validation.


        :return: The message of this ValidateDatabaseToolsConnectionResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that describes the result of the validation.


        :param message: The message of this ValidateDatabaseToolsConnectionResult.
        :type: str
        """
        self._message = message

    @property
    def cause(self):
        """
        Gets the cause of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that describes possible causes for the validation error.


        :return: The cause of this ValidateDatabaseToolsConnectionResult.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """
        Sets the cause of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that describes possible causes for the validation error.


        :param cause: The cause of this ValidateDatabaseToolsConnectionResult.
        :type: str
        """
        self._cause = cause

    @property
    def action(self):
        """
        Gets the action of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that suggests a remedial action to resolve the validation error.


        :return: The action of this ValidateDatabaseToolsConnectionResult.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ValidateDatabaseToolsConnectionResult.
        A human-readable message that suggests a remedial action to resolve the validation error.


        :param action: The action of this ValidateDatabaseToolsConnectionResult.
        :type: str
        """
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
