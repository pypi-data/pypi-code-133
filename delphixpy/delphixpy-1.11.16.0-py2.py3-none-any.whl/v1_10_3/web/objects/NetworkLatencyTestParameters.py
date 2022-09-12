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
#     /delphix-network-latency-test-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_3.web.objects.NetworkTestParameters import NetworkTestParameters
from delphixpy.v1_10_3 import common

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

class NetworkLatencyTestParameters(NetworkTestParameters):
    """
    *(extends* :py:class:`v1_10_3.web.vo.NetworkTestParameters` *)* Parameters
    used to execute a network latency test.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkLatencyTestParameters, self).__init__()
        self._type = ("NetworkLatencyTestParameters", True)
        self._remote_address = (self.__undef__, True)
        self._request_count = (self.__undef__, True)
        self._request_size = (self.__undef__, True)

    API_VERSION = "1.10.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkLatencyTestParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._remote_address = (data.get("remoteAddress", obj.__undef__), dirty)
        if obj._remote_address[0] is not None and obj._remote_address[0] is not obj.__undef__:
            assert isinstance(obj._remote_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._remote_address[0], type(obj._remote_address[0])))
            common.validate_format(obj._remote_address[0], "host", None, None)
        obj._request_count = (data.get("requestCount", obj.__undef__), dirty)
        if obj._request_count[0] is not None and obj._request_count[0] is not obj.__undef__:
            assert isinstance(obj._request_count[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._request_count[0], type(obj._request_count[0])))
            common.validate_format(obj._request_count[0], "None", None, None)
        obj._request_size = (data.get("requestSize", obj.__undef__), dirty)
        if obj._request_size[0] is not None and obj._request_size[0] is not obj.__undef__:
            assert isinstance(obj._request_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._request_size[0], type(obj._request_size[0])))
            common.validate_format(obj._request_size[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkLatencyTestParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "remote_address" == "type" or (self.remote_address is not self.__undef__ and (not (dirty and not self._remote_address[1]) or isinstance(self.remote_address, list) or belongs_to_parent)):
            dct["remoteAddress"] = dictify(self.remote_address)
        if "request_count" == "type" or (self.request_count is not self.__undef__ and (not (dirty and not self._request_count[1]) or isinstance(self.request_count, list) or belongs_to_parent)):
            dct["requestCount"] = dictify(self.request_count)
        elif belongs_to_parent and self.request_count is self.__undef__:
            dct["requestCount"] = 20
        if "request_size" == "type" or (self.request_size is not self.__undef__ and (not (dirty and not self._request_size[1]) or isinstance(self.request_size, list) or belongs_to_parent)):
            dct["requestSize"] = dictify(self.request_size)
        elif belongs_to_parent and self.request_size is self.__undef__:
            dct["requestSize"] = 8
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._remote_address = (self._remote_address[0], True)
        self._request_count = (self._request_count[0], True)
        self._request_size = (self._request_size[0], True)

    def is_dirty(self):
        return any([self._remote_address[1], self._request_count[1], self._request_size[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkLatencyTestParameters):
            return False
        return super(NetworkLatencyTestParameters, self).__eq__(other) and \
               self.remote_address == other.remote_address and \
               self.request_count == other.request_count and \
               self.request_size == other.request_size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def remote_address(self):
        """
        A hostname or literal IP address to test. Either remoteAddress or
        remoteHost must be set, but not both.

        :rtype: ``TEXT_TYPE``
        """
        return self._remote_address[0]

    @remote_address.setter
    def remote_address(self, value):
        self._remote_address = (value, True)

    @property
    def request_count(self):
        """
        *(default value: 20)* Number of requests to send.

        :rtype: ``int``
        """
        return self._request_count[0]

    @request_count.setter
    def request_count(self, value):
        self._request_count = (value, True)

    @property
    def request_size(self):
        """
        *(default value: 8)* The size of requests to send (bytes).

        :rtype: ``int``
        """
        return self._request_size[0]

    @request_size.setter
    def request_size(self, value):
        self._request_size = (value, True)

