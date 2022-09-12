# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessLogPolicy(object):
    """
    Configures the logging policies for the access logs of an API Deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessLogPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this AccessLogPolicy.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled'
        }

        self._is_enabled = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AccessLogPolicy.
        Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.

        Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
        for an API Deployment. If there is an active log object for the API Deployment and its
        category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
        legacy OCI Object Storage log archival bucket.

        Please note that the functionality to push to the legacy OCI Object Storage log
        archival bucket has been deprecated and will be removed in the future.


        :return: The is_enabled of this AccessLogPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AccessLogPolicy.
        Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.

        Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
        for an API Deployment. If there is an active log object for the API Deployment and its
        category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
        legacy OCI Object Storage log archival bucket.

        Please note that the functionality to push to the legacy OCI Object Storage log
        archival bucket has been deprecated and will be removed in the future.


        :param is_enabled: The is_enabled of this AccessLogPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
