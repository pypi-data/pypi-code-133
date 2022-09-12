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
#     /delphix-unix-connectivity-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.ConnectivityParameters import ConnectivityParameters
from delphixpy.v1_11_2 import factory
from delphixpy.v1_11_2 import common

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

class UnixConnectivityParameters(ConnectivityParameters):
    """
    *(extends* :py:class:`v1_11_2.web.vo.ConnectivityParameters` *)* Parameters
    required to connect to a remote UNIX host.
    """
    def __init__(self, undef_enabled=True):
        super(UnixConnectivityParameters, self).__init__()
        self._type = ("UnixConnectivityParameters", True)
        self._port = (self.__undef__, True)
        self._ssh_verification_strategy = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(UnixConnectivityParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        if "sshVerificationStrategy" in data and data["sshVerificationStrategy"] is not None:
            obj._ssh_verification_strategy = (factory.create_object(data["sshVerificationStrategy"], "SshVerificationStrategy"), dirty)
            factory.validate_type(obj._ssh_verification_strategy[0], "SshVerificationStrategy")
        else:
            obj._ssh_verification_strategy = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(UnixConnectivityParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]))):
            dct["port"] = dictify(self.port)
        if "ssh_verification_strategy" == "type" or (self.ssh_verification_strategy is not self.__undef__ and (not (dirty and not self._ssh_verification_strategy[1]))):
            dct["sshVerificationStrategy"] = dictify(self.ssh_verification_strategy)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._port = (self._port[0], True)
        self._ssh_verification_strategy = (self._ssh_verification_strategy[0], True)

    def is_dirty(self):
        return any([self._port[1], self._ssh_verification_strategy[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, UnixConnectivityParameters):
            return False
        return super(UnixConnectivityParameters, self).__eq__(other) and \
               self.port == other.port and \
               self.ssh_verification_strategy == other.ssh_verification_strategy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def port(self):
        """
        *(default value: 22)* SSH port on remote host.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def ssh_verification_strategy(self):
        """
        Mechanism to use for SSH host verification.

        :rtype: :py:class:`v1_11_2.web.vo.SshVerificationStrategy`
        """
        return self._ssh_verification_strategy[0]

    @ssh_verification_strategy.setter
    def ssh_verification_strategy(self, value):
        self._ssh_verification_strategy = (value, True)

