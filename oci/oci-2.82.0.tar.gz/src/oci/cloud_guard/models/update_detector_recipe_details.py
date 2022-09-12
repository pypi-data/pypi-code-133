# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDetectorRecipeDetails(object):
    """
    Update of detector recipe
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDetectorRecipeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDetectorRecipeDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDetectorRecipeDetails.
        :type description: str

        :param detector_rules:
            The value to assign to the detector_rules property of this UpdateDetectorRecipeDetails.
        :type detector_rules: list[oci.cloud_guard.models.UpdateDetectorRecipeDetectorRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDetectorRecipeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDetectorRecipeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'detector_rules': 'list[UpdateDetectorRecipeDetectorRule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'detector_rules': 'detectorRules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._detector_rules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDetectorRecipeDetails.
        Display name of detector recipe.

        Avoid entering confidential information.


        :return: The display_name of this UpdateDetectorRecipeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDetectorRecipeDetails.
        Display name of detector recipe.

        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDetectorRecipeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDetectorRecipeDetails.
        Detector recipe description.

        Avoid entering confidential information.


        :return: The description of this UpdateDetectorRecipeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDetectorRecipeDetails.
        Detector recipe description.

        Avoid entering confidential information.


        :param description: The description of this UpdateDetectorRecipeDetails.
        :type: str
        """
        self._description = description

    @property
    def detector_rules(self):
        """
        Gets the detector_rules of this UpdateDetectorRecipeDetails.
        Detector Rules to update


        :return: The detector_rules of this UpdateDetectorRecipeDetails.
        :rtype: list[oci.cloud_guard.models.UpdateDetectorRecipeDetectorRule]
        """
        return self._detector_rules

    @detector_rules.setter
    def detector_rules(self, detector_rules):
        """
        Sets the detector_rules of this UpdateDetectorRecipeDetails.
        Detector Rules to update


        :param detector_rules: The detector_rules of this UpdateDetectorRecipeDetails.
        :type: list[oci.cloud_guard.models.UpdateDetectorRecipeDetectorRule]
        """
        self._detector_rules = detector_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDetectorRecipeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this UpdateDetectorRecipeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDetectorRecipeDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this UpdateDetectorRecipeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDetectorRecipeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDetectorRecipeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDetectorRecipeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDetectorRecipeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
