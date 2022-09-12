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
#     /delphix-serialization-point.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.UserObject import UserObject
from delphixpy.v1_11_15 import common

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

class SerializationPoint(UserObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.UserObject` *)* A serialization point
    represents the data and metadata associated with a replication spec at a
    point in time.
    """
    def __init__(self, undef_enabled=True):
        super(SerializationPoint, self).__init__()
        self._type = ("SerializationPoint", True)
        self._data_timestamp = (self.__undef__, True)
        self._bytes_transferred = (self.__undef__, True)
        self._average_throughput = (self.__undef__, True)
        self._elapsed_time_nanos = (self.__undef__, True)
        self._tag = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SerializationPoint, cls).from_dict(data, dirty, undef_enabled)
        obj._data_timestamp = (data.get("dataTimestamp", obj.__undef__), dirty)
        if obj._data_timestamp[0] is not None and obj._data_timestamp[0] is not obj.__undef__:
            assert isinstance(obj._data_timestamp[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._data_timestamp[0], type(obj._data_timestamp[0])))
            common.validate_format(obj._data_timestamp[0], "date", None, None)
        obj._bytes_transferred = (data.get("bytesTransferred", obj.__undef__), dirty)
        if obj._bytes_transferred[0] is not None and obj._bytes_transferred[0] is not obj.__undef__:
            assert isinstance(obj._bytes_transferred[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._bytes_transferred[0], type(obj._bytes_transferred[0])))
            common.validate_format(obj._bytes_transferred[0], "None", None, None)
        obj._average_throughput = (data.get("averageThroughput", obj.__undef__), dirty)
        if obj._average_throughput[0] is not None and obj._average_throughput[0] is not obj.__undef__:
            assert isinstance(obj._average_throughput[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._average_throughput[0], type(obj._average_throughput[0])))
            common.validate_format(obj._average_throughput[0], "None", None, None)
        obj._elapsed_time_nanos = (data.get("elapsedTimeNanos", obj.__undef__), dirty)
        if obj._elapsed_time_nanos[0] is not None and obj._elapsed_time_nanos[0] is not obj.__undef__:
            assert isinstance(obj._elapsed_time_nanos[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._elapsed_time_nanos[0], type(obj._elapsed_time_nanos[0])))
            common.validate_format(obj._elapsed_time_nanos[0], "None", None, None)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SerializationPoint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "data_timestamp" == "type" or (self.data_timestamp is not self.__undef__ and (not (dirty and not self._data_timestamp[1]))):
            dct["dataTimestamp"] = dictify(self.data_timestamp)
        if "bytes_transferred" == "type" or (self.bytes_transferred is not self.__undef__ and (not (dirty and not self._bytes_transferred[1]))):
            dct["bytesTransferred"] = dictify(self.bytes_transferred)
        if "average_throughput" == "type" or (self.average_throughput is not self.__undef__ and (not (dirty and not self._average_throughput[1]))):
            dct["averageThroughput"] = dictify(self.average_throughput)
        if "elapsed_time_nanos" == "type" or (self.elapsed_time_nanos is not self.__undef__ and (not (dirty and not self._elapsed_time_nanos[1]))):
            dct["elapsedTimeNanos"] = dictify(self.elapsed_time_nanos)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]))):
            dct["tag"] = dictify(self.tag)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._data_timestamp = (self._data_timestamp[0], True)
        self._bytes_transferred = (self._bytes_transferred[0], True)
        self._average_throughput = (self._average_throughput[0], True)
        self._elapsed_time_nanos = (self._elapsed_time_nanos[0], True)
        self._tag = (self._tag[0], True)

    def is_dirty(self):
        return any([self._data_timestamp[1], self._bytes_transferred[1], self._average_throughput[1], self._elapsed_time_nanos[1], self._tag[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SerializationPoint):
            return False
        return super(SerializationPoint, self).__eq__(other) and \
               self.data_timestamp == other.data_timestamp and \
               self.bytes_transferred == other.bytes_transferred and \
               self.average_throughput == other.average_throughput and \
               self.elapsed_time_nanos == other.elapsed_time_nanos and \
               self.tag == other.tag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def data_timestamp(self):
        """
        Timestamp of the data being stored in the serialization point.

        :rtype: ``TEXT_TYPE``
        """
        return self._data_timestamp[0]

    @data_timestamp.setter
    def data_timestamp(self, value):
        self._data_timestamp = (value, True)

    @property
    def bytes_transferred(self):
        """
        Bytes of the serialization point which have been transferred.

        :rtype: ``int``
        """
        return self._bytes_transferred[0]

    @bytes_transferred.setter
    def bytes_transferred(self, value):
        self._bytes_transferred = (value, True)

    @property
    def average_throughput(self):
        """
        Average throughput of the transfer of the serialization point
        (bytes/s).

        :rtype: ``float``
        """
        return self._average_throughput[0]

    @average_throughput.setter
    def average_throughput(self, value):
        self._average_throughput = (value, True)

    @property
    def elapsed_time_nanos(self):
        """
        The elapsed time spent sending the serialization point (nanoseconds).

        :rtype: ``float``
        """
        return self._elapsed_time_nanos[0]

    @elapsed_time_nanos.setter
    def elapsed_time_nanos(self, value):
        self._elapsed_time_nanos = (value, True)

    @property
    def tag(self):
        """
        An arbitrary string used to map the serialization point to a
        corresponding replication spec or namespace.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

