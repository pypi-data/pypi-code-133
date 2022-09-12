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


class PatchScoringlist(object):
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
        'description': 'str',
        'static_scoringlist': 'CreateApplianceSysctlProfile',
        'xss': 'str',
        'sqli': 'str',
        'fi': 'str',
        'cmdi': 'str',
        'otheri': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'static_scoringlist': 'staticScoringlist',
        'xss': 'xss',
        'sqli': 'sqli',
        'fi': 'fi',
        'cmdi': 'cmdi',
        'otheri': 'otheri'
    }

    def __init__(self, name=None, description=None, static_scoringlist=None, xss=None, sqli=None, fi=None, cmdi=None, otheri=None, local_vars_configuration=None):  # noqa: E501
        """PatchScoringlist - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._static_scoringlist = None
        self._xss = None
        self._sqli = None
        self._fi = None
        self._cmdi = None
        self._otheri = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if static_scoringlist is not None:
            self.static_scoringlist = static_scoringlist
        if xss is not None:
            self.xss = xss
        if sqli is not None:
            self.sqli = sqli
        if fi is not None:
            self.fi = fi
        if cmdi is not None:
            self.cmdi = cmdi
        if otheri is not None:
            self.otheri = otheri

    @property
    def name(self):
        """Gets the name of this PatchScoringlist.  # noqa: E501


        :return: The name of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchScoringlist.


        :param name: The name of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PatchScoringlist.  # noqa: E501


        :return: The description of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PatchScoringlist.


        :param description: The description of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def static_scoringlist(self):
        """Gets the static_scoringlist of this PatchScoringlist.  # noqa: E501


        :return: The static_scoringlist of this PatchScoringlist.  # noqa: E501
        :rtype: CreateApplianceSysctlProfile
        """
        return self._static_scoringlist

    @static_scoringlist.setter
    def static_scoringlist(self, static_scoringlist):
        """Sets the static_scoringlist of this PatchScoringlist.


        :param static_scoringlist: The static_scoringlist of this PatchScoringlist.  # noqa: E501
        :type: CreateApplianceSysctlProfile
        """

        self._static_scoringlist = static_scoringlist

    @property
    def xss(self):
        """Gets the xss of this PatchScoringlist.  # noqa: E501


        :return: The xss of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._xss

    @xss.setter
    def xss(self, xss):
        """Sets the xss of this PatchScoringlist.


        :param xss: The xss of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._xss = xss

    @property
    def sqli(self):
        """Gets the sqli of this PatchScoringlist.  # noqa: E501


        :return: The sqli of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._sqli

    @sqli.setter
    def sqli(self, sqli):
        """Sets the sqli of this PatchScoringlist.


        :param sqli: The sqli of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._sqli = sqli

    @property
    def fi(self):
        """Gets the fi of this PatchScoringlist.  # noqa: E501


        :return: The fi of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._fi

    @fi.setter
    def fi(self, fi):
        """Sets the fi of this PatchScoringlist.


        :param fi: The fi of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._fi = fi

    @property
    def cmdi(self):
        """Gets the cmdi of this PatchScoringlist.  # noqa: E501


        :return: The cmdi of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._cmdi

    @cmdi.setter
    def cmdi(self, cmdi):
        """Sets the cmdi of this PatchScoringlist.


        :param cmdi: The cmdi of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._cmdi = cmdi

    @property
    def otheri(self):
        """Gets the otheri of this PatchScoringlist.  # noqa: E501


        :return: The otheri of this PatchScoringlist.  # noqa: E501
        :rtype: str
        """
        return self._otheri

    @otheri.setter
    def otheri(self, otheri):
        """Sets the otheri of this PatchScoringlist.


        :param otheri: The otheri of this PatchScoringlist.  # noqa: E501
        :type: str
        """

        self._otheri = otheri

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
        if not isinstance(other, PatchScoringlist):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchScoringlist):
            return True

        return self.to_dict() != other.to_dict()
