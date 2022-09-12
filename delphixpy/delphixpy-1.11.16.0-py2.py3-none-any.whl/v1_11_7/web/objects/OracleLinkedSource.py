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
#     /delphix-oracle-linked-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.OracleSource import OracleSource
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

class OracleLinkedSource(OracleSource):
    """
    *(extends* :py:class:`v1_11_7.web.vo.OracleSource` *)* A linked Oracle
    source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleLinkedSource, self).__init__()
        self._type = ("OracleLinkedSource", True)
        self._config = (self.__undef__, True)
        self._backup_level_enabled = (self.__undef__, True)
        self._rman_channels = (self.__undef__, True)
        self._files_per_set = (self.__undef__, True)
        self._check_logical = (self.__undef__, True)
        self._external_file_path = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._encrypted_linking_enabled = (self.__undef__, True)
        self._compressed_linking_enabled = (self.__undef__, True)
        self._bandwidth_limit = (self.__undef__, True)
        self._number_of_connections = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleLinkedSource, cls).from_dict(data, dirty, undef_enabled)
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        obj._backup_level_enabled = (data.get("backupLevelEnabled", obj.__undef__), dirty)
        if obj._backup_level_enabled[0] is not None and obj._backup_level_enabled[0] is not obj.__undef__:
            assert isinstance(obj._backup_level_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._backup_level_enabled[0], type(obj._backup_level_enabled[0])))
            common.validate_format(obj._backup_level_enabled[0], "None", None, None)
        obj._rman_channels = (data.get("rmanChannels", obj.__undef__), dirty)
        if obj._rman_channels[0] is not None and obj._rman_channels[0] is not obj.__undef__:
            assert isinstance(obj._rman_channels[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._rman_channels[0], type(obj._rman_channels[0])))
            common.validate_format(obj._rman_channels[0], "None", None, None)
        obj._files_per_set = (data.get("filesPerSet", obj.__undef__), dirty)
        if obj._files_per_set[0] is not None and obj._files_per_set[0] is not obj.__undef__:
            assert isinstance(obj._files_per_set[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._files_per_set[0], type(obj._files_per_set[0])))
            common.validate_format(obj._files_per_set[0], "None", None, None)
        obj._check_logical = (data.get("checkLogical", obj.__undef__), dirty)
        if obj._check_logical[0] is not None and obj._check_logical[0] is not obj.__undef__:
            assert isinstance(obj._check_logical[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._check_logical[0], type(obj._check_logical[0])))
            common.validate_format(obj._check_logical[0], "None", None, None)
        obj._external_file_path = (data.get("externalFilePath", obj.__undef__), dirty)
        if obj._external_file_path[0] is not None and obj._external_file_path[0] is not obj.__undef__:
            assert isinstance(obj._external_file_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._external_file_path[0], type(obj._external_file_path[0])))
            common.validate_format(obj._external_file_path[0], "None", None, 1024)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._encrypted_linking_enabled = (data.get("encryptedLinkingEnabled", obj.__undef__), dirty)
        if obj._encrypted_linking_enabled[0] is not None and obj._encrypted_linking_enabled[0] is not obj.__undef__:
            assert isinstance(obj._encrypted_linking_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._encrypted_linking_enabled[0], type(obj._encrypted_linking_enabled[0])))
            common.validate_format(obj._encrypted_linking_enabled[0], "None", None, None)
        obj._compressed_linking_enabled = (data.get("compressedLinkingEnabled", obj.__undef__), dirty)
        if obj._compressed_linking_enabled[0] is not None and obj._compressed_linking_enabled[0] is not obj.__undef__:
            assert isinstance(obj._compressed_linking_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._compressed_linking_enabled[0], type(obj._compressed_linking_enabled[0])))
            common.validate_format(obj._compressed_linking_enabled[0], "None", None, None)
        obj._bandwidth_limit = (data.get("bandwidthLimit", obj.__undef__), dirty)
        if obj._bandwidth_limit[0] is not None and obj._bandwidth_limit[0] is not obj.__undef__:
            assert isinstance(obj._bandwidth_limit[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._bandwidth_limit[0], type(obj._bandwidth_limit[0])))
            common.validate_format(obj._bandwidth_limit[0], "None", None, None)
        obj._number_of_connections = (data.get("numberOfConnections", obj.__undef__), dirty)
        if obj._number_of_connections[0] is not None and obj._number_of_connections[0] is not obj.__undef__:
            assert isinstance(obj._number_of_connections[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._number_of_connections[0], type(obj._number_of_connections[0])))
            common.validate_format(obj._number_of_connections[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleLinkedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "backup_level_enabled" == "type" or (self.backup_level_enabled is not self.__undef__ and (not (dirty and not self._backup_level_enabled[1]) or isinstance(self.backup_level_enabled, list) or belongs_to_parent)):
            dct["backupLevelEnabled"] = dictify(self.backup_level_enabled)
        if "rman_channels" == "type" or (self.rman_channels is not self.__undef__ and (not (dirty and not self._rman_channels[1]) or isinstance(self.rman_channels, list) or belongs_to_parent)):
            dct["rmanChannels"] = dictify(self.rman_channels)
        elif belongs_to_parent and self.rman_channels is self.__undef__:
            dct["rmanChannels"] = 2
        if "files_per_set" == "type" or (self.files_per_set is not self.__undef__ and (not (dirty and not self._files_per_set[1]) or isinstance(self.files_per_set, list) or belongs_to_parent)):
            dct["filesPerSet"] = dictify(self.files_per_set)
        elif belongs_to_parent and self.files_per_set is self.__undef__:
            dct["filesPerSet"] = 5
        if "check_logical" == "type" or (self.check_logical is not self.__undef__ and (not (dirty and not self._check_logical[1]) or isinstance(self.check_logical, list) or belongs_to_parent)):
            dct["checkLogical"] = dictify(self.check_logical)
        elif belongs_to_parent and self.check_logical is self.__undef__:
            dct["checkLogical"] = False
        if "external_file_path" == "type" or (self.external_file_path is not self.__undef__ and (not (dirty and not self._external_file_path[1]) or isinstance(self.external_file_path, list) or belongs_to_parent)):
            dct["externalFilePath"] = dictify(self.external_file_path)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "encrypted_linking_enabled" == "type" or (self.encrypted_linking_enabled is not self.__undef__ and (not (dirty and not self._encrypted_linking_enabled[1]) or isinstance(self.encrypted_linking_enabled, list) or belongs_to_parent)):
            dct["encryptedLinkingEnabled"] = dictify(self.encrypted_linking_enabled)
        elif belongs_to_parent and self.encrypted_linking_enabled is self.__undef__:
            dct["encryptedLinkingEnabled"] = False
        if "compressed_linking_enabled" == "type" or (self.compressed_linking_enabled is not self.__undef__ and (not (dirty and not self._compressed_linking_enabled[1]) or isinstance(self.compressed_linking_enabled, list) or belongs_to_parent)):
            dct["compressedLinkingEnabled"] = dictify(self.compressed_linking_enabled)
        elif belongs_to_parent and self.compressed_linking_enabled is self.__undef__:
            dct["compressedLinkingEnabled"] = True
        if "bandwidth_limit" == "type" or (self.bandwidth_limit is not self.__undef__ and (not (dirty and not self._bandwidth_limit[1]) or isinstance(self.bandwidth_limit, list) or belongs_to_parent)):
            dct["bandwidthLimit"] = dictify(self.bandwidth_limit)
        elif belongs_to_parent and self.bandwidth_limit is self.__undef__:
            dct["bandwidthLimit"] = 0
        if "number_of_connections" == "type" or (self.number_of_connections is not self.__undef__ and (not (dirty and not self._number_of_connections[1]) or isinstance(self.number_of_connections, list) or belongs_to_parent)):
            dct["numberOfConnections"] = dictify(self.number_of_connections)
        elif belongs_to_parent and self.number_of_connections is self.__undef__:
            dct["numberOfConnections"] = 1
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._backup_level_enabled = (self._backup_level_enabled[0], True)
        self._rman_channels = (self._rman_channels[0], True)
        self._files_per_set = (self._files_per_set[0], True)
        self._check_logical = (self._check_logical[0], True)
        self._external_file_path = (self._external_file_path[0], True)
        self._operations = (self._operations[0], True)
        self._encrypted_linking_enabled = (self._encrypted_linking_enabled[0], True)
        self._compressed_linking_enabled = (self._compressed_linking_enabled[0], True)
        self._bandwidth_limit = (self._bandwidth_limit[0], True)
        self._number_of_connections = (self._number_of_connections[0], True)

    def is_dirty(self):
        return any([self._config[1], self._backup_level_enabled[1], self._rman_channels[1], self._files_per_set[1], self._check_logical[1], self._external_file_path[1], self._operations[1], self._encrypted_linking_enabled[1], self._compressed_linking_enabled[1], self._bandwidth_limit[1], self._number_of_connections[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleLinkedSource):
            return False
        return super(OracleLinkedSource, self).__eq__(other) and \
               self.config == other.config and \
               self.backup_level_enabled == other.backup_level_enabled and \
               self.rman_channels == other.rman_channels and \
               self.files_per_set == other.files_per_set and \
               self.check_logical == other.check_logical and \
               self.external_file_path == other.external_file_path and \
               self.operations == other.operations and \
               self.encrypted_linking_enabled == other.encrypted_linking_enabled and \
               self.compressed_linking_enabled == other.compressed_linking_enabled and \
               self.bandwidth_limit == other.bandwidth_limit and \
               self.number_of_connections == other.number_of_connections

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def config(self):
        """
        Reference to the configuration for the source.

        :rtype: ``TEXT_TYPE``
        """
        return self._config[0]

    @config.setter
    def config(self, value):
        self._config = (value, True)

    @property
    def backup_level_enabled(self):
        """
        Defines whether backup level is enabled.

        :rtype: ``bool``
        """
        return self._backup_level_enabled[0]

    @backup_level_enabled.setter
    def backup_level_enabled(self, value):
        self._backup_level_enabled = (value, True)

    @property
    def rman_channels(self):
        """
        *(default value: 2)* Number of parallel channels to use.

        :rtype: ``int``
        """
        return self._rman_channels[0]

    @rman_channels.setter
    def rman_channels(self, value):
        self._rman_channels = (value, True)

    @property
    def files_per_set(self):
        """
        *(default value: 5)* Number of data files to include in each RMAN
        backup set.

        :rtype: ``int``
        """
        return self._files_per_set[0]

    @files_per_set.setter
    def files_per_set(self, value):
        self._files_per_set = (value, True)

    @property
    def check_logical(self):
        """
        True if extended block checking should be used for this linked
        database.

        :rtype: ``bool``
        """
        return self._check_logical[0]

    @check_logical.setter
    def check_logical(self, value):
        self._check_logical = (value, True)

    @property
    def external_file_path(self):
        """
        External file path.

        :rtype: ``TEXT_TYPE``
        """
        return self._external_file_path[0]

    @external_file_path.setter
    def external_file_path(self, value):
        self._external_file_path = (value, True)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_11_7.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def encrypted_linking_enabled(self):
        """
        True if SnapSync data from the source should be retrieved through an
        encrypted connection. Enabling this feature can decrease the
        performance of SnapSync from the source but has no impact on the
        performance of VDBs created from the retrieved data.

        :rtype: ``bool``
        """
        return self._encrypted_linking_enabled[0]

    @encrypted_linking_enabled.setter
    def encrypted_linking_enabled(self, value):
        self._encrypted_linking_enabled = (value, True)

    @property
    def compressed_linking_enabled(self):
        """
        *(default value: True)* True if SnapSync data from the source should be
        compressed over the network. Enabling this feature will reduce network
        bandwidth consumption and may significantly improve throughput,
        especially over slow network.

        :rtype: ``bool``
        """
        return self._compressed_linking_enabled[0]

    @compressed_linking_enabled.setter
    def compressed_linking_enabled(self, value):
        self._compressed_linking_enabled = (value, True)

    @property
    def bandwidth_limit(self):
        """
        Bandwidth limit (MB/s) for SnapSync and LogSync network traffic. A
        value of 0 means no limit.

        :rtype: ``int``
        """
        return self._bandwidth_limit[0]

    @bandwidth_limit.setter
    def bandwidth_limit(self, value):
        self._bandwidth_limit = (value, True)

    @property
    def number_of_connections(self):
        """
        *(default value: 1)* Total number of transport connections to use
        during SnapSync.

        :rtype: ``int``
        """
        return self._number_of_connections[0]

    @number_of_connections.setter
    def number_of_connections(self, value):
        self._number_of_connections = (value, True)

