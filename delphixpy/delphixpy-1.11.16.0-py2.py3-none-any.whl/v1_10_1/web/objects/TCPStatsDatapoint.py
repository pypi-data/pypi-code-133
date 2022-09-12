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
#     /delphix-analytics-tcp-stats-datapoint.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_1.web.objects.Datapoint import Datapoint
from delphixpy.v1_10_1 import common

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

class TCPStatsDatapoint(Datapoint):
    """
    *(extends* :py:class:`v1_10_1.web.vo.Datapoint` *)* An analytics datapoint
    generated by the TCP_STATS statistic type.
    """
    def __init__(self, undef_enabled=True):
        super(TCPStatsDatapoint, self).__init__()
        self._type = ("TCPStatsDatapoint", True)
        self._in_bytes = (self.__undef__, True)
        self._in_unordered_bytes = (self.__undef__, True)
        self._out_bytes = (self.__undef__, True)
        self._retransmitted_bytes = (self.__undef__, True)
        self._unacknowledged_bytes = (self.__undef__, True)
        self._unsent_bytes = (self.__undef__, True)
        self._send_window_size = (self.__undef__, True)
        self._congestion_window_size = (self.__undef__, True)
        self._receive_window_size = (self.__undef__, True)
        self._round_trip_time = (self.__undef__, True)

    API_VERSION = "1.10.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(TCPStatsDatapoint, cls).from_dict(data, dirty, undef_enabled)
        obj._in_bytes = (data.get("inBytes", obj.__undef__), dirty)
        if obj._in_bytes[0] is not None and obj._in_bytes[0] is not obj.__undef__:
            assert isinstance(obj._in_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._in_bytes[0], type(obj._in_bytes[0])))
            common.validate_format(obj._in_bytes[0], "None", None, None)
        obj._in_unordered_bytes = (data.get("inUnorderedBytes", obj.__undef__), dirty)
        if obj._in_unordered_bytes[0] is not None and obj._in_unordered_bytes[0] is not obj.__undef__:
            assert isinstance(obj._in_unordered_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._in_unordered_bytes[0], type(obj._in_unordered_bytes[0])))
            common.validate_format(obj._in_unordered_bytes[0], "None", None, None)
        obj._out_bytes = (data.get("outBytes", obj.__undef__), dirty)
        if obj._out_bytes[0] is not None and obj._out_bytes[0] is not obj.__undef__:
            assert isinstance(obj._out_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._out_bytes[0], type(obj._out_bytes[0])))
            common.validate_format(obj._out_bytes[0], "None", None, None)
        obj._retransmitted_bytes = (data.get("retransmittedBytes", obj.__undef__), dirty)
        if obj._retransmitted_bytes[0] is not None and obj._retransmitted_bytes[0] is not obj.__undef__:
            assert isinstance(obj._retransmitted_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._retransmitted_bytes[0], type(obj._retransmitted_bytes[0])))
            common.validate_format(obj._retransmitted_bytes[0], "None", None, None)
        obj._unacknowledged_bytes = (data.get("unacknowledgedBytes", obj.__undef__), dirty)
        if obj._unacknowledged_bytes[0] is not None and obj._unacknowledged_bytes[0] is not obj.__undef__:
            assert isinstance(obj._unacknowledged_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._unacknowledged_bytes[0], type(obj._unacknowledged_bytes[0])))
            common.validate_format(obj._unacknowledged_bytes[0], "None", None, None)
        obj._unsent_bytes = (data.get("unsentBytes", obj.__undef__), dirty)
        if obj._unsent_bytes[0] is not None and obj._unsent_bytes[0] is not obj.__undef__:
            assert isinstance(obj._unsent_bytes[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._unsent_bytes[0], type(obj._unsent_bytes[0])))
            common.validate_format(obj._unsent_bytes[0], "None", None, None)
        obj._send_window_size = (data.get("sendWindowSize", obj.__undef__), dirty)
        if obj._send_window_size[0] is not None and obj._send_window_size[0] is not obj.__undef__:
            assert isinstance(obj._send_window_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._send_window_size[0], type(obj._send_window_size[0])))
            common.validate_format(obj._send_window_size[0], "None", None, None)
        obj._congestion_window_size = (data.get("congestionWindowSize", obj.__undef__), dirty)
        if obj._congestion_window_size[0] is not None and obj._congestion_window_size[0] is not obj.__undef__:
            assert isinstance(obj._congestion_window_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._congestion_window_size[0], type(obj._congestion_window_size[0])))
            common.validate_format(obj._congestion_window_size[0], "None", None, None)
        obj._receive_window_size = (data.get("receiveWindowSize", obj.__undef__), dirty)
        if obj._receive_window_size[0] is not None and obj._receive_window_size[0] is not obj.__undef__:
            assert isinstance(obj._receive_window_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._receive_window_size[0], type(obj._receive_window_size[0])))
            common.validate_format(obj._receive_window_size[0], "None", None, None)
        obj._round_trip_time = (data.get("roundTripTime", obj.__undef__), dirty)
        if obj._round_trip_time[0] is not None and obj._round_trip_time[0] is not obj.__undef__:
            assert isinstance(obj._round_trip_time[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._round_trip_time[0], type(obj._round_trip_time[0])))
            common.validate_format(obj._round_trip_time[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(TCPStatsDatapoint, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "in_bytes" == "type" or (self.in_bytes is not self.__undef__ and (not (dirty and not self._in_bytes[1]))):
            dct["inBytes"] = dictify(self.in_bytes)
        if "in_unordered_bytes" == "type" or (self.in_unordered_bytes is not self.__undef__ and (not (dirty and not self._in_unordered_bytes[1]))):
            dct["inUnorderedBytes"] = dictify(self.in_unordered_bytes)
        if "out_bytes" == "type" or (self.out_bytes is not self.__undef__ and (not (dirty and not self._out_bytes[1]))):
            dct["outBytes"] = dictify(self.out_bytes)
        if "retransmitted_bytes" == "type" or (self.retransmitted_bytes is not self.__undef__ and (not (dirty and not self._retransmitted_bytes[1]))):
            dct["retransmittedBytes"] = dictify(self.retransmitted_bytes)
        if "unacknowledged_bytes" == "type" or (self.unacknowledged_bytes is not self.__undef__ and (not (dirty and not self._unacknowledged_bytes[1]))):
            dct["unacknowledgedBytes"] = dictify(self.unacknowledged_bytes)
        if "unsent_bytes" == "type" or (self.unsent_bytes is not self.__undef__ and (not (dirty and not self._unsent_bytes[1]))):
            dct["unsentBytes"] = dictify(self.unsent_bytes)
        if "send_window_size" == "type" or (self.send_window_size is not self.__undef__ and (not (dirty and not self._send_window_size[1]))):
            dct["sendWindowSize"] = dictify(self.send_window_size)
        if "congestion_window_size" == "type" or (self.congestion_window_size is not self.__undef__ and (not (dirty and not self._congestion_window_size[1]))):
            dct["congestionWindowSize"] = dictify(self.congestion_window_size)
        if "receive_window_size" == "type" or (self.receive_window_size is not self.__undef__ and (not (dirty and not self._receive_window_size[1]))):
            dct["receiveWindowSize"] = dictify(self.receive_window_size)
        if "round_trip_time" == "type" or (self.round_trip_time is not self.__undef__ and (not (dirty and not self._round_trip_time[1]))):
            dct["roundTripTime"] = dictify(self.round_trip_time)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._in_bytes = (self._in_bytes[0], True)
        self._in_unordered_bytes = (self._in_unordered_bytes[0], True)
        self._out_bytes = (self._out_bytes[0], True)
        self._retransmitted_bytes = (self._retransmitted_bytes[0], True)
        self._unacknowledged_bytes = (self._unacknowledged_bytes[0], True)
        self._unsent_bytes = (self._unsent_bytes[0], True)
        self._send_window_size = (self._send_window_size[0], True)
        self._congestion_window_size = (self._congestion_window_size[0], True)
        self._receive_window_size = (self._receive_window_size[0], True)
        self._round_trip_time = (self._round_trip_time[0], True)

    def is_dirty(self):
        return any([self._in_bytes[1], self._in_unordered_bytes[1], self._out_bytes[1], self._retransmitted_bytes[1], self._unacknowledged_bytes[1], self._unsent_bytes[1], self._send_window_size[1], self._congestion_window_size[1], self._receive_window_size[1], self._round_trip_time[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, TCPStatsDatapoint):
            return False
        return super(TCPStatsDatapoint, self).__eq__(other) and \
               self.in_bytes == other.in_bytes and \
               self.in_unordered_bytes == other.in_unordered_bytes and \
               self.out_bytes == other.out_bytes and \
               self.retransmitted_bytes == other.retransmitted_bytes and \
               self.unacknowledged_bytes == other.unacknowledged_bytes and \
               self.unsent_bytes == other.unsent_bytes and \
               self.send_window_size == other.send_window_size and \
               self.congestion_window_size == other.congestion_window_size and \
               self.receive_window_size == other.receive_window_size and \
               self.round_trip_time == other.round_trip_time

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def in_bytes(self):
        """
        Data bytes received.

        :rtype: ``int``
        """
        return self._in_bytes[0]

    @in_bytes.setter
    def in_bytes(self, value):
        self._in_bytes = (value, True)

    @property
    def in_unordered_bytes(self):
        """
        Number of bytes received out of order. This is a subset of the
        'inBytes' value.

        :rtype: ``int``
        """
        return self._in_unordered_bytes[0]

    @in_unordered_bytes.setter
    def in_unordered_bytes(self, value):
        self._in_unordered_bytes = (value, True)

    @property
    def out_bytes(self):
        """
        Data bytes transmitted.

        :rtype: ``int``
        """
        return self._out_bytes[0]

    @out_bytes.setter
    def out_bytes(self, value):
        self._out_bytes = (value, True)

    @property
    def retransmitted_bytes(self):
        """
        Bytes retransmitted.

        :rtype: ``int``
        """
        return self._retransmitted_bytes[0]

    @retransmitted_bytes.setter
    def retransmitted_bytes(self, value):
        self._retransmitted_bytes = (value, True)

    @property
    def unacknowledged_bytes(self):
        """
        Number of bytes sent but unacknowledged.

        :rtype: ``int``
        """
        return self._unacknowledged_bytes[0]

    @unacknowledged_bytes.setter
    def unacknowledged_bytes(self, value):
        self._unacknowledged_bytes = (value, True)

    @property
    def unsent_bytes(self):
        """
        Number of bytes in the transmit queue that have not been sent.

        :rtype: ``int``
        """
        return self._unsent_bytes[0]

    @unsent_bytes.setter
    def unsent_bytes(self, value):
        self._unsent_bytes = (value, True)

    @property
    def send_window_size(self):
        """
        The size of the peer's receive window.

        :rtype: ``int``
        """
        return self._send_window_size[0]

    @send_window_size.setter
    def send_window_size(self, value):
        self._send_window_size = (value, True)

    @property
    def congestion_window_size(self):
        """
        The size of the local congestion window.

        :rtype: ``int``
        """
        return self._congestion_window_size[0]

    @congestion_window_size.setter
    def congestion_window_size(self, value):
        self._congestion_window_size = (value, True)

    @property
    def receive_window_size(self):
        """
        The size of the local receive window.

        :rtype: ``int``
        """
        return self._receive_window_size[0]

    @receive_window_size.setter
    def receive_window_size(self, value):
        self._receive_window_size = (value, True)

    @property
    def round_trip_time(self):
        """
        The smoothed average round trip time for this connection (us).

        :rtype: ``int``
        """
        return self._round_trip_time[0]

    @round_trip_time.setter
    def round_trip_time(self, value):
        self._round_trip_time = (value, True)

