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


class CreateLogfilterUsedBySuccessArray(object):
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
        'tunnel_uid': 'str',
        'tunnel_name': 'str',
        'reverse_proxy_uid': 'str',
        'reverse_proxy_name': 'str'
    }

    attribute_map = {
        'tunnel_uid': 'tunnelUid',
        'tunnel_name': 'tunnelName',
        'reverse_proxy_uid': 'reverseProxyUid',
        'reverse_proxy_name': 'reverseProxyName'
    }

    def __init__(self, tunnel_uid=None, tunnel_name=None, reverse_proxy_uid=None, reverse_proxy_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateLogfilterUsedBySuccessArray - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tunnel_uid = None
        self._tunnel_name = None
        self._reverse_proxy_uid = None
        self._reverse_proxy_name = None
        self.discriminator = None

        if tunnel_uid is not None:
            self.tunnel_uid = tunnel_uid
        if tunnel_name is not None:
            self.tunnel_name = tunnel_name
        if reverse_proxy_uid is not None:
            self.reverse_proxy_uid = reverse_proxy_uid
        if reverse_proxy_name is not None:
            self.reverse_proxy_name = reverse_proxy_name

    @property
    def tunnel_uid(self):
        """Gets the tunnel_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501


        :return: The tunnel_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_uid

    @tunnel_uid.setter
    def tunnel_uid(self, tunnel_uid):
        """Sets the tunnel_uid of this CreateLogfilterUsedBySuccessArray.


        :param tunnel_uid: The tunnel_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :type: str
        """

        self._tunnel_uid = tunnel_uid

    @property
    def tunnel_name(self):
        """Gets the tunnel_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501


        :return: The tunnel_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_name

    @tunnel_name.setter
    def tunnel_name(self, tunnel_name):
        """Sets the tunnel_name of this CreateLogfilterUsedBySuccessArray.


        :param tunnel_name: The tunnel_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :type: str
        """

        self._tunnel_name = tunnel_name

    @property
    def reverse_proxy_uid(self):
        """Gets the reverse_proxy_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501


        :return: The reverse_proxy_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._reverse_proxy_uid

    @reverse_proxy_uid.setter
    def reverse_proxy_uid(self, reverse_proxy_uid):
        """Sets the reverse_proxy_uid of this CreateLogfilterUsedBySuccessArray.


        :param reverse_proxy_uid: The reverse_proxy_uid of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :type: str
        """

        self._reverse_proxy_uid = reverse_proxy_uid

    @property
    def reverse_proxy_name(self):
        """Gets the reverse_proxy_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501


        :return: The reverse_proxy_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :rtype: str
        """
        return self._reverse_proxy_name

    @reverse_proxy_name.setter
    def reverse_proxy_name(self, reverse_proxy_name):
        """Sets the reverse_proxy_name of this CreateLogfilterUsedBySuccessArray.


        :param reverse_proxy_name: The reverse_proxy_name of this CreateLogfilterUsedBySuccessArray.  # noqa: E501
        :type: str
        """

        self._reverse_proxy_name = reverse_proxy_name

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
        if not isinstance(other, CreateLogfilterUsedBySuccessArray):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLogfilterUsedBySuccessArray):
            return True

        return self.to_dict() != other.to_dict()
