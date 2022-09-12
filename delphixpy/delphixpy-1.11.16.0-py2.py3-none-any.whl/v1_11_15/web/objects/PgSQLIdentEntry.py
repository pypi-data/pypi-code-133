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
#     /delphix-pgsql-ident-entry.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_11_15.web.objects.TypedObject import TypedObject
from delphixpy.v1_11_15 import common

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

class PgSQLIdentEntry(TypedObject):
    """
    *(extends* :py:class:`v1_11_15.web.vo.TypedObject` *)* An entry in the
    PostgreSQL username map file (pg_ident.conf).
    """
    def __init__(self, undef_enabled=True):
        super(PgSQLIdentEntry, self).__init__()
        self._type = ("PgSQLIdentEntry", True)
        self._map_name = (self.__undef__, True)
        self._system_username = (self.__undef__, True)
        self._database_username = (self.__undef__, True)

    API_VERSION = "1.11.15"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PgSQLIdentEntry, cls).from_dict(data, dirty, undef_enabled)
        obj._map_name = (data.get("mapName", obj.__undef__), dirty)
        if obj._map_name[0] is not None and obj._map_name[0] is not obj.__undef__:
            assert isinstance(obj._map_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._map_name[0], type(obj._map_name[0])))
            common.validate_format(obj._map_name[0], "None", None, None)
        obj._system_username = (data.get("systemUsername", obj.__undef__), dirty)
        if obj._system_username[0] is not None and obj._system_username[0] is not obj.__undef__:
            assert isinstance(obj._system_username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._system_username[0], type(obj._system_username[0])))
            common.validate_format(obj._system_username[0], "None", None, None)
        obj._database_username = (data.get("databaseUsername", obj.__undef__), dirty)
        if obj._database_username[0] is not None and obj._database_username[0] is not obj.__undef__:
            assert isinstance(obj._database_username[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_username[0], type(obj._database_username[0])))
            common.validate_format(obj._database_username[0], "None", None, 63)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PgSQLIdentEntry, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "map_name" == "type" or (self.map_name is not self.__undef__ and (not (dirty and not self._map_name[1]) or isinstance(self.map_name, list) or belongs_to_parent)):
            dct["mapName"] = dictify(self.map_name)
        if "system_username" == "type" or (self.system_username is not self.__undef__ and (not (dirty and not self._system_username[1]) or isinstance(self.system_username, list) or belongs_to_parent)):
            dct["systemUsername"] = dictify(self.system_username)
        if "database_username" == "type" or (self.database_username is not self.__undef__ and (not (dirty and not self._database_username[1]) or isinstance(self.database_username, list) or belongs_to_parent)):
            dct["databaseUsername"] = dictify(self.database_username)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._map_name = (self._map_name[0], True)
        self._system_username = (self._system_username[0], True)
        self._database_username = (self._database_username[0], True)

    def is_dirty(self):
        return any([self._map_name[1], self._system_username[1], self._database_username[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PgSQLIdentEntry):
            return False
        return super(PgSQLIdentEntry, self).__eq__(other) and \
               self.map_name == other.map_name and \
               self.system_username == other.system_username and \
               self.database_username == other.database_username

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def map_name(self):
        """
        The name of the map to which this entry belongs (used to refer to the
        map in pg_hba.conf).

        :rtype: ``TEXT_TYPE``
        """
        return self._map_name[0]

    @map_name.setter
    def map_name(self, value):
        self._map_name = (value, True)

    @property
    def system_username(self):
        """
        The operating system username this entry matches.

        :rtype: ``TEXT_TYPE``
        """
        return self._system_username[0]

    @system_username.setter
    def system_username(self, value):
        self._system_username = (value, True)

    @property
    def database_username(self):
        """
        The database username this entry matches.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_username[0]

    @database_username.setter
    def database_username(self, value):
        self._database_username = (value, True)

