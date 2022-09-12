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
#     /delphix-storage-device.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.NamedUserObject import NamedUserObject
from delphixpy.v1_11_13 import common

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

class StorageDevice(NamedUserObject):
    """
    *(extends* :py:class:`v1_11_13.web.vo.NamedUserObject` *)* A storage device
    on the system.
    """
    def __init__(self, undef_enabled=True):
        super(StorageDevice, self).__init__()
        self._type = ("StorageDevice", True)
        self._size = (self.__undef__, True)
        self._serial = (self.__undef__, True)
        self._vendor = (self.__undef__, True)
        self._model = (self.__undef__, True)
        self._configured = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(StorageDevice, cls).from_dict(data, dirty, undef_enabled)
        obj._size = (data.get("size", obj.__undef__), dirty)
        if obj._size[0] is not None and obj._size[0] is not obj.__undef__:
            assert isinstance(obj._size[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._size[0], type(obj._size[0])))
            common.validate_format(obj._size[0], "None", None, None)
        obj._serial = (data.get("serial", obj.__undef__), dirty)
        if obj._serial[0] is not None and obj._serial[0] is not obj.__undef__:
            assert isinstance(obj._serial[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._serial[0], type(obj._serial[0])))
            common.validate_format(obj._serial[0], "None", None, None)
        obj._vendor = (data.get("vendor", obj.__undef__), dirty)
        if obj._vendor[0] is not None and obj._vendor[0] is not obj.__undef__:
            assert isinstance(obj._vendor[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._vendor[0], type(obj._vendor[0])))
            common.validate_format(obj._vendor[0], "None", None, None)
        obj._model = (data.get("model", obj.__undef__), dirty)
        if obj._model[0] is not None and obj._model[0] is not obj.__undef__:
            assert isinstance(obj._model[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._model[0], type(obj._model[0])))
            common.validate_format(obj._model[0], "None", None, None)
        obj._configured = (data.get("configured", obj.__undef__), dirty)
        if obj._configured[0] is not None and obj._configured[0] is not obj.__undef__:
            assert isinstance(obj._configured[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._configured[0], type(obj._configured[0])))
            common.validate_format(obj._configured[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(StorageDevice, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "size" == "type" or (self.size is not self.__undef__ and (not (dirty and not self._size[1]))):
            dct["size"] = dictify(self.size)
        if "serial" == "type" or (self.serial is not self.__undef__ and (not (dirty and not self._serial[1]))):
            dct["serial"] = dictify(self.serial)
        if "vendor" == "type" or (self.vendor is not self.__undef__ and (not (dirty and not self._vendor[1]))):
            dct["vendor"] = dictify(self.vendor)
        if "model" == "type" or (self.model is not self.__undef__ and (not (dirty and not self._model[1]))):
            dct["model"] = dictify(self.model)
        if "configured" == "type" or (self.configured is not self.__undef__ and (not (dirty and not self._configured[1]))):
            dct["configured"] = dictify(self.configured)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._size = (self._size[0], True)
        self._serial = (self._serial[0], True)
        self._vendor = (self._vendor[0], True)
        self._model = (self._model[0], True)
        self._configured = (self._configured[0], True)

    def is_dirty(self):
        return any([self._size[1], self._serial[1], self._vendor[1], self._model[1], self._configured[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, StorageDevice):
            return False
        return super(StorageDevice, self).__eq__(other) and \
               self.size == other.size and \
               self.serial == other.serial and \
               self.vendor == other.vendor and \
               self.model == other.model and \
               self.configured == other.configured

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def size(self):
        """
        Physical size of the device, in bytes.

        :rtype: ``float``
        """
        return self._size[0]

    @size.setter
    def size(self, value):
        self._size = (value, True)

    @property
    def serial(self):
        """
        Serial number of the device.

        :rtype: ``TEXT_TYPE``
        """
        return self._serial[0]

    @serial.setter
    def serial(self, value):
        self._serial = (value, True)

    @property
    def vendor(self):
        """
        Vendor ID of the device.

        :rtype: ``TEXT_TYPE``
        """
        return self._vendor[0]

    @vendor.setter
    def vendor(self, value):
        self._vendor = (value, True)

    @property
    def model(self):
        """
        Model ID of the device.

        :rtype: ``TEXT_TYPE``
        """
        return self._model[0]

    @model.setter
    def model(self, value):
        self._model = (value, True)

    @property
    def configured(self):
        """
        True if the device is currently configured in the system.

        :rtype: ``bool``
        """
        return self._configured[0]

    @configured.setter
    def configured(self, value):
        self._configured = (value, True)

