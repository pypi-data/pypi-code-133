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
#     /delphix-ase-backup-location.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_5_3.web.objects.TypedObject import TypedObject
from delphixpy.v1_5_3 import common

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

class ASEBackupLocation(TypedObject):
    """
    *(extends* :py:class:`v1_5_3.web.vo.TypedObject` *)* SAP ASE backup
    location.
    """
    def __init__(self, undef_enabled=True):
        super(ASEBackupLocation, self).__init__()
        self._type = ("ASEBackupLocation", True)
        self._backup_host = (self.__undef__, True)
        self._backup_host_user = (self.__undef__, True)
        self._backup_server_name = (self.__undef__, True)

    API_VERSION = "1.5.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(ASEBackupLocation, cls).from_dict(data, dirty, undef_enabled)
        obj._backup_host = (data.get("backupHost", obj.__undef__), dirty)
        if obj._backup_host[0] is not None and obj._backup_host[0] is not obj.__undef__:
            assert isinstance(obj._backup_host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_host[0], type(obj._backup_host[0])))
            common.validate_format(obj._backup_host[0], "objectReference", None, None)
        obj._backup_host_user = (data.get("backupHostUser", obj.__undef__), dirty)
        if obj._backup_host_user[0] is not None and obj._backup_host_user[0] is not obj.__undef__:
            assert isinstance(obj._backup_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_host_user[0], type(obj._backup_host_user[0])))
            common.validate_format(obj._backup_host_user[0], "objectReference", None, None)
        obj._backup_server_name = (data.get("backupServerName", obj.__undef__), dirty)
        if obj._backup_server_name[0] is not None and obj._backup_server_name[0] is not obj.__undef__:
            assert isinstance(obj._backup_server_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._backup_server_name[0], type(obj._backup_server_name[0])))
            common.validate_format(obj._backup_server_name[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(ASEBackupLocation, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "backup_host" == "type" or (self.backup_host is not self.__undef__ and (not (dirty and not self._backup_host[1]) or isinstance(self.backup_host, list) or belongs_to_parent)):
            dct["backupHost"] = dictify(self.backup_host)
        if "backup_host_user" == "type" or (self.backup_host_user is not self.__undef__ and (not (dirty and not self._backup_host_user[1]) or isinstance(self.backup_host_user, list) or belongs_to_parent)):
            dct["backupHostUser"] = dictify(self.backup_host_user)
        if "backup_server_name" == "type" or (self.backup_server_name is not self.__undef__ and (not (dirty and not self._backup_server_name[1]) or isinstance(self.backup_server_name, list) or belongs_to_parent)):
            dct["backupServerName"] = dictify(self.backup_server_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._backup_host = (self._backup_host[0], True)
        self._backup_host_user = (self._backup_host_user[0], True)
        self._backup_server_name = (self._backup_server_name[0], True)

    def is_dirty(self):
        return any([self._backup_host[1], self._backup_host_user[1], self._backup_server_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, ASEBackupLocation):
            return False
        return super(ASEBackupLocation, self).__eq__(other) and \
               self.backup_host == other.backup_host and \
               self.backup_host_user == other.backup_host_user and \
               self.backup_server_name == other.backup_server_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def backup_host(self):
        """
        Host environment where the backup server is located.

        :rtype: ``TEXT_TYPE``
        """
        return self._backup_host[0]

    @backup_host.setter
    def backup_host(self, value):
        self._backup_host = (value, True)

    @property
    def backup_host_user(self):
        """
        OS user for the host where the backup server is located.

        :rtype: ``TEXT_TYPE``
        """
        return self._backup_host_user[0]

    @backup_host_user.setter
    def backup_host_user(self, value):
        self._backup_host_user = (value, True)

    @property
    def backup_server_name(self):
        """
        Name of the backup server instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._backup_server_name[0]

    @backup_server_name.setter
    def backup_server_name(self, value):
        self._backup_server_name = (value, True)

