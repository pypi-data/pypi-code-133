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
#     /delphix-storage-device-initialize-status.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_9_2 import common

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

class StorageDeviceInitializeStatus(TypedObject):
    """
    *(extends* :py:class:`v1_9_2.web.vo.TypedObject` *)* The status of an
    initialize operation of a storage device in the system.
    """
    def __init__(self, undef_enabled=True):
        super(StorageDeviceInitializeStatus, self).__init__()
        self._type = ("StorageDeviceInitializeStatus", True)
        self._state = (self.__undef__, True)
        self._bytes_done = (self.__undef__, True)
        self._bytes_est = (self.__undef__, True)

    API_VERSION = "1.9.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(StorageDeviceInitializeStatus, cls).from_dict(data, dirty, undef_enabled)
        obj._state = (data.get("state", obj.__undef__), dirty)
        if obj._state[0] is not None and obj._state[0] is not obj.__undef__:
            assert isinstance(obj._state[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._state[0], type(obj._state[0])))
            assert obj._state[0] in ['NONE', 'ACTIVE', 'CANCELED', 'SUSPENDED', 'COMPLETED'], "Expected enum ['NONE', 'ACTIVE', 'CANCELED', 'SUSPENDED', 'COMPLETED'] but got %s" % obj._state[0]
            common.validate_format(obj._state[0], "None", None, None)
        obj._bytes_done = (data.get("bytesDone", obj.__undef__), dirty)
        if obj._bytes_done[0] is not None and obj._bytes_done[0] is not obj.__undef__:
            assert isinstance(obj._bytes_done[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._bytes_done[0], type(obj._bytes_done[0])))
            common.validate_format(obj._bytes_done[0], "None", None, None)
        obj._bytes_est = (data.get("bytesEst", obj.__undef__), dirty)
        if obj._bytes_est[0] is not None and obj._bytes_est[0] is not obj.__undef__:
            assert isinstance(obj._bytes_est[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._bytes_est[0], type(obj._bytes_est[0])))
            common.validate_format(obj._bytes_est[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(StorageDeviceInitializeStatus, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "state" == "type" or (self.state is not self.__undef__ and (not (dirty and not self._state[1]))):
            dct["state"] = dictify(self.state)
        if "bytes_done" == "type" or (self.bytes_done is not self.__undef__ and (not (dirty and not self._bytes_done[1]))):
            dct["bytesDone"] = dictify(self.bytes_done)
        if "bytes_est" == "type" or (self.bytes_est is not self.__undef__ and (not (dirty and not self._bytes_est[1]))):
            dct["bytesEst"] = dictify(self.bytes_est)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._state = (self._state[0], True)
        self._bytes_done = (self._bytes_done[0], True)
        self._bytes_est = (self._bytes_est[0], True)

    def is_dirty(self):
        return any([self._state[1], self._bytes_done[1], self._bytes_est[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, StorageDeviceInitializeStatus):
            return False
        return super(StorageDeviceInitializeStatus, self).__eq__(other) and \
               self.state == other.state and \
               self.bytes_done == other.bytes_done and \
               self.bytes_est == other.bytes_est

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def state(self):
        """
        Initialization state. *(permitted values: NONE, ACTIVE, CANCELED,
        SUSPENDED, COMPLETED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._state[0]

    @state.setter
    def state(self, value):
        self._state = (value, True)

    @property
    def bytes_done(self):
        """
        Amount of data initialized, in bytes.

        :rtype: ``float``
        """
        return self._bytes_done[0]

    @bytes_done.setter
    def bytes_done(self, value):
        self._bytes_done = (value, True)

    @property
    def bytes_est(self):
        """
        Total amount of data to initialize (including data already
        initialized), in bytes.

        :rtype: ``float``
        """
        return self._bytes_est[0]

    @bytes_est.setter
    def bytes_est(self, value):
        self._bytes_est = (value, True)

