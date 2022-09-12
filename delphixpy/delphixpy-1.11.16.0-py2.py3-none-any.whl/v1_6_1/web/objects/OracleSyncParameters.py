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
#     /delphix-oracle-sync-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.SyncParameters import SyncParameters
from delphixpy.v1_6_1 import common

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

class OracleSyncParameters(SyncParameters):
    """
    *(extends* :py:class:`v1_6_1.web.vo.SyncParameters` *)* The parameters to
    use as input to sync Oracle databases.
    """
    def __init__(self, undef_enabled=True):
        super(OracleSyncParameters, self).__init__()
        self._type = ("OracleSyncParameters", True)
        self._double_sync = (self.__undef__, True)
        self._force_full_backup = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleSyncParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._double_sync = (data.get("doubleSync", obj.__undef__), dirty)
        if obj._double_sync[0] is not None and obj._double_sync[0] is not obj.__undef__:
            assert isinstance(obj._double_sync[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._double_sync[0], type(obj._double_sync[0])))
            common.validate_format(obj._double_sync[0], "None", None, None)
        obj._force_full_backup = (data.get("forceFullBackup", obj.__undef__), dirty)
        if obj._force_full_backup[0] is not None and obj._force_full_backup[0] is not obj.__undef__:
            assert isinstance(obj._force_full_backup[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._force_full_backup[0], type(obj._force_full_backup[0])))
            common.validate_format(obj._force_full_backup[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleSyncParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "double_sync" == "type" or (self.double_sync is not self.__undef__ and (not (dirty and not self._double_sync[1]) or isinstance(self.double_sync, list) or belongs_to_parent)):
            dct["doubleSync"] = dictify(self.double_sync)
        elif belongs_to_parent and self.double_sync is self.__undef__:
            dct["doubleSync"] = False
        if "force_full_backup" == "type" or (self.force_full_backup is not self.__undef__ and (not (dirty and not self._force_full_backup[1]))):
            dct["forceFullBackup"] = dictify(self.force_full_backup)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._double_sync = (self._double_sync[0], True)
        self._force_full_backup = (self._force_full_backup[0], True)

    def is_dirty(self):
        return any([self._double_sync[1], self._force_full_backup[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleSyncParameters):
            return False
        return super(OracleSyncParameters, self).__eq__(other) and \
               self.double_sync == other.double_sync and \
               self.force_full_backup == other.force_full_backup

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def double_sync(self):
        """
        True if two SnapSyncs should be performed in immediate succession to
        reduce the number of logs required to provision the snapshot. This may
        significantly reduce the time necessary to provision from a snapshot.

        :rtype: ``bool``
        """
        return self._double_sync[0]

    @double_sync.setter
    def double_sync(self, value):
        self._double_sync = (value, True)

    @property
    def force_full_backup(self):
        """
        Whether or not to take another full backup of the source database.

        :rtype: ``bool``
        """
        return self._force_full_backup[0]

    @force_full_backup.setter
    def force_full_backup(self, value):
        self._force_full_backup = (value, True)

