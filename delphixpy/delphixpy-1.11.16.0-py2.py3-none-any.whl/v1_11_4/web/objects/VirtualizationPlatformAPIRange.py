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
#     /delphix-virtualization-platform-api-range.json
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

class VirtualizationPlatformAPIRange(TypedObject):
    """
    *(extends* :py:class:`v1_11_4.web.vo.TypedObject` *)* A range of
    Virtualization Platform API versions.
    """
    def __init__(self, undef_enabled=True):
        super(VirtualizationPlatformAPIRange, self).__init__()
        self._type = ("VirtualizationPlatformAPIRange", True)
        self._min = (self.__undef__, True)
        self._max = (self.__undef__, True)

    API_VERSION = "1.11.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(VirtualizationPlatformAPIRange, cls).from_dict(data, dirty, undef_enabled)
        if "min" in data and data["min"] is not None:
            obj._min = (factory.create_object(data["min"], "VirtualizationPlatformAPIVersion"), dirty)
            factory.validate_type(obj._min[0], "VirtualizationPlatformAPIVersion")
        else:
            obj._min = (obj.__undef__, dirty)
        if "max" in data and data["max"] is not None:
            obj._max = (factory.create_object(data["max"], "VirtualizationPlatformAPIVersion"), dirty)
            factory.validate_type(obj._max[0], "VirtualizationPlatformAPIVersion")
        else:
            obj._max = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(VirtualizationPlatformAPIRange, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "min" == "type" or (self.min is not self.__undef__ and (not (dirty and not self._min[1]))):
            dct["min"] = dictify(self.min)
        if "max" == "type" or (self.max is not self.__undef__ and (not (dirty and not self._max[1]))):
            dct["max"] = dictify(self.max)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._min = (self._min[0], True)
        self._max = (self._max[0], True)

    def is_dirty(self):
        return any([self._min[1], self._max[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, VirtualizationPlatformAPIRange):
            return False
        return super(VirtualizationPlatformAPIRange, self).__eq__(other) and \
               self.min == other.min and \
               self.max == other.max

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def min(self):
        """
        The minimum version in this range.

        :rtype: :py:class:`v1_11_4.web.vo.VirtualizationPlatformAPIVersion`
        """
        return self._min[0]

    @min.setter
    def min(self, value):
        self._min = (value, True)

    @property
    def max(self):
        """
        The maximum version in this range.

        :rtype: :py:class:`v1_11_4.web.vo.VirtualizationPlatformAPIVersion`
        """
        return self._max[0]

    @max.setter
    def max(self, value):
        self._max = (value, True)

