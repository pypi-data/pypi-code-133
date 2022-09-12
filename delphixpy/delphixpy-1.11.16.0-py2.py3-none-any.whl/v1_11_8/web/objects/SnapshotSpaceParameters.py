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
#     /delphix-snapshotspaceparameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_8.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_8 import common

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

class SnapshotSpaceParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_8.web.vo.TypedObject` *)* Input to the
    operation to determine how much space is used by a set of snapshots.
    """
    def __init__(self, undef_enabled=True):
        super(SnapshotSpaceParameters, self).__init__()
        self._type = ("SnapshotSpaceParameters", True)
        self._object_references = (self.__undef__, True)

    API_VERSION = "1.11.8"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SnapshotSpaceParameters, cls).from_dict(data, dirty, undef_enabled)
        if "objectReferences" not in data:
            raise ValueError("Missing required property \"objectReferences\".")
        obj._object_references = []
        for item in data.get("objectReferences") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._object_references.append(item)
        obj._object_references = (obj._object_references, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SnapshotSpaceParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "object_references" == "type" or (self.object_references is not self.__undef__ and (not (dirty and not self._object_references[1]) or isinstance(self.object_references, list) or belongs_to_parent)):
            dct["objectReferences"] = dictify(self.object_references, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._object_references = (self._object_references[0], True)

    def is_dirty(self):
        return any([self._object_references[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SnapshotSpaceParameters):
            return False
        return super(SnapshotSpaceParameters, self).__eq__(other) and \
               self.object_references == other.object_references

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def object_references(self):
        """
        FilesystemObjects to query, in canonical object reference form.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._object_references[0]

    @object_references.setter
    def object_references(self, value):
        self._object_references = (value, True)

