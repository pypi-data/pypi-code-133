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
#     /delphix-sourcing-policy.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_1.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_1 import common

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

class SourcingPolicy(TypedObject):
    """
    *(extends* :py:class:`v1_5_1.web.vo.TypedObject` *)* Database policies for
    managing SnapSync and LogSync across sources for a MSSQL container.
    """
    def __init__(self, undef_enabled=True):
        super(SourcingPolicy, self).__init__()
        self._type = ("SourcingPolicy", True)
        self._load_from_backup = (self.__undef__, True)
        self._logsync_enabled = (self.__undef__, True)

    API_VERSION = "1.5.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(SourcingPolicy, cls).from_dict(data, dirty, undef_enabled)
        obj._load_from_backup = (data.get("loadFromBackup", obj.__undef__), dirty)
        if obj._load_from_backup[0] is not None and obj._load_from_backup[0] is not obj.__undef__:
            assert isinstance(obj._load_from_backup[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._load_from_backup[0], type(obj._load_from_backup[0])))
            common.validate_format(obj._load_from_backup[0], "None", None, None)
        obj._logsync_enabled = (data.get("logsyncEnabled", obj.__undef__), dirty)
        if obj._logsync_enabled[0] is not None and obj._logsync_enabled[0] is not obj.__undef__:
            assert isinstance(obj._logsync_enabled[0], bool), ("Expected one of ['boolean'], but got %s of type %s" % (obj._logsync_enabled[0], type(obj._logsync_enabled[0])))
            common.validate_format(obj._logsync_enabled[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(SourcingPolicy, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "load_from_backup" == "type" or (self.load_from_backup is not self.__undef__ and (not (dirty and not self._load_from_backup[1]) or isinstance(self.load_from_backup, list) or belongs_to_parent)):
            dct["loadFromBackup"] = dictify(self.load_from_backup)
        elif belongs_to_parent and self.load_from_backup is self.__undef__:
            dct["loadFromBackup"] = False
        if "logsync_enabled" == "type" or (self.logsync_enabled is not self.__undef__ and (not (dirty and not self._logsync_enabled[1]) or isinstance(self.logsync_enabled, list) or belongs_to_parent)):
            dct["logsyncEnabled"] = dictify(self.logsync_enabled)
        elif belongs_to_parent and self.logsync_enabled is self.__undef__:
            dct["logsyncEnabled"] = False
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._load_from_backup = (self._load_from_backup[0], True)
        self._logsync_enabled = (self._logsync_enabled[0], True)

    def is_dirty(self):
        return any([self._load_from_backup[1], self._logsync_enabled[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SourcingPolicy):
            return False
        return super(SourcingPolicy, self).__eq__(other) and \
               self.load_from_backup == other.load_from_backup and \
               self.logsync_enabled == other.logsync_enabled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def load_from_backup(self):
        """
        True if the initial load and subsequent syncs for this container
        restore from already existing database backups. In such cases Delphix
        does not take any full database backups of the source database. When
        false, Delphix will take a full backup of the source.

        :rtype: ``bool``
        """
        return self._load_from_backup[0]

    @load_from_backup.setter
    def load_from_backup(self, value):
        self._load_from_backup = (value, True)

    @property
    def logsync_enabled(self):
        """
        True if LogSync should run for this database.

        :rtype: ``bool``
        """
        return self._logsync_enabled[0]

    @logsync_enabled.setter
    def logsync_enabled(self, value):
        self._logsync_enabled = (value, True)

