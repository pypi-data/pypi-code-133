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
#     /delphix-host-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_4.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_4 import factory
from delphixpy.v1_11_4 import common

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

class HostRuntime(TypedObject):
    """
    *(extends* :py:class:`v1_11_4.web.vo.TypedObject` *)* Runtime, non-
    persistent properties for a host machine.
    """
    def __init__(self, undef_enabled=True):
        super(HostRuntime, self).__init__()
        self._type = ("HostRuntime", True)
        self._available = (self.__undef__, True)
        self._available_timestamp = (self.__undef__, True)
        self._not_available_reason = (self.__undef__, True)
        self._trace_route_info = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(HostRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._available = (data.get("available", obj.__undef__), dirty)
        if obj._available[0] is not None and obj._available[0] is not obj.__undef__:
            assert isinstance(obj._available[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._available[0], type(obj._available[0])))
            common.validate_format(obj._available[0], "None", None, None)
        obj._available_timestamp = (data.get("availableTimestamp", obj.__undef__), dirty)
        if obj._available_timestamp[0] is not None and obj._available_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._available_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._available_timestamp[0], type(obj._available_timestamp[0])))
            common.validate_format(obj._available_timestamp[0], "date", None, None)
        obj._not_available_reason = (data.get("notAvailableReason", obj.__undef__), dirty)
        if obj._not_available_reason[0] is not None and obj._not_available_reason[0] is not obj.__undef__:
            assert isinstance(obj._not_available_reason[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._not_available_reason[0], type(obj._not_available_reason[0])))
            common.validate_format(obj._not_available_reason[0], "None", None, None)
        if "traceRouteInfo" in data and data["traceRouteInfo"] is not None:
            obj._trace_route_info = (factory.create_object(data["traceRouteInfo"], "TracerouteInfo"), dirty)
            factory.validate_type(obj._trace_route_info[0], "TracerouteInfo")
        else:
            obj._trace_route_info = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(HostRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "available" == "type" or (self.available is not self.__undef__ and (not (dirty and not self._available[1]))):
            dct["available"] = dictify(self.available)
        if "available_timestamp" == "type" or (self.available_timestamp is not self.__undef__ and (not (dirty and not self._available_timestamp[1]))):
            dct["availableTimestamp"] = dictify(self.available_timestamp)
        if "not_available_reason" == "type" or (self.not_available_reason is not self.__undef__ and (not (dirty and not self._not_available_reason[1]))):
            dct["notAvailableReason"] = dictify(self.not_available_reason)
        if "trace_route_info" == "type" or (self.trace_route_info is not self.__undef__ and (not (dirty and not self._trace_route_info[1]))):
            dct["traceRouteInfo"] = dictify(self.trace_route_info)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._available = (self._available[0], True)
        self._available_timestamp = (self._available_timestamp[0], True)
        self._not_available_reason = (self._not_available_reason[0], True)
        self._trace_route_info = (self._trace_route_info[0], True)

    def is_dirty(self):
        return any([self._available[1], self._available_timestamp[1], self._not_available_reason[1], self._trace_route_info[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HostRuntime):
            return False
        return super(HostRuntime, self).__eq__(other) and \
               self.available == other.available and \
               self.available_timestamp == other.available_timestamp and \
               self.not_available_reason == other.not_available_reason and \
               self.trace_route_info == other.trace_route_info

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def available(self):
        """
        True if the host is up and a connection can be established.

        :rtype: ``bool``
        """
        return self._available[0]

    @available.setter
    def available(self, value):
        self._available = (value, True)

    @property
    def available_timestamp(self):
        """
        The time that the 'available' propery was last checked.

        :rtype: ``TEXT_TYPE``
        """
        return self._available_timestamp[0]

    @available_timestamp.setter
    def available_timestamp(self, value):
        self._available_timestamp = (value, True)

    @property
    def not_available_reason(self):
        """
        The reason why the host is not available.

        :rtype: ``TEXT_TYPE``
        """
        return self._not_available_reason[0]

    @not_available_reason.setter
    def not_available_reason(self, value):
        self._not_available_reason = (value, True)

    @property
    def trace_route_info(self):
        """
        Traceroute network hops from host to Delphix Engine.

        :rtype: :py:class:`v1_11_4.web.vo.TracerouteInfo`
        """
        return self._trace_route_info[0]

    @trace_route_info.setter
    def trace_route_info(self, value):
        self._trace_route_info = (value, True)

