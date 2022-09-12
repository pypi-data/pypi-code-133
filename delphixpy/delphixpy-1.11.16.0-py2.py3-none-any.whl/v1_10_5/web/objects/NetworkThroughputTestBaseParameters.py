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
#     /delphix-network-throughput-test-base-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_5.web.objects.NetworkTestParameters import NetworkTestParameters
from delphixpy.v1_10_5 import common

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

class NetworkThroughputTestBaseParameters(NetworkTestParameters):
    """
    *(extends* :py:class:`v1_10_5.web.vo.NetworkTestParameters` *)* Base type
    for parameters used to execute a network throughput test.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkThroughputTestBaseParameters, self).__init__()
        self._type = ("NetworkThroughputTestBaseParameters", True)
        self._direction = (self.__undef__, True)
        self._num_connections = (self.__undef__, True)
        self._duration = (self.__undef__, True)

    API_VERSION = "1.10.5"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkThroughputTestBaseParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._direction = (data.get("direction", obj.__undef__), dirty)
        if obj._direction[0] is not None and obj._direction[0] is not obj.__undef__:
            assert isinstance(obj._direction[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._direction[0], type(obj._direction[0])))
            assert obj._direction[0] in ['TRANSMIT', 'RECEIVE'], "Expected enum ['TRANSMIT', 'RECEIVE'] but got %s" % obj._direction[0]
            common.validate_format(obj._direction[0], "None", None, None)
        obj._num_connections = (data.get("numConnections", obj.__undef__), dirty)
        if obj._num_connections[0] is not None and obj._num_connections[0] is not obj.__undef__:
            assert isinstance(obj._num_connections[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._num_connections[0], type(obj._num_connections[0])))
            common.validate_format(obj._num_connections[0], "None", None, None)
        obj._duration = (data.get("duration", obj.__undef__), dirty)
        if obj._duration[0] is not None and obj._duration[0] is not obj.__undef__:
            assert isinstance(obj._duration[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._duration[0], type(obj._duration[0])))
            common.validate_format(obj._duration[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkThroughputTestBaseParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "direction" == "type" or (self.direction is not self.__undef__ and (not (dirty and not self._direction[1]) or isinstance(self.direction, list) or belongs_to_parent)):
            dct["direction"] = dictify(self.direction)
        elif belongs_to_parent and self.direction is self.__undef__:
            dct["direction"] = "TRANSMIT"
        if "num_connections" == "type" or (self.num_connections is not self.__undef__ and (not (dirty and not self._num_connections[1]) or isinstance(self.num_connections, list) or belongs_to_parent)):
            dct["numConnections"] = dictify(self.num_connections)
        elif belongs_to_parent and self.num_connections is self.__undef__:
            dct["numConnections"] = 0
        if "duration" == "type" or (self.duration is not self.__undef__ and (not (dirty and not self._duration[1]) or isinstance(self.duration, list) or belongs_to_parent)):
            dct["duration"] = dictify(self.duration)
        elif belongs_to_parent and self.duration is self.__undef__:
            dct["duration"] = 30
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._direction = (self._direction[0], True)
        self._num_connections = (self._num_connections[0], True)
        self._duration = (self._duration[0], True)

    def is_dirty(self):
        return any([self._direction[1], self._num_connections[1], self._duration[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkThroughputTestBaseParameters):
            return False
        return super(NetworkThroughputTestBaseParameters, self).__eq__(other) and \
               self.direction == other.direction and \
               self.num_connections == other.num_connections and \
               self.duration == other.duration

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def direction(self):
        """
        *(default value: TRANSMIT)* Whether the test is a transmit or receive
        test. *(permitted values: TRANSMIT, RECEIVE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._direction[0]

    @direction.setter
    def direction(self, value):
        self._direction = (value, True)

    @property
    def num_connections(self):
        """
        The number of connections to use for the test. The special value 0 (the
        default) causes the test to automatically discover and use the optimal
        number of connections to use for maximum throughput.

        :rtype: ``int``
        """
        return self._num_connections[0]

    @num_connections.setter
    def num_connections(self, value):
        self._num_connections = (value, True)

    @property
    def duration(self):
        """
        *(default value: 30)* The duration of the test in seconds. Note that
        when numConnections is 0, an initial period of time will be spent
        calculating the optimal number of connections, and that time does not
        count toward the duration of the test.

        :rtype: ``int``
        """
        return self._duration[0]

    @duration.setter
    def duration(self, value):
        self._duration = (value, True)

