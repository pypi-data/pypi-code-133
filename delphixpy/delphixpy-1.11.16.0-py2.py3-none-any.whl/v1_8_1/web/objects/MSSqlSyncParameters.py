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
#     /delphix-mssql-sync-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_8_1.web.objects.SyncParameters import SyncParameters
from delphixpy.v1_8_1 import common

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

class MSSqlSyncParameters(SyncParameters):
    """
    *(extends* :py:class:`v1_8_1.web.vo.SyncParameters` *)* The parameters to
    use as input to sync MSSQL databases.
    """
    def __init__(self, undef_enabled=True):
        super(MSSqlSyncParameters, self).__init__()
        self._type = ("MSSqlSyncParameters", True)
        self._backup_uuid = (self.__undef__, True)
        self._load_from_backup = (self.__undef__, True)

    API_VERSION = "1.8.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MSSqlSyncParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._backup_uuid = (data.get("backupUUID", obj.__undef__), dirty)
        if obj._backup_uuid[0] is not None and obj._backup_uuid[0] is not obj.__undef__:
            assert isinstance(obj._backup_uuid[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_uuid[0], type(obj._backup_uuid[0])))
            common.validate_format(obj._backup_uuid[0], "None", None, None)
        obj._load_from_backup = (data.get("loadFromBackup", obj.__undef__), dirty)
        if obj._load_from_backup[0] is not None and obj._load_from_backup[0] is not obj.__undef__:
            assert isinstance(obj._load_from_backup[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._load_from_backup[0], type(obj._load_from_backup[0])))
            common.validate_format(obj._load_from_backup[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MSSqlSyncParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "backup_uuid" == "type" or (self.backup_uuid is not self.__undef__ and (not (dirty and not self._backup_uuid[1]) or isinstance(self.backup_uuid, list) or belongs_to_parent)):
            dct["backupUUID"] = dictify(self.backup_uuid)
        if "load_from_backup" == "type" or (self.load_from_backup is not self.__undef__ and (not (dirty and not self._load_from_backup[1]) or isinstance(self.load_from_backup, list) or belongs_to_parent)):
            dct["loadFromBackup"] = dictify(self.load_from_backup)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._backup_uuid = (self._backup_uuid[0], True)
        self._load_from_backup = (self._load_from_backup[0], True)

    def is_dirty(self):
        return any([self._backup_uuid[1], self._load_from_backup[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MSSqlSyncParameters):
            return False
        return super(MSSqlSyncParameters, self).__eq__(other) and \
               self.backup_uuid == other.backup_uuid and \
               self.load_from_backup == other.load_from_backup

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def backup_uuid(self):
        """
        The UUID of the full or differential backup of the source database to
        restore from. The backup should be present in the shared backup
        location for the source database. This property is relevant only if
        when loading from an existing backup.

        :rtype: ``TEXT_TYPE``
        """
        return self._backup_uuid[0]

    @backup_uuid.setter
    def backup_uuid(self, value):
        self._backup_uuid = (value, True)

    @property
    def load_from_backup(self):
        """
        When set, this parameter overrides the loadFromBackup property in the
        container's sourcing policy. When set to true, Delphix will restore
        from an already existing database backup. If the backupUUID is set,
        that specific backup will be restored. Otherwise the most recent full
        or differential database backup will be restored. When set to false,
        Delphix will take a copy-only full backup and restore from that.

        :rtype: ``bool``
        """
        return self._load_from_backup[0]

    @load_from_backup.setter
    def load_from_backup(self, value):
        self._load_from_backup = (value, True)

