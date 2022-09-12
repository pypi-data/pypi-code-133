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
#     /delphix-oracle-virtual-pdb-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_4.web.objects.OracleVirtualSource import OracleVirtualSource
from delphixpy.v1_10_4 import common

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

class OracleVirtualPdbSource(OracleVirtualSource):
    """
    *(extends* :py:class:`v1_10_4.web.vo.OracleVirtualSource` *)* A virtual
    Oracle multitenant pluggable database source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleVirtualPdbSource, self).__init__()
        self._type = ("OracleVirtualPdbSource", True)
        self._archivelog_mode = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._config_template = (self.__undef__, True)
        self._node_listeners = (self.__undef__, True)
        self._redo_log_size_in_mb = (self.__undef__, True)
        self._redo_log_groups = (self.__undef__, True)

    API_VERSION = "1.10.4"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleVirtualPdbSource, cls).from_dict(data, dirty, undef_enabled)
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
        dct = super(OracleVirtualPdbSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "archivelog_mode" == "type" or (self.archivelog_mode is not self.__undef__ and (not (dirty and not self._archivelog_mode[1]))):
            dct["archivelogMode"] = dictify(self.archivelog_mode)
        if dirty and "archivelogMode" in dct:
            del dct["archivelogMode"]
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]))):
            dct["configParams"] = dictify(self.config_params)
        if dirty and "configParams" in dct:
            del dct["configParams"]
        if "config_template" == "type" or (self.config_template is not self.__undef__ and (not (dirty and not self._config_template[1]))):
            dct["configTemplate"] = dictify(self.config_template)
        if dirty and "configTemplate" in dct:
            del dct["configTemplate"]
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
        self._archivelog_mode = (self._archivelog_mode[0], True)
        self._config_params = (self._config_params[0], True)
        self._config_template = (self._config_template[0], True)
        self._node_listeners = (self._node_listeners[0], True)
        self._redo_log_size_in_mb = (self._redo_log_size_in_mb[0], True)
        self._redo_log_groups = (self._redo_log_groups[0], True)

    def is_dirty(self):
        return any([self._archivelog_mode[1], self._config_params[1], self._config_template[1], self._node_listeners[1], self._redo_log_size_in_mb[1], self._redo_log_groups[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleVirtualPdbSource):
            return False
        return super(OracleVirtualPdbSource, self).__eq__(other) and \
               self.archivelog_mode == other.archivelog_mode and \
               self.config_params == other.config_params and \
               self.config_template == other.config_template and \
               self.node_listeners == other.node_listeners and \
               self.redo_log_size_in_mb == other.redo_log_size_in_mb and \
               self.redo_log_groups == other.redo_log_groups

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            super(OracleVirtualPdbSource, self).__hash__(),
            self.archivelog_mode,
            self.config_params,
            self.config_template,
            self.node_listeners,
            self.redo_log_size_in_mb,
            self.redo_log_groups,
        )

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def archivelog_mode(self):
        """
        Archive Log Mode of the Oracle virtual database. This is not applicable
        to pluggable databases.

        :rtype: ``bool``
        """
        return self._archivelog_mode[0]

    @property
    def config_params(self):
        """
        Oracle database configuration parameter overrides. This is currently
        not supported for pluggable databases.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @property
    def config_template(self):
        """
        Optional database template to use for provisioning and refresh. If set,
        configParams will be ignored on provision or refresh. This is currently
        not supported for pluggable databases.

        :rtype: ``TEXT_TYPE``
        """
        return self._config_template[0]

    @property
    def node_listeners(self):
        """
        A list of object references to Oracle Node Listeners selected for this
        Virtual Database. Delphix picks one default listener from the target
        environment if this list is empty at virtual database provision time.
        This is not applicable to pluggable databases.

        :rtype: ``list`` of ``TEXT_TYPE``
        """
        return self._node_listeners[0]

    @property
    def redo_log_size_in_mb(self):
        """
        Online Redo Log size in MB. This is not applicable to pluggable
        databases.

        :rtype: ``int``
        """
        return self._redo_log_size_in_mb[0]

    @property
    def redo_log_groups(self):
        """
        Number of Online Redo Log Groups. This is not applicable to pluggable
        databases.

        :rtype: ``int``
        """
        return self._redo_log_groups[0]

