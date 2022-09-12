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
#     /delphix-mssql-link-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_9_2.web.objects.LinkData import LinkData
from delphixpy.v1_9_2 import factory
from delphixpy.v1_9_2 import common

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

class MSSqlLinkData(LinkData):
    """
    *(extends* :py:class:`v1_9_2.web.vo.LinkData` *)* MSSQL specific parameters
    for a link request.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlLinkData, self).__init__()
        self._type = ("MSSqlLinkData", True)
        self._config = (self.__undef__, True)
        self._external_file_path = (self.__undef__, True)
        self._shared_backup_location = (self.__undef__, True)
        self._backup_location_user = (self.__undef__, True)
        self._backup_location_credentials = (self.__undef__, True)
        self._encryption_key = (self.__undef__, True)
        self._sync_parameters = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._source_host_user = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._db_credentials = (self.__undef__, True)
        self._ppt_repository = (self.__undef__, True)
        self._ppt_host_user = (self.__undef__, True)
        self._staging_pre_script = (self.__undef__, True)
        self._staging_post_script = (self.__undef__, True)
        self._ingestion_strategy = (self.__undef__, True)
        self._mssql_netbackup_config = (self.__undef__, True)

    API_VERSION = "1.9.2"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlLinkData, cls).from_dict(data, dirty, undef_enabled)
        if "config" not in data:
            raise ValueError("Missing required property \"config\".")
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        obj._external_file_path = (data.get("externalFilePath", obj.__undef__), dirty)
        if obj._external_file_path[0] is not None and obj._external_file_path[0] is not obj.__undef__:
            assert isinstance(obj._external_file_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._external_file_path[0], type(obj._external_file_path[0])))
            common.validate_format(obj._external_file_path[0], "None", None, 1024)
        obj._shared_backup_location = (data.get("sharedBackupLocation", obj.__undef__), dirty)
        if obj._shared_backup_location[0] is not None and obj._shared_backup_location[0] is not obj.__undef__:
            assert isinstance(obj._shared_backup_location[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._shared_backup_location[0], type(obj._shared_backup_location[0])))
            common.validate_format(obj._shared_backup_location[0], "None", None, 260)
        obj._backup_location_user = (data.get("backupLocationUser", obj.__undef__), dirty)
        if obj._backup_location_user[0] is not None and obj._backup_location_user[0] is not obj.__undef__:
            assert isinstance(obj._backup_location_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_location_user[0], type(obj._backup_location_user[0])))
            common.validate_format(obj._backup_location_user[0], "None", None, 256)
        if "backupLocationCredentials" in data and data["backupLocationCredentials"] is not None:
            obj._backup_location_credentials = (factory.create_object(data["backupLocationCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._backup_location_credentials[0], "PasswordCredential")
        else:
            obj._backup_location_credentials = (obj.__undef__, dirty)
        obj._encryption_key = (data.get("encryptionKey", obj.__undef__), dirty)
        if obj._encryption_key[0] is not None and obj._encryption_key[0] is not obj.__undef__:
            assert isinstance(obj._encryption_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._encryption_key[0], type(obj._encryption_key[0])))
            common.validate_format(obj._encryption_key[0], "None", None, None)
        if "syncParameters" not in data:
            raise ValueError("Missing required property \"syncParameters\".")
        if "syncParameters" in data and data["syncParameters"] is not None:
            obj._sync_parameters = (factory.create_object(data["syncParameters"], "MSSqlSyncParameters"), dirty)
            factory.validate_type(obj._sync_parameters[0], "MSSqlSyncParameters")
        else:
            obj._sync_parameters = (obj.__undef__, dirty)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._source_host_user = (data.get("sourceHostUser", obj.__undef__), dirty)
        if obj._source_host_user[0] is not None and obj._source_host_user[0] is not obj.__undef__:
            assert isinstance(obj._source_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_host_user[0], type(obj._source_host_user[0])))
            common.validate_format(obj._source_host_user[0], "objectReference", None, None)
        if "dbUser" not in data:
            raise ValueError("Missing required property \"dbUser\".")
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, None)
        if "dbCredentials" not in data:
            raise ValueError("Missing required property \"dbCredentials\".")
        if "dbCredentials" in data and data["dbCredentials"] is not None:
            obj._db_credentials = (factory.create_object(data["dbCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._db_credentials[0], "PasswordCredential")
        else:
            obj._db_credentials = (obj.__undef__, dirty)
        if "pptRepository" not in data:
            raise ValueError("Missing required property \"pptRepository\".")
        obj._ppt_repository = (data.get("pptRepository", obj.__undef__), dirty)
        if obj._ppt_repository[0] is not None and obj._ppt_repository[0] is not obj.__undef__:
            assert isinstance(obj._ppt_repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ppt_repository[0], type(obj._ppt_repository[0])))
            common.validate_format(obj._ppt_repository[0], "objectReference", None, None)
        obj._ppt_host_user = (data.get("pptHostUser", obj.__undef__), dirty)
        if obj._ppt_host_user[0] is not None and obj._ppt_host_user[0] is not obj.__undef__:
            assert isinstance(obj._ppt_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._ppt_host_user[0], type(obj._ppt_host_user[0])))
            common.validate_format(obj._ppt_host_user[0], "objectReference", None, None)
        obj._staging_pre_script = (data.get("stagingPreScript", obj.__undef__), dirty)
        if obj._staging_pre_script[0] is not None and obj._staging_pre_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_pre_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_pre_script[0], type(obj._staging_pre_script[0])))
            common.validate_format(obj._staging_pre_script[0], "None", None, 1024)
        obj._staging_post_script = (data.get("stagingPostScript", obj.__undef__), dirty)
        if obj._staging_post_script[0] is not None and obj._staging_post_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_post_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_post_script[0], type(obj._staging_post_script[0])))
            common.validate_format(obj._staging_post_script[0], "None", None, 1024)
        if "ingestionStrategy" in data and data["ingestionStrategy"] is not None:
            obj._ingestion_strategy = (factory.create_object(data["ingestionStrategy"], "IngestionStrategy"), dirty)
            factory.validate_type(obj._ingestion_strategy[0], "IngestionStrategy")
        else:
            obj._ingestion_strategy = (obj.__undef__, dirty)
        if "mssqlNetbackupConfig" in data and data["mssqlNetbackupConfig"] is not None:
            obj._mssql_netbackup_config = (factory.create_object(data["mssqlNetbackupConfig"], "MSSqlNetbackupConfig"), dirty)
            factory.validate_type(obj._mssql_netbackup_config[0], "MSSqlNetbackupConfig")
        else:
            obj._mssql_netbackup_config = (obj.__undef__, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlLinkData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "external_file_path" == "type" or (self.external_file_path is not self.__undef__ and (not (dirty and not self._external_file_path[1]) or isinstance(self.external_file_path, list) or belongs_to_parent)):
            dct["externalFilePath"] = dictify(self.external_file_path)
        if "shared_backup_location" == "type" or (self.shared_backup_location is not self.__undef__ and (not (dirty and not self._shared_backup_location[1]) or isinstance(self.shared_backup_location, list) or belongs_to_parent)):
            dct["sharedBackupLocation"] = dictify(self.shared_backup_location)
        if "backup_location_user" == "type" or (self.backup_location_user is not self.__undef__ and (not (dirty and not self._backup_location_user[1]) or isinstance(self.backup_location_user, list) or belongs_to_parent)):
            dct["backupLocationUser"] = dictify(self.backup_location_user)
        if "backup_location_credentials" == "type" or (self.backup_location_credentials is not self.__undef__ and (not (dirty and not self._backup_location_credentials[1]) or isinstance(self.backup_location_credentials, list) or belongs_to_parent)):
            dct["backupLocationCredentials"] = dictify(self.backup_location_credentials, prop_is_list_or_vo=True)
        if "encryption_key" == "type" or (self.encryption_key is not self.__undef__ and (not (dirty and not self._encryption_key[1]) or isinstance(self.encryption_key, list) or belongs_to_parent)):
            dct["encryptionKey"] = dictify(self.encryption_key)
        if "sync_parameters" == "type" or (self.sync_parameters is not self.__undef__ and (not (dirty and not self._sync_parameters[1]) or isinstance(self.sync_parameters, list) or belongs_to_parent)):
            dct["syncParameters"] = dictify(self.sync_parameters, prop_is_list_or_vo=True)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "source_host_user" == "type" or (self.source_host_user is not self.__undef__ and (not (dirty and not self._source_host_user[1]) or isinstance(self.source_host_user, list) or belongs_to_parent)):
            dct["sourceHostUser"] = dictify(self.source_host_user)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "db_credentials" == "type" or (self.db_credentials is not self.__undef__ and (not (dirty and not self._db_credentials[1]) or isinstance(self.db_credentials, list) or belongs_to_parent)):
            dct["dbCredentials"] = dictify(self.db_credentials, prop_is_list_or_vo=True)
        if "ppt_repository" == "type" or (self.ppt_repository is not self.__undef__ and (not (dirty and not self._ppt_repository[1]) or isinstance(self.ppt_repository, list) or belongs_to_parent)):
            dct["pptRepository"] = dictify(self.ppt_repository)
        if "ppt_host_user" == "type" or (self.ppt_host_user is not self.__undef__ and (not (dirty and not self._ppt_host_user[1]) or isinstance(self.ppt_host_user, list) or belongs_to_parent)):
            dct["pptHostUser"] = dictify(self.ppt_host_user)
        if "staging_pre_script" == "type" or (self.staging_pre_script is not self.__undef__ and (not (dirty and not self._staging_pre_script[1]) or isinstance(self.staging_pre_script, list) or belongs_to_parent)):
            dct["stagingPreScript"] = dictify(self.staging_pre_script)
        if "staging_post_script" == "type" or (self.staging_post_script is not self.__undef__ and (not (dirty and not self._staging_post_script[1]) or isinstance(self.staging_post_script, list) or belongs_to_parent)):
            dct["stagingPostScript"] = dictify(self.staging_post_script)
        if "ingestion_strategy" == "type" or (self.ingestion_strategy is not self.__undef__ and (not (dirty and not self._ingestion_strategy[1]) or isinstance(self.ingestion_strategy, list) or belongs_to_parent)):
            dct["ingestionStrategy"] = dictify(self.ingestion_strategy, prop_is_list_or_vo=True)
        if "mssql_netbackup_config" == "type" or (self.mssql_netbackup_config is not self.__undef__ and (not (dirty and not self._mssql_netbackup_config[1]) or isinstance(self.mssql_netbackup_config, list) or belongs_to_parent)):
            dct["mssqlNetbackupConfig"] = dictify(self.mssql_netbackup_config)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._external_file_path = (self._external_file_path[0], True)
        self._shared_backup_location = (self._shared_backup_location[0], True)
        self._backup_location_user = (self._backup_location_user[0], True)
        self._backup_location_credentials = (self._backup_location_credentials[0], True)
        self._encryption_key = (self._encryption_key[0], True)
        self._sync_parameters = (self._sync_parameters[0], True)
        self._operations = (self._operations[0], True)
        self._source_host_user = (self._source_host_user[0], True)
        self._db_user = (self._db_user[0], True)
        self._db_credentials = (self._db_credentials[0], True)
        self._ppt_repository = (self._ppt_repository[0], True)
        self._ppt_host_user = (self._ppt_host_user[0], True)
        self._staging_pre_script = (self._staging_pre_script[0], True)
        self._staging_post_script = (self._staging_post_script[0], True)
        self._ingestion_strategy = (self._ingestion_strategy[0], True)
        self._mssql_netbackup_config = (self._mssql_netbackup_config[0], True)

    def is_dirty(self):
        return any([self._config[1], self._external_file_path[1], self._shared_backup_location[1], self._backup_location_user[1], self._backup_location_credentials[1], self._encryption_key[1], self._sync_parameters[1], self._operations[1], self._source_host_user[1], self._db_user[1], self._db_credentials[1], self._ppt_repository[1], self._ppt_host_user[1], self._staging_pre_script[1], self._staging_post_script[1], self._ingestion_strategy[1], self._mssql_netbackup_config[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlLinkData):
            return False
        return super(MSSqlLinkData, self).__eq__(other) and \
               self.config == other.config and \
               self.external_file_path == other.external_file_path and \
               self.shared_backup_location == other.shared_backup_location and \
               self.backup_location_user == other.backup_location_user and \
               self.backup_location_credentials == other.backup_location_credentials and \
               self.encryption_key == other.encryption_key and \
               self.sync_parameters == other.sync_parameters and \
               self.operations == other.operations and \
               self.source_host_user == other.source_host_user and \
               self.db_user == other.db_user and \
               self.db_credentials == other.db_credentials and \
               self.ppt_repository == other.ppt_repository and \
               self.ppt_host_user == other.ppt_host_user and \
               self.staging_pre_script == other.staging_pre_script and \
               self.staging_post_script == other.staging_post_script and \
               self.ingestion_strategy == other.ingestion_strategy and \
               self.mssql_netbackup_config == other.mssql_netbackup_config

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
    def shared_backup_location(self):
        """
        Shared source database backup location.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._shared_backup_location[0]

    @shared_backup_location.setter
    def shared_backup_location(self, value):
        self._shared_backup_location = (value, True)

    @property
    def backup_location_user(self):
        """
        The user for accessing the shared backup location.

        :rtype: ``TEXT_TYPE``
        """
        return self._backup_location_user[0]

    @backup_location_user.setter
    def backup_location_user(self, value):
        self._backup_location_user = (value, True)

    @property
    def backup_location_credentials(self):
        """
        The password for accessing the shared backup location.

        :rtype: :py:class:`v1_9_2.web.vo.PasswordCredential`
        """
        return self._backup_location_credentials[0]

    @backup_location_credentials.setter
    def backup_location_credentials(self, value):
        self._backup_location_credentials = (value, True)

    @property
    def encryption_key(self):
        """
        The encryption key to use when restoring encrypted backups.

        :rtype: ``TEXT_TYPE``
        """
        return self._encryption_key[0]

    @encryption_key.setter
    def encryption_key(self, value):
        self._encryption_key = (value, True)

    @property
    def sync_parameters(self):
        """
        Sync parameters for the container.

        :rtype: :py:class:`v1_9_2.web.vo.MSSqlSyncParameters`
        """
        return self._sync_parameters[0]

    @sync_parameters.setter
    def sync_parameters(self, value):
        self._sync_parameters = (value, True)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_9_2.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def source_host_user(self):
        """
        Information about the host OS user on the source to use for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._source_host_user[0]

    @source_host_user.setter
    def source_host_user(self, value):
        self._source_host_user = (value, True)

    @property
    def db_user(self):
        """
        The user name for the source DB user.

        :rtype: ``TEXT_TYPE``
        """
        return self._db_user[0]

    @db_user.setter
    def db_user(self, value):
        self._db_user = (value, True)

    @property
    def db_credentials(self):
        """
        The credential for the source DB user.

        :rtype: :py:class:`v1_9_2.web.vo.PasswordCredential`
        """
        return self._db_credentials[0]

    @db_credentials.setter
    def db_credentials(self, value):
        self._db_credentials = (value, True)

    @property
    def ppt_repository(self):
        """
        The SQL instance on the PPT environment that we want to use for pre-
        provisioning.

        :rtype: ``TEXT_TYPE``
        """
        return self._ppt_repository[0]

    @ppt_repository.setter
    def ppt_repository(self, value):
        self._ppt_repository = (value, True)

    @property
    def ppt_host_user(self):
        """
        Information about the host OS user on the PPT host to use for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._ppt_host_user[0]

    @ppt_host_user.setter
    def ppt_host_user(self, value):
        self._ppt_host_user = (value, True)

    @property
    def staging_pre_script(self):
        """
        A user-provided PowerShell script or executable to run prior to
        restoring from a backup during pre-provisioning.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_pre_script[0]

    @staging_pre_script.setter
    def staging_pre_script(self, value):
        self._staging_pre_script = (value, True)

    @property
    def staging_post_script(self):
        """
        A user-provided PowerShell script or executable to run after restoring
        from a backup during pre-provisioning.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_post_script[0]

    @staging_post_script.setter
    def staging_post_script(self, value):
        self._staging_post_script = (value, True)

    @property
    def ingestion_strategy(self):
        """
        Configuration that determines what ingestion strategy the source will
        use.

        :rtype: :py:class:`v1_9_2.web.vo.IngestionStrategy`
        """
        return self._ingestion_strategy[0]

    @ingestion_strategy.setter
    def ingestion_strategy(self, value):
        self._ingestion_strategy = (value, True)

    @property
    def mssql_netbackup_config(self):
        """
        Configuration for source that allows ingesting NetBackup backups for
        SQL Server.

        :rtype: :py:class:`v1_9_2.web.vo.MSSqlNetbackupConfig`
        """
        return self._mssql_netbackup_config[0]

    @mssql_netbackup_config.setter
    def mssql_netbackup_config(self, value):
        self._mssql_netbackup_config = (value, True)

