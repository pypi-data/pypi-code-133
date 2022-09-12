# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .private_application_package import PrivateApplicationPackage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateApplicationStackPackage(PrivateApplicationPackage):
    """
    A stack package for private applications.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateApplicationStackPackage object with values from keyword arguments. The default value of the :py:attr:`~oci.service_catalog.models.PrivateApplicationStackPackage.package_type` attribute
        of this class is ``STACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PrivateApplicationStackPackage.
        :type id: str

        :param private_application_id:
            The value to assign to the private_application_id property of this PrivateApplicationStackPackage.
        :type private_application_id: str

        :param display_name:
            The value to assign to the display_name property of this PrivateApplicationStackPackage.
        :type display_name: str

        :param version:
            The value to assign to the version property of this PrivateApplicationStackPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this PrivateApplicationStackPackage.
            Allowed values for this property are: "STACK"
        :type package_type: str

        :param time_created:
            The value to assign to the time_created property of this PrivateApplicationStackPackage.
        :type time_created: datetime

        :param content_url:
            The value to assign to the content_url property of this PrivateApplicationStackPackage.
        :type content_url: str

        :param mime_type:
            The value to assign to the mime_type property of this PrivateApplicationStackPackage.
        :type mime_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'private_application_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'package_type': 'str',
            'time_created': 'datetime',
            'content_url': 'str',
            'mime_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'private_application_id': 'privateApplicationId',
            'display_name': 'displayName',
            'version': 'version',
            'package_type': 'packageType',
            'time_created': 'timeCreated',
            'content_url': 'contentUrl',
            'mime_type': 'mimeType'
        }

        self._id = None
        self._private_application_id = None
        self._display_name = None
        self._version = None
        self._package_type = None
        self._time_created = None
        self._content_url = None
        self._mime_type = None
        self._package_type = 'STACK'

    @property
    def content_url(self):
        """
        Gets the content_url of this PrivateApplicationStackPackage.
        The content URL of the terraform configuration.


        :return: The content_url of this PrivateApplicationStackPackage.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this PrivateApplicationStackPackage.
        The content URL of the terraform configuration.


        :param content_url: The content_url of this PrivateApplicationStackPackage.
        :type: str
        """
        self._content_url = content_url

    @property
    def mime_type(self):
        """
        Gets the mime_type of this PrivateApplicationStackPackage.
        The MIME type of the terraform configuration.


        :return: The mime_type of this PrivateApplicationStackPackage.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this PrivateApplicationStackPackage.
        The MIME type of the terraform configuration.


        :param mime_type: The mime_type of this PrivateApplicationStackPackage.
        :type: str
        """
        self._mime_type = mime_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
