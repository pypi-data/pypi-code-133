# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .api_specification_route_backend import ApiSpecificationRouteBackend
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HTTPBackend(ApiSpecificationRouteBackend):
    """
    Send the request to an HTTP backend.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HTTPBackend object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.HTTPBackend.type` attribute
        of this class is ``HTTP_BACKEND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this HTTPBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND"
        :type type: str

        :param url:
            The value to assign to the url property of this HTTPBackend.
        :type url: str

        :param connect_timeout_in_seconds:
            The value to assign to the connect_timeout_in_seconds property of this HTTPBackend.
        :type connect_timeout_in_seconds: float

        :param read_timeout_in_seconds:
            The value to assign to the read_timeout_in_seconds property of this HTTPBackend.
        :type read_timeout_in_seconds: float

        :param send_timeout_in_seconds:
            The value to assign to the send_timeout_in_seconds property of this HTTPBackend.
        :type send_timeout_in_seconds: float

        :param is_ssl_verify_disabled:
            The value to assign to the is_ssl_verify_disabled property of this HTTPBackend.
        :type is_ssl_verify_disabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'url': 'str',
            'connect_timeout_in_seconds': 'float',
            'read_timeout_in_seconds': 'float',
            'send_timeout_in_seconds': 'float',
            'is_ssl_verify_disabled': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'url': 'url',
            'connect_timeout_in_seconds': 'connectTimeoutInSeconds',
            'read_timeout_in_seconds': 'readTimeoutInSeconds',
            'send_timeout_in_seconds': 'sendTimeoutInSeconds',
            'is_ssl_verify_disabled': 'isSslVerifyDisabled'
        }

        self._type = None
        self._url = None
        self._connect_timeout_in_seconds = None
        self._read_timeout_in_seconds = None
        self._send_timeout_in_seconds = None
        self._is_ssl_verify_disabled = None
        self._type = 'HTTP_BACKEND'

    @property
    def url(self):
        """
        **[Required]** Gets the url of this HTTPBackend.

        :return: The url of this HTTPBackend.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this HTTPBackend.

        :param url: The url of this HTTPBackend.
        :type: str
        """
        self._url = url

    @property
    def connect_timeout_in_seconds(self):
        """
        Gets the connect_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for establishing a connection with a proxied server.


        :return: The connect_timeout_in_seconds of this HTTPBackend.
        :rtype: float
        """
        return self._connect_timeout_in_seconds

    @connect_timeout_in_seconds.setter
    def connect_timeout_in_seconds(self, connect_timeout_in_seconds):
        """
        Sets the connect_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for establishing a connection with a proxied server.


        :param connect_timeout_in_seconds: The connect_timeout_in_seconds of this HTTPBackend.
        :type: float
        """
        self._connect_timeout_in_seconds = connect_timeout_in_seconds

    @property
    def read_timeout_in_seconds(self):
        """
        Gets the read_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for reading a response from the proxied server.


        :return: The read_timeout_in_seconds of this HTTPBackend.
        :rtype: float
        """
        return self._read_timeout_in_seconds

    @read_timeout_in_seconds.setter
    def read_timeout_in_seconds(self, read_timeout_in_seconds):
        """
        Sets the read_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for reading a response from the proxied server.


        :param read_timeout_in_seconds: The read_timeout_in_seconds of this HTTPBackend.
        :type: float
        """
        self._read_timeout_in_seconds = read_timeout_in_seconds

    @property
    def send_timeout_in_seconds(self):
        """
        Gets the send_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for transmitting a request to the proxied server.


        :return: The send_timeout_in_seconds of this HTTPBackend.
        :rtype: float
        """
        return self._send_timeout_in_seconds

    @send_timeout_in_seconds.setter
    def send_timeout_in_seconds(self, send_timeout_in_seconds):
        """
        Sets the send_timeout_in_seconds of this HTTPBackend.
        Defines a timeout for transmitting a request to the proxied server.


        :param send_timeout_in_seconds: The send_timeout_in_seconds of this HTTPBackend.
        :type: float
        """
        self._send_timeout_in_seconds = send_timeout_in_seconds

    @property
    def is_ssl_verify_disabled(self):
        """
        Gets the is_ssl_verify_disabled of this HTTPBackend.
        Defines whether or not to uphold SSL verification.


        :return: The is_ssl_verify_disabled of this HTTPBackend.
        :rtype: bool
        """
        return self._is_ssl_verify_disabled

    @is_ssl_verify_disabled.setter
    def is_ssl_verify_disabled(self, is_ssl_verify_disabled):
        """
        Sets the is_ssl_verify_disabled of this HTTPBackend.
        Defines whether or not to uphold SSL verification.


        :param is_ssl_verify_disabled: The is_ssl_verify_disabled of this HTTPBackend.
        :type: bool
        """
        self._is_ssl_verify_disabled = is_ssl_verify_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
