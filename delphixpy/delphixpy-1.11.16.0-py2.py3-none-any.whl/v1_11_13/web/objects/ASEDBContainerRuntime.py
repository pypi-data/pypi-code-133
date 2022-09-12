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
#     /delphix-ase-db-container-runtime.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_13.web.objects.DBContainerRuntime import DBContainerRuntime
from delphixpy.v1_11_13 import common

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

class ASEDBContainerRuntime(DBContainerRuntime):
    """
    *(extends* :py:class:`v1_11_13.web.vo.DBContainerRuntime` *)* Runtime
    properties of an SAP ASE database container.
    """
    def __init__(self, undef_enabled=True):
        super(ASEDBContainerRuntime, self).__init__()
        self._type = ("ASEDBContainerRuntime", True)
        self._last_restored_backup_date = (self.__undef__, True)
        self._last_restored_backup_time_zone = (self.__undef__, True)

    API_VERSION = "1.11.13"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEDBContainerRuntime, cls).from_dict(data, dirty, undef_enabled)
        obj._last_restored_backup_date = (data.get("lastRestoredBackupDate", obj.__undef__), dirty)
        if obj._last_restored_backup_date[0] is not None and obj._last_restored_backup_date[0] is not obj.__undef__:
            assert isinstance(obj._last_restored_backup_date[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_restored_backup_date[0], type(obj._last_restored_backup_date[0])))
            common.validate_format(obj._last_restored_backup_date[0], "date", None, None)
        obj._last_restored_backup_time_zone = (data.get("lastRestoredBackupTimeZone", obj.__undef__), dirty)
        if obj._last_restored_backup_time_zone[0] is not None and obj._last_restored_backup_time_zone[0] is not obj.__undef__:
            assert isinstance(obj._last_restored_backup_time_zone[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._last_restored_backup_time_zone[0], type(obj._last_restored_backup_time_zone[0])))
            common.validate_format(obj._last_restored_backup_time_zone[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEDBContainerRuntime, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "last_restored_backup_date" == "type" or (self.last_restored_backup_date is not self.__undef__ and (not (dirty and not self._last_restored_backup_date[1]))):
            dct["lastRestoredBackupDate"] = dictify(self.last_restored_backup_date)
        if "last_restored_backup_time_zone" == "type" or (self.last_restored_backup_time_zone is not self.__undef__ and (not (dirty and not self._last_restored_backup_time_zone[1]))):
            dct["lastRestoredBackupTimeZone"] = dictify(self.last_restored_backup_time_zone)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._last_restored_backup_date = (self._last_restored_backup_date[0], True)
        self._last_restored_backup_time_zone = (self._last_restored_backup_time_zone[0], True)

    def is_dirty(self):
        return any([self._last_restored_backup_date[1], self._last_restored_backup_time_zone[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEDBContainerRuntime):
            return False
        return super(ASEDBContainerRuntime, self).__eq__(other) and \
               self.last_restored_backup_date == other.last_restored_backup_date and \
               self.last_restored_backup_time_zone == other.last_restored_backup_time_zone

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def last_restored_backup_date(self):
        """
        The source database backupset that was last restored in this container.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_restored_backup_date[0]

    @last_restored_backup_date.setter
    def last_restored_backup_date(self, value):
        self._last_restored_backup_date = (value, True)

    @property
    def last_restored_backup_time_zone(self):
        """
        The timezone for the last restored source database backupset in this
        container.

        :rtype: ``TEXT_TYPE``
        """
        return self._last_restored_backup_time_zone[0]

    @last_restored_backup_time_zone.setter
    def last_restored_backup_time_zone(self, value):
        self._last_restored_backup_time_zone = (value, True)

