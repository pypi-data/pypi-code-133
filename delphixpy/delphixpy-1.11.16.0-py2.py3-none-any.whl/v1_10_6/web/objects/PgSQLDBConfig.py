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
#     /delphix-pgsql-db-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_6.web.objects.TypedObject import TypedObject
from delphixpy.v1_10_6 import factory
from delphixpy.v1_10_6 import common

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

class PgSQLDBConfig(TypedObject):
    """
    *(extends* :py:class:`v1_10_6.web.vo.TypedObject` *)* Configuration
    information for a PostgreSQL database in a cluster.
    """
    def __init__(self, undef_enabled=True):
        super(PgSQLDBConfig, self).__init__()
        self._type = ("PgSQLDBConfig", True)
        self._database_name = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._credentials = (self.__undef__, True)
        self._database_cluster = (self.__undef__, True)

    API_VERSION = "1.10.6"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PgSQLDBConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._database_name = (data.get("databaseName", obj.__undef__), dirty)
        if obj._database_name[0] is not None and obj._database_name[0] is not obj.__undef__:
            assert isinstance(obj._database_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_name[0], type(obj._database_name[0])))
            common.validate_format(obj._database_name[0], "None", None, 63)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "None", None, 256)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "Credential"), dirty)
            factory.validate_type(obj._credentials[0], "Credential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        obj._database_cluster = (data.get("databaseCluster", obj.__undef__), dirty)
        if obj._database_cluster[0] is not None and obj._database_cluster[0] is not obj.__undef__:
            assert isinstance(obj._database_cluster[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_cluster[0], type(obj._database_cluster[0])))
            common.validate_format(obj._database_cluster[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PgSQLDBConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "database_name" == "type" or (self.database_name is not self.__undef__ and (not (dirty and not self._database_name[1]) or isinstance(self.database_name, list) or belongs_to_parent)):
            dct["databaseName"] = dictify(self.database_name)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials, prop_is_list_or_vo=True)
        if "database_cluster" == "type" or (self.database_cluster is not self.__undef__ and (not (dirty and not self._database_cluster[1]))):
            dct["databaseCluster"] = dictify(self.database_cluster)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._database_name = (self._database_name[0], True)
        self._user = (self._user[0], True)
        self._credentials = (self._credentials[0], True)
        self._database_cluster = (self._database_cluster[0], True)

    def is_dirty(self):
        return any([self._database_name[1], self._user[1], self._credentials[1], self._database_cluster[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PgSQLDBConfig):
            return False
        return super(PgSQLDBConfig, self).__eq__(other) and \
               self.database_name == other.database_name and \
               self.user == other.user and \
               self.credentials == other.credentials and \
               self.database_cluster == other.database_cluster

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def database_name(self):
        """
        The name of the database.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_name[0]

    @database_name.setter
    def database_name(self, value):
        self._database_name = (value, True)

    @property
    def user(self):
        """
        The username of the database user.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def credentials(self):
        """
        The password of the database user.

        :rtype: :py:class:`v1_10_6.web.vo.Credential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

    @property
    def database_cluster(self):
        """
        The PostgreSQL cluster this database is part of.

        :rtype: ``TEXT_TYPE``
        """
        return self._database_cluster[0]

    @database_cluster.setter
    def database_cluster(self, value):
        self._database_cluster = (value, True)

