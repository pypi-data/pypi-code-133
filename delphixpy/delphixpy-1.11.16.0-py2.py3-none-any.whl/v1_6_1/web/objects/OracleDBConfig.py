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
#     /delphix-oracle-db-config.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_6_1.web.objects.OracleBaseDBConfig import OracleBaseDBConfig
from delphixpy.v1_6_1 import factory
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

class OracleDBConfig(OracleBaseDBConfig):
    """
    *(extends* :py:class:`v1_6_1.web.vo.OracleBaseDBConfig` *)* The source
    config represents the dynamically discovered attributes of an Oracle
    source.
    """
    def __init__(self, undef_enabled=True):
        super(OracleDBConfig, self).__init__()
        self._type = ("OracleDBConfig", True)
        self._cdb_type = (self.__undef__, True)
        self._database_name = (self.__undef__, True)
        self._non_sys_credentials = (self.__undef__, True)
        self._non_sys_user = (self.__undef__, True)
        self._repository = (self.__undef__, True)
        self._unique_name = (self.__undef__, True)

    API_VERSION = "1.6.1"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(OracleDBConfig, cls).from_dict(data, dirty, undef_enabled)
        obj._cdb_type = (data.get("cdbType", obj.__undef__), dirty)
        if obj._cdb_type[0] is not None and obj._cdb_type[0] is not obj.__undef__:
            assert isinstance(obj._cdb_type[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._cdb_type[0], type(obj._cdb_type[0])))
            assert obj._cdb_type[0] in ['UNKNOWN', 'ROOT_CDB', 'NON_CDB', 'AUX_CDB'], "Expected enum ['UNKNOWN', 'ROOT_CDB', 'NON_CDB', 'AUX_CDB'] but got %s" % obj._cdb_type[0]
            common.validate_format(obj._cdb_type[0], "None", None, None)
        obj._database_name = (data.get("databaseName", obj.__undef__), dirty)
        if obj._database_name[0] is not None and obj._database_name[0] is not obj.__undef__:
            assert isinstance(obj._database_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._database_name[0], type(obj._database_name[0])))
            common.validate_format(obj._database_name[0], "None", None, 8)
        if "nonSysCredentials" in data and data["nonSysCredentials"] is not None:
            obj._non_sys_credentials = (factory.create_object(data["nonSysCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._non_sys_credentials[0], "PasswordCredential")
        else:
            obj._non_sys_credentials = (obj.__undef__, dirty)
        obj._non_sys_user = (data.get("nonSysUser", obj.__undef__), dirty)
        if obj._non_sys_user[0] is not None and obj._non_sys_user[0] is not obj.__undef__:
            assert isinstance(obj._non_sys_user[0], TEXT_TYPE), ("Expected one of ['string', 'null'], but got %s of type %s" % (obj._non_sys_user[0], type(obj._non_sys_user[0])))
            common.validate_format(obj._non_sys_user[0], "None", None, 30)
        obj._repository = (data.get("repository", obj.__undef__), dirty)
        if obj._repository[0] is not None and obj._repository[0] is not obj.__undef__:
            assert isinstance(obj._repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._repository[0], type(obj._repository[0])))
            common.validate_format(obj._repository[0], "objectReference", None, None)
        obj._unique_name = (data.get("uniqueName", obj.__undef__), dirty)
        if obj._unique_name[0] is not None and obj._unique_name[0] is not obj.__undef__:
            assert isinstance(obj._unique_name[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._unique_name[0], type(obj._unique_name[0])))
            common.validate_format(obj._unique_name[0], "None", None, 30)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(OracleDBConfig, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "cdb_type" == "type" or (self.cdb_type is not self.__undef__ and (not (dirty and not self._cdb_type[1]))):
            dct["cdbType"] = dictify(self.cdb_type)
        if dirty and "cdbType" in dct:
            del dct["cdbType"]
        if "database_name" == "type" or (self.database_name is not self.__undef__ and (not (dirty and not self._database_name[1]) or isinstance(self.database_name, list) or belongs_to_parent)):
            dct["databaseName"] = dictify(self.database_name)
        if "non_sys_credentials" == "type" or (self.non_sys_credentials is not self.__undef__ and (not (dirty and not self._non_sys_credentials[1]) or isinstance(self.non_sys_credentials, list) or belongs_to_parent)):
            dct["nonSysCredentials"] = dictify(self.non_sys_credentials)
        if "non_sys_user" == "type" or (self.non_sys_user is not self.__undef__ and (not (dirty and not self._non_sys_user[1]) or isinstance(self.non_sys_user, list) or belongs_to_parent)):
            dct["nonSysUser"] = dictify(self.non_sys_user)
        if "repository" == "type" or (self.repository is not self.__undef__ and (not (dirty and not self._repository[1]) or isinstance(self.repository, list) or belongs_to_parent)):
            dct["repository"] = dictify(self.repository)
        if "unique_name" == "type" or (self.unique_name is not self.__undef__ and (not (dirty and not self._unique_name[1]) or isinstance(self.unique_name, list) or belongs_to_parent)):
            dct["uniqueName"] = dictify(self.unique_name)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._cdb_type = (self._cdb_type[0], True)
        self._database_name = (self._database_name[0], True)
        self._non_sys_credentials = (self._non_sys_credentials[0], True)
        self._non_sys_user = (self._non_sys_user[0], True)
        self._repository = (self._repository[0], True)
        self._unique_name = (self._unique_name[0], True)

    def is_dirty(self):
        return any([self._cdb_type[1], self._database_name[1], self._non_sys_credentials[1], self._non_sys_user[1], self._repository[1], self._unique_name[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, OracleDBConfig):
            return False
        return super(OracleDBConfig, self).__eq__(other) and \
               self.cdb_type == other.cdb_type and \
               self.database_name == other.database_name and \
               self.non_sys_credentials == other.non_sys_credentials and \
               self.non_sys_user == other.non_sys_user and \
               self.repository == other.repository and \
               self.unique_name == other.unique_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def cdb_type(self):
        """
        The container type of this database. *(permitted values: UNKNOWN,
        ROOT_CDB, NON_CDB, AUX_CDB)*

        :rtype: ``TEXT_TYPE``
        """
        return self._cdb_type[0]

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
    def non_sys_credentials(self):
        """
        The password of a database user that does not have administrative
        privileges.

        :rtype: :py:class:`v1_6_1.web.vo.PasswordCredential`
        """
        return self._non_sys_credentials[0]

    @non_sys_credentials.setter
    def non_sys_credentials(self, value):
        self._non_sys_credentials = (value, True)

    @property
    def non_sys_user(self):
        """
        The username of a database user that does not have administrative
        privileges.

        :rtype: ``TEXT_TYPE`` *or* ``null``
        """
        return self._non_sys_user[0]

    @non_sys_user.setter
    def non_sys_user(self, value):
        self._non_sys_user = (value, True)

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

    @property
    def unique_name(self):
        """
        The unique name.

        :rtype: ``TEXT_TYPE``
        """
        return self._unique_name[0]

    @unique_name.setter
    def unique_name(self, value):
        self._unique_name = (value, True)

