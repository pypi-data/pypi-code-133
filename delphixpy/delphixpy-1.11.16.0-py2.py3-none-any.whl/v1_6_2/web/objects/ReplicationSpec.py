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
#     /delphix-replicationspec.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_2.web.objects.UserObject import UserObject
from delphixpy.v1_6_2 import factory
from delphixpy.v1_6_2 import common

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

class ReplicationSpec(UserObject):
    """
    *(extends* :py:class:`v1_6_2.web.vo.UserObject` *)* Replication setup.
    """
    def __init__(self, undef_enabled=True):
        super(ReplicationSpec, self).__init__()
        self._type = ("ReplicationSpec", True)
        self._bandwidth_limit = (self.__undef__, True)
        self._compressed = (self.__undef__, True)
        self._description = (self.__undef__, True)
        self._enabled = (self.__undef__, True)
        self._encrypted = (self.__undef__, True)
        self._number_of_connections = (self.__undef__, True)
        self._object_specification = (self.__undef__, True)
        self._runtime = (self.__undef__, True)
        self._schedule = (self.__undef__, True)
        self._tag = (self.__undef__, True)
        self._target_credential = (self.__undef__, True)
        self._target_host = (self.__undef__, True)
        self._target_port = (self.__undef__, True)
        self._target_principal = (self.__undef__, True)
        self._use_system_socks_setting = (self.__undef__, True)

    API_VERSION = "1.6.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ReplicationSpec, cls).from_dict(data, dirty, undef_enabled)
        obj._bandwidth_limit = (data.get("bandwidthLimit", obj.__undef__), dirty)
        if obj._bandwidth_limit[0] is not None and obj._bandwidth_limit[0] is not obj.__undef__:
            assert isinstance(obj._bandwidth_limit[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._bandwidth_limit[0], type(obj._bandwidth_limit[0])))
            common.validate_format(obj._bandwidth_limit[0], "None", None, None)
        obj._compressed = (data.get("compressed", obj.__undef__), dirty)
        if obj._compressed[0] is not None and obj._compressed[0] is not obj.__undef__:
            assert isinstance(obj._compressed[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._compressed[0], type(obj._compressed[0])))
            common.validate_format(obj._compressed[0], "None", None, None)
        obj._description = (data.get("description", obj.__undef__), dirty)
        if obj._description[0] is not None and obj._description[0] is not obj.__undef__:
            assert isinstance(obj._description[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._description[0], type(obj._description[0])))
            common.validate_format(obj._description[0], "None", None, 4096)
        obj._enabled = (data.get("enabled", obj.__undef__), dirty)
        if obj._enabled[0] is not None and obj._enabled[0] is not obj.__undef__:
            assert isinstance(obj._enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._enabled[0], type(obj._enabled[0])))
            common.validate_format(obj._enabled[0], "None", None, None)
        obj._encrypted = (data.get("encrypted", obj.__undef__), dirty)
        if obj._encrypted[0] is not None and obj._encrypted[0] is not obj.__undef__:
            assert isinstance(obj._encrypted[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._encrypted[0], type(obj._encrypted[0])))
            common.validate_format(obj._encrypted[0], "None", None, None)
        obj._number_of_connections = (data.get("numberOfConnections", obj.__undef__), dirty)
        if obj._number_of_connections[0] is not None and obj._number_of_connections[0] is not obj.__undef__:
            assert isinstance(obj._number_of_connections[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._number_of_connections[0], type(obj._number_of_connections[0])))
            common.validate_format(obj._number_of_connections[0], "None", None, None)
        if "objectSpecification" in data and data["objectSpecification"] is not None:
            obj._object_specification = (factory.create_object(data["objectSpecification"], "ReplicationObjectSpecification"), dirty)
            factory.validate_type(obj._object_specification[0], "ReplicationObjectSpecification")
        else:
            obj._object_specification = (obj.__undef__, dirty)
        if "runtime" in data and data["runtime"] is not None:
            obj._runtime = (factory.create_object(data["runtime"], "ReplicationSpecRuntime"), dirty)
            factory.validate_type(obj._runtime[0], "ReplicationSpecRuntime")
        else:
            obj._runtime = (obj.__undef__, dirty)
        obj._schedule = (data.get("schedule", obj.__undef__), dirty)
        if obj._schedule[0] is not None and obj._schedule[0] is not obj.__undef__:
            assert isinstance(obj._schedule[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._schedule[0], type(obj._schedule[0])))
            common.validate_format(obj._schedule[0], "None", 1, 256)
        obj._tag = (data.get("tag", obj.__undef__), dirty)
        if obj._tag[0] is not None and obj._tag[0] is not obj.__undef__:
            assert isinstance(obj._tag[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._tag[0], type(obj._tag[0])))
            common.validate_format(obj._tag[0], "None", 1, 256)
        if "targetCredential" in data and data["targetCredential"] is not None:
            obj._target_credential = (factory.create_object(data["targetCredential"], "PasswordCredential"), dirty)
            factory.validate_type(obj._target_credential[0], "PasswordCredential")
        else:
            obj._target_credential = (obj.__undef__, dirty)
        obj._target_host = (data.get("targetHost", obj.__undef__), dirty)
        if obj._target_host[0] is not None and obj._target_host[0] is not obj.__undef__:
            assert isinstance(obj._target_host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_host[0], type(obj._target_host[0])))
            common.validate_format(obj._target_host[0], "host", None, None)
        obj._target_port = (data.get("targetPort", obj.__undef__), dirty)
        if obj._target_port[0] is not None and obj._target_port[0] is not obj.__undef__:
            assert isinstance(obj._target_port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._target_port[0], type(obj._target_port[0])))
            common.validate_format(obj._target_port[0], "None", None, None)
        obj._target_principal = (data.get("targetPrincipal", obj.__undef__), dirty)
        if obj._target_principal[0] is not None and obj._target_principal[0] is not obj.__undef__:
            assert isinstance(obj._target_principal[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._target_principal[0], type(obj._target_principal[0])))
            common.validate_format(obj._target_principal[0], "None", None, None)
        obj._use_system_socks_setting = (data.get("useSystemSocksSetting", obj.__undef__), dirty)
        if obj._use_system_socks_setting[0] is not None and obj._use_system_socks_setting[0] is not obj.__undef__:
            assert isinstance(obj._use_system_socks_setting[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._use_system_socks_setting[0], type(obj._use_system_socks_setting[0])))
            common.validate_format(obj._use_system_socks_setting[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ReplicationSpec, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "bandwidth_limit" == "type" or (self.bandwidth_limit is not self.__undef__ and (not (dirty and not self._bandwidth_limit[1]) or isinstance(self.bandwidth_limit, list) or belongs_to_parent)):
            dct["bandwidthLimit"] = dictify(self.bandwidth_limit)
        elif belongs_to_parent and self.bandwidth_limit is self.__undef__:
            dct["bandwidthLimit"] = 0
        if "compressed" == "type" or (self.compressed is not self.__undef__ and (not (dirty and not self._compressed[1]) or isinstance(self.compressed, list) or belongs_to_parent)):
            dct["compressed"] = dictify(self.compressed)
        elif belongs_to_parent and self.compressed is self.__undef__:
            dct["compressed"] = True
        if "description" == "type" or (self.description is not self.__undef__ and (not (dirty and not self._description[1]) or isinstance(self.description, list) or belongs_to_parent)):
            dct["description"] = dictify(self.description)
        if "enabled" == "type" or (self.enabled is not self.__undef__ and (not (dirty and not self._enabled[1]) or isinstance(self.enabled, list) or belongs_to_parent)):
            dct["enabled"] = dictify(self.enabled)
        elif belongs_to_parent and self.enabled is self.__undef__:
            dct["enabled"] = False
        if "encrypted" == "type" or (self.encrypted is not self.__undef__ and (not (dirty and not self._encrypted[1]) or isinstance(self.encrypted, list) or belongs_to_parent)):
            dct["encrypted"] = dictify(self.encrypted)
        elif belongs_to_parent and self.encrypted is self.__undef__:
            dct["encrypted"] = False
        if "number_of_connections" == "type" or (self.number_of_connections is not self.__undef__ and (not (dirty and not self._number_of_connections[1]) or isinstance(self.number_of_connections, list) or belongs_to_parent)):
            dct["numberOfConnections"] = dictify(self.number_of_connections)
        elif belongs_to_parent and self.number_of_connections is self.__undef__:
            dct["numberOfConnections"] = 1
        if "object_specification" == "type" or (self.object_specification is not self.__undef__ and (not (dirty and not self._object_specification[1]) or isinstance(self.object_specification, list) or belongs_to_parent)):
            dct["objectSpecification"] = dictify(self.object_specification, prop_is_list_or_vo=True)
        if "runtime" == "type" or (self.runtime is not self.__undef__ and (not (dirty and not self._runtime[1]))):
            dct["runtime"] = dictify(self.runtime)
        if "schedule" == "type" or (self.schedule is not self.__undef__ and (not (dirty and not self._schedule[1]) or isinstance(self.schedule, list) or belongs_to_parent)):
            dct["schedule"] = dictify(self.schedule)
        if "tag" == "type" or (self.tag is not self.__undef__ and (not (dirty and not self._tag[1]))):
            dct["tag"] = dictify(self.tag)
        if "target_credential" == "type" or (self.target_credential is not self.__undef__ and (not (dirty and not self._target_credential[1]) or isinstance(self.target_credential, list) or belongs_to_parent)):
            dct["targetCredential"] = dictify(self.target_credential, prop_is_list_or_vo=True)
        if "target_host" == "type" or (self.target_host is not self.__undef__ and (not (dirty and not self._target_host[1]) or isinstance(self.target_host, list) or belongs_to_parent)):
            dct["targetHost"] = dictify(self.target_host)
        if "target_port" == "type" or (self.target_port is not self.__undef__ and (not (dirty and not self._target_port[1]) or isinstance(self.target_port, list) or belongs_to_parent)):
            dct["targetPort"] = dictify(self.target_port)
        elif belongs_to_parent and self.target_port is self.__undef__:
            dct["targetPort"] = 8415
        if "target_principal" == "type" or (self.target_principal is not self.__undef__ and (not (dirty and not self._target_principal[1]) or isinstance(self.target_principal, list) or belongs_to_parent)):
            dct["targetPrincipal"] = dictify(self.target_principal)
        if "use_system_socks_setting" == "type" or (self.use_system_socks_setting is not self.__undef__ and (not (dirty and not self._use_system_socks_setting[1]) or isinstance(self.use_system_socks_setting, list) or belongs_to_parent)):
            dct["useSystemSocksSetting"] = dictify(self.use_system_socks_setting)
        elif belongs_to_parent and self.use_system_socks_setting is self.__undef__:
            dct["useSystemSocksSetting"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._bandwidth_limit = (self._bandwidth_limit[0], True)
        self._compressed = (self._compressed[0], True)
        self._description = (self._description[0], True)
        self._enabled = (self._enabled[0], True)
        self._encrypted = (self._encrypted[0], True)
        self._number_of_connections = (self._number_of_connections[0], True)
        self._object_specification = (self._object_specification[0], True)
        self._runtime = (self._runtime[0], True)
        self._schedule = (self._schedule[0], True)
        self._tag = (self._tag[0], True)
        self._target_credential = (self._target_credential[0], True)
        self._target_host = (self._target_host[0], True)
        self._target_port = (self._target_port[0], True)
        self._target_principal = (self._target_principal[0], True)
        self._use_system_socks_setting = (self._use_system_socks_setting[0], True)

    def is_dirty(self):
        return any([self._bandwidth_limit[1], self._compressed[1], self._description[1], self._enabled[1], self._encrypted[1], self._number_of_connections[1], self._object_specification[1], self._runtime[1], self._schedule[1], self._tag[1], self._target_credential[1], self._target_host[1], self._target_port[1], self._target_principal[1], self._use_system_socks_setting[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ReplicationSpec):
            return False
        return super(ReplicationSpec, self).__eq__(other) and \
               self.bandwidth_limit == other.bandwidth_limit and \
               self.compressed == other.compressed and \
               self.description == other.description and \
               self.enabled == other.enabled and \
               self.encrypted == other.encrypted and \
               self.number_of_connections == other.number_of_connections and \
               self.object_specification == other.object_specification and \
               self.runtime == other.runtime and \
               self.schedule == other.schedule and \
               self.tag == other.tag and \
               self.target_credential == other.target_credential and \
               self.target_host == other.target_host and \
               self.target_port == other.target_port and \
               self.target_principal == other.target_principal and \
               self.use_system_socks_setting == other.use_system_socks_setting

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def bandwidth_limit(self):
        """
        Bandwidth limit (MB/s) for replication network traffic. A value of 0
        means no limit.

        :rtype: ``int``
        """
        return self._bandwidth_limit[0]

    @bandwidth_limit.setter
    def bandwidth_limit(self, value):
        self._bandwidth_limit = (value, True)

    @property
    def compressed(self):
        """
        *(default value: True)* Compress replication network traffic.

        :rtype: ``bool``
        """
        return self._compressed[0]

    @compressed.setter
    def compressed(self, value):
        self._compressed = (value, True)

    @property
    def description(self):
        """
        Description of this replication spec.

        :rtype: ``TEXT_TYPE``
        """
        return self._description[0]

    @description.setter
    def description(self, value):
        self._description = (value, True)

    @property
    def enabled(self):
        """
        Indication whether the replication spec schedule is enabled or not.

        :rtype: ``bool``
        """
        return self._enabled[0]

    @enabled.setter
    def enabled(self, value):
        self._enabled = (value, True)

    @property
    def encrypted(self):
        """
        Encrypt replication network traffic.

        :rtype: ``bool``
        """
        return self._encrypted[0]

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = (value, True)

    @property
    def number_of_connections(self):
        """
        *(default value: 1)* Total number of transport connections to use.

        :rtype: ``int``
        """
        return self._number_of_connections[0]

    @number_of_connections.setter
    def number_of_connections(self, value):
        self._number_of_connections = (value, True)

    @property
    def object_specification(self):
        """
        Specification of the objects to replicate.

        :rtype: :py:class:`v1_6_2.web.vo.ReplicationObjectSpecification`
        """
        return self._object_specification[0]

    @object_specification.setter
    def object_specification(self, value):
        self._object_specification = (value, True)

    @property
    def runtime(self):
        """
        Runtime properties of this replication spec.

        :rtype: :py:class:`v1_6_2.web.vo.ReplicationSpecRuntime`
        """
        return self._runtime[0]

    @runtime.setter
    def runtime(self, value):
        self._runtime = (value, True)

    @property
    def schedule(self):
        """
        Replication schedule in the form of a quartz-formatted string.

        :rtype: ``TEXT_TYPE``
        """
        return self._schedule[0]

    @schedule.setter
    def schedule(self, value):
        self._schedule = (value, True)

    @property
    def tag(self):
        """
        Globally unique identifier for this replication spec.

        :rtype: ``TEXT_TYPE``
        """
        return self._tag[0]

    @tag.setter
    def tag(self, value):
        self._tag = (value, True)

    @property
    def target_credential(self):
        """
        Credential used to authenticate to the replication target host.

        :rtype: :py:class:`v1_6_2.web.vo.PasswordCredential`
        """
        return self._target_credential[0]

    @target_credential.setter
    def target_credential(self, value):
        self._target_credential = (value, True)

    @property
    def target_host(self):
        """
        Replication target host address.

        :rtype: ``TEXT_TYPE``
        """
        return self._target_host[0]

    @target_host.setter
    def target_host(self, value):
        self._target_host = (value, True)

    @property
    def target_port(self):
        """
        *(default value: 8415)* Target TCP port number for the Delphix Session
        Protocol.

        :rtype: ``int``
        """
        return self._target_port[0]

    @target_port.setter
    def target_port(self, value):
        self._target_port = (value, True)

    @property
    def target_principal(self):
        """
        Principal name used to authenticate to the replication target host.

        :rtype: ``TEXT_TYPE``
        """
        return self._target_principal[0]

    @target_principal.setter
    def target_principal(self, value):
        self._target_principal = (value, True)

    @property
    def use_system_socks_setting(self):
        """
        Connect to the replication target host via the system-wide SOCKS proxy.

        :rtype: ``bool``
        """
        return self._use_system_socks_setting[0]

    @use_system_socks_setting.setter
    def use_system_socks_setting(self, value):
        self._use_system_socks_setting = (value, True)

