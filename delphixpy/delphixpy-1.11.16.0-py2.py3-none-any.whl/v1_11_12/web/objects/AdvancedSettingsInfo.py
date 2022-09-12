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
#     /delphix-system-advanced-settings.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_12.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_12 import factory
from delphixpy.v1_11_12 import common

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

class AdvancedSettingsInfo(TypedObject):
    """
    *(extends* :py:class:`v1_11_12.web.vo.TypedObject` *)* Set advanced
    virtualization, OS, network, and service tunables.
    """
    def __init__(self, undef_enabled=True):
        super(AdvancedSettingsInfo, self).__init__()
        self._type = ("AdvancedSettingsInfo", True)
        self._modified_tunables = (self.__undef__, True)

    API_VERSION = "1.11.12"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AdvancedSettingsInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._modified_tunables = []
        for item in data.get("modifiedTunables") or []:
            obj._modified_tunables.append(factory.create_object(item))
            factory.validate_type(obj._modified_tunables[-1], "Tunable")
        obj._modified_tunables = (obj._modified_tunables, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AdvancedSettingsInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "modified_tunables" == "type" or (self.modified_tunables is not self.__undef__ and (not (dirty and not self._modified_tunables[1]))):
            dct["modifiedTunables"] = dictify(self.modified_tunables)
        if dirty and "modifiedTunables" in dct:
            del dct["modifiedTunables"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._modified_tunables = (self._modified_tunables[0], True)

    def is_dirty(self):
        return any([self._modified_tunables[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AdvancedSettingsInfo):
            return False
        return super(AdvancedSettingsInfo, self).__eq__(other) and \
               self.modified_tunables == other.modified_tunables

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            super(AdvancedSettingsInfo, self).__hash__(),
            self.modified_tunables,
        )

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def modified_tunables(self):
        """
        List of modified system tunables.

        :rtype: ``list`` of :py:class:`v1_11_12.web.vo.Tunable`
        """
        return self._modified_tunables[0]

