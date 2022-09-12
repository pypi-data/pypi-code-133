# coding: utf8
#
# Copyright 2022 by Delphix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This class has been automatically generated from:
#     /delphix-windows-host.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.Host import Host
from delphixpy.v1_11_7 import common

class __Undef(object):
    def __repr__(self):
        return "undef"

    def __setattr__(self, name, value):
        raise Exception('Cannot modify attributes of __Undef.')

_UNDEFINED = __Undef()

try:
    TEXT_TYPE = unicode
except NameError:
    TEXT_TYPE = str

class WindowsHost(Host):
    """
    *(extends* :py:class:`v1_11_7.web.vo.Host` *)* The representation of a
    Windows host object.
    """
    def __init__(self, undef_enabled=True):
        super(WindowsHost, self).__init__()
        self._type = ("WindowsHost", True)
        self._connector_port = (self.__undef__, True)
        self._connector_authentication_key = (self.__undef__, True)
        self._toolkit_path = (self.__undef__, True)
        self._connector_version = (self.__undef__, True)
        self._connector_dot_net_framework_version = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(WindowsHost, cls).from_dict(data, dirty, undef_enabled)
        obj._connector_port = (data.get("connectorPort", obj.__undef__), dirty)
        if obj._connector_port[0] is not None and obj._connector_port[0] is not obj.__undef__:
            assert isinstance(obj._connector_port[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._connector_port[0], type(obj._connector_port[0])))
            common.validate_format(obj._connector_port[0], "None", None, None)
        obj._connector_authentication_key = (data.get("connectorAuthenticationKey", obj.__undef__), dirty)
        if obj._connector_authentication_key[0] is not None and obj._connector_authentication_key[0] is not obj.__undef__:
            assert isinstance(obj._connector_authentication_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_authentication_key[0], type(obj._connector_authentication_key[0])))
            common.validate_format(obj._connector_authentication_key[0], "None", None, None)
        obj._toolkit_path = (data.get("toolkitPath", obj.__undef__), dirty)
        if obj._toolkit_path[0] is not None and obj._toolkit_path[0] is not obj.__undef__:
            assert isinstance(obj._toolkit_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit_path[0], type(obj._toolkit_path[0])))
            common.validate_format(obj._toolkit_path[0], "None", None, None)
        obj._connector_version = (data.get("connectorVersion", obj.__undef__), dirty)
        if obj._connector_version[0] is not None and obj._connector_version[0] is not obj.__undef__:
            assert isinstance(obj._connector_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_version[0], type(obj._connector_version[0])))
            common.validate_format(obj._connector_version[0], "None", None, None)
        obj._connector_dot_net_framework_version = (data.get("connectorDotNetFrameworkVersion", obj.__undef__), dirty)
        if obj._connector_dot_net_framework_version[0] is not None and obj._connector_dot_net_framework_version[0] is not obj.__undef__:
            assert isinstance(obj._connector_dot_net_framework_version[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connector_dot_net_framework_version[0], type(obj._connector_dot_net_framework_version[0])))
            common.validate_format(obj._connector_dot_net_framework_version[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(WindowsHost, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "connector_port" == "type" or (self.connector_port is not self.__undef__ and (not (dirty and not self._connector_port[1]) or isinstance(self.connector_port, list) or belongs_to_parent)):
            dct["connectorPort"] = dictify(self.connector_port)
        if "connector_authentication_key" == "type" or (self.connector_authentication_key is not self.__undef__ and (not (dirty and not self._connector_authentication_key[1]) or isinstance(self.connector_authentication_key, list) or belongs_to_parent)):
            dct["connectorAuthenticationKey"] = dictify(self.connector_authentication_key)
        if "toolkit_path" == "type" or (self.toolkit_path is not self.__undef__ and (not (dirty and not self._toolkit_path[1]))):
            dct["toolkitPath"] = dictify(self.toolkit_path)
        if dirty and "toolkitPath" in dct:
            del dct["toolkitPath"]
        if "connector_version" == "type" or (self.connector_version is not self.__undef__ and (not (dirty and not self._connector_version[1]))):
            dct["connectorVersion"] = dictify(self.connector_version)
        if dirty and "connectorVersion" in dct:
            del dct["connectorVersion"]
        if "connector_dot_net_framework_version" == "type" or (self.connector_dot_net_framework_version is not self.__undef__ and (not (dirty and not self._connector_dot_net_framework_version[1]))):
            dct["connectorDotNetFrameworkVersion"] = dictify(self.connector_dot_net_framework_version)
        if dirty and "connectorDotNetFrameworkVersion" in dct:
            del dct["connectorDotNetFrameworkVersion"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._connector_port = (self._connector_port[0], True)
        self._connector_authentication_key = (self._connector_authentication_key[0], True)
        self._toolkit_path = (self._toolkit_path[0], True)
        self._connector_version = (self._connector_version[0], True)
        self._connector_dot_net_framework_version = (self._connector_dot_net_framework_version[0], True)

    def is_dirty(self):
        return any([self._connector_port[1], self._connector_authentication_key[1], self._toolkit_path[1], self._connector_version[1], self._connector_dot_net_framework_version[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, WindowsHost):
            return False
        return super(WindowsHost, self).__eq__(other) and \
               self.connector_port == other.connector_port and \
               self.connector_authentication_key == other.connector_authentication_key and \
               self.toolkit_path == other.toolkit_path and \
               self.connector_version == other.connector_version and \
               self.connector_dot_net_framework_version == other.connector_dot_net_framework_version

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def connector_port(self):
        """
        The port that the connector connects on.

        :rtype: ``float``
        """
        return self._connector_port[0]

    @connector_port.setter
    def connector_port(self, value):
        self._connector_port = (value, True)

    @property
    def connector_authentication_key(self):
        """
        Unique per Delphix key used to authenticate with the remote Delphix
        Connector.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_authentication_key[0]

    @connector_authentication_key.setter
    def connector_authentication_key(self, value):
        self._connector_authentication_key = (value, True)

    @property
    def toolkit_path(self):
        """
        The path for the toolkit that resides on the host.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit_path[0]

    @property
    def connector_version(self):
        """
        The Windows Connector version that is installed on the provided host.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_version[0]

    @property
    def connector_dot_net_framework_version(self):
        """
        The .NET Framework version used for Windows Connector Service.

        :rtype: ``TEXT_TYPE``
        """
        return self._connector_dot_net_framework_version[0]

