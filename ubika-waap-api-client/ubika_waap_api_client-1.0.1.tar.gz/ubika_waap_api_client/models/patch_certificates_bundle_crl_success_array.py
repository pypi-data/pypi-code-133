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


class PatchCertificatesBundleCrlSuccessArray(object):
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
        'uid': 'str',
        'name': 'str',
        'expiration': 'str',
        'issuer': 'str',
        'next_update': 'str',
        'enable_auto_update': 'bool',
        'download_url': 'str',
        'download_method': 'str',
        'refresh_cron_time': 'str',
        'enable': 'bool',
        'enable_proxy': 'bool',
        'enable_proxy_authentication': 'bool',
        'proxy_profile_uid': 'str',
        'header_host': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'expiration': 'expiration',
        'issuer': 'issuer',
        'next_update': 'nextUpdate',
        'enable_auto_update': 'enableAutoUpdate',
        'download_url': 'downloadUrl',
        'download_method': 'downloadMethod',
        'refresh_cron_time': 'refreshCronTime',
        'enable': 'enable',
        'enable_proxy': 'enableProxy',
        'enable_proxy_authentication': 'enableProxyAuthentication',
        'proxy_profile_uid': 'proxyProfileUid',
        'header_host': 'headerHost'
    }

    def __init__(self, uid=None, name=None, expiration=None, issuer=None, next_update=None, enable_auto_update=None, download_url=None, download_method=None, refresh_cron_time=None, enable=None, enable_proxy=None, enable_proxy_authentication=None, proxy_profile_uid=None, header_host=None, local_vars_configuration=None):  # noqa: E501
        """PatchCertificatesBundleCrlSuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._expiration = None
        self._issuer = None
        self._next_update = None
        self._enable_auto_update = None
        self._download_url = None
        self._download_method = None
        self._refresh_cron_time = None
        self._enable = None
        self._enable_proxy = None
        self._enable_proxy_authentication = None
        self._proxy_profile_uid = None
        self._header_host = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if expiration is not None:
            self.expiration = expiration
        if issuer is not None:
            self.issuer = issuer
        if next_update is not None:
            self.next_update = next_update
        if enable_auto_update is not None:
            self.enable_auto_update = enable_auto_update
        if download_url is not None:
            self.download_url = download_url
        if download_method is not None:
            self.download_method = download_method
        if refresh_cron_time is not None:
            self.refresh_cron_time = refresh_cron_time
        if enable is not None:
            self.enable = enable
        if enable_proxy is not None:
            self.enable_proxy = enable_proxy
        if enable_proxy_authentication is not None:
            self.enable_proxy_authentication = enable_proxy_authentication
        if proxy_profile_uid is not None:
            self.proxy_profile_uid = proxy_profile_uid
        if header_host is not None:
            self.header_host = header_host

    @property
    def uid(self):
        """Gets the uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PatchCertificatesBundleCrlSuccessArray.


        :param uid: The uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The name of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchCertificatesBundleCrlSuccessArray.


        :param name: The name of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def expiration(self):
        """Gets the expiration of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The expiration of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PatchCertificatesBundleCrlSuccessArray.


        :param expiration: The expiration of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def issuer(self):
        """Gets the issuer of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The issuer of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this PatchCertificatesBundleCrlSuccessArray.


        :param issuer: The issuer of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def next_update(self):
        """Gets the next_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The next_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._next_update

    @next_update.setter
    def next_update(self, next_update):
        """Sets the next_update of this PatchCertificatesBundleCrlSuccessArray.


        :param next_update: The next_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._next_update = next_update

    @property
    def enable_auto_update(self):
        """Gets the enable_auto_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The enable_auto_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_update

    @enable_auto_update.setter
    def enable_auto_update(self, enable_auto_update):
        """Sets the enable_auto_update of this PatchCertificatesBundleCrlSuccessArray.


        :param enable_auto_update: The enable_auto_update of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: bool
        """

        self._enable_auto_update = enable_auto_update

    @property
    def download_url(self):
        """Gets the download_url of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The download_url of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this PatchCertificatesBundleCrlSuccessArray.


        :param download_url: The download_url of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def download_method(self):
        """Gets the download_method of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The download_method of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._download_method

    @download_method.setter
    def download_method(self, download_method):
        """Sets the download_method of this PatchCertificatesBundleCrlSuccessArray.


        :param download_method: The download_method of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._download_method = download_method

    @property
    def refresh_cron_time(self):
        """Gets the refresh_cron_time of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The refresh_cron_time of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._refresh_cron_time

    @refresh_cron_time.setter
    def refresh_cron_time(self, refresh_cron_time):
        """Sets the refresh_cron_time of this PatchCertificatesBundleCrlSuccessArray.


        :param refresh_cron_time: The refresh_cron_time of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._refresh_cron_time = refresh_cron_time

    @property
    def enable(self):
        """Gets the enable of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The enable of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PatchCertificatesBundleCrlSuccessArray.


        :param enable: The enable of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def enable_proxy(self):
        """Gets the enable_proxy of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The enable_proxy of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._enable_proxy

    @enable_proxy.setter
    def enable_proxy(self, enable_proxy):
        """Sets the enable_proxy of this PatchCertificatesBundleCrlSuccessArray.


        :param enable_proxy: The enable_proxy of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: bool
        """

        self._enable_proxy = enable_proxy

    @property
    def enable_proxy_authentication(self):
        """Gets the enable_proxy_authentication of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The enable_proxy_authentication of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: bool
        """
        return self._enable_proxy_authentication

    @enable_proxy_authentication.setter
    def enable_proxy_authentication(self, enable_proxy_authentication):
        """Sets the enable_proxy_authentication of this PatchCertificatesBundleCrlSuccessArray.


        :param enable_proxy_authentication: The enable_proxy_authentication of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: bool
        """

        self._enable_proxy_authentication = enable_proxy_authentication

    @property
    def proxy_profile_uid(self):
        """Gets the proxy_profile_uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The proxy_profile_uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._proxy_profile_uid

    @proxy_profile_uid.setter
    def proxy_profile_uid(self, proxy_profile_uid):
        """Sets the proxy_profile_uid of this PatchCertificatesBundleCrlSuccessArray.


        :param proxy_profile_uid: The proxy_profile_uid of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._proxy_profile_uid = proxy_profile_uid

    @property
    def header_host(self):
        """Gets the header_host of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501


        :return: The header_host of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._header_host

    @header_host.setter
    def header_host(self, header_host):
        """Sets the header_host of this PatchCertificatesBundleCrlSuccessArray.


        :param header_host: The header_host of this PatchCertificatesBundleCrlSuccessArray.  # noqa: E501
        :type: str
        """

        self._header_host = header_host

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
        if not isinstance(other, PatchCertificatesBundleCrlSuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchCertificatesBundleCrlSuccessArray):
            return True

        return self.to_dict() != other.to_dict()
