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
#     /delphix-auth-filter-result.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_6_2 import common

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

class AuthFilterResult(TypedObject):
    """
    *(extends* :py:class:`v1_6_2.web.vo.TypedObject` *)* Result of an auth
    filter request.
    """
    def __init__(self, undef_enabled=True):
        super(AuthFilterResult, self).__init__()
        self._type = ("AuthFilterResult", True)
        self._objects = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AuthFilterResult, cls).from_dict(data, dirty, undef_enabled)
        obj._objects = []
        for item in data.get("objects") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._objects.append(item)
        obj._objects = (obj._objects, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AuthFilterResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "objects" == "type" or (self.objects is not self.__undef__ and (not (dirty and not self._objects[1]))):
            dct["objects"] = dictify(self.objects)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._objects = (self._objects[0], True)

    def is_dirty(self):
        return any([self._objects[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AuthFilterResult):
            return False
        return super(AuthFilterResult, self).__eq__(other) and \
               self.objects == other.objects

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def objects(self):
        """
        The list of objects that have been filtered.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._objects[0]

    @objects.setter
    def objects(self, value):
        self._objects = (value, True)

