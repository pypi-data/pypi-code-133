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


class CreateTunnelPerformance(object):
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
        'timeout': 'int',
        'proxy_timeout': 'int',
        'keep_alive_timeout': 'int',
        'ramdisk_cache': 'CreateTunnelPerformanceRamdiskCache',
        'request_timeout_profile': 'ApplySSLKeyUid',
        'compression_profile': 'ApplySSLKeyUid',
        'workflow_preserve_deflate': 'bool'
    }

    attribute_map = {
        'timeout': 'timeout',
        'proxy_timeout': 'proxyTimeout',
        'keep_alive_timeout': 'keepAliveTimeout',
        'ramdisk_cache': 'ramdiskCache',
        'request_timeout_profile': 'requestTimeoutProfile',
        'compression_profile': 'compressionProfile',
        'workflow_preserve_deflate': 'workflowPreserveDeflate'
    }

    def __init__(self, timeout=None, proxy_timeout=None, keep_alive_timeout=None, ramdisk_cache=None, request_timeout_profile=None, compression_profile=None, workflow_preserve_deflate=None, local_vars_configuration=None):  # noqa: E501
        """CreateTunnelPerformance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timeout = None
        self._proxy_timeout = None
        self._keep_alive_timeout = None
        self._ramdisk_cache = None
        self._request_timeout_profile = None
        self._compression_profile = None
        self._workflow_preserve_deflate = None
        self.discriminator = None

        if timeout is not None:
            self.timeout = timeout
        if proxy_timeout is not None:
            self.proxy_timeout = proxy_timeout
        if keep_alive_timeout is not None:
            self.keep_alive_timeout = keep_alive_timeout
        if ramdisk_cache is not None:
            self.ramdisk_cache = ramdisk_cache
        if request_timeout_profile is not None:
            self.request_timeout_profile = request_timeout_profile
        if compression_profile is not None:
            self.compression_profile = compression_profile
        if workflow_preserve_deflate is not None:
            self.workflow_preserve_deflate = workflow_preserve_deflate

    @property
    def timeout(self):
        """Gets the timeout of this CreateTunnelPerformance.  # noqa: E501


        :return: The timeout of this CreateTunnelPerformance.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateTunnelPerformance.


        :param timeout: The timeout of this CreateTunnelPerformance.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def proxy_timeout(self):
        """Gets the proxy_timeout of this CreateTunnelPerformance.  # noqa: E501


        :return: The proxy_timeout of this CreateTunnelPerformance.  # noqa: E501
        :rtype: int
        """
        return self._proxy_timeout

    @proxy_timeout.setter
    def proxy_timeout(self, proxy_timeout):
        """Sets the proxy_timeout of this CreateTunnelPerformance.


        :param proxy_timeout: The proxy_timeout of this CreateTunnelPerformance.  # noqa: E501
        :type: int
        """

        self._proxy_timeout = proxy_timeout

    @property
    def keep_alive_timeout(self):
        """Gets the keep_alive_timeout of this CreateTunnelPerformance.  # noqa: E501


        :return: The keep_alive_timeout of this CreateTunnelPerformance.  # noqa: E501
        :rtype: int
        """
        return self._keep_alive_timeout

    @keep_alive_timeout.setter
    def keep_alive_timeout(self, keep_alive_timeout):
        """Sets the keep_alive_timeout of this CreateTunnelPerformance.


        :param keep_alive_timeout: The keep_alive_timeout of this CreateTunnelPerformance.  # noqa: E501
        :type: int
        """

        self._keep_alive_timeout = keep_alive_timeout

    @property
    def ramdisk_cache(self):
        """Gets the ramdisk_cache of this CreateTunnelPerformance.  # noqa: E501


        :return: The ramdisk_cache of this CreateTunnelPerformance.  # noqa: E501
        :rtype: CreateTunnelPerformanceRamdiskCache
        """
        return self._ramdisk_cache

    @ramdisk_cache.setter
    def ramdisk_cache(self, ramdisk_cache):
        """Sets the ramdisk_cache of this CreateTunnelPerformance.


        :param ramdisk_cache: The ramdisk_cache of this CreateTunnelPerformance.  # noqa: E501
        :type: CreateTunnelPerformanceRamdiskCache
        """

        self._ramdisk_cache = ramdisk_cache

    @property
    def request_timeout_profile(self):
        """Gets the request_timeout_profile of this CreateTunnelPerformance.  # noqa: E501


        :return: The request_timeout_profile of this CreateTunnelPerformance.  # noqa: E501
        :rtype: ApplySSLKeyUid
        """
        return self._request_timeout_profile

    @request_timeout_profile.setter
    def request_timeout_profile(self, request_timeout_profile):
        """Sets the request_timeout_profile of this CreateTunnelPerformance.


        :param request_timeout_profile: The request_timeout_profile of this CreateTunnelPerformance.  # noqa: E501
        :type: ApplySSLKeyUid
        """

        self._request_timeout_profile = request_timeout_profile

    @property
    def compression_profile(self):
        """Gets the compression_profile of this CreateTunnelPerformance.  # noqa: E501


        :return: The compression_profile of this CreateTunnelPerformance.  # noqa: E501
        :rtype: ApplySSLKeyUid
        """
        return self._compression_profile

    @compression_profile.setter
    def compression_profile(self, compression_profile):
        """Sets the compression_profile of this CreateTunnelPerformance.


        :param compression_profile: The compression_profile of this CreateTunnelPerformance.  # noqa: E501
        :type: ApplySSLKeyUid
        """

        self._compression_profile = compression_profile

    @property
    def workflow_preserve_deflate(self):
        """Gets the workflow_preserve_deflate of this CreateTunnelPerformance.  # noqa: E501


        :return: The workflow_preserve_deflate of this CreateTunnelPerformance.  # noqa: E501
        :rtype: bool
        """
        return self._workflow_preserve_deflate

    @workflow_preserve_deflate.setter
    def workflow_preserve_deflate(self, workflow_preserve_deflate):
        """Sets the workflow_preserve_deflate of this CreateTunnelPerformance.


        :param workflow_preserve_deflate: The workflow_preserve_deflate of this CreateTunnelPerformance.  # noqa: E501
        :type: bool
        """

        self._workflow_preserve_deflate = workflow_preserve_deflate

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
        if not isinstance(other, CreateTunnelPerformance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTunnelPerformance):
            return True

        return self.to_dict() != other.to_dict()
