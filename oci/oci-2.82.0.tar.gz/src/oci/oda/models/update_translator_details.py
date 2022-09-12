# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTranslatorDetails(object):
    """
    Properties to update a Translator.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTranslatorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param base_url:
            The value to assign to the base_url property of this UpdateTranslatorDetails.
        :type base_url: str

        :param auth_token:
            The value to assign to the auth_token property of this UpdateTranslatorDetails.
        :type auth_token: str

        :param properties:
            The value to assign to the properties property of this UpdateTranslatorDetails.
        :type properties: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTranslatorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTranslatorDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'base_url': 'str',
            'auth_token': 'str',
            'properties': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'base_url': 'baseUrl',
            'auth_token': 'authToken',
            'properties': 'properties',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._base_url = None
        self._auth_token = None
        self._properties = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def base_url(self):
        """
        Gets the base_url of this UpdateTranslatorDetails.
        The base URL for invoking the Translation Service.


        :return: The base_url of this UpdateTranslatorDetails.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this UpdateTranslatorDetails.
        The base URL for invoking the Translation Service.


        :param base_url: The base_url of this UpdateTranslatorDetails.
        :type: str
        """
        self._base_url = base_url

    @property
    def auth_token(self):
        """
        Gets the auth_token of this UpdateTranslatorDetails.
        The authentication token to use when invoking the Translation Service


        :return: The auth_token of this UpdateTranslatorDetails.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this UpdateTranslatorDetails.
        The authentication token to use when invoking the Translation Service


        :param auth_token: The auth_token of this UpdateTranslatorDetails.
        :type: str
        """
        self._auth_token = auth_token

    @property
    def properties(self):
        """
        Gets the properties of this UpdateTranslatorDetails.
        Properties used when invoking the translation service.
        Each property is a simple key-value pair.


        :return: The properties of this UpdateTranslatorDetails.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateTranslatorDetails.
        Properties used when invoking the translation service.
        Each property is a simple key-value pair.


        :param properties: The properties of this UpdateTranslatorDetails.
        :type: dict(str, str)
        """
        self._properties = properties

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTranslatorDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateTranslatorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTranslatorDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateTranslatorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTranslatorDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateTranslatorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTranslatorDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateTranslatorDetails.
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
