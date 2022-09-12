# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .stream_packaging_config_encryption import StreamPackagingConfigEncryption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StreamPackagingConfigEncryptionNone(StreamPackagingConfigEncryption):
    """
    Disables encryption.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StreamPackagingConfigEncryptionNone object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.StreamPackagingConfigEncryptionNone.algorithm` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this StreamPackagingConfigEncryptionNone.
            Allowed values for this property are: "NONE", "AES128"
        :type algorithm: str

        """
        self.swagger_types = {
            'algorithm': 'str'
        }

        self.attribute_map = {
            'algorithm': 'algorithm'
        }

        self._algorithm = None
        self._algorithm = 'NONE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
