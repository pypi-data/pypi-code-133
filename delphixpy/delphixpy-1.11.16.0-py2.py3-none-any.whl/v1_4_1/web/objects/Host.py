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
#     /delphix-host.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_1.web.objects.ReadonlyNamedUserObject import ReadonlyNamedUserObject
from delphixpy.v1_4_1 import factory
from delphixpy.v1_4_1 import common

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

class Host(ReadonlyNamedUserObject):
    """
    *(extends* :py:class:`v1_4_1.web.vo.ReadonlyNamedUserObject` *)* The
    representation of a host object.
    """
    def __init__(self, undef_enabled=True):
        super(Host, self).__init__()
        self._type = ("Host", True)
        self._addresses = (self.__undef__, True)
        self._date_added = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._host_configuration = (self.__undef__, True)
        self._host_runtime = (self.__undef__, True)
        self._privilege_elevation_profile = (self.__undef__, True)
        self._ssh_port = (self.__undef__, True)
        self._toolkit_path = (self.__undef__, True)

    API_VERSION = "1.4.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(Host, cls).from_dict(data, dirty, undef_enabled)
        obj._addresses = []
        for item in data.get("addresses") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "host", None, None)
            obj._addresses.append(item)
        obj._addresses = (obj._addresses, dirty)
        obj._date_added = (data.get("dateAdded", obj.__undef__), dirty)
        if obj._date_added[0] is not None and obj._date_added[0] is not obj.__undef__:
            assert isinstance(obj._date_added[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._date_added[0], type(obj._date_added[0])))
            common.validate_format(obj._date_added[0], "None", None, None)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        if "hostConfiguration" in data and data["hostConfiguration"] is not None:
            obj._host_configuration = (factory.create_object(data["hostConfiguration"], "HostConfiguration"), dirty)
            factory.validate_type(obj._host_configuration[0], "HostConfiguration")
        else:
            obj._host_configuration = (obj.__undef__, dirty)
        if "hostRuntime" in data and data["hostRuntime"] is not None:
            obj._host_runtime = (factory.create_object(data["hostRuntime"], "HostRuntime"), dirty)
            factory.validate_type(obj._host_runtime[0], "HostRuntime")
        else:
            obj._host_runtime = (obj.__undef__, dirty)
        obj._privilege_elevation_profile = (data.get("privilegeElevationProfile", obj.__undef__), dirty)
        if obj._privilege_elevation_profile[0] is not None and obj._privilege_elevation_profile[0] is not obj.__undef__:
            assert isinstance(obj._privilege_elevation_profile[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._privilege_elevation_profile[0], type(obj._privilege_elevation_profile[0])))
            common.validate_format(obj._privilege_elevation_profile[0], "objectReference", None, None)
        obj._ssh_port = (data.get("sshPort", obj.__undef__), dirty)
        if obj._ssh_port[0] is not None and obj._ssh_port[0] is not obj.__undef__:
            assert isinstance(obj._ssh_port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._ssh_port[0], type(obj._ssh_port[0])))
            common.validate_format(obj._ssh_port[0], "None", None, None)
        obj._toolkit_path = (data.get("toolkitPath", obj.__undef__), dirty)
        if obj._toolkit_path[0] is not None and obj._toolkit_path[0] is not obj.__undef__:
            assert isinstance(obj._toolkit_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit_path[0], type(obj._toolkit_path[0])))
            common.validate_format(obj._toolkit_path[0], "None", None, 256)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(Host, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "addresses" == "type" or (self.addresses is not self.__undef__ and (not (dirty and not self._addresses[1]) or isinstance(self.addresses, list) or belongs_to_parent)):
            dct["addresses"] = dictify(self.addresses, prop_is_list_or_vo=True)
        if "date_added" == "type" or (self.date_added is not self.__undef__ and (not (dirty and not self._date_added[1]))):
            dct["dateAdded"] = dictify(self.date_added)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]))):
            dct["enabled"] = dictify(self.enabled)
        if "host_configuration" == "type" or (self.host_configuration is not self.__undef__ and (not (dirty and not self._host_configuration[1]))):
            dct["hostConfiguration"] = dictify(self.host_configuration)
        if "host_runtime" == "type" or (self.host_runtime is not self.__undef__ and (not (dirty and not self._host_runtime[1]))):
            dct["hostRuntime"] = dictify(self.host_runtime)
        if "privilege_elevation_profile" == "type" or (self.privilege_elevation_profile is not self.__undef__ and (not (dirty and not self._privilege_elevation_profile[1]) or isinstance(self.privilege_elevation_profile, list) or belongs_to_parent)):
            dct["privilegeElevationProfile"] = dictify(self.privilege_elevation_profile)
        if "ssh_port" == "type" or (self.ssh_port is not self.__undef__ and (not (dirty and not self._ssh_port[1]) or isinstance(self.ssh_port, list) or belongs_to_parent)):
            dct["sshPort"] = dictify(self.ssh_port)
        elif belongs_to_parent and self.ssh_port is self.__undef__:
            dct["sshPort"] = 22
        if "toolkit_path" == "type" or (self.toolkit_path is not self.__undef__ and (not (dirty and not self._toolkit_path[1]) or isinstance(self.toolkit_path, list) or belongs_to_parent)):
            dct["toolkitPath"] = dictify(self.toolkit_path)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._addresses = (self._addresses[0], True)
        self._date_added = (self._date_added[0], True)
        self._enabled = (self._enabled[0], True)
        self._host_configuration = (self._host_configuration[0], True)
        self._host_runtime = (self._host_runtime[0], True)
        self._privilege_elevation_profile = (self._privilege_elevation_profile[0], True)
        self._ssh_port = (self._ssh_port[0], True)
        self._toolkit_path = (self._toolkit_path[0], True)

    def is_dirty(self):
        return any([self._addresses[1], self._date_added[1], self._enabled[1], self._host_configuration[1], self._host_runtime[1], self._privilege_elevation_profile[1], self._ssh_port[1], self._toolkit_path[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Host):
            return False
        return super(Host, self).__eq__(other) and \
               self.addresses == other.addresses and \
               self.date_added == other.date_added and \
               self.enabled == other.enabled and \
               self.host_configuration == other.host_configuration and \
               self.host_runtime == other.host_runtime and \
               self.privilege_elevation_profile == other.privilege_elevation_profile and \
               self.ssh_port == other.ssh_port and \
               self.toolkit_path == other.toolkit_path

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def addresses(self):
        """
        The addresses associated with the host.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._addresses[0]

    @addresses.setter
    def addresses(self, value):
        self._addresses = (value, True)

    @property
    def date_added(self):
        """
        The date the host was added.

        :rtype: ``TEXT_TYPE``
        """
        return self._date_added[0]

    @date_added.setter
    def date_added(self, value):
        self._date_added = (value, True)

    @property
    def enabled(self):
        """
        The boolean value indicating whether the host is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def host_configuration(self):
        """
        The host configuration object associated with the host.

        :rtype: :py:class:`v1_4_1.web.vo.HostConfiguration`
        """
        return self._host_configuration[0]

    @host_configuration.setter
    def host_configuration(self, value):
        self._host_configuration = (value, True)

    @property
    def host_runtime(self):
        """
        Runtime properties for this host.

        :rtype: :py:class:`v1_4_1.web.vo.HostRuntime`
        """
        return self._host_runtime[0]

    @host_runtime.setter
    def host_runtime(self, value):
        self._host_runtime = (value, True)

    @property
    def privilege_elevation_profile(self):
        """
        Profile for escalating user privileges.

        :rtype: ``TEXT_TYPE``
        """
        return self._privilege_elevation_profile[0]

    @privilege_elevation_profile.setter
    def privilege_elevation_profile(self, value):
        self._privilege_elevation_profile = (value, True)

    @property
    def ssh_port(self):
        """
        *(default value: 22)* The port number used to connect to the host via
        SSH.

        :rtype: ``int``
        """
        return self._ssh_port[0]

    @ssh_port.setter
    def ssh_port(self, value):
        self._ssh_port = (value, True)

    @property
    def toolkit_path(self):
        """
        The path for the toolkit that resides on the host.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit_path[0]

    @toolkit_path.setter
    def toolkit_path(self, value):
        self._toolkit_path = (value, True)

