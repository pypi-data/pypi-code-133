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
#     /delphix-pgsql-source-connection-info.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_0.web.objects.SourceConnectionInfo import SourceConnectionInfo
from delphixpy.v1_10_0 import common

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

class PgSQLSourceConnectionInfo(SourceConnectionInfo):
    """
    *(extends* :py:class:`v1_10_0.web.vo.SourceConnectionInfo` *)* Contains
    information that can be used to connect to a PostgreSQL source.
    """
    def __init__(self, undef_enabled=True):
        super(PgSQLSourceConnectionInfo, self).__init__()
        self._type = ("PgSQLSourceConnectionInfo", True)
        self._host = (self.__undef__, True)
        self._port = (self.__undef__, True)
        self._user = (self.__undef__, True)
        self._pg_data_directory = (self.__undef__, True)
        self._jdbc_string = (self.__undef__, True)

    API_VERSION = "1.10.0"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(PgSQLSourceConnectionInfo, cls).from_dict(data, dirty, undef_enabled)
        obj._host = (data.get("host", obj.__undef__), dirty)
        if obj._host[0] is not None and obj._host[0] is not obj.__undef__:
            assert isinstance(obj._host[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._host[0], type(obj._host[0])))
            common.validate_format(obj._host[0], "None", None, None)
        obj._port = (data.get("port", obj.__undef__), dirty)
        if obj._port[0] is not None and obj._port[0] is not obj.__undef__:
            assert isinstance(obj._port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._port[0], type(obj._port[0])))
            common.validate_format(obj._port[0], "None", None, None)
        obj._user = (data.get("user", obj.__undef__), dirty)
        if obj._user[0] is not None and obj._user[0] is not obj.__undef__:
            assert isinstance(obj._user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._user[0], type(obj._user[0])))
            common.validate_format(obj._user[0], "None", None, None)
        obj._pg_data_directory = (data.get("pgDataDirectory", obj.__undef__), dirty)
        if obj._pg_data_directory[0] is not None and obj._pg_data_directory[0] is not obj.__undef__:
            assert isinstance(obj._pg_data_directory[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._pg_data_directory[0], type(obj._pg_data_directory[0])))
            common.validate_format(obj._pg_data_directory[0], "None", None, None)
        obj._jdbc_string = (data.get("jdbcString", obj.__undef__), dirty)
        if obj._jdbc_string[0] is not None and obj._jdbc_string[0] is not obj.__undef__:
            assert isinstance(obj._jdbc_string[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._jdbc_string[0], type(obj._jdbc_string[0])))
            common.validate_format(obj._jdbc_string[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(PgSQLSourceConnectionInfo, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "host" == "type" or (self.host is not self.__undef__ and (not (dirty and not self._host[1]))):
            dct["host"] = dictify(self.host)
        if "port" == "type" or (self.port is not self.__undef__ and (not (dirty and not self._port[1]))):
            dct["port"] = dictify(self.port)
        if "user" == "type" or (self.user is not self.__undef__ and (not (dirty and not self._user[1]))):
            dct["user"] = dictify(self.user)
        if "pg_data_directory" == "type" or (self.pg_data_directory is not self.__undef__ and (not (dirty and not self._pg_data_directory[1]))):
            dct["pgDataDirectory"] = dictify(self.pg_data_directory)
        if "jdbc_string" == "type" or (self.jdbc_string is not self.__undef__ and (not (dirty and not self._jdbc_string[1]))):
            dct["jdbcString"] = dictify(self.jdbc_string)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._host = (self._host[0], True)
        self._port = (self._port[0], True)
        self._user = (self._user[0], True)
        self._pg_data_directory = (self._pg_data_directory[0], True)
        self._jdbc_string = (self._jdbc_string[0], True)

    def is_dirty(self):
        return any([self._host[1], self._port[1], self._user[1], self._pg_data_directory[1], self._jdbc_string[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, PgSQLSourceConnectionInfo):
            return False
        return super(PgSQLSourceConnectionInfo, self).__eq__(other) and \
               self.host == other.host and \
               self.port == other.port and \
               self.user == other.user and \
               self.pg_data_directory == other.pg_data_directory and \
               self.jdbc_string == other.jdbc_string

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def host(self):
        """
        The hostname or IP address of the host where the source resides.

        :rtype: ``TEXT_TYPE``
        """
        return self._host[0]

    @host.setter
    def host(self, value):
        self._host = (value, True)

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
    def pg_data_directory(self):
        """
        The data directory for the PostgreSQL cluster.

        :rtype: ``TEXT_TYPE``
        """
        return self._pg_data_directory[0]

    @pg_data_directory.setter
    def pg_data_directory(self, value):
        self._pg_data_directory = (value, True)

    @property
    def jdbc_string(self):
        """
        The JDBC string used to connect to the PostgreSQL server instance.

        :rtype: ``TEXT_TYPE``
        """
        return self._jdbc_string[0]

    @jdbc_string.setter
    def jdbc_string(self, value):
        self._jdbc_string = (value, True)

