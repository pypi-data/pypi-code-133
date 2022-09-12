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
#     /delphix-auth-filter-parameters.json
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

class AuthFilterParameters(TypedObject):
    """
    *(extends* :py:class:`v1_11_3.web.vo.TypedObject` *)* The parameters to use
    as input to filter a list of objects or object type by a permission.
    """
    def __init__(self, undef_enabled=True):
        super(AuthFilterParameters, self).__init__()
        self._type = ("AuthFilterParameters", True)
        self._permission = (self.__undef__, True)
        self._objects = (self.__undef__, True)
        self._object_type = (self.__undef__, True)

    API_VERSION = "1.11.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(AuthFilterParameters, cls).from_dict(data, dirty, undef_enabled)
        if "permission" not in data:
            raise ValueError("Missing required property \"permission\".")
        obj._permission = (data.get("permission", obj.__undef__), dirty)
        if obj._permission[0] is not None and obj._permission[0] is not obj.__undef__:
            assert isinstance(obj._permission[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._permission[0], type(obj._permission[0])))
            common.validate_format(obj._permission[0], "objectReference", None, None)
        obj._objects = []
        for item in data.get("objects") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._objects.append(item)
        obj._objects = (obj._objects, dirty)
        obj._object_type = (data.get("objectType", obj.__undef__), dirty)
        if obj._object_type[0] is not None and obj._object_type[0] is not obj.__undef__:
            assert isinstance(obj._object_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._object_type[0], type(obj._object_type[0])))
            common.validate_format(obj._object_type[0], "type", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(AuthFilterParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "permission" == "type" or (self.permission is not self.__undef__ and (not (dirty and not self._permission[1]) or isinstance(self.permission, list) or belongs_to_parent)):
            dct["permission"] = dictify(self.permission)
        if "objects" == "type" or (self.objects is not self.__undef__ and (not (dirty and not self._objects[1]))):
            dct["objects"] = dictify(self.objects)
        if "object_type" == "type" or (self.object_type is not self.__undef__ and (not (dirty and not self._object_type[1]))):
            dct["objectType"] = dictify(self.object_type)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._permission = (self._permission[0], True)
        self._objects = (self._objects[0], True)
        self._object_type = (self._object_type[0], True)

    def is_dirty(self):
        return any([self._permission[1], self._objects[1], self._object_type[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, AuthFilterParameters):
            return False
        return super(AuthFilterParameters, self).__eq__(other) and \
               self.permission == other.permission and \
               self.objects == other.objects and \
               self.object_type == other.object_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def permission(self):
        """
        The permission to filter by.

        :rtype: ``TEXT_TYPE``
        """
        return self._permission[0]

    @permission.setter
    def permission(self, value):
        self._permission = (value, True)

    @property
    def objects(self):
        """
        The list of objects to filter. This option is mutually exclusive with
        the "objectType" field.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._objects[0]

    @objects.setter
    def objects(self, value):
        self._objects = (value, True)

    @property
    def object_type(self):
        """
        The object type on which to perform filtering. This option is mutually
        exclusive with the "objects" field.

        :rtype: ``TEXT_TYPE``
        """
        return self._object_type[0]

    @object_type.setter
    def object_type(self, value):
        self._object_type = (value, True)

