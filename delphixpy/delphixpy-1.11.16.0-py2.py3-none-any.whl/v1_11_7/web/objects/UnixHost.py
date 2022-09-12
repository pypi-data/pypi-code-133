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
#     /delphix-unix-host.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.Host import Host
from delphixpy.v1_11_7 import factory
from delphixpy.v1_11_7 import common

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

class UnixHost(Host):
    """
    *(extends* :py:class:`v1_11_7.web.vo.Host` *)* The representation of a Unix
    host object.
    """
    def __init__(self, undef_enabled=True):
        super(UnixHost, self).__init__()
        self._type = ("UnixHost", True)
        self._toolkit_path = (self.__undef__, True)
        self._oracle_jdbc_keystore_password = (self.__undef__, True)
        self._ssh_verification_strategy = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(UnixHost, cls).from_dict(data, dirty, undef_enabled)
        obj._toolkit_path = (data.get("toolkitPath", obj.__undef__), dirty)
        if obj._toolkit_path[0] is not None and obj._toolkit_path[0] is not obj.__undef__:
            assert isinstance(obj._toolkit_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._toolkit_path[0], type(obj._toolkit_path[0])))
            common.validate_format(obj._toolkit_path[0], "None", None, None)
        obj._oracle_jdbc_keystore_password = (data.get("oracleJdbcKeystorePassword", obj.__undef__), dirty)
        if obj._oracle_jdbc_keystore_password[0] is not None and obj._oracle_jdbc_keystore_password[0] is not obj.__undef__:
            assert isinstance(obj._oracle_jdbc_keystore_password[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._oracle_jdbc_keystore_password[0], type(obj._oracle_jdbc_keystore_password[0])))
            common.validate_format(obj._oracle_jdbc_keystore_password[0], "password", 1, None)
        if "sshVerificationStrategy" in data and data["sshVerificationStrategy"] is not None:
            obj._ssh_verification_strategy = (factory.create_object(data["sshVerificationStrategy"], "SshVerificationStrategy"), dirty)
            factory.validate_type(obj._ssh_verification_strategy[0], "SshVerificationStrategy")
        else:
            obj._ssh_verification_strategy = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(UnixHost, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "toolkit_path" == "type" or (self.toolkit_path is not self.__undef__ and (not (dirty and not self._toolkit_path[1]) or isinstance(self.toolkit_path, list) or belongs_to_parent)):
            dct["toolkitPath"] = dictify(self.toolkit_path)
        if "oracle_jdbc_keystore_password" == "type" or (self.oracle_jdbc_keystore_password is not self.__undef__ and (not (dirty and not self._oracle_jdbc_keystore_password[1]) or isinstance(self.oracle_jdbc_keystore_password, list) or belongs_to_parent)):
            dct["oracleJdbcKeystorePassword"] = dictify(self.oracle_jdbc_keystore_password)
        if "ssh_verification_strategy" == "type" or (self.ssh_verification_strategy is not self.__undef__ and (not (dirty and not self._ssh_verification_strategy[1]) or isinstance(self.ssh_verification_strategy, list) or belongs_to_parent)):
            dct["sshVerificationStrategy"] = dictify(self.ssh_verification_strategy, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._toolkit_path = (self._toolkit_path[0], True)
        self._oracle_jdbc_keystore_password = (self._oracle_jdbc_keystore_password[0], True)
        self._ssh_verification_strategy = (self._ssh_verification_strategy[0], True)

    def is_dirty(self):
        return any([self._toolkit_path[1], self._oracle_jdbc_keystore_password[1], self._ssh_verification_strategy[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, UnixHost):
            return False
        return super(UnixHost, self).__eq__(other) and \
               self.toolkit_path == other.toolkit_path and \
               self.oracle_jdbc_keystore_password == other.oracle_jdbc_keystore_password and \
               self.ssh_verification_strategy == other.ssh_verification_strategy

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def toolkit_path(self):
        """
        The path for the toolkit that resides on the host.

        :rtype: ``TEXT_TYPE``
        """
        return self._toolkit_path[0]

    @toolkit_path.setter
    def toolkit_path(self, value):
        self._toolkit_path = (value, True)

    @property
    def oracle_jdbc_keystore_password(self):
        """
        The password for the user managed Oracle JDBC keystore.

        :rtype: ``TEXT_TYPE``
        """
        return self._oracle_jdbc_keystore_password[0]

    @oracle_jdbc_keystore_password.setter
    def oracle_jdbc_keystore_password(self, value):
        self._oracle_jdbc_keystore_password = (value, True)

    @property
    def ssh_verification_strategy(self):
        """
        Mechanism to use for ssh host verification.

        :rtype: :py:class:`v1_11_7.web.vo.SshVerificationStrategy`
        """
        return self._ssh_verification_strategy[0]

    @ssh_verification_strategy.setter
    def ssh_verification_strategy(self, value):
        self._ssh_verification_strategy = (value, True)

