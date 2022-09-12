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
#     /delphix-snapshot-space-map.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_0.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_0 import common

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

class SnapshotSpaceMap(TypedObject):
    """
    *(extends* :py:class:`v1_9_0.web.vo.TypedObject` *)* Mapping of containers
    and snapshots to their respective space usage.
    """
    def __init__(self, undef_enabled=True):
        super(SnapshotSpaceMap, self).__init__()
        self._type = ("SnapshotSpaceMap", True)
        self._size_map = (self.__undef__, True)

    API_VERSION = "1.9.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SnapshotSpaceMap, cls).from_dict(data, dirty, undef_enabled)
        obj._size_map = (data.get("sizeMap", obj.__undef__), dirty)
        if obj._size_map[0] is not None and obj._size_map[0] is not obj.__undef__:
            assert isinstance(obj._size_map[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._size_map[0], type(obj._size_map[0])))
            common.validate_format(obj._size_map[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SnapshotSpaceMap, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "size_map" == "type" or (self.size_map is not self.__undef__ and (not (dirty and not self._size_map[1]))):
            dct["sizeMap"] = dictify(self.size_map)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._size_map = (self._size_map[0], True)

    def is_dirty(self):
        return any([self._size_map[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SnapshotSpaceMap):
            return False
        return super(SnapshotSpaceMap, self).__eq__(other) and \
               self.size_map == other.size_map

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def size_map(self):
        """
        Amount of space, per object, in bytes, that it uses.

        :rtype: ``dict``
        """
        return self._size_map[0]

    @size_map.setter
    def size_map(self, value):
        self._size_map = (value, True)

