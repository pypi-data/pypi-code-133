# coding: utf-8

"""
    UBIKA WAAP Gateway and Cloud API

    The UBIKA's WAAP management API provides a REST/JSON programming interface. It allows automation and scripting of WAAP administration tasks, such as management of reverse proxies and tunnels. The API documentation is shipped with the product itself. Once the product installed, you can access the documentation on the following URL https://ManagementWAAP:3001/api/v1/doc/  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ubika_waap_api_client.configuration import Configuration


class UpdateReverseProxyProfile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'start_server': 'int',
        'server_limit': 'int',
        'max_clients': 'int',
        'max_spare_threads': 'int',
        'min_spare_threads': 'int',
        'thread_per_child': 'int',
        'max_requests_per_child': 'int',
        'limit_request_field_size': 'int',
        'timeout': 'int',
        'proxy_timeout': 'int',
        'keep_alive': 'bool',
        'keep_alive_timeout': 'int',
        'max_keep_alive_requests': 'int',
        'ssl_session_cache_size': 'int',
        'ssl_session_cache_timeout': 'int'
    }

    attribute_map = {
        'name': 'name',
        'start_server': 'startServer',
        'server_limit': 'serverLimit',
        'max_clients': 'maxClients',
        'max_spare_threads': 'maxSpareThreads',
        'min_spare_threads': 'minSpareThreads',
        'thread_per_child': 'threadPerChild',
        'max_requests_per_child': 'maxRequestsPerChild',
        'limit_request_field_size': 'limitRequestFieldSize',
        'timeout': 'timeout',
        'proxy_timeout': 'proxyTimeout',
        'keep_alive': 'keepAlive',
        'keep_alive_timeout': 'keepAliveTimeout',
        'max_keep_alive_requests': 'maxKeepAliveRequests',
        'ssl_session_cache_size': 'sslSessionCacheSize',
        'ssl_session_cache_timeout': 'sslSessionCacheTimeout'
    }

    def __init__(self, name=None, start_server=None, server_limit=None, max_clients=None, max_spare_threads=None, min_spare_threads=None, thread_per_child=None, max_requests_per_child=None, limit_request_field_size=None, timeout=None, proxy_timeout=None, keep_alive=None, keep_alive_timeout=None, max_keep_alive_requests=None, ssl_session_cache_size=None, ssl_session_cache_timeout=None, local_vars_configuration=None):  # noqa: E501
        """UpdateReverseProxyProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._start_server = None
        self._server_limit = None
        self._max_clients = None
        self._max_spare_threads = None
        self._min_spare_threads = None
        self._thread_per_child = None
        self._max_requests_per_child = None
        self._limit_request_field_size = None
        self._timeout = None
        self._proxy_timeout = None
        self._keep_alive = None
        self._keep_alive_timeout = None
        self._max_keep_alive_requests = None
        self._ssl_session_cache_size = None
        self._ssl_session_cache_timeout = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if start_server is not None:
            self.start_server = start_server
        if server_limit is not None:
            self.server_limit = server_limit
        if max_clients is not None:
            self.max_clients = max_clients
        if max_spare_threads is not None:
            self.max_spare_threads = max_spare_threads
        if min_spare_threads is not None:
            self.min_spare_threads = min_spare_threads
        if thread_per_child is not None:
            self.thread_per_child = thread_per_child
        if max_requests_per_child is not None:
            self.max_requests_per_child = max_requests_per_child
        if limit_request_field_size is not None:
            self.limit_request_field_size = limit_request_field_size
        if timeout is not None:
            self.timeout = timeout
        if proxy_timeout is not None:
            self.proxy_timeout = proxy_timeout
        if keep_alive is not None:
            self.keep_alive = keep_alive
        if keep_alive_timeout is not None:
            self.keep_alive_timeout = keep_alive_timeout
        if max_keep_alive_requests is not None:
            self.max_keep_alive_requests = max_keep_alive_requests
        if ssl_session_cache_size is not None:
            self.ssl_session_cache_size = ssl_session_cache_size
        if ssl_session_cache_timeout is not None:
            self.ssl_session_cache_timeout = ssl_session_cache_timeout

    @property
    def name(self):
        """Gets the name of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The name of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateReverseProxyProfile.


        :param name: The name of this UpdateReverseProxyProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_server(self):
        """Gets the start_server of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The start_server of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._start_server

    @start_server.setter
    def start_server(self, start_server):
        """Sets the start_server of this UpdateReverseProxyProfile.


        :param start_server: The start_server of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._start_server = start_server

    @property
    def server_limit(self):
        """Gets the server_limit of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The server_limit of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._server_limit

    @server_limit.setter
    def server_limit(self, server_limit):
        """Sets the server_limit of this UpdateReverseProxyProfile.


        :param server_limit: The server_limit of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._server_limit = server_limit

    @property
    def max_clients(self):
        """Gets the max_clients of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The max_clients of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_clients

    @max_clients.setter
    def max_clients(self, max_clients):
        """Sets the max_clients of this UpdateReverseProxyProfile.


        :param max_clients: The max_clients of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._max_clients = max_clients

    @property
    def max_spare_threads(self):
        """Gets the max_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The max_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_spare_threads

    @max_spare_threads.setter
    def max_spare_threads(self, max_spare_threads):
        """Sets the max_spare_threads of this UpdateReverseProxyProfile.


        :param max_spare_threads: The max_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._max_spare_threads = max_spare_threads

    @property
    def min_spare_threads(self):
        """Gets the min_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The min_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._min_spare_threads

    @min_spare_threads.setter
    def min_spare_threads(self, min_spare_threads):
        """Sets the min_spare_threads of this UpdateReverseProxyProfile.


        :param min_spare_threads: The min_spare_threads of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._min_spare_threads = min_spare_threads

    @property
    def thread_per_child(self):
        """Gets the thread_per_child of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The thread_per_child of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._thread_per_child

    @thread_per_child.setter
    def thread_per_child(self, thread_per_child):
        """Sets the thread_per_child of this UpdateReverseProxyProfile.


        :param thread_per_child: The thread_per_child of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._thread_per_child = thread_per_child

    @property
    def max_requests_per_child(self):
        """Gets the max_requests_per_child of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The max_requests_per_child of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_requests_per_child

    @max_requests_per_child.setter
    def max_requests_per_child(self, max_requests_per_child):
        """Sets the max_requests_per_child of this UpdateReverseProxyProfile.


        :param max_requests_per_child: The max_requests_per_child of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._max_requests_per_child = max_requests_per_child

    @property
    def limit_request_field_size(self):
        """Gets the limit_request_field_size of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The limit_request_field_size of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._limit_request_field_size

    @limit_request_field_size.setter
    def limit_request_field_size(self, limit_request_field_size):
        """Sets the limit_request_field_size of this UpdateReverseProxyProfile.


        :param limit_request_field_size: The limit_request_field_size of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._limit_request_field_size = limit_request_field_size

    @property
    def timeout(self):
        """Gets the timeout of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateReverseProxyProfile.


        :param timeout: The timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def proxy_timeout(self):
        """Gets the proxy_timeout of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The proxy_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._proxy_timeout

    @proxy_timeout.setter
    def proxy_timeout(self, proxy_timeout):
        """Sets the proxy_timeout of this UpdateReverseProxyProfile.


        :param proxy_timeout: The proxy_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._proxy_timeout = proxy_timeout

    @property
    def keep_alive(self):
        """Gets the keep_alive of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The keep_alive of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: bool
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """Sets the keep_alive of this UpdateReverseProxyProfile.


        :param keep_alive: The keep_alive of this UpdateReverseProxyProfile.  # noqa: E501
        :type: bool
        """

        self._keep_alive = keep_alive

    @property
    def keep_alive_timeout(self):
        """Gets the keep_alive_timeout of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The keep_alive_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._keep_alive_timeout

    @keep_alive_timeout.setter
    def keep_alive_timeout(self, keep_alive_timeout):
        """Sets the keep_alive_timeout of this UpdateReverseProxyProfile.


        :param keep_alive_timeout: The keep_alive_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._keep_alive_timeout = keep_alive_timeout

    @property
    def max_keep_alive_requests(self):
        """Gets the max_keep_alive_requests of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The max_keep_alive_requests of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_keep_alive_requests

    @max_keep_alive_requests.setter
    def max_keep_alive_requests(self, max_keep_alive_requests):
        """Sets the max_keep_alive_requests of this UpdateReverseProxyProfile.


        :param max_keep_alive_requests: The max_keep_alive_requests of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._max_keep_alive_requests = max_keep_alive_requests

    @property
    def ssl_session_cache_size(self):
        """Gets the ssl_session_cache_size of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The ssl_session_cache_size of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._ssl_session_cache_size

    @ssl_session_cache_size.setter
    def ssl_session_cache_size(self, ssl_session_cache_size):
        """Sets the ssl_session_cache_size of this UpdateReverseProxyProfile.


        :param ssl_session_cache_size: The ssl_session_cache_size of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._ssl_session_cache_size = ssl_session_cache_size

    @property
    def ssl_session_cache_timeout(self):
        """Gets the ssl_session_cache_timeout of this UpdateReverseProxyProfile.  # noqa: E501


        :return: The ssl_session_cache_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :rtype: int
        """
        return self._ssl_session_cache_timeout

    @ssl_session_cache_timeout.setter
    def ssl_session_cache_timeout(self, ssl_session_cache_timeout):
        """Sets the ssl_session_cache_timeout of this UpdateReverseProxyProfile.


        :param ssl_session_cache_timeout: The ssl_session_cache_timeout of this UpdateReverseProxyProfile.  # noqa: E501
        :type: int
        """

        self._ssl_session_cache_timeout = ssl_session_cache_timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateReverseProxyProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateReverseProxyProfile):
            return True

        return self.to_dict() != other.to_dict()
