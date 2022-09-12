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
#     /delphix-mssql-linked-source.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_7_1.web.objects.MSSqlSource import MSSqlSource
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

class MSSqlLinkedSource(MSSqlSource):
    """
    *(extends* :py:class:`v1_7_1.web.vo.MSSqlSource` *)* A linked MSSQL source.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlLinkedSource, self).__init__()
        self._type = ("MSSqlLinkedSource", True)
        self._backup_location_credentials = (self.__undef__, True)
        self._backup_location_user = (self.__undef__, True)
        self._config = (self.__undef__, True)
        self._encryption_key = (self.__undef__, True)
        self._external_file_path = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._shared_backup_location = (self.__undef__, True)
        self._staging_source = (self.__undef__, True)
        self._validated_sync_mode = (self.__undef__, True)

    API_VERSION = "1.7.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlLinkedSource, cls).from_dict(data, dirty, undef_enabled)
        if "backupLocationCredentials" in data and data["backupLocationCredentials"] is not None:
            obj._backup_location_credentials = (factory.create_object(data["backupLocationCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._backup_location_credentials[0], "PasswordCredential")
        else:
            obj._backup_location_credentials = (obj.__undef__, dirty)
        obj._backup_location_user = (data.get("backupLocationUser", obj.__undef__), dirty)
        if obj._backup_location_user[0] is not None and obj._backup_location_user[0] is not obj.__undef__:
            assert isinstance(obj._backup_location_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_location_user[0], type(obj._backup_location_user[0])))
            common.validate_format(obj._backup_location_user[0], "None", None, 256)
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        obj._encryption_key = (data.get("encryptionKey", obj.__undef__), dirty)
        if obj._encryption_key[0] is not None and obj._encryption_key[0] is not obj.__undef__:
            assert isinstance(obj._encryption_key[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._encryption_key[0], type(obj._encryption_key[0])))
            common.validate_format(obj._encryption_key[0], "None", None, None)
        obj._external_file_path = (data.get("externalFilePath", obj.__undef__), dirty)
        if obj._external_file_path[0] is not None and obj._external_file_path[0] is not obj.__undef__:
            assert isinstance(obj._external_file_path[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._external_file_path[0], type(obj._external_file_path[0])))
            common.validate_format(obj._external_file_path[0], "None", None, 1024)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        obj._shared_backup_location = (data.get("sharedBackupLocation", obj.__undef__), dirty)
        if obj._shared_backup_location[0] is not None and obj._shared_backup_location[0] is not obj.__undef__:
            assert isinstance(obj._shared_backup_location[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._shared_backup_location[0], type(obj._shared_backup_location[0])))
            common.validate_format(obj._shared_backup_location[0], "None", None, 260)
        obj._staging_source = (data.get("stagingSource", obj.__undef__), dirty)
        if obj._staging_source[0] is not None and obj._staging_source[0] is not obj.__undef__:
            assert isinstance(obj._staging_source[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_source[0], type(obj._staging_source[0])))
            common.validate_format(obj._staging_source[0], "objectReference", None, None)
        obj._validated_sync_mode = (data.get("validatedSyncMode", obj.__undef__), dirty)
        if obj._validated_sync_mode[0] is not None and obj._validated_sync_mode[0] is not obj.__undef__:
            assert isinstance(obj._validated_sync_mode[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._validated_sync_mode[0], type(obj._validated_sync_mode[0])))
            assert obj._validated_sync_mode[0] in ['TRANSACTION_LOG', 'FULL_OR_DIFFERENTIAL', 'FULL', 'NONE'], "Expected enum ['TRANSACTION_LOG', 'FULL_OR_DIFFERENTIAL', 'FULL', 'NONE'] but got %s" % obj._validated_sync_mode[0]
            common.validate_format(obj._validated_sync_mode[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlLinkedSource, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "backup_location_credentials" == "type" or (self.backup_location_credentials is not self.__undef__ and (not (dirty and not self._backup_location_credentials[1]) or isinstance(self.backup_location_credentials, list) or belongs_to_parent)):
            dct["backupLocationCredentials"] = dictify(self.backup_location_credentials, prop_is_list_or_vo=True)
        if "backup_location_user" == "type" or (self.backup_location_user is not self.__undef__ and (not (dirty and not self._backup_location_user[1]) or isinstance(self.backup_location_user, list) or belongs_to_parent)):
            dct["backupLocationUser"] = dictify(self.backup_location_user)
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "encryption_key" == "type" or (self.encryption_key is not self.__undef__ and (not (dirty and not self._encryption_key[1]) or isinstance(self.encryption_key, list) or belongs_to_parent)):
            dct["encryptionKey"] = dictify(self.encryption_key)
        if "external_file_path" == "type" or (self.external_file_path is not self.__undef__ and (not (dirty and not self._external_file_path[1]) or isinstance(self.external_file_path, list) or belongs_to_parent)):
            dct["externalFilePath"] = dictify(self.external_file_path)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "shared_backup_location" == "type" or (self.shared_backup_location is not self.__undef__ and (not (dirty and not self._shared_backup_location[1]) or isinstance(self.shared_backup_location, list) or belongs_to_parent)):
            dct["sharedBackupLocation"] = dictify(self.shared_backup_location)
        if "staging_source" == "type" or (self.staging_source is not self.__undef__ and (not (dirty and not self._staging_source[1]))):
            dct["stagingSource"] = dictify(self.staging_source)
        if "validated_sync_mode" == "type" or (self.validated_sync_mode is not self.__undef__ and (not (dirty and not self._validated_sync_mode[1]) or isinstance(self.validated_sync_mode, list) or belongs_to_parent)):
            dct["validatedSyncMode"] = dictify(self.validated_sync_mode)
        elif belongs_to_parent and self.validated_sync_mode is self.__undef__:
            dct["validatedSyncMode"] = "TRANSACTION_LOG"
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._backup_location_credentials = (self._backup_location_credentials[0], True)
        self._backup_location_user = (self._backup_location_user[0], True)
        self._config = (self._config[0], True)
        self._encryption_key = (self._encryption_key[0], True)
        self._external_file_path = (self._external_file_path[0], True)
        self._operations = (self._operations[0], True)
        self._shared_backup_location = (self._shared_backup_location[0], True)
        self._staging_source = (self._staging_source[0], True)
        self._validated_sync_mode = (self._validated_sync_mode[0], True)

    def is_dirty(self):
        return any([self._backup_location_credentials[1], self._backup_location_user[1], self._config[1], self._encryption_key[1], self._external_file_path[1], self._operations[1], self._shared_backup_location[1], self._staging_source[1], self._validated_sync_mode[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlLinkedSource):
            return False
        return super(MSSqlLinkedSource, self).__eq__(other) and \
               self.backup_location_credentials == other.backup_location_credentials and \
               self.backup_location_user == other.backup_location_user and \
               self.config == other.config and \
               self.encryption_key == other.encryption_key and \
               self.external_file_path == other.external_file_path and \
               self.operations == other.operations and \
               self.shared_backup_location == other.shared_backup_location and \
               self.staging_source == other.staging_source and \
               self.validated_sync_mode == other.validated_sync_mode

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def backup_location_credentials(self):
        """
        The password for accessing the shared backup location.

        :rtype: :py:class:`v1_7_1.web.vo.PasswordCredential`
        """
        return self._backup_location_credentials[0]

    @backup_location_credentials.setter
    def backup_location_credentials(self, value):
        self._backup_location_credentials = (value, True)

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

        :rtype: :py:class:`v1_7_1.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

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
    def staging_source(self):
        """
        The staging source for pre-provisioning of the database.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_source[0]

    @staging_source.setter
    def staging_source(self, value):
        self._staging_source = (value, True)

    @property
    def validated_sync_mode(self):
        """
        *(default value: TRANSACTION_LOG)* Specifies the backup types validated
        sync will use to synchronize the dSource with the source database.
        *(permitted values: TRANSACTION_LOG, FULL_OR_DIFFERENTIAL, FULL, NONE)*

        :rtype: ``TEXT_TYPE``
        """
        return self._validated_sync_mode[0]

    @validated_sync_mode.setter
    def validated_sync_mode(self, value):
        self._validated_sync_mode = (value, True)

