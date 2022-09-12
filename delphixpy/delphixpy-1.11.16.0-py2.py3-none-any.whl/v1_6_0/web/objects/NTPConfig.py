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
#     /delphix-ntp-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_0 import common

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

class NTPConfig(TypedObject):
    """
    *(extends* :py:class:`v1_6_0.web.vo.TypedObject` *)* NTP (Network Time
    Protocol) configuration.
    """
    def __init__(self, undef_enabled=True):
        super(NTPConfig, self).__init__()
        self._type = ("NTPConfig", True)
        self._enabled = (self.__undef__, True)
        self._multicast_address = (self.__undef__, True)
        self._servers = (self.__undef__, True)
        self._use_multicast = (self.__undef__, True)

    API_VERSION = "1.6.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NTPConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._multicast_address = (data.get("multicastAddress", obj.__undef__), dirty)
        if obj._multicast_address[0] is not None and obj._multicast_address[0] is not obj.__undef__:
            assert isinstance(obj._multicast_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._multicast_address[0], type(obj._multicast_address[0])))
            common.validate_format(obj._multicast_address[0], "ipv4Address", None, None)
        obj._servers = []
        for item in data.get("servers") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "host", None, None)
            obj._servers.append(item)
        obj._servers = (obj._servers, dirty)
        obj._use_multicast = (data.get("useMulticast", obj.__undef__), dirty)
        if obj._use_multicast[0] is not None and obj._use_multicast[0] is not obj.__undef__:
            assert isinstance(obj._use_multicast[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._use_multicast[0], type(obj._use_multicast[0])))
            common.validate_format(obj._use_multicast[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NTPConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]) or isinstance(self.enabled, list) or belongs_to_parent)):
            dct["enabled"] = dictify(self.enabled)
        elif belongs_to_parent and self.enabled is self.__undef__:
            dct["enabled"] = False
        if "multicast_address" == "type" or (self.multicast_address is not self.__undef__ and (not (dirty and not self._multicast_address[1]) or isinstance(self.multicast_address, list) or belongs_to_parent)):
            dct["multicastAddress"] = dictify(self.multicast_address)
        elif belongs_to_parent and self.multicast_address is self.__undef__:
            dct["multicastAddress"] = "224.0.1.1"
        if "servers" == "type" or (self.servers is not self.__undef__ and (not (dirty and not self._servers[1]) or isinstance(self.servers, list) or belongs_to_parent)):
            dct["servers"] = dictify(self.servers, prop_is_list_or_vo=True)
        if "use_multicast" == "type" or (self.use_multicast is not self.__undef__ and (not (dirty and not self._use_multicast[1]) or isinstance(self.use_multicast, list) or belongs_to_parent)):
            dct["useMulticast"] = dictify(self.use_multicast)
        elif belongs_to_parent and self.use_multicast is self.__undef__:
            dct["useMulticast"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._enabled = (self._enabled[0], True)
        self._multicast_address = (self._multicast_address[0], True)
        self._servers = (self._servers[0], True)
        self._use_multicast = (self._use_multicast[0], True)

    def is_dirty(self):
        return any([self._enabled[1], self._multicast_address[1], self._servers[1], self._use_multicast[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NTPConfig):
            return False
        return super(NTPConfig, self).__eq__(other) and \
               self.enabled == other.enabled and \
               self.multicast_address == other.multicast_address and \
               self.servers == other.servers and \
               self.use_multicast == other.use_multicast

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def enabled(self):
        """
        If true, then time is synchronized with the configured NTP servers. The
        management service is automatically restarted if this value is changed.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def multicast_address(self):
        """
        *(default value: 224.0.1.1)* Address to use for multicast NTP
        discovery. This is only valid when 'useMulticast' is set.

        :rtype: ``TEXT_TYPE``
        """
        return self._multicast_address[0]

    @multicast_address.setter
    def multicast_address(self, value):
        self._multicast_address = (value, True)

    @property
    def servers(self):
        """
        A list of NTP servers to use for synchronization. At least one server
        must be specified if multicast is not being used.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._servers[0]

    @servers.setter
    def servers(self, value):
        self._servers = (value, True)

    @property
    def use_multicast(self):
        """
        If true, discover NTP servers using multicast.

        :rtype: ``bool``
        """
        return self._use_multicast[0]

    @use_multicast.setter
    def use_multicast(self, value):
        self._use_multicast = (value, True)

