# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractWriteAttribute(object):
    """
    The abstract write attribute.
    """

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLEWRITEATTRIBUTE"
    MODEL_TYPE_ORACLEWRITEATTRIBUTE = "ORACLEWRITEATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLEATPWRITEATTRIBUTE"
    MODEL_TYPE_ORACLEATPWRITEATTRIBUTE = "ORACLEATPWRITEATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLEADWCWRITEATTRIBUTE"
    MODEL_TYPE_ORACLEADWCWRITEATTRIBUTE = "ORACLEADWCWRITEATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "OBJECTSTORAGEWRITEATTRIBUTE"
    MODEL_TYPE_OBJECTSTORAGEWRITEATTRIBUTE = "OBJECTSTORAGEWRITEATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_WRITE_ATTRIBUTE = "ORACLE_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_ATP_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_ATP_WRITE_ATTRIBUTE = "ORACLE_ATP_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "ORACLE_ADWC_WRITE_ATTRIBUTE"
    MODEL_TYPE_ORACLE_ADWC_WRITE_ATTRIBUTE = "ORACLE_ADWC_WRITE_ATTRIBUTE"

    #: A constant which can be used with the model_type property of a AbstractWriteAttribute.
    #: This constant has a value of "OBJECT_STORAGE_WRITE_ATTRIBUTE"
    MODEL_TYPE_OBJECT_STORAGE_WRITE_ATTRIBUTE = "OBJECT_STORAGE_WRITE_ATTRIBUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractWriteAttribute object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.OracleAdwcWriteAttribute`
        * :class:`~oci.data_integration.models.OracleAtpWriteAttributes`
        * :class:`~oci.data_integration.models.OracleWriteAttribute`
        * :class:`~oci.data_integration.models.OracleWriteAttributes`
        * :class:`~oci.data_integration.models.OracleAtpWriteAttribute`
        * :class:`~oci.data_integration.models.ObjectStorageWriteAttribute`
        * :class:`~oci.data_integration.models.OracleAdwcWriteAttributes`
        * :class:`~oci.data_integration.models.ObjectStorageWriteAttributes`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this AbstractWriteAttribute.
            Allowed values for this property are: "ORACLEWRITEATTRIBUTE", "ORACLEATPWRITEATTRIBUTE", "ORACLEADWCWRITEATTRIBUTE", "OBJECTSTORAGEWRITEATTRIBUTE", "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        """
        self.swagger_types = {
            'model_type': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType'
        }

        self._model_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'ORACLEADWCWRITEATTRIBUTE':
            return 'OracleAdwcWriteAttribute'

        if type == 'ORACLE_ATP_WRITE_ATTRIBUTE':
            return 'OracleAtpWriteAttributes'

        if type == 'ORACLEWRITEATTRIBUTE':
            return 'OracleWriteAttribute'

        if type == 'ORACLE_WRITE_ATTRIBUTE':
            return 'OracleWriteAttributes'

        if type == 'ORACLEATPWRITEATTRIBUTE':
            return 'OracleAtpWriteAttribute'

        if type == 'OBJECTSTORAGEWRITEATTRIBUTE':
            return 'ObjectStorageWriteAttribute'

        if type == 'ORACLE_ADWC_WRITE_ATTRIBUTE':
            return 'OracleAdwcWriteAttributes'

        if type == 'OBJECT_STORAGE_WRITE_ATTRIBUTE':
            return 'ObjectStorageWriteAttributes'
        else:
            return 'AbstractWriteAttribute'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this AbstractWriteAttribute.
        The type of the abstract write attribute.

        Allowed values for this property are: "ORACLEWRITEATTRIBUTE", "ORACLEATPWRITEATTRIBUTE", "ORACLEADWCWRITEATTRIBUTE", "OBJECTSTORAGEWRITEATTRIBUTE", "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this AbstractWriteAttribute.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AbstractWriteAttribute.
        The type of the abstract write attribute.


        :param model_type: The model_type of this AbstractWriteAttribute.
        :type: str
        """
        allowed_values = ["ORACLEWRITEATTRIBUTE", "ORACLEATPWRITEATTRIBUTE", "ORACLEADWCWRITEATTRIBUTE", "OBJECTSTORAGEWRITEATTRIBUTE", "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
