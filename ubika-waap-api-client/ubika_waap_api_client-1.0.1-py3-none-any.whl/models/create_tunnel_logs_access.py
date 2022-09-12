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


class CreateTunnelLogsAccess(object):
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
        'file': 'bool',
        'file_format_profile': 'str',
        'database': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'file_format_profile': 'fileFormatProfile',
        'database': 'database'
    }

    def __init__(self, file=None, file_format_profile=None, database=None, local_vars_configuration=None):  # noqa: E501
        """CreateTunnelLogsAccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self._file_format_profile = None
        self._database = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if file_format_profile is not None:
            self.file_format_profile = file_format_profile
        if database is not None:
            self.database = database

    @property
    def file(self):
        """Gets the file of this CreateTunnelLogsAccess.  # noqa: E501


        :return: The file of this CreateTunnelLogsAccess.  # noqa: E501
        :rtype: bool
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateTunnelLogsAccess.


        :param file: The file of this CreateTunnelLogsAccess.  # noqa: E501
        :type: bool
        """

        self._file = file

    @property
    def file_format_profile(self):
        """Gets the file_format_profile of this CreateTunnelLogsAccess.  # noqa: E501


        :return: The file_format_profile of this CreateTunnelLogsAccess.  # noqa: E501
        :rtype: str
        """
        return self._file_format_profile

    @file_format_profile.setter
    def file_format_profile(self, file_format_profile):
        """Sets the file_format_profile of this CreateTunnelLogsAccess.


        :param file_format_profile: The file_format_profile of this CreateTunnelLogsAccess.  # noqa: E501
        :type: str
        """

        self._file_format_profile = file_format_profile

    @property
    def database(self):
        """Gets the database of this CreateTunnelLogsAccess.  # noqa: E501


        :return: The database of this CreateTunnelLogsAccess.  # noqa: E501
        :rtype: bool
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this CreateTunnelLogsAccess.


        :param database: The database of this CreateTunnelLogsAccess.  # noqa: E501
        :type: bool
        """

        self._database = database

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
        if not isinstance(other, CreateTunnelLogsAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateTunnelLogsAccess):
            return True

        return self.to_dict() != other.to_dict()
