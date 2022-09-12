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
#     /delphix-oracle-virtual-cdb-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.OracleVirtualSource import OracleVirtualSource
from delphixpy.v1_10_6 import factory
from delphixpy.v1_10_6 import common

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

class OracleVirtualCdbSource(OracleVirtualSource):
    """
    *(extends* :py:class:`v1_10_6.web.vo.OracleVirtualSource` *)* A virtual
    Oracle multitenant container database source. Certain fields of the Oracle
    virtual source are not applicable to the virtual container database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleVirtualCdbSource, self).__init__()
        self._type = ("OracleVirtualCdbSource", True)
        self._custom_env_vars = (self.__undef__, True)
        self._file_mapping_rules = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._archivelog_mode = (self.__undef__, True)
        self._node_listeners = (self.__undef__, True)
        self._redo_log_size_in_mb = (self.__undef__, True)
        self._redo_log_groups = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleVirtualCdbSource, cls).from_dict(data, dirty, undef_enabled)
        obj._custom_env_vars = []
        for item in data.get("customEnvVars") or []:
            obj._custom_env_vars.append(factory.create_object(item))
            factory.validate_type(obj._custom_env_vars[-1], "OracleCustomEnvVar")
        obj._custom_env_vars = (obj._custom_env_vars, dirty)
        obj._file_mapping_rules = (data.get("fileMappingRules", obj.__undef__), dirty)
        if obj._file_mapping_rules[0] is not None and obj._file_mapping_rules[0] is not obj.__undef__:
            assert isinstance(obj._file_mapping_rules[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._file_mapping_rules[0], type(obj._file_mapping_rules[0])))
            common.validate_format(obj._file_mapping_rules[0], "None", None, None)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "VirtualSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "VirtualSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._archivelog_mode = (data.get("archivelogMode", obj.__undef__), dirty)
        if obj._archivelog_mode[0] is not None and obj._archivelog_mode[0] is not obj.__undef__:
            assert isinstance(obj._archivelog_mode[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._archivelog_mode[0], type(obj._archivelog_mode[0])))
            common.validate_format(obj._archivelog_mode[0], "None", None, None)
        obj._node_listeners = []
        for item in data.get("nodeListeners") or []:
            assert isinstance(item, TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "objectReference", None, None)
            obj._node_listeners.append(item)
        obj._node_listeners = (obj._node_listeners, dirty)
        obj._redo_log_size_in_mb = (data.get("redoLogSizeInMB", obj.__undef__), dirty)
        if obj._redo_log_size_in_mb[0] is not None and obj._redo_log_size_in_mb[0] is not obj.__undef__:
            assert isinstance(obj._redo_log_size_in_mb[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._redo_log_size_in_mb[0], type(obj._redo_log_size_in_mb[0])))
            common.validate_format(obj._redo_log_size_in_mb[0], "None", None, None)
        obj._redo_log_groups = (data.get("redoLogGroups", obj.__undef__), dirty)
        if obj._redo_log_groups[0] is not None and obj._redo_log_groups[0] is not obj.__undef__:
            assert isinstance(obj._redo_log_groups[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._redo_log_groups[0], type(obj._redo_log_groups[0])))
            common.validate_format(obj._redo_log_groups[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleVirtualCdbSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "custom_env_vars" == "type" or (self.custom_env_vars is not self.__undef__ and (not (dirty and not self._custom_env_vars[1]))):
            dct["customEnvVars"] = dictify(self.custom_env_vars)
        if dirty and "customEnvVars" in dct:
            del dct["customEnvVars"]
        if "file_mapping_rules" == "type" or (self.file_mapping_rules is not self.__undef__ and (not (dirty and not self._file_mapping_rules[1]))):
            dct["fileMappingRules"] = dictify(self.file_mapping_rules)
        if dirty and "fileMappingRules" in dct:
            del dct["fileMappingRules"]
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]))):
            dct["operations"] = dictify(self.operations)
        if dirty and "operations" in dct:
            del dct["operations"]
        if "archivelog_mode" == "type" or (self.archivelog_mode is not self.__undef__ and (not (dirty and not self._archivelog_mode[1]))):
            dct["archivelogMode"] = dictify(self.archivelog_mode)
        if dirty and "archivelogMode" in dct:
            del dct["archivelogMode"]
        if "node_listeners" == "type" or (self.node_listeners is not self.__undef__ and (not (dirty and not self._node_listeners[1]))):
            dct["nodeListeners"] = dictify(self.node_listeners)
        if dirty and "nodeListeners" in dct:
            del dct["nodeListeners"]
        if "redo_log_size_in_mb" == "type" or (self.redo_log_size_in_mb is not self.__undef__ and (not (dirty and not self._redo_log_size_in_mb[1]))):
            dct["redoLogSizeInMB"] = dictify(self.redo_log_size_in_mb)
        if dirty and "redoLogSizeInMB" in dct:
            del dct["redoLogSizeInMB"]
        if "redo_log_groups" == "type" or (self.redo_log_groups is not self.__undef__ and (not (dirty and not self._redo_log_groups[1]))):
            dct["redoLogGroups"] = dictify(self.redo_log_groups)
        if dirty and "redoLogGroups" in dct:
            del dct["redoLogGroups"]
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._custom_env_vars = (self._custom_env_vars[0], True)
        self._file_mapping_rules = (self._file_mapping_rules[0], True)
        self._operations = (self._operations[0], True)
        self._archivelog_mode = (self._archivelog_mode[0], True)
        self._node_listeners = (self._node_listeners[0], True)
        self._redo_log_size_in_mb = (self._redo_log_size_in_mb[0], True)
        self._redo_log_groups = (self._redo_log_groups[0], True)

    def is_dirty(self):
        return any([self._custom_env_vars[1], self._file_mapping_rules[1], self._operations[1], self._archivelog_mode[1], self._node_listeners[1], self._redo_log_size_in_mb[1], self._redo_log_groups[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleVirtualCdbSource):
            return False
        return super(OracleVirtualCdbSource, self).__eq__(other) and \
               self.custom_env_vars == other.custom_env_vars and \
               self.file_mapping_rules == other.file_mapping_rules and \
               self.operations == other.operations and \
               self.archivelog_mode == other.archivelog_mode and \
               self.node_listeners == other.node_listeners and \
               self.redo_log_size_in_mb == other.redo_log_size_in_mb and \
               self.redo_log_groups == other.redo_log_groups

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            super(OracleVirtualCdbSource, self).__hash__(),
            self.custom_env_vars,
            self.file_mapping_rules,
            self.operations,
            self.archivelog_mode,
            self.node_listeners,
            self.redo_log_size_in_mb,
            self.redo_log_groups,
        )

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def custom_env_vars(self):
        """
        Custom environment variables for Oracle databases. These can only be
        set at the PDB level. Delphix applies the PDB setting to the virtual
        CDB.

        :rtype: ``list`` of :py:class:`v1_10_6.web.vo.OracleCustomEnvVar`
        """
        return self._custom_env_vars[0]

    @property
    def file_mapping_rules(self):
        """
        Database file mapping rules. These can only be set at the PDB level.
        Delphix applies the PDB setting to the virtual CDB.

        :rtype: ``TEXT_TYPE``
        """
        return self._file_mapping_rules[0]

    @property
    def operations(self):
        """
        User-specified operation hooks for this source. This is currently not
        supported for virtual container databases.

        :rtype: :py:class:`v1_10_6.web.vo.VirtualSourceOperations`
        """
        return self._operations[0]

    @property
    def archivelog_mode(self):
        """
        *(default value: True)* Archive Log Mode of the Oracle virtual
        database. NOARCHIVELOG mode is currently not supported for virtual
        container databases.

        :rtype: ``bool``
        """
        return self._archivelog_mode[0]

    @property
    def node_listeners(self):
        """
        A list of object references to Oracle Node Listeners selected for this
        Virtual Database. Delphix picks one default listener from the target
        environment if this list is empty at virtual database provision time.
        This is currently not supported for virtual container databases.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._node_listeners[0]

    @property
    def redo_log_size_in_mb(self):
        """
        Online Redo Log size in MB. Customizing Online Redo Log size is
        currently not supported for virtual container databases.

        :rtype: ``int``
        """
        return self._redo_log_size_in_mb[0]

    @property
    def redo_log_groups(self):
        """
        Number of Online Redo Log Groups. Customizing number of Online Redo Log
        Groups is currently not supported for virtual container databases.

        :rtype: ``int``
        """
        return self._redo_log_groups[0]

