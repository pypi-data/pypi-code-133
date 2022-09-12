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
#     /delphix-network-throughput-test-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_1.web.objects.NetworkThroughputTestBaseParameters import NetworkThroughputTestBaseParameters
from delphixpy.v1_11_1 import common

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

class NetworkThroughputTestParameters(NetworkThroughputTestBaseParameters):
    """
    *(extends* :py:class:`v1_11_1.web.vo.NetworkThroughputTestBaseParameters`
    *)* Parameters used to execute a network throughput test.
    """
    def __init__(self, undef_enabled=True):
        super(NetworkThroughputTestParameters, self).__init__()
        self._type = ("NetworkThroughputTestParameters", True)
        self._remote_host = (self.__undef__, True)
        self._remote_address = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._block_size = (self.__undef__, True)
        self._send_socket_buffer = (self.__undef__, True)

    API_VERSION = "1.11.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(NetworkThroughputTestParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._remote_host = (data.get("remoteHost", obj.__undef__), dirty)
        if obj._remote_host[0] is not None and obj._remote_host[0] is not obj.__undef__:
            assert isinstance(obj._remote_host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._remote_host[0], type(obj._remote_host[0])))
            common.validate_format(obj._remote_host[0], "objectReference", None, None)
        obj._remote_address = (data.get("remoteAddress", obj.__undef__), dirty)
        if obj._remote_address[0] is not None and obj._remote_address[0] is not obj.__undef__:
            assert isinstance(obj._remote_address[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._remote_address[0], type(obj._remote_address[0])))
            common.validate_format(obj._remote_address[0], "host", None, None)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        obj._block_size = (data.get("blockSize", obj.__undef__), dirty)
        if obj._block_size[0] is not None and obj._block_size[0] is not obj.__undef__:
            assert isinstance(obj._block_size[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._block_size[0], type(obj._block_size[0])))
            common.validate_format(obj._block_size[0], "None", None, None)
        obj._send_socket_buffer = (data.get("sendSocketBuffer", obj.__undef__), dirty)
        if obj._send_socket_buffer[0] is not None and obj._send_socket_buffer[0] is not obj.__undef__:
            assert isinstance(obj._send_socket_buffer[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._send_socket_buffer[0], type(obj._send_socket_buffer[0])))
            common.validate_format(obj._send_socket_buffer[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(NetworkThroughputTestParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "remote_host" == "type" or (self.remote_host is not self.__undef__ and (not (dirty and not self._remote_host[1]) or isinstance(self.remote_host, list) or belongs_to_parent)):
            dct["remoteHost"] = dictify(self.remote_host)
        if "remote_address" == "type" or (self.remote_address is not self.__undef__ and (not (dirty and not self._remote_address[1]) or isinstance(self.remote_address, list) or belongs_to_parent)):
            dct["remoteAddress"] = dictify(self.remote_address)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]) or isinstance(self.port, list) or belongs_to_parent)):
            dct["port"] = dictify(self.port)
        if "block_size" == "type" or (self.block_size is not self.__undef__ and (not (dirty and not self._block_size[1]) or isinstance(self.block_size, list) or belongs_to_parent)):
            dct["blockSize"] = dictify(self.block_size)
        elif belongs_to_parent and self.block_size is self.__undef__:
            dct["blockSize"] = 16384
        if "send_socket_buffer" == "type" or (self.send_socket_buffer is not self.__undef__ and (not (dirty and not self._send_socket_buffer[1]) or isinstance(self.send_socket_buffer, list) or belongs_to_parent)):
            dct["sendSocketBuffer"] = dictify(self.send_socket_buffer)
        elif belongs_to_parent and self.send_socket_buffer is self.__undef__:
            dct["sendSocketBuffer"] = 4194304
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._remote_host = (self._remote_host[0], True)
        self._remote_address = (self._remote_address[0], True)
        self._port = (self._port[0], True)
        self._block_size = (self._block_size[0], True)
        self._send_socket_buffer = (self._send_socket_buffer[0], True)

    def is_dirty(self):
        return any([self._remote_host[1], self._remote_address[1], self._port[1], self._block_size[1], self._send_socket_buffer[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, NetworkThroughputTestParameters):
            return False
        return super(NetworkThroughputTestParameters, self).__eq__(other) and \
               self.remote_host == other.remote_host and \
               self.remote_address == other.remote_address and \
               self.port == other.port and \
               self.block_size == other.block_size and \
               self.send_socket_buffer == other.send_socket_buffer

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def remote_host(self):
        """
        The remote host for the test. The host must be part of an existing
        environment. If the host has multiple addresses and remoteAddress is
        not specified, then the default address used when adding the host will
        be used.

        :rtype: ``TEXT_TYPE``
        """
        return self._remote_host[0]

    @remote_host.setter
    def remote_host(self, value):
        self._remote_host = (value, True)

    @property
    def remote_address(self):
        """
        A hostname or literal IP address to test. This parameter is optional
        and can be provided if the remoteHost has multiple addresses.

        :rtype: ``TEXT_TYPE``
        """
        return self._remote_address[0]

    @remote_address.setter
    def remote_address(self, value):
        self._remote_address = (value, True)

    @property
    def port(self):
        """
        The TCP port number that the server (the receiver) will be listening
        on.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def block_size(self):
        """
        *(default value: 16384)* The size of each transmit request in bytes.

        :rtype: ``int``
        """
        return self._block_size[0]

    @block_size.setter
    def block_size(self, value):
        self._block_size = (value, True)

    @property
    def send_socket_buffer(self):
        """
        *(default value: 4194304)* The size of the send socket buffer in bytes.

        :rtype: ``int``
        """
        return self._send_socket_buffer[0]

    @send_socket_buffer.setter
    def send_socket_buffer(self, value):
        self._send_socket_buffer = (value, True)

