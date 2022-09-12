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
#     /delphix-object-store.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_12.web.objects.TypedObject import TypedObject
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

class ObjectStore(TypedObject):
    """
    *(extends* :py:class:`v1_11_12.web.vo.TypedObject` *)* An object store.
    """
    def __init__(self, undef_enabled=True):
        super(ObjectStore, self).__init__()
        self._type = ("ObjectStore", True)
        self._size = (self.__undef__, True)
        self._cache_devices = (self.__undef__, True)

    API_VERSION = "1.11.12"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ObjectStore, cls).from_dict(data, dirty, undef_enabled)
        obj._size = (data.get("size", obj.__undef__), dirty)
        if obj._size[0] is not None and obj._size[0] is not obj.__undef__:
            assert isinstance(obj._size[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._size[0], type(obj._size[0])))
            common.validate_format(obj._size[0], "None", None, None)
        obj._cache_devices = []
        for item in data.get("cacheDevices") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._cache_devices.append(item)
        obj._cache_devices = (obj._cache_devices, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ObjectStore, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "size" == "type" or (self.size is not self.__undef__ and (not (dirty and not self._size[1]) or isinstance(self.size, list) or belongs_to_parent)):
            dct["size"] = dictify(self.size)
        if "cache_devices" == "type" or (self.cache_devices is not self.__undef__ and (not (dirty and not self._cache_devices[1]) or isinstance(self.cache_devices, list) or belongs_to_parent)):
            dct["cacheDevices"] = dictify(self.cache_devices, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._size = (self._size[0], True)
        self._cache_devices = (self._cache_devices[0], True)

    def is_dirty(self):
        return any([self._size[1], self._cache_devices[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ObjectStore):
            return False
        return super(ObjectStore, self).__eq__(other) and \
               self.size == other.size and \
               self.cache_devices == other.cache_devices

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def size(self):
        """
        Physical size of the object store, in bytes.

        :rtype: ``float``
        """
        return self._size[0]

    @size.setter
    def size(self, value):
        self._size = (value, True)

    @property
    def cache_devices(self):
        """
        List of storage devices to use.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._cache_devices[0]

    @cache_devices.setter
    def cache_devices(self, value):
        self._cache_devices = (value, True)

