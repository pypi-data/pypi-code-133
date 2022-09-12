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
#     /delphix-network-throughput-test-base.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_11.web.objects.NetworkTest import NetworkTest
from delphixpy.v1_11_11 import common

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

class NetworkThroughputTestBase(NetworkTest):
    """
    *(extends* :py:class:`v1_11_11.web.vo.NetworkTest` *)* The base type for
    all throughput tests.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkThroughputTestBase, self).__init__()
        self._type = ("NetworkThroughputTestBase", True)
        self._throughput = (self.__undef__, True)
        self._num_connections = (self.__undef__, True)

    API_VERSION = "1.11.11"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkThroughputTestBase, cls).from_dict(data, dirty, undef_enabled)
        obj._throughput = (data.get("throughput", obj.__undef__), dirty)
        if obj._throughput[0] is not None and obj._throughput[0] is not obj.__undef__:
            assert isinstance(obj._throughput[0], float), ("Expected one of ['number'], but got %s of type %s" % (obj._throughput[0], type(obj._throughput[0])))
            common.validate_format(obj._throughput[0], "None", None, None)
        obj._num_connections = (data.get("numConnections", obj.__undef__), dirty)
        if obj._num_connections[0] is not None and obj._num_connections[0] is not obj.__undef__:
            assert isinstance(obj._num_connections[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._num_connections[0], type(obj._num_connections[0])))
            common.validate_format(obj._num_connections[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkThroughputTestBase, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "throughput" == "type" or (self.throughput is not self.__undef__ and (not (dirty and not self._throughput[1]))):
            dct["throughput"] = dictify(self.throughput)
        if "num_connections" == "type" or (self.num_connections is not self.__undef__ and (not (dirty and not self._num_connections[1]))):
            dct["numConnections"] = dictify(self.num_connections)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._throughput = (self._throughput[0], True)
        self._num_connections = (self._num_connections[0], True)

    def is_dirty(self):
        return any([self._throughput[1], self._num_connections[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkThroughputTestBase):
            return False
        return super(NetworkThroughputTestBase, self).__eq__(other) and \
               self.throughput == other.throughput and \
               self.num_connections == other.num_connections

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def throughput(self):
        """
        Average throughput measured.

        :rtype: ``float``
        """
        return self._throughput[0]

    @throughput.setter
    def throughput(self, value):
        self._throughput = (value, True)

    @property
    def num_connections(self):
        """
        Number of connections used to achieve maximum sustained throughput.

        :rtype: ``int``
        """
        return self._num_connections[0]

    @num_connections.setter
    def num_connections(self, value):
        self._num_connections = (value, True)

