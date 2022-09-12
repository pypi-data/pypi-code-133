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
#     /delphix-mysql-attach-data.json
#
# Do not edit this file manually!
#

from __future__ import unicode_literals

from delphixpy.v1_10_3.web.objects.AttachData import AttachData
from delphixpy.v1_10_3 import factory
from delphixpy.v1_10_3 import common

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

class MySQLAttachData(AttachData):
    """
    *(extends* :py:class:`v1_10_3.web.vo.AttachData` *)* Represents the MySQL
    parameters of an attach request.
    """
    def __init__(self, undef_enabled=True):
        super(MySQLAttachData, self).__init__()
        self._type = ("MySQLAttachData", True)
        self._config = (self.__undef__, True)
        self._config_params = (self.__undef__, True)
        self._operations = (self.__undef__, True)
        self._db_user = (self.__undef__, True)
        self._db_credentials = (self.__undef__, True)
        self._staging_repository = (self.__undef__, True)
        self._staging_host_user = (self.__undef__, True)
        self._staging_port = (self.__undef__, True)

    API_VERSION = "1.10.3"

    @classmethod
    def from_dict(cls, data, dirty=False, undef_enabled=True):
        obj = super(MySQLAttachData, cls).from_dict(data, dirty, undef_enabled)
        if "config" not in data:
            raise ValueError("Missing required property \"config\".")
        obj._config = (data.get("config", obj.__undef__), dirty)
        if obj._config[0] is not None and obj._config[0] is not obj.__undef__:
            assert isinstance(obj._config[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._config[0], type(obj._config[0])))
            common.validate_format(obj._config[0], "objectReference", None, None)
        obj._config_params = (data.get("configParams", obj.__undef__), dirty)
        if obj._config_params[0] is not None and obj._config_params[0] is not obj.__undef__:
            assert isinstance(obj._config_params[0], dict), ("Expected one of ['object'], but got %s of type %s" % (obj._config_params[0], type(obj._config_params[0])))
            common.validate_format(obj._config_params[0], "None", None, None)
        if "operations" in data and data["operations"] is not None:
            obj._operations = (factory.create_object(data["operations"], "LinkedSourceOperations"), dirty)
            factory.validate_type(obj._operations[0], "LinkedSourceOperations")
        else:
            obj._operations = (obj.__undef__, dirty)
        if "dbUser" not in data:
            raise ValueError("Missing required property \"dbUser\".")
        obj._db_user = (data.get("dbUser", obj.__undef__), dirty)
        if obj._db_user[0] is not None and obj._db_user[0] is not obj.__undef__:
            assert isinstance(obj._db_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._db_user[0], type(obj._db_user[0])))
            common.validate_format(obj._db_user[0], "None", None, None)
        if "dbCredentials" not in data:
            raise ValueError("Missing required property \"dbCredentials\".")
        if "dbCredentials" in data and data["dbCredentials"] is not None:
            obj._db_credentials = (factory.create_object(data["dbCredentials"], "PasswordCredential"), dirty)
            factory.validate_type(obj._db_credentials[0], "PasswordCredential")
        else:
            obj._db_credentials = (obj.__undef__, dirty)
        if "stagingRepository" not in data:
            raise ValueError("Missing required property \"stagingRepository\".")
        obj._staging_repository = (data.get("stagingRepository", obj.__undef__), dirty)
        if obj._staging_repository[0] is not None and obj._staging_repository[0] is not obj.__undef__:
            assert isinstance(obj._staging_repository[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_repository[0], type(obj._staging_repository[0])))
            common.validate_format(obj._staging_repository[0], "objectReference", None, None)
        if "stagingHostUser" not in data:
            raise ValueError("Missing required property \"stagingHostUser\".")
        obj._staging_host_user = (data.get("stagingHostUser", obj.__undef__), dirty)
        if obj._staging_host_user[0] is not None and obj._staging_host_user[0] is not obj.__undef__:
            assert isinstance(obj._staging_host_user[0], TEXT_TYPE), ("Expected one of ['string'], but got %s of type %s" % (obj._staging_host_user[0], type(obj._staging_host_user[0])))
            common.validate_format(obj._staging_host_user[0], "objectReference", None, None)
        if "stagingPort" not in data:
            raise ValueError("Missing required property \"stagingPort\".")
        obj._staging_port = (data.get("stagingPort", obj.__undef__), dirty)
        if obj._staging_port[0] is not None and obj._staging_port[0] is not obj.__undef__:
            assert isinstance(obj._staging_port[0], int), ("Expected one of ['integer'], but got %s of type %s" % (obj._staging_port[0], type(obj._staging_port[0])))
            common.validate_format(obj._staging_port[0], "None", None, None)
        return obj

    def to_dict(self, dirty=False, belongs_to_parent=False):
        dct = super(MySQLAttachData, self).to_dict(dirty, belongs_to_parent)

        def dictify(obj, prop_is_list_or_vo=False):
            if isinstance(obj, list):
                return [dictify(o, prop_is_list_or_vo) for o in obj]
            elif hasattr(obj, "to_dict"):
                return obj.to_dict(dirty=dirty, belongs_to_parent=prop_is_list_or_vo)
            else:
                return obj
        if "config" == "type" or (self.config is not self.__undef__ and (not (dirty and not self._config[1]) or isinstance(self.config, list) or belongs_to_parent)):
            dct["config"] = dictify(self.config)
        if "config_params" == "type" or (self.config_params is not self.__undef__ and (not (dirty and not self._config_params[1]) or isinstance(self.config_params, list) or belongs_to_parent)):
            dct["configParams"] = dictify(self.config_params, prop_is_list_or_vo=True)
        if "operations" == "type" or (self.operations is not self.__undef__ and (not (dirty and not self._operations[1]) or isinstance(self.operations, list) or belongs_to_parent)):
            dct["operations"] = dictify(self.operations, prop_is_list_or_vo=True)
        if "db_user" == "type" or (self.db_user is not self.__undef__ and (not (dirty and not self._db_user[1]) or isinstance(self.db_user, list) or belongs_to_parent)):
            dct["dbUser"] = dictify(self.db_user)
        if "db_credentials" == "type" or (self.db_credentials is not self.__undef__ and (not (dirty and not self._db_credentials[1]) or isinstance(self.db_credentials, list) or belongs_to_parent)):
            dct["dbCredentials"] = dictify(self.db_credentials, prop_is_list_or_vo=True)
        if "staging_repository" == "type" or (self.staging_repository is not self.__undef__ and (not (dirty and not self._staging_repository[1]) or isinstance(self.staging_repository, list) or belongs_to_parent)):
            dct["stagingRepository"] = dictify(self.staging_repository)
        if "staging_host_user" == "type" or (self.staging_host_user is not self.__undef__ and (not (dirty and not self._staging_host_user[1]) or isinstance(self.staging_host_user, list) or belongs_to_parent)):
            dct["stagingHostUser"] = dictify(self.staging_host_user)
        if "staging_port" == "type" or (self.staging_port is not self.__undef__ and (not (dirty and not self._staging_port[1]) or isinstance(self.staging_port, list) or belongs_to_parent)):
            dct["stagingPort"] = dictify(self.staging_port)
        return dct

    def dirty(self):
        return self.from_dict(self.to_dict(dirty=False), dirty=True)

    def force_dirty(self):
        self._config = (self._config[0], True)
        self._config_params = (self._config_params[0], True)
        self._operations = (self._operations[0], True)
        self._db_user = (self._db_user[0], True)
        self._db_credentials = (self._db_credentials[0], True)
        self._staging_repository = (self._staging_repository[0], True)
        self._staging_host_user = (self._staging_host_user[0], True)
        self._staging_port = (self._staging_port[0], True)

    def is_dirty(self):
        return any([self._config[1], self._config_params[1], self._operations[1], self._db_user[1], self._db_credentials[1], self._staging_repository[1], self._staging_host_user[1], self._staging_port[1]])

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, MySQLAttachData):
            return False
        return super(MySQLAttachData, self).__eq__(other) and \
               self.config == other.config and \
               self.config_params == other.config_params and \
               self.operations == other.operations and \
               self.db_user == other.db_user and \
               self.db_credentials == other.db_credentials and \
               self.staging_repository == other.staging_repository and \
               self.staging_host_user == other.staging_host_user and \
               self.staging_port == other.staging_port

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return common.generate_repr_string(self)

    @property
    def config(self):
        """
        Reference to the configuration for the source. Must be an existing
        linked source config.

        :rtype: ``TEXT_TYPE``
        """
        return self._config[0]

    @config.setter
    def config(self, value):
        self._config = (value, True)

    @property
    def config_params(self):
        """
        MySQL database configuration parameter overrides.

        :rtype: ``dict``
        """
        return self._config_params[0]

    @config_params.setter
    def config_params(self, value):
        self._config_params = (value, True)

    @property
    def operations(self):
        """
        User-specified operation hooks for this source.

        :rtype: :py:class:`v1_10_3.web.vo.LinkedSourceOperations`
        """
        return self._operations[0]

    @operations.setter
    def operations(self, value):
        self._operations = (value, True)

    @property
    def db_user(self):
        """
        The database username.

        :rtype: ``TEXT_TYPE``
        """
        return self._db_user[0]

    @db_user.setter
    def db_user(self, value):
        self._db_user = (value, True)

    @property
    def db_credentials(self):
        """
        The credentials for the database user.

        :rtype: :py:class:`v1_10_3.web.vo.PasswordCredential`
        """
        return self._db_credentials[0]

    @db_credentials.setter
    def db_credentials(self, value):
        self._db_credentials = (value, True)

    @property
    def staging_repository(self):
        """
        The MySQL installation on the staging environment to use for validated
        sync.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_repository[0]

    @staging_repository.setter
    def staging_repository(self, value):
        self._staging_repository = (value, True)

    @property
    def staging_host_user(self):
        """
        OS user on the staging host to use for attaching.

        :rtype: ``TEXT_TYPE``
        """
        return self._staging_host_user[0]

    @staging_host_user.setter
    def staging_host_user(self, value):
        self._staging_host_user = (value, True)

    @property
    def staging_port(self):
        """
        The port on which the MySQL staging instance will listen.

        :rtype: ``int``
        """
        return self._staging_port[0]

    @staging_port.setter
    def staging_port(self, value):
        self._staging_port = (value, True)

