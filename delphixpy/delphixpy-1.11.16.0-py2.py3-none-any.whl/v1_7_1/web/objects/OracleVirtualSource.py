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
#     /delphix-oracle-virtual-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.OracleSource import OracleSource
from delphixpy.v1_7_1 import factory
from delphixpy.v1_7_1 import common

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

class OracleVirtualSource(OracleSource):
    """
    *(extends* :py:class:`v1_7_1.web.vo.OracleSource` *)* A virtual Oracle
    source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleVirtualSource, self).__init__()
        self._type = ("OracleVirtualSource", True)
        self._archivelog_mode = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._config_template = (self.__undef__, True)
        self._custom_env_vars = (self.__undef__, True)
        self._file_mapping_rules = (self.__undef__, True)
        self._manual_provisioning = (self.__undef__, True)
        self._mount_base = (self.__undef__, True)
        self._node_listener_list = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._redo_log_groups = (self.__undef__, True)
        self._redo_log_size_in_mb = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleVirtualSource, cls).from_dict(data, dirty, undef_enabled)
        obj._archivelog_mode = (data.get("archivelogMode", obj.__undef__), dirty)
        if obj._archivelog_mode[0] is not None and obj._archivelog_mode[0] is not obj.__undef__:
            assert isinstance(obj._archivelog_mode[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._archivelog_mode[0], type(obj._archivelog_mode[0])))
            common.validate_format(obj._archivelog_mode[0], "None", None, None)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        obj._config_template = (data.get("configTemplate", obj.__undef__), dirty)
        if obj._config_template[0] is not None and obj._config_template[0] is not obj.__undef__:
            assert isinstance(obj._config_template[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config_template[0], type(obj._config_template[0])))
            common.validate_format(obj._config_template[0], "objectReference", None, None)
        obj._custom_env_vars = []
        for item in data.get("customEnvVars") or []:
            obj._custom_env_vars.append(factory.create_object(item))
            factory.validate_type(obj._custom_env_vars[-1], "OracleCustomEnvVar")
        obj._custom_env_vars = (obj._custom_env_vars, dirty)
        obj._file_mapping_rules = (data.get("fileMappingRules", obj.__undef__), dirty)
        if obj._file_mapping_rules[0] is not None and obj._file_mapping_rules[0] is not obj.__undef__:
            assert isinstance(obj._file_mapping_rules[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._file_mapping_rules[0], type(obj._file_mapping_rules[0])))
            common.validate_format(obj._file_mapping_rules[0], "None", None, None)
        obj._manual_provisioning = (data.get("manualProvisioning", obj.__undef__), dirty)
        if obj._manual_provisioning[0] is not None and obj._manual_provisioning[0] is not obj.__undef__:
            assert isinstance(obj._manual_provisioning[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._manual_provisioning[0], type(obj._manual_provisioning[0])))
            common.validate_format(obj._manual_provisioning[0], "None", None, None)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 256)
        obj._node_listener_list = []
        for item in data.get("nodeListenerList") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._node_listener_list.append(item)
        obj._node_listener_list = (obj._node_listener_list, dirty)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "VirtualSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "VirtualSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._redo_log_groups = (data.get("redoLogGroups", obj.__undef__), dirty)
        if obj._redo_log_groups[0] is not None and obj._redo_log_groups[0] is not obj.__undef__:
            assert isinstance(obj._redo_log_groups[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._redo_log_groups[0], type(obj._redo_log_groups[0])))
            common.validate_format(obj._redo_log_groups[0], "None", None, None)
        obj._redo_log_size_in_mb = (data.get("redoLogSizeInMB", obj.__undef__), dirty)
        if obj._redo_log_size_in_mb[0] is not None and obj._redo_log_size_in_mb[0] is not obj.__undef__:
            assert isinstance(obj._redo_log_size_in_mb[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._redo_log_size_in_mb[0], type(obj._redo_log_size_in_mb[0])))
            common.validate_format(obj._redo_log_size_in_mb[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleVirtualSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "archivelog_mode" == "type" or (self.archivelog_mode is not self.__undef__ and (not (dirty and not self._archivelog_mode[1]) or isinstance(self.archivelog_mode, list) or belongs_to_parent)):
            dct["archivelogMode"] = dictify(self.archivelog_mode)
        elif belongs_to_parent and self.archivelog_mode is self.__undef__:
            dct["archivelogMode"] = True
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "config_template" == "type" or (self.config_template is not self.__undef__ and (not (dirty and not self._config_template[1]) or isinstance(self.config_template, list) or belongs_to_parent)):
            dct["configTemplate"] = dictify(self.config_template)
        if "custom_env_vars" == "type" or (self.custom_env_vars is not self.__undef__ and (not (dirty and not self._custom_env_vars[1]) or isinstance(self.custom_env_vars, list) or belongs_to_parent)):
            dct["customEnvVars"] = dictify(self.custom_env_vars, prop_is_list_or_vo=True)
        if "file_mapping_rules" == "type" or (self.file_mapping_rules is not self.__undef__ and (not (dirty and not self._file_mapping_rules[1]) or isinstance(self.file_mapping_rules, list) or belongs_to_parent)):
            dct["fileMappingRules"] = dictify(self.file_mapping_rules)
        if "manual_provisioning" == "type" or (self.manual_provisioning is not self.__undef__ and (not (dirty and not self._manual_provisioning[1]) or isinstance(self.manual_provisioning, list) or belongs_to_parent)):
            dct["manualProvisioning"] = dictify(self.manual_provisioning)
        elif belongs_to_parent and self.manual_provisioning is self.__undef__:
            dct["manualProvisioning"] = False
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "node_listener_list" == "type" or (self.node_listener_list is not self.__undef__ and (not (dirty and not self._node_listener_list[1]) or isinstance(self.node_listener_list, list) or belongs_to_parent)):
            dct["nodeListenerList"] = dictify(self.node_listener_list, prop_is_list_or_vo=True)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "redo_log_groups" == "type" or (self.redo_log_groups is not self.__undef__ and (not (dirty and not self._redo_log_groups[1]) or isinstance(self.redo_log_groups, list) or belongs_to_parent)):
            dct["redoLogGroups"] = dictify(self.redo_log_groups)
        elif belongs_to_parent and self.redo_log_groups is self.__undef__:
            dct["redoLogGroups"] = 3
        if "redo_log_size_in_mb" == "type" or (self.redo_log_size_in_mb is not self.__undef__ and (not (dirty and not self._redo_log_size_in_mb[1]) or isinstance(self.redo_log_size_in_mb, list) or belongs_to_parent)):
            dct["redoLogSizeInMB"] = dictify(self.redo_log_size_in_mb)
        elif belongs_to_parent and self.redo_log_size_in_mb is self.__undef__:
            dct["redoLogSizeInMB"] = 0
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._archivelog_mode = (self._archivelog_mode[0], True)
        self._config_params = (self._config_params[0], True)
        self._config_template = (self._config_template[0], True)
        self._custom_env_vars = (self._custom_env_vars[0], True)
        self._file_mapping_rules = (self._file_mapping_rules[0], True)
        self._manual_provisioning = (self._manual_provisioning[0], True)
        self._mount_base = (self._mount_base[0], True)
        self._node_listener_list = (self._node_listener_list[0], True)
        self._operations = (self._operations[0], True)
        self._redo_log_groups = (self._redo_log_groups[0], True)
        self._redo_log_size_in_mb = (self._redo_log_size_in_mb[0], True)

    def is_dirty(self):
        return any([self._archivelog_mode[1], self._config_params[1], self._config_template[1], self._custom_env_vars[1], self._file_mapping_rules[1], self._manual_provisioning[1], self._mount_base[1], self._node_listener_list[1], self._operations[1], self._redo_log_groups[1], self._redo_log_size_in_mb[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleVirtualSource):
            return False
        return super(OracleVirtualSource, self).__eq__(other) and \
               self.archivelog_mode == other.archivelog_mode and \
               self.config_params == other.config_params and \
               self.config_template == other.config_template and \
               self.custom_env_vars == other.custom_env_vars and \
               self.file_mapping_rules == other.file_mapping_rules and \
               self.manual_provisioning == other.manual_provisioning and \
               self.mount_base == other.mount_base and \
               self.node_listener_list == other.node_listener_list and \
               self.operations == other.operations and \
               self.redo_log_groups == other.redo_log_groups and \
               self.redo_log_size_in_mb == other.redo_log_size_in_mb

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def archivelog_mode(self):
        """
        *(default value: True)* Archive Log Mode of the Oracle virtual
        database.

        :rtype: ``bool``
        """
        return self._archivelog_mode[0]

    @archivelog_mode.setter
    def archivelog_mode(self, value):
        self._archivelog_mode = (value, True)

    @property
    def config_params(self):
        """
        Oracle database configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

    @property
    def config_template(self):
        """
        Optional database template to use for provisioning and refresh. If set,
        configParams will be ignored on provision or refresh.

        :rtype: ``TEXT_TYPE``
        """
        return self._config_template[0]

    @config_template.setter
    def config_template(self, value):
        self._config_template = (value, True)

    @property
    def custom_env_vars(self):
        """
        Custom environment variables for Oracle databases.

        :rtype: ``list`` of :py:class:`v1_7_1.web.vo.OracleCustomEnvVar`
        """
        return self._custom_env_vars[0]

    @custom_env_vars.setter
    def custom_env_vars(self, value):
        self._custom_env_vars = (value, True)

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
    def manual_provisioning(self):
        """
        Flag indicating whether the database should be provisioned in manual
        mode.

        :rtype: ``bool``
        """
        return self._manual_provisioning[0]

    @manual_provisioning.setter
    def manual_provisioning(self, value):
        self._manual_provisioning = (value, True)

    @property
    def mount_base(self):
        """
        The base mount point to use for the NFS mounts.

        :rtype: ``TEXT_TYPE``
        """
        return self._mount_base[0]

    @mount_base.setter
    def mount_base(self, value):
        self._mount_base = (value, True)

    @property
    def node_listener_list(self):
        """
        A list of object references of Oracle Node Listeners selected for this
        Virtual Database. Delphix picks one default listener from the target
        environment if this list is empty at virtual database provision time.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._node_listener_list[0]

    @node_listener_list.setter
    def node_listener_list(self, value):
        self._node_listener_list = (value, True)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_7_1.web.vo.VirtualSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def redo_log_groups(self):
        """
        *(default value: 3)* Number of Online Redo Log Groups.

        :rtype: ``int``
        """
        return self._redo_log_groups[0]

    @redo_log_groups.setter
    def redo_log_groups(self, value):
        self._redo_log_groups = (value, True)

    @property
    def redo_log_size_in_mb(self):
        """
        Online Redo Log size in MB.

        :rtype: ``int``
        """
        return self._redo_log_size_in_mb[0]

    @redo_log_size_in_mb.setter
    def redo_log_size_in_mb(self, value):
        self._redo_log_size_in_mb = (value, True)

