# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBitbucketCloudAppPasswordConnectionDetails(CreateConnectionDetails):
    """
    The details for creating a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`.
    This type corresponds to a connection in Bitbucket Cloud that is authenticated with username and app password.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBitbucketCloudAppPasswordConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateBitbucketCloudAppPasswordConnectionDetails.connection_type` attribute
        of this class is ``BITBUCKET_CLOUD_APP_PASSWORD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type project_id: str

        :param connection_type:
            The value to assign to the connection_type property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type connection_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param username:
            The value to assign to the username property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type username: str

        :param app_password:
            The value to assign to the app_password property of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type app_password: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'connection_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'username': 'str',
            'app_password': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'connection_type': 'connectionType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'username': 'username',
            'app_password': 'appPassword'
        }

        self._description = None
        self._display_name = None
        self._project_id = None
        self._connection_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._username = None
        self._app_password = None
        self._connection_type = 'BITBUCKET_CLOUD_APP_PASSWORD'

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateBitbucketCloudAppPasswordConnectionDetails.
        Public Bitbucket Cloud Username in plain text(not more than 30 characters)


        :return: The username of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateBitbucketCloudAppPasswordConnectionDetails.
        Public Bitbucket Cloud Username in plain text(not more than 30 characters)


        :param username: The username of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def app_password(self):
        """
        **[Required]** Gets the app_password of this CreateBitbucketCloudAppPasswordConnectionDetails.
        OCID of personal Bitbucket Cloud AppPassword saved in secret store


        :return: The app_password of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :rtype: str
        """
        return self._app_password

    @app_password.setter
    def app_password(self, app_password):
        """
        Sets the app_password of this CreateBitbucketCloudAppPasswordConnectionDetails.
        OCID of personal Bitbucket Cloud AppPassword saved in secret store


        :param app_password: The app_password of this CreateBitbucketCloudAppPasswordConnectionDetails.
        :type: str
        """
        self._app_password = app_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
