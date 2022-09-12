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
#     /delphix-typed-object.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7 import common

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

class TypedObject(object):
    """
    Super schema for all other schemas.
    """
    def __init__(self, undef_enabled=True):
        self.__undef__ = _UNDEFINED if undef_enabled else None
        self._type = ("TypedObject", True)
        self._type = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = cls()
        obj.__undef__ = _UNDEFINED if undef_enabled else None
        if "type" not in data:
            raise ValueError("Missing required property \"type\".")
        obj._type = (data.get("type", obj.__undef__), dirty)
        if obj._type[0] is not None and obj._type[0] is not obj.__undef__:
            assert isinstance(obj._type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._type[0], type(obj._type[0])))
            common.validate_format(obj._type[0], "type", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = {}

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "type" == "type" or (self.type is not self.__undef__ and (not (dirty and not self._type[1]) or isinstance(self.type, list) or belongs_to_parent)):
            dct["type"] = dictify(self.type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._type = (self._type[0], True)

    def is_dirty(self):
        return any([self._type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TypedObject):
            return False
        return self.type == other.type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def type(self):
        """
        Object type.

        :rtype: ``TEXT_TYPE``
        """
        return self._type[0]

    @type.setter
    def type(self, value):
        self._type = (value, True)

