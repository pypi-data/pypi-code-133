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
#     /delphix-storage-device-removal-verify-result.json
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

class StorageDeviceRemovalVerifyResult(TypedObject):
    """
    *(extends* :py:class:`v1_6_2.web.vo.TypedObject` *)* The .
    """
    def __init__(self, undef_enabled=True):
        super(StorageDeviceRemovalVerifyResult, self).__init__()
        self._type = ("StorageDeviceRemovalVerifyResult", True)
        self._new_free_bytes = (self.__undef__, True)
        self._new_mapping_memory = (self.__undef__, True)
        self._old_free_bytes = (self.__undef__, True)
        self._old_mapping_memory = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(StorageDeviceRemovalVerifyResult, cls).from_dict(data, dirty, undef_enabled)
        obj._new_free_bytes = (data.get("newFreeBytes", obj.__undef__), dirty)
        if obj._new_free_bytes[0] is not None and obj._new_free_bytes[0] is not obj.__undef__:
            assert isinstance(obj._new_free_bytes[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._new_free_bytes[0], type(obj._new_free_bytes[0])))
            common.validate_format(obj._new_free_bytes[0], "None", None, None)
        obj._new_mapping_memory = (data.get("newMappingMemory", obj.__undef__), dirty)
        if obj._new_mapping_memory[0] is not None and obj._new_mapping_memory[0] is not obj.__undef__:
            assert isinstance(obj._new_mapping_memory[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._new_mapping_memory[0], type(obj._new_mapping_memory[0])))
            common.validate_format(obj._new_mapping_memory[0], "None", None, None)
        obj._old_free_bytes = (data.get("oldFreeBytes", obj.__undef__), dirty)
        if obj._old_free_bytes[0] is not None and obj._old_free_bytes[0] is not obj.__undef__:
            assert isinstance(obj._old_free_bytes[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._old_free_bytes[0], type(obj._old_free_bytes[0])))
            common.validate_format(obj._old_free_bytes[0], "None", None, None)
        obj._old_mapping_memory = (data.get("oldMappingMemory", obj.__undef__), dirty)
        if obj._old_mapping_memory[0] is not None and obj._old_mapping_memory[0] is not obj.__undef__:
            assert isinstance(obj._old_mapping_memory[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._old_mapping_memory[0], type(obj._old_mapping_memory[0])))
            common.validate_format(obj._old_mapping_memory[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(StorageDeviceRemovalVerifyResult, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "new_free_bytes" == "type" or (self.new_free_bytes is not self.__undef__ and (not (dirty and not self._new_free_bytes[1]))):
            dct["newFreeBytes"] = dictify(self.new_free_bytes)
        if "new_mapping_memory" == "type" or (self.new_mapping_memory is not self.__undef__ and (not (dirty and not self._new_mapping_memory[1]))):
            dct["newMappingMemory"] = dictify(self.new_mapping_memory)
        if "old_free_bytes" == "type" or (self.old_free_bytes is not self.__undef__ and (not (dirty and not self._old_free_bytes[1]))):
            dct["oldFreeBytes"] = dictify(self.old_free_bytes)
        if "old_mapping_memory" == "type" or (self.old_mapping_memory is not self.__undef__ and (not (dirty and not self._old_mapping_memory[1]))):
            dct["oldMappingMemory"] = dictify(self.old_mapping_memory)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._new_free_bytes = (self._new_free_bytes[0], True)
        self._new_mapping_memory = (self._new_mapping_memory[0], True)
        self._old_free_bytes = (self._old_free_bytes[0], True)
        self._old_mapping_memory = (self._old_mapping_memory[0], True)

    def is_dirty(self):
        return any([self._new_free_bytes[1], self._new_mapping_memory[1], self._old_free_bytes[1], self._old_mapping_memory[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, StorageDeviceRemovalVerifyResult):
            return False
        return super(StorageDeviceRemovalVerifyResult, self).__eq__(other) and \
               self.new_free_bytes == other.new_free_bytes and \
               self.new_mapping_memory == other.new_mapping_memory and \
               self.old_free_bytes == other.old_free_bytes and \
               self.old_mapping_memory == other.old_mapping_memory

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def new_free_bytes(self):
        """
        Free space of the pool if this device is removed, in bytes.

        :rtype: ``float``
        """
        return self._new_free_bytes[0]

    @new_free_bytes.setter
    def new_free_bytes(self, value):
        self._new_free_bytes = (value, True)

    @property
    def new_mapping_memory(self):
        """
        Amount of memory to be used by mappings if this device is removed, in
        bytes.

        :rtype: ``float``
        """
        return self._new_mapping_memory[0]

    @new_mapping_memory.setter
    def new_mapping_memory(self, value):
        self._new_mapping_memory = (value, True)

    @property
    def old_free_bytes(self):
        """
        Free space of the pool before this device is removed, in bytes.

        :rtype: ``float``
        """
        return self._old_free_bytes[0]

    @old_free_bytes.setter
    def old_free_bytes(self, value):
        self._old_free_bytes = (value, True)

    @property
    def old_mapping_memory(self):
        """
        Amount of memory used by removal mappings before this device is
        removed, in bytes.

        :rtype: ``float``
        """
        return self._old_mapping_memory[0]

    @old_mapping_memory.setter
    def old_mapping_memory(self, value):
        self._old_mapping_memory = (value, True)

