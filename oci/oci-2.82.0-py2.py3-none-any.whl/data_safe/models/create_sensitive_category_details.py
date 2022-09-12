# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_sensitive_type_details import CreateSensitiveTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSensitiveCategoryDetails(CreateSensitiveTypeDetails):
    """
    Details to create a new sensitive category.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSensitiveCategoryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.CreateSensitiveCategoryDetails.entity_type` attribute
        of this class is ``SENSITIVE_CATEGORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this CreateSensitiveCategoryDetails.
            Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY"
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateSensitiveCategoryDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSensitiveCategoryDetails.
        :type compartment_id: str

        :param short_name:
            The value to assign to the short_name property of this CreateSensitiveCategoryDetails.
        :type short_name: str

        :param description:
            The value to assign to the description property of this CreateSensitiveCategoryDetails.
        :type description: str

        :param parent_category_id:
            The value to assign to the parent_category_id property of this CreateSensitiveCategoryDetails.
        :type parent_category_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSensitiveCategoryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSensitiveCategoryDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'short_name': 'str',
            'description': 'str',
            'parent_category_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'short_name': 'shortName',
            'description': 'description',
            'parent_category_id': 'parentCategoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._entity_type = None
        self._display_name = None
        self._compartment_id = None
        self._short_name = None
        self._description = None
        self._parent_category_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._entity_type = 'SENSITIVE_CATEGORY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
