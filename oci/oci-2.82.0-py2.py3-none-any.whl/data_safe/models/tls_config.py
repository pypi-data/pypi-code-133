# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TlsConfig(object):
    """
    The details required to establish a TLS enabled connection.
    """

    #: A constant which can be used with the status property of a TlsConfig.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a TlsConfig.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the certificate_store_type property of a TlsConfig.
    #: This constant has a value of "JKS"
    CERTIFICATE_STORE_TYPE_JKS = "JKS"

    def __init__(self, **kwargs):
        """
        Initializes a new TlsConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this TlsConfig.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param certificate_store_type:
            The value to assign to the certificate_store_type property of this TlsConfig.
            Allowed values for this property are: "JKS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type certificate_store_type: str

        :param store_password:
            The value to assign to the store_password property of this TlsConfig.
        :type store_password: str

        :param trust_store_content:
            The value to assign to the trust_store_content property of this TlsConfig.
        :type trust_store_content: str

        :param key_store_content:
            The value to assign to the key_store_content property of this TlsConfig.
        :type key_store_content: str

        """
        self.swagger_types = {
            'status': 'str',
            'certificate_store_type': 'str',
            'store_password': 'str',
            'trust_store_content': 'str',
            'key_store_content': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'certificate_store_type': 'certificateStoreType',
            'store_password': 'storePassword',
            'trust_store_content': 'trustStoreContent',
            'key_store_content': 'keyStoreContent'
        }

        self._status = None
        self._certificate_store_type = None
        self._store_password = None
        self._trust_store_content = None
        self._key_store_content = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TlsConfig.
        Status to represent whether the database connection is TLS enabled or not.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TlsConfig.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TlsConfig.
        Status to represent whether the database connection is TLS enabled or not.


        :param status: The status of this TlsConfig.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def certificate_store_type(self):
        """
        Gets the certificate_store_type of this TlsConfig.
        The format of the certificate store.

        Allowed values for this property are: "JKS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The certificate_store_type of this TlsConfig.
        :rtype: str
        """
        return self._certificate_store_type

    @certificate_store_type.setter
    def certificate_store_type(self, certificate_store_type):
        """
        Sets the certificate_store_type of this TlsConfig.
        The format of the certificate store.


        :param certificate_store_type: The certificate_store_type of this TlsConfig.
        :type: str
        """
        allowed_values = ["JKS"]
        if not value_allowed_none_or_none_sentinel(certificate_store_type, allowed_values):
            certificate_store_type = 'UNKNOWN_ENUM_VALUE'
        self._certificate_store_type = certificate_store_type

    @property
    def store_password(self):
        """
        Gets the store_password of this TlsConfig.
        The password to read the trust store and key store files, if they are password protected.


        :return: The store_password of this TlsConfig.
        :rtype: str
        """
        return self._store_password

    @store_password.setter
    def store_password(self, store_password):
        """
        Sets the store_password of this TlsConfig.
        The password to read the trust store and key store files, if they are password protected.


        :param store_password: The store_password of this TlsConfig.
        :type: str
        """
        self._store_password = store_password

    @property
    def trust_store_content(self):
        """
        Gets the trust_store_content of this TlsConfig.
        Base64 encoded string of trust store file content.


        :return: The trust_store_content of this TlsConfig.
        :rtype: str
        """
        return self._trust_store_content

    @trust_store_content.setter
    def trust_store_content(self, trust_store_content):
        """
        Sets the trust_store_content of this TlsConfig.
        Base64 encoded string of trust store file content.


        :param trust_store_content: The trust_store_content of this TlsConfig.
        :type: str
        """
        self._trust_store_content = trust_store_content

    @property
    def key_store_content(self):
        """
        Gets the key_store_content of this TlsConfig.
        Base64 encoded string of key store file content.


        :return: The key_store_content of this TlsConfig.
        :rtype: str
        """
        return self._key_store_content

    @key_store_content.setter
    def key_store_content(self, key_store_content):
        """
        Sets the key_store_content of this TlsConfig.
        Base64 encoded string of key store file content.


        :param key_store_content: The key_store_content of this TlsConfig.
        :type: str
        """
        self._key_store_content = key_store_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
