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
#     /delphix-js-bookmark-usage-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_14.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_14 import common

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

class JSBookmarkUsageData(TypedObject):
    """
    *(extends* :py:class:`v1_11_14.web.vo.TypedObject` *)* The space usage
    information for a Self-Service bookmark.
    """
    def __init__(self, undef_enabled=True):
        super(JSBookmarkUsageData, self).__init__()
        self._type = ("JSBookmarkUsageData", True)
        self._bookmark = (self.__undef__, True)
        self._data_layout = (self.__undef__, True)
        self._unique = (self.__undef__, True)
        self._shared = (self.__undef__, True)
        self._externally_referenced = (self.__undef__, True)

    API_VERSION = "1.11.14"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSBookmarkUsageData, cls).from_dict(data, dirty, undef_enabled)
        obj._bookmark = (data.get("bookmark", obj.__undef__), dirty)
        if obj._bookmark[0] is not None and obj._bookmark[0] is not obj.__undef__:
            assert isinstance(obj._bookmark[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._bookmark[0], type(obj._bookmark[0])))
            common.validate_format(obj._bookmark[0], "objectReference", None, None)
        obj._data_layout = (data.get("dataLayout", obj.__undef__), dirty)
        if obj._data_layout[0] is not None and obj._data_layout[0] is not obj.__undef__:
            assert isinstance(obj._data_layout[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_layout[0], type(obj._data_layout[0])))
            common.validate_format(obj._data_layout[0], "None", None, None)
        obj._unique = (data.get("unique", obj.__undef__), dirty)
        if obj._unique[0] is not None and obj._unique[0] is not obj.__undef__:
            assert isinstance(obj._unique[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unique[0], type(obj._unique[0])))
            common.validate_format(obj._unique[0], "None", None, None)
        obj._shared = (data.get("shared", obj.__undef__), dirty)
        if obj._shared[0] is not None and obj._shared[0] is not obj.__undef__:
            assert isinstance(obj._shared[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._shared[0], type(obj._shared[0])))
            common.validate_format(obj._shared[0], "None", None, None)
        obj._externally_referenced = (data.get("externallyReferenced", obj.__undef__), dirty)
        if obj._externally_referenced[0] is not None and obj._externally_referenced[0] is not obj.__undef__:
            assert isinstance(obj._externally_referenced[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._externally_referenced[0], type(obj._externally_referenced[0])))
            common.validate_format(obj._externally_referenced[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSBookmarkUsageData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "bookmark" == "type" or (self.bookmark is not self.__undef__ and (not (dirty and not self._bookmark[1]))):
            dct["bookmark"] = dictify(self.bookmark)
        if "data_layout" == "type" or (self.data_layout is not self.__undef__ and (not (dirty and not self._data_layout[1]))):
            dct["dataLayout"] = dictify(self.data_layout)
        if "unique" == "type" or (self.unique is not self.__undef__ and (not (dirty and not self._unique[1]))):
            dct["unique"] = dictify(self.unique)
        if "shared" == "type" or (self.shared is not self.__undef__ and (not (dirty and not self._shared[1]))):
            dct["shared"] = dictify(self.shared)
        if "externally_referenced" == "type" or (self.externally_referenced is not self.__undef__ and (not (dirty and not self._externally_referenced[1]))):
            dct["externallyReferenced"] = dictify(self.externally_referenced)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._bookmark = (self._bookmark[0], True)
        self._data_layout = (self._data_layout[0], True)
        self._unique = (self._unique[0], True)
        self._shared = (self._shared[0], True)
        self._externally_referenced = (self._externally_referenced[0], True)

    def is_dirty(self):
        return any([self._bookmark[1], self._data_layout[1], self._unique[1], self._shared[1], self._externally_referenced[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSBookmarkUsageData):
            return False
        return super(JSBookmarkUsageData, self).__eq__(other) and \
               self.bookmark == other.bookmark and \
               self.data_layout == other.data_layout and \
               self.unique == other.unique and \
               self.shared == other.shared and \
               self.externally_referenced == other.externally_referenced

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def bookmark(self):
        """
        The Self-Service bookmark that this usage information is for.

        :rtype: ``TEXT_TYPE``
        """
        return self._bookmark[0]

    @bookmark.setter
    def bookmark(self, value):
        self._bookmark = (value, True)

    @property
    def data_layout(self):
        """
        The data layout that this bookmark belongs to.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_layout[0]

    @data_layout.setter
    def data_layout(self, value):
        self._data_layout = (value, True)

    @property
    def unique(self):
        """
        The amount of space that will be freed if this bookmark is deleted.

        :rtype: ``float``
        """
        return self._unique[0]

    @unique.setter
    def unique(self, value):
        self._unique = (value, True)

    @property
    def shared(self):
        """
        The amount of space referenced by this bookmark that cannot be freed up
        by deleting this bookmark because it is also referenced by neighboring
        bookmarks or branches that have been created or restored from this
        bookmark.

        :rtype: ``float``
        """
        return self._shared[0]

    @shared.setter
    def shared(self, value):
        self._shared = (value, True)

    @property
    def externally_referenced(self):
        """
        The amount of space referenced by this bookmark that cannot be freed up
        by deleting this bookmark because it is also being referenced outside
        of Self-Service (e.g. by retention policy).

        :rtype: ``float``
        """
        return self._externally_referenced[0]

    @externally_referenced.setter
    def externally_referenced(self, value):
        self._externally_referenced = (value, True)

