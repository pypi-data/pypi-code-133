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
#     /delphix-nfs-read-write-sizes.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_4_2.web.objects.TypedObject import TypedObject
from delphixpy.v1_4_2 import common

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

class NfsReadWriteSizes(TypedObject):
    """
    *(extends* :py:class:`v1_4_2.web.vo.TypedObject` *)* NFS read/write sizes
    from target host to Delphix Engine.
    """
    def __init__(self, undef_enabled=True):
        super(NfsReadWriteSizes, self).__init__()
        self._type = ("NfsReadWriteSizes", True)
        self._current_read_size = (self.__undef__, True)
        self._current_write_size = (self.__undef__, True)
        self._max_read_size = (self.__undef__, True)
        self._max_write_size = (self.__undef__, True)

    API_VERSION = "1.4.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NfsReadWriteSizes, cls).from_dict(data, dirty, undef_enabled)
        obj._current_read_size = (data.get("currentReadSize", obj.__undef__), dirty)
        if obj._current_read_size[0] is not None and obj._current_read_size[0] is not obj.__undef__:
            assert isinstance(obj._current_read_size[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._current_read_size[0], type(obj._current_read_size[0])))
            common.validate_format(obj._current_read_size[0], "None", None, None)
        obj._current_write_size = (data.get("currentWriteSize", obj.__undef__), dirty)
        if obj._current_write_size[0] is not None and obj._current_write_size[0] is not obj.__undef__:
            assert isinstance(obj._current_write_size[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._current_write_size[0], type(obj._current_write_size[0])))
            common.validate_format(obj._current_write_size[0], "None", None, None)
        obj._max_read_size = (data.get("maxReadSize", obj.__undef__), dirty)
        if obj._max_read_size[0] is not None and obj._max_read_size[0] is not obj.__undef__:
            assert isinstance(obj._max_read_size[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._max_read_size[0], type(obj._max_read_size[0])))
            common.validate_format(obj._max_read_size[0], "None", None, None)
        obj._max_write_size = (data.get("maxWriteSize", obj.__undef__), dirty)
        if obj._max_write_size[0] is not None and obj._max_write_size[0] is not obj.__undef__:
            assert isinstance(obj._max_write_size[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._max_write_size[0], type(obj._max_write_size[0])))
            common.validate_format(obj._max_write_size[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NfsReadWriteSizes, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "current_read_size" == "type" or (self.current_read_size is not self.__undef__ and (not (dirty and not self._current_read_size[1]))):
            dct["currentReadSize"] = dictify(self.current_read_size)
        if "current_write_size" == "type" or (self.current_write_size is not self.__undef__ and (not (dirty and not self._current_write_size[1]))):
            dct["currentWriteSize"] = dictify(self.current_write_size)
        if "max_read_size" == "type" or (self.max_read_size is not self.__undef__ and (not (dirty and not self._max_read_size[1]))):
            dct["maxReadSize"] = dictify(self.max_read_size)
        if "max_write_size" == "type" or (self.max_write_size is not self.__undef__ and (not (dirty and not self._max_write_size[1]))):
            dct["maxWriteSize"] = dictify(self.max_write_size)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._current_read_size = (self._current_read_size[0], True)
        self._current_write_size = (self._current_write_size[0], True)
        self._max_read_size = (self._max_read_size[0], True)
        self._max_write_size = (self._max_write_size[0], True)

    def is_dirty(self):
        return any([self._current_read_size[1], self._current_write_size[1], self._max_read_size[1], self._max_write_size[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NfsReadWriteSizes):
            return False
        return super(NfsReadWriteSizes, self).__eq__(other) and \
               self.current_read_size == other.current_read_size and \
               self.current_write_size == other.current_write_size and \
               self.max_read_size == other.max_read_size and \
               self.max_write_size == other.max_write_size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def current_read_size(self):
        """
        NFS current read size.

        :rtype: ``TEXT_TYPE``
        """
        return self._current_read_size[0]

    @current_read_size.setter
    def current_read_size(self, value):
        self._current_read_size = (value, True)

    @property
    def current_write_size(self):
        """
        NFS current write size.

        :rtype: ``TEXT_TYPE``
        """
        return self._current_write_size[0]

    @current_write_size.setter
    def current_write_size(self, value):
        self._current_write_size = (value, True)

    @property
    def max_read_size(self):
        """
        Maximum NFS read size.

        :rtype: ``TEXT_TYPE``
        """
        return self._max_read_size[0]

    @max_read_size.setter
    def max_read_size(self, value):
        self._max_read_size = (value, True)

    @property
    def max_write_size(self):
        """
        Maximum NFS write size.

        :rtype: ``TEXT_TYPE``
        """
        return self._max_write_size[0]

    @max_write_size.setter
    def max_write_size(self, value):
        self._max_write_size = (value, True)

