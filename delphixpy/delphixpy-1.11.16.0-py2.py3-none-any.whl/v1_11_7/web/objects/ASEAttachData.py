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
#     /delphix-ase-attach-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_7.web.objects.AttachData import AttachData
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

class ASEAttachData(AttachData):
    """
    *(extends* :py:class:`v1_11_7.web.vo.AttachData` *)* Represents the SAP ASE
    specific parameters of an attach request.
    """
    def __init__(self, undef_enabled=True):
        super(ASEAttachData, self).__init__()
        self._type = ("ASEAttachData", True)
        self._config = (self.__undef__, True)
        self._external_file_path = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._mount_base = (self.__undef__, True)
        self._load_backup_path = (self.__undef__, True)
        self._load_location = (self.__undef__, True)
        self._dump_credentials = (self.__undef__, True)
        self._source_host_user = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._db_credentials = (self.__undef__, True)
        self._staging_repository = (self.__undef__, True)
        self._staging_host_user = (self.__undef__, True)
        self._staging_pre_script = (self.__undef__, True)
        self._staging_post_script = (self.__undef__, True)
        self._staging_operations = (self.__undef__, True)
        self._validated_sync_mode = (self.__undef__, True)
        self._dump_history_file_enabled = (self.__undef__, True)

    API_VERSION = "1.11.7"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEAttachData, cls).from_dict(data, dirty, undef_enabled)
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
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._mount_base = (data.get("mountBase", obj.__undef__), dirty)
        if obj._mount_base[0] is not None and obj._mount_base[0] is not obj.__undef__:
            assert isinstance(obj._mount_base[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._mount_base[0], type(obj._mount_base[0])))
            common.validate_format(obj._mount_base[0], "None", None, 87)
        if "loadBackupPath" not in data:
            raise ValueError("Missing required property \"loadBackupPath\".")
        obj._load_backup_path = (data.get("loadBackupPath", obj.__undef__), dirty)
        if obj._load_backup_path[0] is not None and obj._load_backup_path[0] is not obj.__undef__:
            assert isinstance(obj._load_backup_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._load_backup_path[0], type(obj._load_backup_path[0])))
            common.validate_format(obj._load_backup_path[0], "None", None, 1024)
        if "loadLocation" in data and data["loadLocation"] is not None:
            obj._load_location = (factory.create_object(data["loadLocation"], "ASEBackupLocation"), dirty)
            factory.validate_type(obj._load_location[0], "ASEBackupLocation")
        else:
            obj._load_location = (obj.__undef__, dirty)
        if "dumpCredentials" in data and data["dumpCredentials"] is not None:
            obj._dump_credentials = (factory.create_object(data["dumpCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._dump_credentials[0], "PasswordCredential")
        else:
            obj._dump_credentials = (obj.__undef__, dirty)
        if "sourceHostUser" not in data:
            raise ValueError("Missing required property \"sourceHostUser\".")
        obj._source_host_user = (data.get("sourceHostUser", obj.__undef__), dirty)
        if obj._source_host_user[0] is not None and obj._source_host_user[0] is not obj.__undef__:
            assert isinstance(obj._source_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._source_host_user[0], type(obj._source_host_user[0])))
            common.validate_format(obj._source_host_user[0], "objectReference", None, None)
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, None)
        if "dbCredentials" not in data:
            raise ValueError("Missing required property \"dbCredentials\".")
        if "dbCredentials" in data and data["dbCredentials"] is not None:
            obj._db_credentials = (factory.create_object(data["dbCredentials"], "Credential"), dirty)
            factory.validate_type(obj._db_credentials[0], "Credential")
        else:
            obj._db_credentials = (obj.__undef__, dirty)
        if "stagingRepository" not in data:
            raise ValueError("Missing required property \"stagingRepository\".")
        obj._staging_repository = (data.get("stagingRepository", obj.__undef__), dirty)
        if obj._staging_repository[0] is not None and obj._staging_repository[0] is not obj.__undef__:
            assert isinstance(obj._staging_repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_repository[0], type(obj._staging_repository[0])))
            common.validate_format(obj._staging_repository[0], "objectReference", None, None)
        if "stagingHostUser" not in data:
            raise ValueError("Missing required property \"stagingHostUser\".")
        obj._staging_host_user = (data.get("stagingHostUser", obj.__undef__), dirty)
        if obj._staging_host_user[0] is not None and obj._staging_host_user[0] is not obj.__undef__:
            assert isinstance(obj._staging_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_host_user[0], type(obj._staging_host_user[0])))
            common.validate_format(obj._staging_host_user[0], "objectReference", None, None)
        obj._staging_pre_script = (data.get("stagingPreScript", obj.__undef__), dirty)
        if obj._staging_pre_script[0] is not None and obj._staging_pre_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_pre_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_pre_script[0], type(obj._staging_pre_script[0])))
            common.validate_format(obj._staging_pre_script[0], "None", None, 1024)
        obj._staging_post_script = (data.get("stagingPostScript", obj.__undef__), dirty)
        if obj._staging_post_script[0] is not None and obj._staging_post_script[0] is not obj.__undef__:
            assert isinstance(obj._staging_post_script[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_post_script[0], type(obj._staging_post_script[0])))
            common.validate_format(obj._staging_post_script[0], "None", None, 1024)
        if "stagingOperations" in data and data["stagingOperations"] is not None:
            obj._staging_operations = (factory.create_object(data["stagingOperations"], "StagingSourceOperations"), dirty)
            factory.validate_type(obj._staging_operations[0], "StagingSourceOperations")
        else:
            obj._staging_operations = (obj.__undef__, dirty)
        obj._validated_sync_mode = (data.get("validatedSyncMode", obj.__undef__), dirty)
        if obj._validated_sync_mode[0] is not None and obj._validated_sync_mode[0] is not obj.__undef__:
            assert isinstance(obj._validated_sync_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._validated_sync_mode[0], type(obj._validated_sync_mode[0])))
            assert obj._validated_sync_mode[0] in ['ENABLED', 'DISABLED'], "Expected enum ['ENABLED', 'DISABLED'] but got %s" % obj._validated_sync_mode[0]
            common.validate_format(obj._validated_sync_mode[0], "None", None, None)
        obj._dump_history_file_enabled = (data.get("dumpHistoryFileEnabled", obj.__undef__), dirty)
        if obj._dump_history_file_enabled[0] is not None and obj._dump_history_file_enabled[0] is not obj.__undef__:
            assert isinstance(obj._dump_history_file_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._dump_history_file_enabled[0], type(obj._dump_history_file_enabled[0])))
            common.validate_format(obj._dump_history_file_enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEAttachData, self).to_dict(dirty, belongs_to_parent)

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
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "mount_base" == "type" or (self.mount_base is not self.__undef__ and (not (dirty and not self._mount_base[1]) or isinstance(self.mount_base, list) or belongs_to_parent)):
            dct["mountBase"] = dictify(self.mount_base)
        if "load_backup_path" == "type" or (self.load_backup_path is not self.__undef__ and (not (dirty and not self._load_backup_path[1]) or isinstance(self.load_backup_path, list) or belongs_to_parent)):
            dct["loadBackupPath"] = dictify(self.load_backup_path)
        if "load_location" == "type" or (self.load_location is not self.__undef__ and (not (dirty and not self._load_location[1]) or isinstance(self.load_location, list) or belongs_to_parent)):
            dct["loadLocation"] = dictify(self.load_location)
        if "dump_credentials" == "type" or (self.dump_credentials is not self.__undef__ and (not (dirty and not self._dump_credentials[1]) or isinstance(self.dump_credentials, list) or belongs_to_parent)):
            dct["dumpCredentials"] = dictify(self.dump_credentials)
        if "source_host_user" == "type" or (self.source_host_user is not self.__undef__ and (not (dirty and not self._source_host_user[1]) or isinstance(self.source_host_user, list) or belongs_to_parent)):
            dct["sourceHostUser"] = dictify(self.source_host_user)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "db_credentials" == "type" or (self.db_credentials is not self.__undef__ and (not (dirty and not self._db_credentials[1]) or isinstance(self.db_credentials, list) or belongs_to_parent)):
            dct["dbCredentials"] = dictify(self.db_credentials, prop_is_list_or_vo=True)
        if "staging_repository" == "type" or (self.staging_repository is not self.__undef__ and (not (dirty and not self._staging_repository[1]) or isinstance(self.staging_repository, list) or belongs_to_parent)):
            dct["stagingRepository"] = dictify(self.staging_repository)
        if "staging_host_user" == "type" or (self.staging_host_user is not self.__undef__ and (not (dirty and not self._staging_host_user[1]) or isinstance(self.staging_host_user, list) or belongs_to_parent)):
            dct["stagingHostUser"] = dictify(self.staging_host_user)
        if "staging_pre_script" == "type" or (self.staging_pre_script is not self.__undef__ and (not (dirty and not self._staging_pre_script[1]) or isinstance(self.staging_pre_script, list) or belongs_to_parent)):
            dct["stagingPreScript"] = dictify(self.staging_pre_script)
        if "staging_post_script" == "type" or (self.staging_post_script is not self.__undef__ and (not (dirty and not self._staging_post_script[1]) or isinstance(self.staging_post_script, list) or belongs_to_parent)):
            dct["stagingPostScript"] = dictify(self.staging_post_script)
        if "staging_operations" == "type" or (self.staging_operations is not self.__undef__ and (not (dirty and not self._staging_operations[1]) or isinstance(self.staging_operations, list) or belongs_to_parent)):
            dct["stagingOperations"] = dictify(self.staging_operations, prop_is_list_or_vo=True)
        if "validated_sync_mode" == "type" or (self.validated_sync_mode is not self.__undef__ and (not (dirty and not self._validated_sync_mode[1]) or isinstance(self.validated_sync_mode, list) or belongs_to_parent)):
            dct["validatedSyncMode"] = dictify(self.validated_sync_mode)
        elif belongs_to_parent and self.validated_sync_mode is self.__undef__:
            dct["validatedSyncMode"] = "ENABLED"
        if "dump_history_file_enabled" == "type" or (self.dump_history_file_enabled is not self.__undef__ and (not (dirty and not self._dump_history_file_enabled[1]) or isinstance(self.dump_history_file_enabled, list) or belongs_to_parent)):
            dct["dumpHistoryFileEnabled"] = dictify(self.dump_history_file_enabled)
        elif belongs_to_parent and self.dump_history_file_enabled is self.__undef__:
            dct["dumpHistoryFileEnabled"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._external_file_path = (self._external_file_path[0], True)
        self._operations = (self._operations[0], True)
        self._mount_base = (self._mount_base[0], True)
        self._load_backup_path = (self._load_backup_path[0], True)
        self._load_location = (self._load_location[0], True)
        self._dump_credentials = (self._dump_credentials[0], True)
        self._source_host_user = (self._source_host_user[0], True)
        self._db_user = (self._db_user[0], True)
        self._db_credentials = (self._db_credentials[0], True)
        self._staging_repository = (self._staging_repository[0], True)
        self._staging_host_user = (self._staging_host_user[0], True)
        self._staging_pre_script = (self._staging_pre_script[0], True)
        self._staging_post_script = (self._staging_post_script[0], True)
        self._staging_operations = (self._staging_operations[0], True)
        self._validated_sync_mode = (self._validated_sync_mode[0], True)
        self._dump_history_file_enabled = (self._dump_history_file_enabled[0], True)

    def is_dirty(self):
        return any([self._config[1], self._external_file_path[1], self._operations[1], self._mount_base[1], self._load_backup_path[1], self._load_location[1], self._dump_credentials[1], self._source_host_user[1], self._db_user[1], self._db_credentials[1], self._staging_repository[1], self._staging_host_user[1], self._staging_pre_script[1], self._staging_post_script[1], self._staging_operations[1], self._validated_sync_mode[1], self._dump_history_file_enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEAttachData):
            return False
        return super(ASEAttachData, self).__eq__(other) and \
               self.config == other.config and \
               self.external_file_path == other.external_file_path and \
               self.operations == other.operations and \
               self.mount_base == other.mount_base and \
               self.load_backup_path == other.load_backup_path and \
               self.load_location == other.load_location and \
               self.dump_credentials == other.dump_credentials and \
               self.source_host_user == other.source_host_user and \
               self.db_user == other.db_user and \
               self.db_credentials == other.db_credentials and \
               self.staging_repository == other.staging_repository and \
               self.staging_host_user == other.staging_host_user and \
               self.staging_pre_script == other.staging_pre_script and \
               self.staging_post_script == other.staging_post_script and \
               self.staging_operations == other.staging_operations and \
               self.validated_sync_mode == other.validated_sync_mode and \
               self.dump_history_file_enabled == other.dump_history_file_enabled

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
    def load_backup_path(self):
        """
        Source database backup location.

        :rtype: ``TEXT_TYPE``
        """
        return self._load_backup_path[0]

    @load_backup_path.setter
    def load_backup_path(self, value):
        self._load_backup_path = (value, True)

    @property
    def load_location(self):
        """
        Backup location to use for loading backups from the source.

        :rtype: :py:class:`v1_11_7.web.vo.ASEBackupLocation`
        """
        return self._load_location[0]

    @load_location.setter
    def load_location(self, value):
        self._load_location = (value, True)

    @property
    def dump_credentials(self):
        """
        The credential for the source DB user.

        :rtype: :py:class:`v1_11_7.web.vo.PasswordCredential`
        """
        return self._dump_credentials[0]

    @dump_credentials.setter
    def dump_credentials(self, value):
        self._dump_credentials = (value, True)

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
        The credentials of the database user.

        :rtype: :py:class:`v1_11_7.web.vo.Credential`
        """
        return self._db_credentials[0]

    @db_credentials.setter
    def db_credentials(self, value):
        self._db_credentials = (value, True)

    @property
    def staging_repository(self):
        """
        The SAP ASE instance on the staging environment that we want to use for
        validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_repository[0]

    @staging_repository.setter
    def staging_repository(self, value):
        self._staging_repository = (value, True)

    @property
    def staging_host_user(self):
        """
        Information about the host OS user on the staging environment to use
        for linking.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_host_user[0]

    @staging_host_user.setter
    def staging_host_user(self, value):
        self._staging_host_user = (value, True)

    @property
    def staging_pre_script(self):
        """
        A user-provided shell script or executable to run prior to restoring
        from a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_pre_script[0]

    @staging_pre_script.setter
    def staging_pre_script(self, value):
        self._staging_pre_script = (value, True)

    @property
    def staging_post_script(self):
        """
        A user-provided shell script or executable to run after restoring from
        a backup during validated sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_post_script[0]

    @staging_post_script.setter
    def staging_post_script(self, value):
        self._staging_post_script = (value, True)

    @property
    def staging_operations(self):
        """
        User-specified operation hooks.

        :rtype: :py:class:`v1_11_7.web.vo.StagingSourceOperations`
        """
        return self._staging_operations[0]

    @staging_operations.setter
    def staging_operations(self, value):
        self._staging_operations = (value, True)

    @property
    def validated_sync_mode(self):
        """
        *(default value: ENABLED)* Specifies the validated sync mode to
        synchronize the dSource with the source database. *(permitted values:
        ENABLED, DISABLED)*

        :rtype: ``TEXT_TYPE``
        """
        return self._validated_sync_mode[0]

    @validated_sync_mode.setter
    def validated_sync_mode(self, value):
        self._validated_sync_mode = (value, True)

    @property
    def dump_history_file_enabled(self):
        """
        Specifies if Dump History File is enabled for backup history detection.

        :rtype: ``bool``
        """
        return self._dump_history_file_enabled[0]

    @dump_history_file_enabled.setter
    def dump_history_file_enabled(self, value):
        self._dump_history_file_enabled = (value, True)

