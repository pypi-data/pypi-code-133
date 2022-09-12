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
#     /delphix-js-bookmark-tag-usage-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_3 import common

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

class JSBookmarkTagUsageData(TypedObject):
    """
    *(extends* :py:class:`v1_11_3.web.vo.TypedObject` *)* The space usage
    information for a Self-Service bookmark tag.
    """
    def __init__(self, undef_enabled=True):
        super(JSBookmarkTagUsageData, self).__init__()
        self._type = ("JSBookmarkTagUsageData", True)
        self._bookmark_tag = (self.__undef__, True)
        self._unique = (self.__undef__, True)
        self._referenced = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(JSBookmarkTagUsageData, cls).from_dict(data, dirty, undef_enabled)
        obj._bookmark_tag = (data.get("bookmarkTag", obj.__undef__), dirty)
        if obj._bookmark_tag[0] is not None and obj._bookmark_tag[0] is not obj.__undef__:
            assert isinstance(obj._bookmark_tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._bookmark_tag[0], type(obj._bookmark_tag[0])))
            common.validate_format(obj._bookmark_tag[0], "None", None, None)
        obj._unique = (data.get("unique", obj.__undef__), dirty)
        if obj._unique[0] is not None and obj._unique[0] is not obj.__undef__:
            assert isinstance(obj._unique[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._unique[0], type(obj._unique[0])))
            common.validate_format(obj._unique[0], "None", None, None)
        obj._referenced = (data.get("referenced", obj.__undef__), dirty)
        if obj._referenced[0] is not None and obj._referenced[0] is not obj.__undef__:
            assert isinstance(obj._referenced[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._referenced[0], type(obj._referenced[0])))
            common.validate_format(obj._referenced[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(JSBookmarkTagUsageData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "bookmark_tag" == "type" or (self.bookmark_tag is not self.__undef__ and (not (dirty and not self._bookmark_tag[1]))):
            dct["bookmarkTag"] = dictify(self.bookmark_tag)
        if "unique" == "type" or (self.unique is not self.__undef__ and (not (dirty and not self._unique[1]))):
            dct["unique"] = dictify(self.unique)
        if "referenced" == "type" or (self.referenced is not self.__undef__ and (not (dirty and not self._referenced[1]))):
            dct["referenced"] = dictify(self.referenced)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._bookmark_tag = (self._bookmark_tag[0], True)
        self._unique = (self._unique[0], True)
        self._referenced = (self._referenced[0], True)

    def is_dirty(self):
        return any([self._bookmark_tag[1], self._unique[1], self._referenced[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, JSBookmarkTagUsageData):
            return False
        return super(JSBookmarkTagUsageData, self).__eq__(other) and \
               self.bookmark_tag == other.bookmark_tag and \
               self.unique == other.unique and \
               self.referenced == other.referenced

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def bookmark_tag(self):
        """
        The amount of space that will be freed if bookmarks with this tag are
        deleted.

        :rtype: ``TEXT_TYPE``
        """
        return self._bookmark_tag[0]

    @bookmark_tag.setter
    def bookmark_tag(self, value):
        self._bookmark_tag = (value, True)

    @property
    def unique(self):
        """
        The space that is being consumed by the set of bookmarks with the given
        tag. This represents the minimum amount of space that will be freed if
        all of the bookmarks are deleted.

        :rtype: ``float``
        """
        return self._unique[0]

    @unique.setter
    def unique(self, value):
        self._unique = (value, True)

    @property
    def referenced(self):
        """
        The total amount of space referenced by bookmarks with this tag. This
        is the sum of the bookmarks' unique, shared, and externallyReferenced
        space.

        :rtype: ``float``
        """
        return self._referenced[0]

    @referenced.setter
    def referenced(self, value):
        self._referenced = (value, True)

