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
#     /delphix-traceroute-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_1 import common

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

class TracerouteInfo(TypedObject):
    """
    *(extends* :py:class:`v1_6_1.web.vo.TypedObject` *)* Trace route info from
    target host to Delphix Engine.
    """
    def __init__(self, undef_enabled=True):
        super(TracerouteInfo, self).__init__()
        self._type = ("TracerouteInfo", True)
        self._network_hops = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TracerouteInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._network_hops = (data.get("networkHops", obj.__undef__), dirty)
        if obj._network_hops[0] is not None and obj._network_hops[0] is not obj.__undef__:
            assert isinstance(obj._network_hops[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._network_hops[0], type(obj._network_hops[0])))
            common.validate_format(obj._network_hops[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TracerouteInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "network_hops" == "type" or (self.network_hops is not self.__undef__ and (not (dirty and not self._network_hops[1]))):
            dct["networkHops"] = dictify(self.network_hops)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._network_hops = (self._network_hops[0], True)

    def is_dirty(self):
        return any([self._network_hops[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TracerouteInfo):
            return False
        return super(TracerouteInfo, self).__eq__(other) and \
               self.network_hops == other.network_hops

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def network_hops(self):
        """
        Latency of network hops from host to Delphix Engine.

        :rtype: ``TEXT_TYPE``
        """
        return self._network_hops[0]

    @network_hops.setter
    def network_hops(self, value):
        self._network_hops = (value, True)

