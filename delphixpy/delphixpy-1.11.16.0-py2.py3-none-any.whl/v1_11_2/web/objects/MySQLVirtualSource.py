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
#     /delphix-mysql-virtual-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_2.web.objects.MySQLSource import MySQLSource
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

class MySQLVirtualSource(MySQLSource):
    """
    *(extends* :py:class:`v1_11_2.web.vo.MySQLSource` *)* A virtual MySQL
    source.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLVirtualSource, self).__init__()
        self._type = ("MySQLVirtualSource", True)
        self._operations = (self.__undef__, True)
        self._mount_base = (self.__undef__, True)
        self._file_mapping_rules = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._allow_auto_vdb_restart_on_host_reboot = (self.__undef__, True)

    API_VERSION = "1.11.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLVirtualSource, cls).from_dict(data, dirty, undef_enabled)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "VirtualSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "VirtualSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 256)
        obj._file_mapping_rules = (data.get("fileMappingRules", obj.__undef__), dirty)
        if obj._file_mapping_rules[0] is not None and obj._file_mapping_rules[0] is not obj.__undef__:
            assert isinstance(obj._file_mapping_rules[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._file_mapping_rules[0], type(obj._file_mapping_rules[0])))
            common.validate_format(obj._file_mapping_rules[0], "None", None, None)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        obj._allow_auto_vdb_restart_on_host_reboot = (data.get("allowAutoVDBRestartOnHostReboot", obj.__undef__), dirty)
        if obj._allow_auto_vdb_restart_on_host_reboot[0] is not None and obj._allow_auto_vdb_restart_on_host_reboot[0] is not obj.__undef__:
            assert isinstance(obj._allow_auto_vdb_restart_on_host_reboot[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._allow_auto_vdb_restart_on_host_reboot[0], type(obj._allow_auto_vdb_restart_on_host_reboot[0])))
            common.validate_format(obj._allow_auto_vdb_restart_on_host_reboot[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLVirtualSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "file_mapping_rules" == "type" or (self.file_mapping_rules is not self.__undef__ and (not (dirty and not self._file_mapping_rules[1]) or isinstance(self.file_mapping_rules, list) or belongs_to_parent)):
            dct["fileMappingRules"] = dictify(self.file_mapping_rules)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "allow_auto_vdb_restart_on_host_reboot" == "type" or (self.allow_auto_vdb_restart_on_host_reboot is not self.__undef__ and (not (dirty and not self._allow_auto_vdb_restart_on_host_reboot[1]) or isinstance(self.allow_auto_vdb_restart_on_host_reboot, list) or belongs_to_parent)):
            dct["allowAutoVDBRestartOnHostReboot"] = dictify(self.allow_auto_vdb_restart_on_host_reboot)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._operations = (self._operations[0], True)
        self._mount_base = (self._mount_base[0], True)
        self._file_mapping_rules = (self._file_mapping_rules[0], True)
        self._config_params = (self._config_params[0], True)
        self._allow_auto_vdb_restart_on_host_reboot = (self._allow_auto_vdb_restart_on_host_reboot[0], True)

    def is_dirty(self):
        return any([self._operations[1], self._mount_base[1], self._file_mapping_rules[1], self._config_params[1], self._allow_auto_vdb_restart_on_host_reboot[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLVirtualSource):
            return False
        return super(MySQLVirtualSource, self).__eq__(other) and \
               self.operations == other.operations and \
               self.mount_base == other.mount_base and \
               self.file_mapping_rules == other.file_mapping_rules and \
               self.config_params == other.config_params and \
               self.allow_auto_vdb_restart_on_host_reboot == other.allow_auto_vdb_restart_on_host_reboot

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_11_2.web.vo.VirtualSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def mount_base(self):
        """
        The base mount point for the NFS mounts.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_base[0]

    @mount_base.setter
    def mount_base(self, value):
        self._mount_base = (value, True)

    @property
    def file_mapping_rules(self):
        """
        Database file mapping rules.

        :rtype: ``TEXT_TYPE``
        """
        return self._file_mapping_rules[0]

    @file_mapping_rules.setter
    def file_mapping_rules(self, value):
        self._file_mapping_rules = (value, True)

    @property
    def config_params(self):
        """
        MySQL database configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

    @property
    def allow_auto_vdb_restart_on_host_reboot(self):
        """
        Indicates whether Delphix should automatically restart this virtual
        source when target host reboot is detected.

        :rtype: ``bool``
        """
        return self._allow_auto_vdb_restart_on_host_reboot[0]

    @allow_auto_vdb_restart_on_host_reboot.setter
    def allow_auto_vdb_restart_on_host_reboot(self, value):
        self._allow_auto_vdb_restart_on_host_reboot = (value, True)

