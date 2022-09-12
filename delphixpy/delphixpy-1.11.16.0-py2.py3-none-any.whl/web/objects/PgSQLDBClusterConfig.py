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
#     /delphix-pgsql-db-cluster-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.web.objects.SourceConfig import SourceConfig
from delphixpy import factory
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

class PgSQLDBClusterConfig(SourceConfig):
    """
    *(extends* :py:class:`delphixpy.web.vo.SourceConfig` *)* Configuration
    information for a PostgreSQL database cluster.
    """
    def __init__(self, undef_enabled=True):
        super(PgSQLDBClusterConfig, self).__init__()
        self._type = ("PgSQLDBClusterConfig", True)
        self._cluster_data_directory = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._credentials = (self.__undef__, True)
        self._connection_database = (self.__undef__, True)
        self._repository = (self.__undef__, True)

    API_VERSION = "1.11.16"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PgSQLDBClusterConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._cluster_data_directory = (data.get("clusterDataDirectory", obj.__undef__), dirty)
        if obj._cluster_data_directory[0] is not None and obj._cluster_data_directory[0] is not obj.__undef__:
            assert isinstance(obj._cluster_data_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cluster_data_directory[0], type(obj._cluster_data_directory[0])))
            common.validate_format(obj._cluster_data_directory[0], "None", None, None)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "None", None, 256)
        if "credentials" in data and data["credentials"] is not None:
            obj._credentials = (factory.create_object(data["credentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._credentials[0], "PasswordCredential")
        else:
            obj._credentials = (obj.__undef__, dirty)
        obj._connection_database = (data.get("connectionDatabase", obj.__undef__), dirty)
        if obj._connection_database[0] is not None and obj._connection_database[0] is not obj.__undef__:
            assert isinstance(obj._connection_database[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._connection_database[0], type(obj._connection_database[0])))
            common.validate_format(obj._connection_database[0], "None", None, 256)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PgSQLDBClusterConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cluster_data_directory" == "type" or (self.cluster_data_directory is not self.__undef__ and (not (dirty and not self._cluster_data_directory[1]) or isinstance(self.cluster_data_directory, list) or belongs_to_parent)):
            dct["clusterDataDirectory"] = dictify(self.cluster_data_directory)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]) or isinstance(self.port, list) or belongs_to_parent)):
            dct["port"] = dictify(self.port)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]) or isinstance(self.user, list) or belongs_to_parent)):
            dct["user"] = dictify(self.user)
        if "credentials" == "type" or (self.credentials is not self.__undef__ and (not (dirty and not self._credentials[1]) or isinstance(self.credentials, list) or belongs_to_parent)):
            dct["credentials"] = dictify(self.credentials)
        if "connection_database" == "type" or (self.connection_database is not self.__undef__ and (not (dirty and not self._connection_database[1]) or isinstance(self.connection_database, list) or belongs_to_parent)):
            dct["connectionDatabase"] = dictify(self.connection_database)
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cluster_data_directory = (self._cluster_data_directory[0], True)
        self._port = (self._port[0], True)
        self._user = (self._user[0], True)
        self._credentials = (self._credentials[0], True)
        self._connection_database = (self._connection_database[0], True)
        self._repository = (self._repository[0], True)

    def is_dirty(self):
        return any([self._cluster_data_directory[1], self._port[1], self._user[1], self._credentials[1], self._connection_database[1], self._repository[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PgSQLDBClusterConfig):
            return False
        return super(PgSQLDBClusterConfig, self).__eq__(other) and \
               self.cluster_data_directory == other.cluster_data_directory and \
               self.port == other.port and \
               self.user == other.user and \
               self.credentials == other.credentials and \
               self.connection_database == other.connection_database and \
               self.repository == other.repository

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cluster_data_directory(self):
        """
        The data directory for the PostgreSQL cluster.

        :rtype: ``TEXT_TYPE``
        """
        return self._cluster_data_directory[0]

    @cluster_data_directory.setter
    def cluster_data_directory(self, value):
        self._cluster_data_directory = (value, True)

    @property
    def port(self):
        """
        The port on which the PostgresSQL server for the cluster is listening.

        :rtype: ``int``
        """
        return self._port[0]

    @port.setter
    def port(self, value):
        self._port = (value, True)

    @property
    def user(self):
        """
        The username of the database cluster user.

        :rtype: ``TEXT_TYPE``
        """
        return self._user[0]

    @user.setter
    def user(self, value):
        self._user = (value, True)

    @property
    def credentials(self):
        """
        The password of the database cluster user.

        :rtype: :py:class:`delphixpy.web.vo.PasswordCredential`
        """
        return self._credentials[0]

    @credentials.setter
    def credentials(self, value):
        self._credentials = (value, True)

    @property
    def connection_database(self):
        """
        The database that must be used to run SQL queries against this cluster.

        :rtype: ``TEXT_TYPE``
        """
        return self._connection_database[0]

    @connection_database.setter
    def connection_database(self, value):
        self._connection_database = (value, True)

    @property
    def repository(self):
        """
        The object reference of the source repository.

        :rtype: ``TEXT_TYPE``
        """
        return self._repository[0]

    @repository.setter
    def repository(self, value):
        self._repository = (value, True)

