# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GzipCompressionPolicy(object):
    """
    An object that specifies the gzip compression policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GzipCompressionPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this GzipCompressionPolicy.
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
        Gets the is_enabled of this GzipCompressionPolicy.
        When true, support for gzip compression is enabled. HTTP responses will be compressed with gzip only if the
        client indicates support for gzip via the \"Accept-Encoding: gzip\" request header.

        When false, support for gzip compression is disabled and HTTP responses will not be compressed with gzip
        even if the client indicates support for gzip.


        :return: The is_enabled of this GzipCompressionPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this GzipCompressionPolicy.
        When true, support for gzip compression is enabled. HTTP responses will be compressed with gzip only if the
        client indicates support for gzip via the \"Accept-Encoding: gzip\" request header.

        When false, support for gzip compression is disabled and HTTP responses will not be compressed with gzip
        even if the client indicates support for gzip.


        :param is_enabled: The is_enabled of this GzipCompressionPolicy.
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
