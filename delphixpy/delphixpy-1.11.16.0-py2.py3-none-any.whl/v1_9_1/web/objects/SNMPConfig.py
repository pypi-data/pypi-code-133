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
#     /delphix-snmp-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_1 import common

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

class SNMPConfig(TypedObject):
    """
    *(extends* :py:class:`v1_9_1.web.vo.TypedObject` *)* SNMP configuration.
    """
    def __init__(self, undef_enabled=True):
        super(SNMPConfig, self).__init__()
        self._type = ("SNMPConfig", True)
        self._enabled = (self.__undef__, True)
        self._community = (self.__undef__, True)
        self._authorized_network = (self.__undef__, True)
        self._location = (self.__undef__, True)
        self._severity = (self.__undef__, True)

    API_VERSION = "1.9.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SNMPConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._community = (data.get("community", obj.__undef__), dirty)
        if obj._community[0] is not None and obj._community[0] is not obj.__undef__:
            assert isinstance(obj._community[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._community[0], type(obj._community[0])))
            common.validate_format(obj._community[0], "None", None, None)
        obj._authorized_network = (data.get("authorizedNetwork", obj.__undef__), dirty)
        if obj._authorized_network[0] is not None and obj._authorized_network[0] is not obj.__undef__:
            assert isinstance(obj._authorized_network[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._authorized_network[0], type(obj._authorized_network[0])))
            common.validate_format(obj._authorized_network[0], "cidrAddress", None, None)
        obj._location = (data.get("location", obj.__undef__), dirty)
        if obj._location[0] is not None and obj._location[0] is not obj.__undef__:
            assert isinstance(obj._location[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._location[0], type(obj._location[0])))
            common.validate_format(obj._location[0], "None", None, None)
        obj._severity = (data.get("severity", obj.__undef__), dirty)
        if obj._severity[0] is not None and obj._severity[0] is not obj.__undef__:
            assert isinstance(obj._severity[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._severity[0], type(obj._severity[0])))
            assert obj._severity[0] in ['CRITICAL', 'WARNING', 'INFORMATIONAL'], "Expected enum ['CRITICAL', 'WARNING', 'INFORMATIONAL'] but got %s" % obj._severity[0]
            common.validate_format(obj._severity[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SNMPConfig, self).to_dict(dirty, belongs_to_parent)

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
            dct["enabled"] = True
        if "community" == "type" or (self.community is not self.__undef__ and (not (dirty and not self._community[1]) or isinstance(self.community, list) or belongs_to_parent)):
            dct["community"] = dictify(self.community)
        elif belongs_to_parent and self.community is self.__undef__:
            dct["community"] = "public"
        if "authorized_network" == "type" or (self.authorized_network is not self.__undef__ and (not (dirty and not self._authorized_network[1]) or isinstance(self.authorized_network, list) or belongs_to_parent)):
            dct["authorizedNetwork"] = dictify(self.authorized_network)
        elif belongs_to_parent and self.authorized_network is self.__undef__:
            dct["authorizedNetwork"] = "0.0.0.0/0"
        if "location" == "type" or (self.location is not self.__undef__ and (not (dirty and not self._location[1]) or isinstance(self.location, list) or belongs_to_parent)):
            dct["location"] = dictify(self.location)
        if "severity" == "type" or (self.severity is not self.__undef__ and (not (dirty and not self._severity[1]) or isinstance(self.severity, list) or belongs_to_parent)):
            dct["severity"] = dictify(self.severity)
        elif belongs_to_parent and self.severity is self.__undef__:
            dct["severity"] = "WARNING"
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._enabled = (self._enabled[0], True)
        self._community = (self._community[0], True)
        self._authorized_network = (self._authorized_network[0], True)
        self._location = (self._location[0], True)
        self._severity = (self._severity[0], True)

    def is_dirty(self):
        return any([self._enabled[1], self._community[1], self._authorized_network[1], self._location[1], self._severity[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SNMPConfig):
            return False
        return super(SNMPConfig, self).__eq__(other) and \
               self.enabled == other.enabled and \
               self.community == other.community and \
               self.authorized_network == other.authorized_network and \
               self.location == other.location and \
               self.severity == other.severity

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def enabled(self):
        """
        *(default value: True)* True if the SNMP service is enabled.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def community(self):
        """
        *(default value: public)* The community string that clients must
        provide when querying this server.

        :rtype: ``TEXT_TYPE``
        """
        return self._community[0]

    @community.setter
    def community(self, value):
        self._community = (value, True)

    @property
    def authorized_network(self):
        """
        *(default value: 0.0.0.0/0)* The network which is authorized to query
        this SNMP server, in CIDR notation. Toallow any client, then leave
        unset or set to 0.0.0.0/0. To block all clients, set to 127.0.0.1/8.

        :rtype: ``TEXT_TYPE``
        """
        return self._authorized_network[0]

    @authorized_network.setter
    def authorized_network(self, value):
        self._authorized_network = (value, True)

    @property
    def location(self):
        """
        The physical location of this Delphix Engine (OID 1.3.6.1.2.1.1.6 -
        sysLocation).

        :rtype: ``TEXT_TYPE``
        """
        return self._location[0]

    @location.setter
    def location(self, value):
        self._location = (value, True)

    @property
    def severity(self):
        """
        *(default value: WARNING)* SNMP trap severity. SNMP managers are only
        notified of events at or above this level. *(permitted values:
        CRITICAL, WARNING, INFORMATIONAL)*

        :rtype: ``TEXT_TYPE``
        """
        return self._severity[0]

    @severity.setter
    def severity(self, value):
        self._severity = (value, True)

