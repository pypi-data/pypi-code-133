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
#     /delphix-oracle-sync-from-external-parameters.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.OracleSyncParameters import OracleSyncParameters
from delphixpy import common

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

class OracleSyncFromExternalParameters(OracleSyncParameters):
    """
    *(extends* :py:class:`delphixpy.web.vo.OracleSyncParameters` *)* The
    parameters to use as input to sync an external Oracle database.
    """
    def __init__(self, undef_enabled=True):
        super(OracleSyncFromExternalParameters, self).__init__()
        self._type = ("OracleSyncFromExternalParameters", True)
        self._force_full_backup = (self.__undef__, True)
        self._double_sync = (self.__undef__, True)
        self._skip_space_check = (self.__undef__, True)
        self._do_not_resume = (self.__undef__, True)
        self._files_for_full_backup = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleSyncFromExternalParameters, cls).from_dict(data, dirty, undef_enabled)
        obj._force_full_backup = (data.get("forceFullBackup", obj.__undef__), dirty)
        if obj._force_full_backup[0] is not None and obj._force_full_backup[0] is not obj.__undef__:
            assert isinstance(obj._force_full_backup[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._force_full_backup[0], type(obj._force_full_backup[0])))
            common.validate_format(obj._force_full_backup[0], "None", None, None)
        obj._double_sync = (data.get("doubleSync", obj.__undef__), dirty)
        if obj._double_sync[0] is not None and obj._double_sync[0] is not obj.__undef__:
            assert isinstance(obj._double_sync[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._double_sync[0], type(obj._double_sync[0])))
            common.validate_format(obj._double_sync[0], "None", None, None)
        obj._skip_space_check = (data.get("skipSpaceCheck", obj.__undef__), dirty)
        if obj._skip_space_check[0] is not None and obj._skip_space_check[0] is not obj.__undef__:
            assert isinstance(obj._skip_space_check[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._skip_space_check[0], type(obj._skip_space_check[0])))
            common.validate_format(obj._skip_space_check[0], "None", None, None)
        obj._do_not_resume = (data.get("doNotResume", obj.__undef__), dirty)
        if obj._do_not_resume[0] is not None and obj._do_not_resume[0] is not obj.__undef__:
            assert isinstance(obj._do_not_resume[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._do_not_resume[0], type(obj._do_not_resume[0])))
            common.validate_format(obj._do_not_resume[0], "None", None, None)
        obj._files_for_full_backup = []
        for item in data.get("filesForFullBackup") or []:
            assert isinstance(item, int), ("Expected one of ['integer'], but got %s of type %s" % (item, type(item)))
            common.validate_format(item, "None", None, None)
            obj._files_for_full_backup.append(item)
        obj._files_for_full_backup = (obj._files_for_full_backup, dirty)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleSyncFromExternalParameters, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "force_full_backup" == "type" or (self.force_full_backup is not self.__undef__ and (not (dirty and not self._force_full_backup[1]) or isinstance(self.force_full_backup, list) or belongs_to_parent)):
            dct["forceFullBackup"] = dictify(self.force_full_backup)
        elif belongs_to_parent and self.force_full_backup is self.__undef__:
            dct["forceFullBackup"] = False
        if "double_sync" == "type" or (self.double_sync is not self.__undef__ and (not (dirty and not self._double_sync[1]) or isinstance(self.double_sync, list) or belongs_to_parent)):
            dct["doubleSync"] = dictify(self.double_sync)
        elif belongs_to_parent and self.double_sync is self.__undef__:
            dct["doubleSync"] = False
        if "skip_space_check" == "type" or (self.skip_space_check is not self.__undef__ and (not (dirty and not self._skip_space_check[1]) or isinstance(self.skip_space_check, list) or belongs_to_parent)):
            dct["skipSpaceCheck"] = dictify(self.skip_space_check)
        elif belongs_to_parent and self.skip_space_check is self.__undef__:
            dct["skipSpaceCheck"] = False
        if "do_not_resume" == "type" or (self.do_not_resume is not self.__undef__ and (not (dirty and not self._do_not_resume[1]) or isinstance(self.do_not_resume, list) or belongs_to_parent)):
            dct["doNotResume"] = dictify(self.do_not_resume)
        elif belongs_to_parent and self.do_not_resume is self.__undef__:
            dct["doNotResume"] = False
        if "files_for_full_backup" == "type" or (self.files_for_full_backup is not self.__undef__ and (not (dirty and not self._files_for_full_backup[1]) or isinstance(self.files_for_full_backup, list) or belongs_to_parent)):
            dct["filesForFullBackup"] = dictify(self.files_for_full_backup, prop_is_list_or_vo=True)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._force_full_backup = (self._force_full_backup[0], True)
        self._double_sync = (self._double_sync[0], True)
        self._skip_space_check = (self._skip_space_check[0], True)
        self._do_not_resume = (self._do_not_resume[0], True)
        self._files_for_full_backup = (self._files_for_full_backup[0], True)

    def is_dirty(self):
        return any([self._force_full_backup[1], self._double_sync[1], self._skip_space_check[1], self._do_not_resume[1], self._files_for_full_backup[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleSyncFromExternalParameters):
            return False
        return super(OracleSyncFromExternalParameters, self).__eq__(other) and \
               self.force_full_backup == other.force_full_backup and \
               self.double_sync == other.double_sync and \
               self.skip_space_check == other.skip_space_check and \
               self.do_not_resume == other.do_not_resume and \
               self.files_for_full_backup == other.files_for_full_backup

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

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
    def skip_space_check(self):
        """
        Skip check that tests if there is enough space available to store the
        database in the Delphix Engine. The Delphix Engine estimates how much
        space a database will occupy after compression and prevents SnapSync if
        insufficient space is available. This safeguard can be overridden using
        this option. This may be useful when linking highly compressible
        databases.

        :rtype: ``bool``
        """
        return self._skip_space_check[0]

    @skip_space_check.setter
    def skip_space_check(self, value):
        self._skip_space_check = (value, True)

    @property
    def do_not_resume(self):
        """
        Indicates whether a fresh SnapSync must be started regardless if it was
        possible to resume the current SnapSync. If true, we will not resume
        but instead ignore previous progress and backup all datafiles even if
        already completed from previous failed SnapSync. This does not force a
        full backup, if an incremental was in progress this will start a new
        incremental snapshot.

        :rtype: ``bool``
        """
        return self._do_not_resume[0]

    @do_not_resume.setter
    def do_not_resume(self, value):
        self._do_not_resume = (value, True)

    @property
    def files_for_full_backup(self):
        """
        List of datafiles to take a full backup of. This would be useful in
        situations where certain datafiles could not be backed up during
        previous SnapSync due to corruption or because they went offline.

        :rtype: ``list`` of ``int``
        """
        return self._files_for_full_backup[0]

    @files_for_full_backup.setter
    def files_for_full_backup(self, value):
        self._files_for_full_backup = (value, True)

